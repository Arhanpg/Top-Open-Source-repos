"""Offline unit tests for the resumable public GitHub catalogue collector."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import catalogue_audit as audit


def repository(index: int) -> dict:
    return {
        "id": index,
        "name": f"repo-{index}",
        "full_name": f"Example/repo-{index}",
        "html_url": f"https://github.com/Example/repo-{index}",
        "description": "Example public repository",
        "default_branch": "main",
        "visibility": "public",
        "archived": False,
        "fork": False,
        "disabled": False,
        "is_template": False,
        "license": {"spdx_id": "MIT"},
        "created_at": "2020-01-01T00:00:00Z",
        "updated_at": "2026-01-01T00:00:00Z",
        "pushed_at": "2026-01-02T00:00:00Z",
        "stargazers_count": 10,
        "forks_count": 2,
        "open_issues_count": 0,
        "topics": ["example"],
    }


class MappingEligibilityTests(unittest.TestCase):
    def test_official_directory_listed_mapping_is_collectable(self):
        self.assertTrue(audit.is_collectable_mapping("official-directory-listed"))

    def test_official_project_linked_mapping_is_collectable(self):
        self.assertTrue(audit.is_collectable_mapping("official-project-linked"))

    def test_unverified_candidate_is_not_collectable_by_default(self):
        self.assertFalse(audit.is_collectable_mapping("mapping unverified"))


class ManifestParserTests(unittest.TestCase):
    def test_package_json(self):
        manifest = json.dumps({
            "dependencies": {"requests": "^2", "zod": "^3"},
            "devDependencies": {"pytest": "^8"},
        })
        self.assertEqual(
            audit.parse_manifest_hints("package.json", manifest),
            ["pytest", "requests", "zod"],
        )

    def test_requirements_txt(self):
        manifest = "requests>=2.31\nnumpy==2.0\n# comment\n"
        self.assertEqual(
            audit.parse_manifest_hints("requirements.txt", manifest),
            ["numpy", "requests"],
        )

    def test_go_mod(self):
        manifest = """module example.com/app

go 1.23

require (
    github.com/google/uuid v1.6.0
    golang.org/x/sys v0.28.0
)
"""
        self.assertEqual(
            audit.parse_manifest_hints("go.mod", manifest),
            ["github.com/google/uuid", "golang.org/x/sys"],
        )

    def test_cargo_toml(self):
        manifest = """[package]
name = "demo"

[dependencies]
serde = "1.0"
tokio = { version = "1", features = ["full"] }

[dev-dependencies]
criterion = "0.5"
"""
        self.assertEqual(
            audit.parse_manifest_hints("Cargo.toml", manifest),
            ["criterion", "serde", "tokio"],
        )

    def test_pyproject_toml_pep621_and_optional_groups(self):
        manifest = """[project]
name = "demo"
dependencies = [
    "requests>=2.31",
    "numpy~=2.0",
]

[project.optional-dependencies]
dev = ["pytest>=8"]
"""
        self.assertEqual(
            audit.parse_manifest_hints("pyproject.toml", manifest),
            ["numpy", "pytest", "requests"],
        )

    def test_pyproject_toml_poetry_groups(self):
        manifest = """[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.115"

[tool.poetry.group.dev.dependencies]
ruff = "^0.9"
"""
        self.assertEqual(
            audit.parse_manifest_hints("pyproject.toml", manifest),
            ["fastapi", "ruff"],
        )

    def test_composer_json(self):
        manifest = json.dumps({
            "require": {"php": "^8.2", "guzzlehttp/guzzle": "^7"},
            "require-dev": {"phpunit/phpunit": "^11"},
        })
        self.assertEqual(
            audit.parse_manifest_hints("composer.json", manifest),
            ["guzzlehttp/guzzle", "phpunit/phpunit"],
        )

    def test_changed_upstream_source_invalidates_captured_evidence(self):
        previous = repository(1)
        previous["readme_status"] = "captured"
        previous["readme_url"] = "https://github.com/Example/repo-1/blob/main/README.md"
        previous["readme_sha"] = "old-readme-sha"
        previous["languages_status"] = "captured"
        previous["languages_bytes"] = {"Python": 500}
        previous["manifest_status"] = "captured"
        previous["manifest_paths"] = [{"path": "pyproject.toml"}]
        previous["audit_status"] = "evidence captured; manual review pending"
        previous["manual_review_status"] = "README reviewed"

        changed = repository(1)
        changed["pushed_at"] = "2026-11-24T01:00:00Z"

        refreshed = audit.repo_metadata(changed, previous, "scan-2")
        self.assertEqual(refreshed["readme_status"], "pending")
        self.assertEqual(refreshed["languages_status"], "pending")
        self.assertEqual(refreshed["manifest_status"], "pending")
        self.assertEqual(refreshed["audit_status"], "evidence stale; recapture required")
        self.assertIn("refresh required", refreshed["manual_review_status"])

    def test_unchanged_upstream_source_preserves_captured_evidence(self):
        previous = repository(1)
        previous["readme_status"] = "captured"
        previous["languages_status"] = "captured"
        previous["manifest_status"] = "captured"
        previous["readme_sha"] = "same-sha"

        refreshed = audit.repo_metadata(repository(1), previous, "scan-2")
        self.assertEqual(refreshed["readme_status"], "captured")
        self.assertEqual(refreshed["languages_status"], "captured")
        self.assertEqual(refreshed["manifest_status"], "captured")
        self.assertEqual(refreshed["readme_sha"], "same-sha")

    def test_pending_rotation_prevents_first_failed_repositories_from_starving_later_rows(self):
        pending = [(f"Example/{name}", {"readme_status": "error"}) for name in ["a", "b", "c", "d", "e"]]
        first = audit.rotate_pending(pending, None, 2)
        self.assertEqual([name for name, _ in first], ["Example/a", "Example/b"])
        second = audit.rotate_pending(pending, first[-1][0].casefold(), 2)
        self.assertEqual([name for name, _ in second], ["Example/c", "Example/d"])
        third = audit.rotate_pending(pending, second[-1][0].casefold(), 2)
        self.assertEqual([name for name, _ in third], ["Example/e", "Example/a"])

    def test_api_get_paces_each_rest_request(self):
        original = audit.LAST_API_REQUEST_AT
        try:
            audit.LAST_API_REQUEST_AT = 100.0
            with patch.object(audit.time, "monotonic", return_value=100.0):
                with patch.object(audit.time, "sleep") as sleep:
                    audit.pace_api_requests()
            sleep.assert_called_once_with(audit.API_REQUEST_INTERVAL_SECONDS)
        finally:
            audit.LAST_API_REQUEST_AT = original


    def test_readme_section_extraction_preserves_feature_and_setup_evidence(self):
        raw = """# Example project

A short introductory paragraph.

## Features
- Fast batch processing
- JSON and CSV input support

## Getting Started
Install the package and run the command.

## Security
Do not expose the service to untrusted networks.
"""
        sections = audit.extract_readme_sections(raw)
        by_category = {row["category"]: row for row in sections}
        self.assertIn("Features and capabilities", by_category)
        self.assertIn("Fast batch processing", by_category["Features and capabilities"]["excerpt"])
        self.assertIn("Getting started and usage", by_category)
        self.assertIn("Install the package", by_category["Getting started and usage"]["excerpt"])
        self.assertIn("Limitations and security", by_category)
        self.assertLessEqual(
            sum(len(row["excerpt"].split()) for row in sections),
            audit.README_EXCERPT_WORDS,
        )



    def test_global_batch_round_robins_accounts_and_reallocates_exhausted_slots(self):
        queues = {
            "company-a::account-a": [
                ("A/repo-1", {"id": 1}),
                ("A/repo-2", {"id": 2}),
                ("A/repo-3", {"id": 3}),
            ],
            "company-b::account-b": [
                ("B/repo-1", {"id": 4}),
            ],
            "company-c::account-c": [
                ("C/repo-1", {"id": 5}),
                ("C/repo-2", {"id": 6}),
            ],
        }
        selected = audit.select_global_batch(queues, 5)
        self.assertEqual(
            [(account, full) for account, full, _ in selected],
            [
                ("company-a::account-a", "A/repo-1"),
                ("company-b::account-b", "B/repo-1"),
                ("company-c::account-c", "C/repo-1"),
                ("company-a::account-a", "A/repo-2"),
                ("company-c::account-c", "C/repo-2"),
            ],
        )
        self.assertEqual(queues["company-a::account-a"][0][0], "A/repo-3")

class InventoryTests(unittest.TestCase):
    def test_zero_byte_readme_is_terminal_unavailable_not_capture_error(self):
        item = repository(1)
        empty_readme = {
            "empty": True,
            "url": "https://github.com/Example/repo-1/blob/main/README",
            "path": "README",
            "sha": "empty-blob-sha",
            "excerpt": "",
            "headings": [],
        }
        with patch.object(audit, "get_languages", return_value={}):
            with patch.object(audit, "get_readme", return_value=empty_readme):
                with patch.object(audit, "get_manifests", return_value=([], False)):
                    result = audit.enrich(item, None, 6, False)
        self.assertEqual(result["readme_status"], "unavailable")
        self.assertEqual(result["readme_unavailable_reason"], "README file is present but zero bytes")
        self.assertEqual(result["audit_status"], "evidence captured; manual review pending")
        self.assertEqual(result["capture_errors"], [])


    def test_manifest_content_uses_raw_endpoint_and_parses_dependency_hints(self):
        content = b'{"dependencies":{"fastapi":"^0.1","pydantic":"^2"}}'
        with patch.object(audit, "raw_get_bytes", return_value=(content, len(content), False)) as raw:
            result = audit.get_manifest_content(
                "Example/repo-1", "package.json", "main", None, "tree-blob-sha"
            )
        self.assertEqual(result["content_status"], "captured")
        self.assertEqual(result["sha"], "tree-blob-sha")
        self.assertEqual(result["dependency_hints"], ["fastapi", "pydantic"])
        self.assertIn("raw.githubusercontent.com/Example/repo-1/main/package.json", raw.call_args.args[0])

    def test_manifest_file_above_limit_is_recorded_without_download_body(self):
        with patch.object(audit, "raw_get_bytes", return_value=(b"", 300_000, True)):
            result = audit.get_manifest_content(
                "Example/repo-1", "package.json", "main", None, "tree-blob-sha"
            )
        self.assertEqual(result["content_status"], "skipped_size_limit")
        self.assertEqual(result["dependency_hints"], [])

    def test_large_readme_falls_back_to_public_raw_download(self):
        raw_readme = b"# Large README\n\nThis project provides a documented test utility.\n"
        payload = {
            "content": "",
            "size": 1_500_000,
            "path": "README.md",
            "html_url": "https://github.com/Example/repo-1/blob/main/README.md",
            "download_url": "https://raw.githubusercontent.com/Example/repo-1/main/README.md",
            "sha": "large-readme-sha",
        }
        with patch.object(audit, "api_get", return_value=(payload, {})):
            with patch.object(audit, "raw_get_bytes", return_value=(raw_readme, len(raw_readme), False)) as raw:
                result = audit.get_readme("Example/repo-1", None)
        self.assertEqual(result["sha"], "large-readme-sha")
        self.assertFalse(result["truncated"])
        self.assertIn("documented test utility", result["excerpt"])
        raw.assert_called_once_with(payload["download_url"], audit.MAX_README_BYTES)

    def test_nonempty_readme_metadata_without_content_is_error(self):
        with patch.object(audit, "api_get", return_value=({
            "content": "",
            "size": 24,
            "path": "README.md",
            "html_url": "https://github.com/Example/repo-1/blob/main/README.md",
        }, {})):
            with self.assertRaisesRegex(RuntimeError, "non-empty file"):
                audit.get_readme("Example/repo-1", None)

    def test_auto_account_type_resolves_organization(self):
        with patch.object(audit, "api_get", return_value=({"type": "Organization"}, {})):
            self.assertEqual(audit.resolve_type("Example", "auto", None), "org")

    def test_page_cap_checkpoints_and_resume_reaches_final_page(self):
        calls: list[int] = []
        first_page = [repository(i) for i in range(1, 101)]
        second_page = [repository(101)]

        def fake_api(url: str, token: str | None, retries: int = 6):
            page = int(parse_qs(urlparse(url).query)["page"][0])
            calls.append(page)
            headers = {}
            if page == 1:
                headers["link"] = (
                    f'<{audit.API}/orgs/Example/repos?per_page=100&page=2>; rel="next"'
                )
                return first_page, headers
            return second_page, headers

        with tempfile.TemporaryDirectory() as temp:
            company_dir = Path(temp) / "example"
            with patch.object(audit, "api_get", side_effect=fake_api):
                capped = audit.inventory(
                    "Example", "org", "Example Company", company_dir,
                    "verified", "tests", None, 1, 0, False,
                )
                self.assertFalse(capped["pagination_complete"])
                self.assertEqual(capped["next_page"], 2)
                self.assertEqual(len(capped["repositories"]), 100)

                resumed = audit.inventory(
                    "Example", "org", "Example Company", company_dir,
                    "verified", "tests", None, 0, 0, False,
                )
                self.assertTrue(resumed["pagination_complete"])
                self.assertIsNone(resumed["next_page"])
                self.assertEqual(len(resumed["repositories"]), 101)
                self.assertEqual(calls, [1, 2])

    def test_interrupted_scheduled_refresh_resumes_next_page(self):
        calls: list[int] = []
        first_page = [repository(i) for i in range(1, 101)]
        second_page = [repository(101)]

        def fake_api(url: str, token: str | None, retries: int = 6):
            page = int(parse_qs(urlparse(url).query)["page"][0])
            calls.append(page)
            headers = {}
            if page == 1:
                headers["link"] = (
                    f'<{audit.API}/orgs/Example/repos?per_page=100&page=2>; rel="next"'
                )
                return first_page, headers
            return second_page, headers

        with tempfile.TemporaryDirectory() as temp:
            company_dir = Path(temp) / "example"
            with patch.object(audit, "api_get", side_effect=fake_api):
                first = audit.inventory(
                    "Example", "org", "Example Company", company_dir,
                    "verified", "tests", None, 1, 0, True,
                )
                self.assertTrue(first["refresh_in_progress"])
                resumed = audit.inventory(
                    "Example", "org", "Example Company", company_dir,
                    "verified", "tests", None, 0, 0, True,
                )
                self.assertTrue(resumed["pagination_complete"])
                self.assertEqual(calls, [1, 2])

    def test_empty_git_repository_tree_409_is_terminal_not_failure(self):
        item = repository(1)
        with patch.object(audit, "get_languages", return_value={}):
            with patch.object(audit, "get_readme", return_value=None):
                with patch.object(
                    audit,
                    "get_manifests",
                    side_effect=audit.APIError(409, '{"message":"Git Repository is empty."}', {}),
                ):
                    result = audit.enrich(item, None, 6, False)
        self.assertEqual(result["manifest_status"], "unavailable")
        self.assertEqual(result["manifest_unavailable_reason"], "repository has no Git commit/tree")
        self.assertEqual(result["audit_status"], "evidence captured; manual review pending")
        self.assertEqual(result["capture_errors"], [])

    def test_unexpected_git_tree_409_remains_a_capture_error(self):
        item = repository(1)
        with patch.object(audit, "get_languages", return_value={}):
            with patch.object(audit, "get_readme", return_value=None):
                with patch.object(
                    audit,
                    "get_manifests",
                    side_effect=audit.APIError(409, '{"message":"Conflict for another reason"}', {}),
                ):
                    result = audit.enrich(item, None, 6, False)
        self.assertEqual(result["manifest_status"], "error")
        self.assertEqual(result["audit_status"], "evidence capture incomplete")
        self.assertTrue(any("manifest tree:" in error for error in result["capture_errors"]))

    def test_empty_organization_completes(self):
        with tempfile.TemporaryDirectory() as temp:
            company_dir = Path(temp) / "empty"
            with patch.object(audit, "api_get", return_value=([], {})):
                state = audit.inventory(
                    "EmptyOrg", "org", "Empty Company", company_dir,
                    "verified", "tests", None, 0, 0, False,
                )
                self.assertTrue(state["pagination_complete"])
                self.assertEqual(state["repositories"], {})
                repeated = audit.inventory(
                    "EmptyOrg", "org", "Empty Company", company_dir,
                    "verified", "tests", None, 0, 0, False,
                )
                self.assertTrue(repeated["pagination_complete"])


if __name__ == "__main__":
    unittest.main()
