# Running the inventory collector

The catalogue contains 160 source-company entries and 151 unique company folders. The account mappings are initial research candidates, not verified ownership claims. For safety, the collector skips unverified rows by default.

## Setup

Use Python 3.10+; the collector uses only the Python standard library.

PowerShell:

```powershell
$env:GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
python scripts/audit_org_repos.py --company Microsoft --include-unverified --max-repos 20
```

Bash:

```bash
export GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
python3 scripts/audit_org_repos.py --company Microsoft --include-unverified --max-repos 20
```

Remove `--max-repos` for a full paginated inventory of the selected account. The script supports organizations (`/orgs/{account}/repos`) and user accounts (`/users/{account}/repos`); edit `account_type` in the CSV when an account is a user rather than an organization.

## Output and resume behaviour

- `organizations/{company}/repositories/INVENTORY.md` — generated repository index with upstream URLs, descriptions, language breakdown, fork/archive flags and README review status.
- `organizations/{company}/repositories/inventory.json` — structured metadata and pagination information.
- `.catalogue-cache/{account}/{repo}/README.md` — fetched upstream README for local review; it is **not copied into the tracked catalogue**.
- `.catalogue-cache/{account}/{repo}/metadata.json` — fetched language and repository metadata.
- `.catalogue-state.json` — checkpoint of successfully processed repository names. Keep this file to resume; delete it only to force a complete refetch.

A `GITHUB_TOKEN` is strongly recommended for large organizations. The collector uses all public repositories, including forks and archived repositories, and paginates through 100 repositories per page. Do not treat a run with `--max-repos` as complete.

## Important research boundary

The script collects repository metadata and downloads README files; it does **not** invent natural-language feature summaries or claim the README has been reviewed by a researcher. After collection, inspect the local cached README and relevant manifests, then add a company repository record using the schema in `docs/REPOSITORY-ENTRY-SCHEMA.md`. Mark entries as README reviewed only after that inspection.

Before removing `--include-unverified`, verify the account using the company's own website, engineering blog or official documentation and change the mapping status in `config/company_accounts.csv` to `verified`. Do not use a similarly named account as evidence of corporate ownership.
