# Running the public GitHub repository catalogue auditor

The auditor is designed for large organization inventories and resumable batches. It enumerates public repositories, captures README/language/manifest evidence, and creates one Markdown dossier per repository.

## Requirements

- Python 3.11 or newer.
- A GitHub token in `GITHUB_TOKEN` for higher authenticated API limits.
- Company/account mappings in `config/company_accounts.csv`.

## Run a single account

PowerShell:

```powershell
$env:GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
python scripts/catalogue_audit.py --company Microsoft --phase inventory
python scripts/catalogue_audit.py --company Microsoft --phase enrich --enrich-limit 50
python scripts/catalogue_audit.py --company Microsoft --phase export
```

Bash:

```bash
export GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
python3 scripts/catalogue_audit.py --company Microsoft --phase all --enrich-limit 50
```

The `--company` filter accepts a company name or GitHub account login. Omit it to process every eligible mapping. Use `--include-unverified` only when deliberately scanning candidate handles; generated records retain the unverified mapping warning.

## Phases and resume behaviour

- **inventory:** fetch every page of public repository metadata; keep forks and archived projects; persist the next page and accumulated rows after every response.
- **enrich:** fetch a repository README, language-byte statistics, recursive repository tree and up to six representative build/dependency manifests. Save each repository immediately.
- **export:** generate an account index and one Markdown dossier per repository.
- **all:** execute inventory, enrich a bounded batch, then export.

Useful options:

| Option | Meaning |
|---|---|
| `--enrich-limit 50` | Capture evidence for up to 50 repositories per account per run |
| `--enrich-limit 0` | Process all pending repositories for that account |
| `--manifest-limit 6` | Maximum manifests retrieved per repository |
| `--max-pages 1` | Test with one inventory page; capped runs are never marked complete |
| `--refresh-inventory` | Re-enumerate from page one while preserving existing repository audit captures |
| `--force-enrich` | Re-fetch README/language/manifest evidence for already captured repositories |

Re-running the same account resumes from its saved `next_page` and skips README captures already completed or confirmed unavailable. Keep the generated inventory JSON files: they are the checkpoints.

## Output layout

```text
organizations/<company>/
  ACCOUNT-INVENTORY.md
  accounts/<github-account>/
    README.md
    repositories/
      inventory.json
      AUDIT-INDEX.md
      INVENTORY.md
      <repository-name>-<github-id>.md
```

- `inventory.json` stores repository metadata and per-repository capture state.
- `AUDIT-INDEX.md` lists every enumerated public repository for that account.
- Each Markdown dossier contains the GitHub description, README introduction/headings and selected evidence excerpts, language byte statistics, manifest links and dependency clues, license/archive/fork metadata and the current review state.
- Raw README and manifest files are cached in `.catalogue-cache/`, which is ignored by Git.

## Evidence boundaries

README downloads are marked `readme_captured`, not fully reviewed. Captured headings and excerpts are source evidence, not a completed technical interpretation. A reviewer must still interpret the purpose, features, architecture, dependencies and limitations before marking a repository fully README-reviewed.

The manifest scan selects representative build/dependency files. Monorepos can contain many nested applications and dependency files; this first-pass capture is not a complete dependency graph. GitHub language statistics are byte counts, not a framework detector.

## GitHub Actions automation

The workflow at `.github/workflows/catalogue-inventory.yml` runs daily on verified account mappings and can be manually dispatched for one company. Each run captures a bounded number of README records per account and commits generated `organizations/` files directly to `main`.

The workflow uses the repository's `GITHUB_TOKEN`; it needs Actions permission to write repository contents and direct pushes must be allowed by branch rules. Use manual dispatch with `include_unverified=true` only after validating the handle through official evidence.

## Rate limits and scale

Large organizations need multiple API requests per repository. Authenticated requests, retries, delays and bounded runs help avoid secondary rate limits. If a run is interrupted, rerun it: saved page and repository state is designed to resume. Check workflow logs and capture errors; do not mark an account complete until pagination has reached its final page and every intended enrichment batch has been processed.

## Related guidance

- [Company/account discovery](ORGANIZATION-DISCOVERY.md)
- [Inventory process](INVENTORY-PROCESS.md)
- [Repository entry schema](REPOSITORY-ENTRY-SCHEMA.md)
- [Research status definitions](RESEARCH-STATUS.md)
