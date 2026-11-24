import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import repository_technical_audit as audit


class RepositoryAuditTests(unittest.TestCase):
    def test_readme_feature_extraction(self):
        readme = """# Demo

## Overview
A sample toolkit.

## Features
- Incremental event parsing
- Deterministic JSON export
"""
        result = audit.feature_bullets(readme)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["evidence"], ["README.md#Features"])

    def test_readme_purpose_uses_first_prose(self):
        readme = """# Demo

[![Build](https://example.invalid/badge)](https://example.invalid)

A toolkit for processing structured event streams.

## Features
- Event replay
"""
        self.assertEqual(audit.purpose(readme), "A toolkit for processing structured event streams.")

    def test_package_json_dependencies(self):
        body = json.dumps({
            "dependencies": {"express": "^5"},
            "devDependencies": {"jest": "^30"},
        })
        self.assertEqual(audit.deps_for("package.json", body), ["express", "jest"])

    def test_pyproject_dependencies(self):
        body = '[project]\nname = "demo"\ndependencies = ["fastapi>=0.1", "uvicorn[standard]"]\n'
        self.assertEqual(audit.deps_for("pyproject.toml", body), ["fastapi", "uvicorn"])

    def test_language_stats_do_not_invent_frameworks(self):
        record = audit.simple_audit(
            {"description": "Example toolkit", "languages_bytes": {"Python": 1000}},
            "", [], [],
        )
        self.assertEqual(record["technology_stack"]["languages"], ["Python"])
        self.assertEqual(record["technology_stack"]["frameworks_and_libraries"], [])
        self.assertEqual(record["core_features"], [])

    def test_account_queues_are_round_robin(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for company, account, names in [
                ("company-a", "org-a", ["one", "two", "three"]),
                ("company-b", "org-b", ["four", "five"]),
            ]:
                folder = root / "organizations" / company / "accounts" / account
                folder.mkdir(parents=True)
                repos = {}
                for index, name in enumerate(names, 1):
                    full = f"{account}/{name}"
                    repos[full] = {"id": index, "name": name, "full_name": full}
                (folder / "inventory.json").write_text(
                    json.dumps({"company": company, "account": account, "repositories": repos}),
                    encoding="utf-8",
                )
            with patch.object(audit, "ROOT", root):
                tasks = audit.load_tasks(None, None, False, False)
            self.assertEqual([x["account"] for x in tasks[:4]], ["org-a", "org-b", "org-a", "org-b"])

    def test_incomplete_yaml_markdown_pair_is_requeued(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "organizations" / "company" / "accounts" / "org"
            audit_dir = folder / "technical-audits"
            audit_dir.mkdir(parents=True)
            full = "org/demo"
            repo = {"id": 7, "name": "demo", "full_name": full}
            stem = "demo-7"
            digest = audit.fingerprint(repo)
            (audit_dir / f"{stem}.yaml").write_text(
                f'audit_status: "llm_interpreted"\nevidence_fingerprint: "{digest}"\n',
                encoding="utf-8",
            )
            (folder / "inventory.json").write_text(
                json.dumps({"company": "company", "account": "org", "repositories": {full: repo}}),
                encoding="utf-8",
            )
            with patch.object(audit, "ROOT", root):
                tasks = audit.load_tasks(None, None, False, True)
            self.assertEqual([x["repo"]["full_name"] for x in tasks], [full])

    def test_manually_reviewed_complete_pair_is_skipped(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "organizations" / "company" / "accounts" / "org"
            audit_dir = folder / "technical-audits"
            audit_dir.mkdir(parents=True)
            full = "org/demo"
            repo = {"id": 7, "name": "demo", "full_name": full}
            (audit_dir / "demo-7.yaml").write_text('audit_status: "manual_reviewed"\n', encoding="utf-8")
            (audit_dir / "demo-7.md").write_text("# Reviewed\n", encoding="utf-8")
            (folder / "inventory.json").write_text(
                json.dumps({"company": "company", "account": "org", "repositories": {full: repo}}),
                encoding="utf-8",
            )
            with patch.object(audit, "ROOT", root):
                self.assertEqual(audit.load_tasks(None, None, False, False), [])


if __name__ == "__main__":
    unittest.main()
