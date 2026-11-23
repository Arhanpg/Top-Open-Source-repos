#!/usr/bin/env python3
"""Resumable public GitHub organization inventory collector.

This tool inventories repository metadata, language statistics, and README URLs.
It stores fetched README text in a local cache for later review but does not copy
upstream README prose into the catalogue. It does not invent project summaries.
"""
from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

API = "https://api.github.com"
USER_AGENT = "Top-Open-Source-Repos-Catalogue/1.0"


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "unnamed"


def api_get(url: str, token: str | None, retries: int = 6) -> tuple[Any, dict[str, str]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": USER_AGENT,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    for attempt in range(retries):
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                payload = response.read().decode("utf-8")
                return json.loads(payload), {k.lower(): v for k, v in response.headers.items()}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code in (403, 429, 500, 502, 503, 504):
                retry_after = exc.headers.get("Retry-After")
                reset = exc.headers.get("X-RateLimit-Reset")
                delay = int(retry_after) if retry_after and retry_after.isdigit() else 2 ** attempt
                if exc.code == 403 and reset and reset.isdigit():
                    delay = max(delay, int(reset) - int(time.time()) + 2)
                print(f"[retry] HTTP {exc.code}; waiting {min(max(delay, 2), 900)}s", file=sys.stderr)
                time.sleep(min(max(delay, 2), 900))
                continue
            raise RuntimeError(f"GitHub API HTTP {exc.code}: {body[:500]}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt + 1 == retries:
                raise
            time.sleep(min(2 ** attempt, 60))
    raise RuntimeError("API retry budget exhausted")


def paginated_repositories(account: str, account_type: str, token: str | None):
    page = 1
    while True:
        if account_type == "org":
            path = f"/orgs/{urllib.parse.quote(account)}/repos"
            query = {"type": "public", "sort": "full_name", "direction": "asc"}
        elif account_type == "user":
            path = f"/users/{urllib.parse.quote(account)}/repos"
            query = {"type": "owner", "sort": "full_name", "direction": "asc"}
        else:
            raise ValueError(f"Unsupported account_type: {account_type}")
        query.update({"per_page": "100", "page": str(page)})
        url = API + path + "?" + urllib.parse.urlencode(query)
        rows, _ = api_get(url, token)
        if not isinstance(rows, list):
            raise RuntimeError(f"Expected repository array from {url}")
        if not rows:
            break
        yield page, rows
        if len(rows) < 100:
            break
        page += 1


def readme_text(full_name: str, token: str | None) -> tuple[str | None, str | None]:
    url = f"{API}/repos/{full_name}/readme"
    try:
        payload, _ = api_get(url, token)
        encoded = payload.get("content", "")
        if not encoded:
            return None, payload.get("html_url")
        raw = base64.b64decode(encoded).decode("utf-8", errors="replace")
        return raw, payload.get("html_url")
    except RuntimeError as exc:
        if "HTTP 404" in str(exc):
            return None, None
        raise


def language_breakdown(full_name: str, token: str | None) -> dict[str, int]:
    payload, _ = api_get(f"{API}/repos/{full_name}/languages", token)
    return payload if isinstance(payload, dict) else {}


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_state(path: Path) -> dict[str, Any]:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"completed_repositories": [], "accounts": {}}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mapping", type=Path, default=Path("config/company_accounts.csv"))
    parser.add_argument("--company", help="Exact company name or GitHub account handle")
    parser.add_argument("--include-unverified", action="store_true",
                        help="Also inventory candidate accounts; outputs remain marked unverified")
    parser.add_argument("--output", type=Path, default=Path("organizations"))
    parser.add_argument("--cache", type=Path, default=Path(".catalogue-cache"))
    parser.add_argument("--state", type=Path, default=Path(".catalogue-state.json"))
    parser.add_argument("--max-repos", type=int, default=0,
                        help="Optional per-account cap for a test run; 0 means no cap")
    parser.add_argument("--delay", type=float, default=0.15,
                        help="Pause between repository metadata requests")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Warning: GITHUB_TOKEN is unset; unauthenticated API rate limits apply.", file=sys.stderr)
    if not args.mapping.exists():
        print(f"Mapping file not found: {args.mapping}", file=sys.stderr)
        return 2

    state = load_state(args.state)
    completed = set(state.get("completed_repositories", []))
    with args.mapping.open(newline="", encoding="utf-8-sig") as handle:
        companies = list(csv.DictReader(handle))

    selected = []
    for company in companies:
        if args.company and args.company.casefold() not in (
            company.get("company", "").casefold(), company.get("account", "").casefold()
        ):
            continue
        verified = company.get("mapping_status", "").strip().casefold() in {
            "verified", "official", "confirmed"
        }
        if not verified and not args.include_unverified:
            print(f"[skip mapping] {company.get('company')} ({company.get('account')}): "
                  f"mapping status is not verified")
            continue
        selected.append(company)

    if not selected:
        print("No eligible company mappings selected. Verify mappings or pass --include-unverified.")
        return 0

    for company in selected:
        name = company["company"].strip()
        account = company["account"].strip()
        account_type = company.get("account_type", "org").strip().lower()
        company_dir = args.output / slug(name)
        repo_dir = company_dir / "repositories"
        company_repo_rows = []
        count = 0
        pages = 0
        started = datetime.now(timezone.utc).isoformat()

        print(f"\n[company] {name} -> {account} ({account_type})")
        for page, repositories in paginated_repositories(account, account_type, token):
            pages = page
            for repo in repositories:
                if args.max_repos and count >= args.max_repos:
                    break
                full_name = repo["full_name"]
                count += 1
                company_repo_rows.append({
                    "name": repo.get("name"),
                    "full_name": full_name,
                    "url": repo.get("html_url"),
                    "description": repo.get("description"),
                    "default_branch": repo.get("default_branch"),
                    "archived": repo.get("archived"),
                    "fork": repo.get("fork"),
                    "disabled": repo.get("disabled"),
                    "license": (repo.get("license") or {}).get("spdx_id"),
                    "created_at": repo.get("created_at"),
                    "updated_at": repo.get("updated_at"),
                    "pushed_at": repo.get("pushed_at"),
                    "stars": repo.get("stargazers_count"),
                    "forks": repo.get("forks_count"),
                    "open_issues": repo.get("open_issues_count"),
                    "readme_url": f"{full_name}/blob/{repo.get('default_branch')}/README.md",
                    "review_status": "metadata only",
                })
                if full_name in completed:
                    continue
                folder = args.cache / slug(account) / slug(repo["name"])
                try:
                    languages = language_breakdown(full_name, token)
                    text, readme_url = readme_text(full_name, token)
                    folder.mkdir(parents=True, exist_ok=True)
                    if text is not None:
                        (folder / "README.md").write_text(text, encoding="utf-8")
                    record = {
                        "repository": full_name,
                        "url": repo.get("html_url"),
                        "readme_url": readme_url,
                        "readme_downloaded": text is not None,
                        "languages_bytes": languages,
                        "metadata": company_repo_rows[-1],
                        "captured_at": datetime.now(timezone.utc).isoformat(),
                        "review_status": "README downloaded; feature summary review pending"
                    }
                    write_json(folder / "metadata.json", record)
                    completed.add(full_name)
                    state["completed_repositories"] = sorted(completed)
                    write_json(args.state, state)
                except Exception as exc:
                    print(f"[error] {full_name}: {exc}", file=sys.stderr)
                time.sleep(max(args.delay, 0))

            if args.max_repos and count >= args.max_repos:
                break

        now = datetime.now(timezone.utc).isoformat()
        company_dir.mkdir(parents=True, exist_ok=True)
        write_json(repo_dir / "inventory.json", {
            "company": name,
            "account": account,
            "account_type": account_type,
            "mapping_status": company.get("mapping_status"),
            "source_groups": company.get("source_groups"),
            "retrieved_at": now,
            "started_at": started,
            "pages_fetched": pages,
            "repository_count_in_this_run": len(company_repo_rows),
            "pagination_complete": not bool(args.max_repos and count >= args.max_repos),
            "repositories": company_repo_rows,
        })
        table = [
            f"# {name} — public GitHub repository inventory",
            "",
            f"- Account: https://github.com/{account}",
            f"- Mapping status: {company.get('mapping_status')}",
            f"- Retrieved: {now}",
            f"- Pages fetched: {pages}",
            f"- Repositories in this run: {len(company_repo_rows)}",
            f"- Pagination complete: {'No (test cap applied)' if args.max_repos and count >= args.max_repos else 'Yes (final page reached)'}",
            "",
            "| Repository | Upstream description | Languages (bytes) | Archived | Fork | README audit |",
            "|---|---|---|---:|---:|---|",
        ]
        for item in company_repo_rows:
            lang_path = args.cache / slug(account) / slug(item["name"]) / "metadata.json"
            langs = {}
            if lang_path.exists():
                try:
                    langs = json.loads(lang_path.read_text(encoding="utf-8")).get("languages_bytes", {})
                except Exception:
                    pass
            lang_text = ", ".join(f"{k} ({v})" for k, v in sorted(langs.items(), key=lambda kv: -kv[1])) or "Unknown"
            desc = (item.get("description") or "No GitHub description").replace("|", "\\|").replace("\n", " ")
            table.append(
                f"| [{item['name']}]({item['url']}) | {desc} | {lang_text} | "
                f"{item.get('archived')} | {item.get('fork')} | README review pending |"
            )
        (repo_dir / "INVENTORY.md").write_text("\n".join(table) + "\n", encoding="utf-8")
        state.setdefault("accounts", {})[account] = {
            "company": name, "pages_fetched": pages, "retrieved_at": now,
            "repository_count_in_this_run": len(company_repo_rows)
        }
        write_json(args.state, state)
        print(f"[done] {name}: {len(company_repo_rows)} repositories, {pages} pages")

    print("\nInventory collection finished. README content is cached locally only.")
    print("Review cached READMEs before adding purpose/features summaries to tracked catalogue files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
