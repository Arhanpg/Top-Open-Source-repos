#!/usr/bin/env python3
"""Resumable public GitHub inventory and README evidence collector.

Tracked per-account inventory.json files are the checkpoints. Automated
captures are never labelled as manually README-reviewed.
"""
from __future__ import annotations
import argparse, base64, csv, json, os, re, sys, time, tomllib, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

API = "https://api.github.com"
UA = "Top-Open-Source-Repos-Catalogue/2.0"
PER_PAGE = 100

class APIError(RuntimeError):
    def __init__(self, status: int, message: str, headers: dict[str, str] | None = None):
        super().__init__(f"GitHub API HTTP {status}: {message[:400]}")
        self.status, self.headers = status, headers or {}

def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-") or "unnamed"

def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)

def read_json(path: Path, default: Any) -> Any:
    if not path.exists(): return default
    try: return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc: raise RuntimeError(f"Unreadable checkpoint {path}: {exc}") from exc

def api_get(url: str, token: str | None, retries: int = 6):
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28", "User-Agent": UA}
    if token: headers["Authorization"] = f"Bearer {token}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=45) as response:
                return json.loads(response.read().decode("utf-8")), {k.lower(): v for k, v in response.headers.items()}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            hdr = {k.lower(): v for k, v in exc.headers.items()}
            if exc.code not in {403, 408, 429, 500, 502, 503, 504} or attempt == retries - 1:
                raise APIError(exc.code, body, hdr) from exc
            retry = hdr.get("retry-after", "")
            reset, remaining = hdr.get("x-ratelimit-reset", ""), hdr.get("x-ratelimit-remaining", "")
            if retry.isdigit(): wait = int(retry)
            elif exc.code == 403 and remaining == "0" and reset.isdigit(): wait = max(2, int(reset) - int(time.time()) + 2)
            else: wait = min(2 ** attempt, 60)
            wait = min(max(wait, 2), 900)
            print(f"[retry] HTTP {exc.code}; waiting {wait}s", file=sys.stderr)
            time.sleep(wait)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            if attempt == retries - 1: raise RuntimeError(f"Request failed after {retries} attempts: {exc}") from exc
            wait = min(2 ** attempt, 60)
            print(f"[retry] request error; waiting {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError("GitHub retry budget exhausted")

def resolve_type(account: str, configured: str, token: str | None) -> str:
    kind = (configured or "auto").casefold().strip()
    if kind in {"org", "organization"}: return "org"
    if kind in {"user", "corporate-user"}: return "user"
    if kind != "auto": raise ValueError(f"Unsupported account_type {configured!r} for {account}")
    profile, _ = api_get(f"{API}/users/{urllib.parse.quote(account)}", token)
    result = str(profile.get("type", "")).casefold()
    if result == "organization": return "org"
    if result == "user": return "user"
    raise RuntimeError(f"Could not determine account type for {account}: {result!r}")

def repos_url(account: str, kind: str, page: int) -> str:
    if kind == "org": path, params = f"/orgs/{urllib.parse.quote(account)}/repos", {"type":"public","sort":"full_name","direction":"asc"}
    elif kind == "user": path, params = f"/users/{urllib.parse.quote(account)}/repos", {"type":"owner","sort":"full_name","direction":"asc"}
    else: raise ValueError(f"Invalid resolved account type: {kind}")
    params.update(per_page=str(PER_PAGE), page=str(page))
    return API + path + "?" + urllib.parse.urlencode(params)

def link_next(link: str) -> int | None:
    for part in link.split(","):
        match = re.match(r"\s*<([^>]+)>\s*;\s*rel=\"?next\"?", part)
        if match:
            query = urllib.parse.parse_qs(urllib.parse.urlparse(match.group(1)).query)
            return int(query.get("page", ["0"])[0]) or None
    return None

def repo_metadata(row: dict[str, Any], old: dict[str, Any] | None, scan_id: str) -> dict[str, Any]:
    lic = row.get("license") or {}
    item = {
        "id":row.get("id"), "name":row.get("name"), "full_name":row.get("full_name"),
        "url":row.get("html_url"), "description":row.get("description"),
        "default_branch":row.get("default_branch"), "visibility":row.get("visibility", "public"),
        "archived":bool(row.get("archived")), "fork":bool(row.get("fork")),
        "disabled":bool(row.get("disabled")), "is_template":bool(row.get("is_template")),
        "license_spdx":lic.get("spdx_id"), "created_at":row.get("created_at"),
        "updated_at":row.get("updated_at"), "pushed_at":row.get("pushed_at"),
        "stars":row.get("stargazers_count"), "forks":row.get("forks_count"),
        "open_issues":row.get("open_issues_count"), "topics":row.get("topics", []),
        "last_seen_scan_id":scan_id,
    }
    for key in ("readme_status","readme_url","readme_path","readme_sha","readme_excerpt","readme_headings",
                "languages_bytes","languages_status","manifest_status","manifest_paths","manifest_truncated",
                "enriched_at","audit_status","manual_review_status","capture_errors"):
        if old and key in old: item[key] = old[key]
    item.setdefault("readme_status", "pending")
    item.setdefault("languages_status", "pending")
    item.setdefault("manifest_status", "pending")
    item.setdefault("audit_status", "metadata only")
    item.setdefault("manual_review_status", "manual technical interpretation pending")
    return item

def inventory(account: str, kind: str, company: str, company_dir: Path, mapping_status: str,
              source_groups: str, token: str | None, max_pages: int, delay: float, refresh: bool):
    account_dir = company_dir / "accounts" / slug(account)
    checkpoint = account_dir / "inventory.json"
    state = read_json(checkpoint, {"schema_version":2,"company":company,"account":account,"repositories":{},
                                    "pages_fetched":0,"next_page":1,"pagination_complete":False})
    state.update(company=company, account=account, account_type=kind, mapping_status=mapping_status, source_groups=source_groups)
    # A scheduled refresh starts a new scan only after the previous scan completed.
    # If a runner was interrupted mid-refresh, resume its saved next_page rather
    # than restarting from page one on every scheduled retry.
    active_refresh = bool(state.get("refresh_in_progress"))
    needs_initial_scan = not state.get("repositories") and not state.get("pagination_complete")
    if (refresh and not active_refresh and not state.get("pagination_complete")) or needs_initial_scan or (refresh and state.get("pagination_complete")):
        state.update(next_page=1, pages_this_scan=0, scan_id=now(), pagination_complete=False, refresh_in_progress=True)
        write_json(checkpoint, state)
    elif state.get("pagination_complete"):
        print(f"[inventory] {account}: already complete ({len(state['repositories'])} records); use --refresh-inventory to rescan")
        return state
    state.setdefault("scan_id", now())
    state.setdefault("pages_this_scan", 0)
    pages_run = 0
    while not state.get("pagination_complete"):
        page = int(state.get("next_page") or 1)
        rows, headers = api_get(repos_url(account, kind, page), token)
        if not isinstance(rows, list): raise RuntimeError(f"Expected array from {account} repository page {page}")
        records = state.setdefault("repositories", {})
        for row in rows:
            full = row.get("full_name")
            if full: records[full] = repo_metadata(row, records.get(full), state["scan_id"])
        following = link_next(headers.get("link", ""))
        state["next_page"] = following
        state["pagination_complete"] = following is None
        if following is None:
            state["refresh_in_progress"] = False
            for item in records.values(): item["public_in_latest_scan"] = item.get("last_seen_scan_id") == state["scan_id"]
        state["pages_fetched"] = int(state.get("pages_fetched",0)) + 1
        state["pages_this_scan"] = int(state.get("pages_this_scan",0)) + 1
        state["repository_count"] = len(records)
        state["retrieved_at"] = now()
        write_json(checkpoint, state)
        pages_run += 1
        print(f"[inventory] {account}: page {page}, {len(rows)} rows; known total {len(records)}")
        if state["pagination_complete"] or (max_pages and pages_run >= max_pages): break
        time.sleep(delay)
    return state

def get_readme(full: str, token: str | None):
    try: payload, _ = api_get(f"{API}/repos/{full}/readme", token)
    except APIError as exc:
        if exc.status == 404: return None
        raise
    content = payload.get("content", "")
    if not content: raise RuntimeError("README metadata returned without base64 content")
    raw = base64.b64decode(content).decode("utf-8", errors="replace")
    headings = [re.sub(r"^#{1,6}\s*", "", line).strip() for line in raw.splitlines() if re.match(r"^#{1,6}\s+", line)][:30]
    snippets, words = [], 0
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith(("#","!","<","[![","<!--","\x60\x60\x60","---","|",">","[")): continue
        line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
        tokens = line.split()
        if not tokens: continue
        tokens = tokens[:max(0,100-words)]
        if tokens: snippets.append(" ".join(tokens)); words += len(tokens)
        if words >= 100: break
    return {"url":payload.get("html_url"),"path":payload.get("path"),"sha":payload.get("sha"),
            "excerpt":" ".join(snippets),"headings":headings}

def get_languages(full: str, token: str | None) -> dict[str,int]:
    data,_=api_get(f"{API}/repos/{full}/languages",token)
    if not isinstance(data,dict): raise RuntimeError("Unexpected language response")
    return {str(k):int(v) for k,v in data.items()}

MANIFESTS={"package.json","pyproject.toml","pom.xml","cargo.toml","go.mod","requirements.txt","build.gradle",
           "build.gradle.kts","cmakelists.txt","dockerfile","composer.json","gemfile","pipfile","setup.py","makefile","chart.yaml"}
MAX_MANIFEST_BYTES = 256_000

def _add_pep508_hint(spec: Any, output: set[str]) -> None:
    if isinstance(spec, str):
        match = re.match(r"^\\s*([A-Za-z0-9_.-]+)", spec)
        if match:
            output.add(match.group(1))

def _add_toml_dependency_table(table: Any, output: set[str]) -> None:
    if isinstance(table, dict):
        for package_name in table:
            if str(package_name).casefold() != "python":
                output.add(str(package_name))

def parse_manifest_hints(path: str, content: str) -> list[str]:
    """Extract conservative dependency-name clues; filenames alone are not proof."""
    basename = path.rsplit("/", 1)[-1].casefold()
    hints: set[str] = set()
    if basename == "package.json":
        try:
            data = json.loads(content)
            for section in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
                hints.update(str(name) for name in (data.get(section) or {}).keys())
        except (json.JSONDecodeError, AttributeError, TypeError):
            pass
    elif basename in {"requirements.txt", "pipfile"}:
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith(("#", "[", "-")):
                continue
            candidate = re.split(r"[<=>~!;\\s\\[]", line)[0]
            if re.fullmatch(r"[A-Za-z0-9_.-]+", candidate):
                hints.add(candidate)
    elif basename == "go.mod":
        hints.update(re.findall(r"^\\s*(?:require\\s+)?([A-Za-z0-9._/-]+)\\s+v[0-9][^\\s]*", content, re.MULTILINE))
    elif basename in {"cargo.toml", "pyproject.toml"}:
        try:
            data = tomllib.loads(content)
        except tomllib.TOMLDecodeError:
            data = {}
        if basename == "cargo.toml":
            for section in ("dependencies", "dev-dependencies", "build-dependencies"):
                _add_toml_dependency_table(data.get(section), hints)
        else:
            project = data.get("project", {}) if isinstance(data, dict) else {}
            if isinstance(project, dict):
                for spec in project.get("dependencies", []) or []:
                    _add_pep508_hint(spec, hints)
                optional = project.get("optional-dependencies", {}) or {}
                if isinstance(optional, dict):
                    for group_specs in optional.values():
                        for spec in group_specs or []:
                            _add_pep508_hint(spec, hints)
            poetry = (data.get("tool", {}) or {}).get("poetry", {}) if isinstance(data, dict) else {}
            if isinstance(poetry, dict):
                _add_toml_dependency_table(poetry.get("dependencies"), hints)
                _add_toml_dependency_table(poetry.get("dev-dependencies"), hints)
                groups = poetry.get("group", {}) or {}
                if isinstance(groups, dict):
                    for group_data in groups.values():
                        if isinstance(group_data, dict):
                            _add_toml_dependency_table(group_data.get("dependencies"), hints)
    elif basename == "pom.xml":
        hints.update(re.findall(r"<artifactId>\\s*([^<]+)\\s*</artifactId>", content))
    elif basename == "composer.json":
        try:
            data = json.loads(content)
            for section in ("require", "require-dev"):
                hints.update(str(name) for name in (data.get(section) or {}).keys() if name != "php")
        except (json.JSONDecodeError, AttributeError, TypeError):
            pass
    return sorted(hints)[:60]

def get_manifest_content(full: str, path: str, branch: str, token: str | None) -> dict[str, Any]:
    encoded_path = urllib.parse.quote(path, safe="/")
    ref = urllib.parse.urlencode({"ref": branch})
    payload, _ = api_get(f"{API}/repos/{full}/contents/{encoded_path}?{ref}", token)
    size = int(payload.get("size") or 0)
    result = {"path": path, "sha": payload.get("sha"), "size": size}
    if size > MAX_MANIFEST_BYTES:
        result["content_status"] = "skipped_size_limit"
        result["dependency_hints"] = []
        return result
    encoded = payload.get("content", "")
    if not encoded:
        result["content_status"] = "content_not_returned"
        result["dependency_hints"] = []
        return result
    content = base64.b64decode(encoded).decode("utf-8", errors="replace")
    result["content_status"] = "captured"
    result["dependency_hints"] = parse_manifest_hints(path, content)
    return result

def get_manifests(full: str, branch: str, limit: int, token: str | None):
    branch_q=urllib.parse.quote(branch or "HEAD",safe="")
    tree,_=api_get(f"{API}/repos/{full}/git/trees/{branch_q}?recursive=1",token)
    paths=[item.get("path","") for item in tree.get("tree",[]) if item.get("type")=="blob"]
    found=[p for p in paths if p.rsplit("/",1)[-1].casefold() in MANIFESTS or p.endswith((".csproj",".fsproj",".sln"))]
    found=sorted(set(found),key=lambda p:(p.count("/"),p.casefold()))[:limit]
    rows=[]
    for path in found:
        try:
            rows.append(get_manifest_content(full,path,branch,token))
        except Exception as exc:
            rows.append({"path":path,"content_status":"error","dependency_hints":[],"capture_error":str(exc)[:300]})
    return rows, bool(tree.get("truncated"))

def enrich(repo: dict[str,Any], token: str | None, manifest_limit: int, force: bool):
    errors=[]; full=repo["full_name"]
    if force or repo.get("languages_status")!="captured":
        try: repo["languages_bytes"]=get_languages(full,token); repo["languages_status"]="captured"
        except Exception as exc: repo["languages_status"]="error"; errors.append(f"languages: {exc}")
    if force or repo.get("readme_status") not in {"captured","unavailable"}:
        try:
            doc=get_readme(full,token)
            if doc is None:
                repo.update(readme_status="unavailable",readme_url=None,readme_path=None,readme_sha=None,readme_excerpt="",readme_headings=[])
            else:
                repo.update(readme_status="captured",readme_url=doc["url"],readme_path=doc["path"],readme_sha=doc["sha"],readme_excerpt=doc["excerpt"],readme_headings=doc["headings"])
        except Exception as exc: repo["readme_status"]="error"; errors.append(f"README: {exc}")
    if force or repo.get("manifest_status") not in {"captured","none_found","unavailable"}:
        try:
            files,truncated=get_manifests(full,str(repo.get("default_branch") or "HEAD"),manifest_limit,token)
            repo["manifest_paths"]=files; repo["manifest_truncated"]=truncated
            manifest_errors = [item for item in files if item.get("content_status") == "error"]
            repo["manifest_status"] = ("partial" if manifest_errors else "captured") if files else "none_found"
            errors.extend(f"manifest {item.get('path')}: {item.get('capture_error', 'capture failed')}" for item in manifest_errors)
        except APIError as exc:
            if exc.status==404: repo["manifest_status"]="unavailable"
            else: repo["manifest_status"]="error"; errors.append(f"manifest tree: {exc}")
        except Exception as exc: repo["manifest_status"]="error"; errors.append(f"manifest tree: {exc}")
    repo["capture_errors"]=errors; repo["enriched_at"]=now()
    complete=(repo.get("readme_status") in {"captured","unavailable"} and repo.get("languages_status")=="captured" and repo.get("manifest_status") in {"captured","none_found","unavailable"})
    repo["audit_status"]="evidence captured; manual review pending" if complete else "evidence capture incomplete"
    return repo

def doc_path(account_dir: Path, repo: dict[str,Any]) -> Path:
    return account_dir/"repositories"/f"{slug(repo.get('name') or 'repository')}-{repo.get('id') or 'unknown'}.md"

def md(value: Any) -> str:
    return str(value if value is not None else "").replace("|","\\|").replace("\n"," ").strip()

def render_repo(repo: dict[str,Any], company: str, account: str, mapping_status: str) -> str:
    full=repo["full_name"]; url=repo.get("url") or f"https://github.com/{full}"
    branch=str(repo.get("default_branch") or "Unknown")
    readme=repo.get("readme_url") or f"{url}/blob/{urllib.parse.quote(branch,safe='')}/README.md"
    langs=repo.get("languages_bytes") or {}
    lang_rows="\n".join(f"| {md(k)} | {v:,} |" for k,v in sorted(langs.items(),key=lambda x:-x[1])) or "| Unknown | Not captured |"
    headings="\n".join(f"- {h}" for h in repo.get("readme_headings",[])) or "- No headings captured"
    manifests="\n".join(
        f"- {m['path']} (capture: {m.get('content_status', 'path only')})" +
        (f" — dependency clues: {', '.join(m.get('dependency_hints', [])[:20])}" if m.get("dependency_hints") else "") +
        (f" — error: {m.get('capture_error')}" if m.get("capture_error") else "")
        for m in repo.get("manifest_paths",[])
    ) or "- No recognised manifests found or captured"
    return f"""# {full}

- Company: {company}
- GitHub account: [https://github.com/{account}](https://github.com/{account})
- Mapping status: {mapping_status}
- Repository: [{full}]({url})
- Default branch: {branch}
- README: [Open upstream README]({readme})
- README blob SHA: {repo.get('readme_sha') or 'Not captured'}
- Repository ID: {repo.get('id')}
- Evidence state: {repo.get('audit_status')}
- Manual review: {repo.get('manual_review_status','manual technical interpretation pending')}

## Upstream description

{repo.get('description') or 'No GitHub description supplied.'}

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: {repo.get('readme_status','pending')}
- Captured: {repo.get('enriched_at') or 'Not yet captured'}

### Short excerpt (up to 100 words)

> {repo.get('readme_excerpt') or 'No README excerpt captured. Use the upstream README link.'}

### README headings

{headings}

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
{lang_rows}

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

{manifests}

- Manifest scan truncated by GitHub: {repo.get('manifest_truncated',False)}
- Manifest capture state: {repo.get('manifest_status','pending')}

## Lifecycle metadata

- Archived: {repo.get('archived')}
- Fork: {repo.get('fork')}
- Disabled: {repo.get('disabled')}
- Licence SPDX: {repo.get('license_spdx') or 'Unknown'}
- Stars at capture: {repo.get('stars')}
- Forks at capture: {repo.get('forks')}
- Last updated: {repo.get('updated_at')}
- Last pushed: {repo.get('pushed_at')}
- Topics: {', '.join(repo.get('topics') or []) or 'Not supplied'}

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository]({url})
- [README]({readme})
- [Issues]({url}/issues)
- [Releases]({url}/releases)

Capture errors: {('; '.join(repo.get('capture_errors') or []) or 'None')}

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
"""

def counts(state: dict[str,Any]) -> dict[str,int]:
    repos=list(state.get("repositories",{}).values())
    return {"total":len(repos),"readme_captured":sum(x.get("readme_status")=="captured" for x in repos),
            "readme_unavailable":sum(x.get("readme_status")=="unavailable" for x in repos),
            "pending_or_error":sum(x.get("readme_status") not in {"captured","unavailable"} for x in repos),
            "evidence_captured":sum(x.get("audit_status")=="evidence captured; manual review pending" for x in repos),
            "manual_readme_reviewed":sum(x.get("manual_review_status")=="README reviewed" for x in repos)}

def export(state: dict[str,Any], company_dir: Path, account_dir: Path):
    items=sorted(state.get("repositories",{}).values(),key=lambda x:x.get("full_name","").casefold())
    metric=counts(state); account=state["account"]
    status=[f"# {state['company']} — GitHub account {account}","",f"- Account type: {state.get('account_type')}",f"- Mapping status: {state.get('mapping_status')}",
            f"- Retrieved: {state.get('retrieved_at')}",f"- Pages in latest scan: {state.get('pages_this_scan',0)}",f"- Pagination complete: {state.get('pagination_complete')}",f"- Next page: {state.get('next_page')}","",
            "## Capture metrics","","| Metric | Count |","|---|---:|"]
    status += [f"| {k.replace('_',' ').title()} | {v:,} |" for k,v in metric.items()]
    status += ["","README captured means downloaded, not manually interpreted. Evidence captured means README, language and manifest collection reached terminal states. Manual review is separate.","See [INVENTORY.md](INVENTORY.md) for repository links."]
    (account_dir/"README.md").parent.mkdir(parents=True,exist_ok=True)
    (account_dir/"README.md").write_text("\n".join(status)+"\n",encoding="utf-8")
    lines=[f"# {state['company']} / {account} — repository inventory","",f"- Pagination complete: {state.get('pagination_complete')}",f"- Pages in latest scan: {state.get('pages_this_scan',0)}",f"- Repository records: {len(items):,}","",
           "| Repository | Description | Stars | Languages | Archived | Fork | In latest scan | README state | Dossier |","|---|---|---:|---|---:|---:|---|---|---|"]
    for item in items:
        path=doc_path(account_dir,item)
        link=f"[Open]({path.relative_to(account_dir).as_posix()})" if path.exists() else "Not generated"
        languages=", ".join(sorted((item.get("languages_bytes") or {}).keys())) or "Pending"
        seen=str(bool(item.get("public_in_latest_scan"))) if state.get("pagination_complete") else "Not confirmed"
        lines.append(f"| [{md(item.get('full_name'))}]({item.get('url') or ''}) | {md(item.get('description') or 'No description')} | {item.get('stars') or 0} | {md(languages)} | {bool(item.get('archived'))} | {bool(item.get('fork'))} | {seen} | {item.get('readme_status','pending')} | {link} |")
    (account_dir/"INVENTORY.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    dirs=sorted((company_dir/"accounts").glob("*/inventory.json")) if (company_dir/"accounts").exists() else []
    summary=[f"# {state['company']} — GitHub account inventories","","Each account is tracked separately. Completion of one account does not prove company-wide account discovery is complete.","",
             "| Account | Type | Mapping | Repositories | Inventory complete | Record |","|---|---|---|---:|---:|---|"]
    for file in dirs:
        other=read_json(file,{})
        if other: summary.append(f"| [{other.get('account')}]({('https://github.com/'+other.get('account'))}) | {other.get('account_type')} | {other.get('mapping_status')} | {len(other.get('repositories',{}))} | {bool(other.get('pagination_complete'))} | [Open](accounts/{file.parent.name}/README.md) |")
    (company_dir/"ACCOUNT-INVENTORY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

def run_account(row: dict[str,str], args, token: str | None) -> bool:
    company,account=row["company"].strip(),row["account"].strip()
    mapping=row.get("mapping_status","unverified").strip()
    verified=mapping.casefold() in {"verified","official","confirmed"}
    if not verified and not args.include_unverified:
        print(f"[skip mapping] {company}/{account}: not verified"); return True
    company_dir=args.output/slug(company); account_dir=company_dir/"accounts"/slug(account); checkpoint=account_dir/"inventory.json"
    try:
        if args.phase in {"inventory","all"}:
            kind=resolve_type(account,row.get("account_type","auto"),token)
            state=inventory(account,kind,company,company_dir,mapping,row.get("source_groups",""),token,args.max_pages,args.delay,args.refresh_inventory)
        else:
            state=read_json(checkpoint,{})
            if not state: print(f"[missing checkpoint] {account}: run inventory first"); return False
        if args.phase in {"enrich","all"}:
            pending=[]
            for full,repo in state.get("repositories",{}).items():
                complete=repo.get("readme_status") in {"captured","unavailable"} and repo.get("languages_status")=="captured" and repo.get("manifest_status") in {"captured","none_found","unavailable"}
                if args.force_enrich or not complete: pending.append((full,repo))
            pending.sort(key=lambda x:x[0].casefold())
            selected=pending if args.enrich_limit==0 else pending[:args.enrich_limit]
            print(f"[enrich] {account}: {len(selected)} selected / {len(pending)} pending")
            for n,(full,repo) in enumerate(selected,1):
                print(f"[enrich] {n}/{len(selected)} {full}")
                enrich(repo,token,args.manifest_limit,args.force_enrich)
                state["repositories"][full]=repo
                write_json(checkpoint,state)
                target=doc_path(account_dir,repo); target.parent.mkdir(parents=True,exist_ok=True)
                target.write_text(render_repo(repo,company,account,mapping),encoding="utf-8")
                time.sleep(args.delay)
        if args.phase in {"inventory","enrich","export","all"}:
            write_json(checkpoint,state); export(state,company_dir,account_dir)
        metric=counts(state)
        errors=any(x.get("audit_status")=="evidence capture incomplete" for x in state.get("repositories",{}).values())
        print(f"[done] {company}/{account}: {metric['total']} repos; pagination_complete={state.get('pagination_complete')}; README captured={metric['readme_captured']}; manual reviews={metric['manual_readme_reviewed']}")
        return not errors
    except Exception as exc:
        print(f"[account error] {company}/{account}: {exc}",file=sys.stderr)
        if checkpoint.exists():
            try: export(read_json(checkpoint,{}),company_dir,account_dir)
            except Exception as nested: print(f"[export error] {nested}",file=sys.stderr)
        return False

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mapping",type=Path,default=Path("config/company_accounts.csv"))
    p.add_argument("--company",help="Case-insensitive company name or GitHub account login")
    p.add_argument("--include-unverified",action="store_true")
    p.add_argument("--output",type=Path,default=Path("organizations"))
    p.add_argument("--phase",choices=("inventory","enrich","export","all"),default="all")
    p.add_argument("--enrich-limit",type=int,default=50,help="Repositories per account; 0 means all pending")
    p.add_argument("--manifest-limit",type=int,default=6)
    p.add_argument("--max-pages",type=int,default=0,help="Optional page cap for tests; capped scans are incomplete")
    p.add_argument("--delay",type=float,default=0.2)
    p.add_argument("--refresh-inventory",action="store_true")
    p.add_argument("--force-enrich",action="store_true")
    args=p.parse_args()
    if min(args.enrich_limit,args.manifest_limit,args.max_pages)<0 or args.delay<0: p.error("limits and delay must be non-negative")
    if args.manifest_limit==0: args.manifest_limit=1
    if not args.mapping.exists(): print(f"Missing mapping file: {args.mapping}",file=sys.stderr); return 2
    token=os.environ.get("GITHUB_TOKEN")
    if not token: print("Warning: GITHUB_TOKEN is unset; unauthenticated rate limits apply.",file=sys.stderr)
    try:
        with args.mapping.open(newline="",encoding="utf-8-sig") as f: rows=list(csv.DictReader(f))
    except Exception as exc: print(f"Cannot read mapping file: {exc}",file=sys.stderr); return 2
    if not rows: print("Mapping CSV has no company rows.",file=sys.stderr); return 2
    selected=[r for r in rows if not args.company or args.company.casefold() in r.get("company","").casefold() or args.company.casefold() in r.get("account","").casefold()]
    if not selected: print("No company mapping matched the filter.",file=sys.stderr); return 2
    ok=True
    for row in selected: ok=run_account(row,args,token) and ok
    print("Run finished. Check each account's README.md and INVENTORY.md for pagination and capture status.")
    return 0 if ok else 1

if __name__=="__main__": raise SystemExit(main())
