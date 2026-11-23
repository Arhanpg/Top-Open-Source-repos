# Inventory and README audit process

1. Verify the GitHub account using a link from the company's own website, engineering blog, or official documentation. Record whether it is an organization, corporate user, foundation, product team, or community.
2. Enumerate public repositories from the verified account using GitHub's organization/user repositories endpoint with pagination. Continue until there is no next page. Store `retrieved_at`, pages fetched, total repository count, and completion status.
3. Keep public forks, archived repositories, templates, and mirrors in the inventory but label each clearly. Exclude nothing without documenting the filter.
4. Retrieve the default branch README for every repository. If no README exists, record that explicitly. Never replace missing evidence with repository name guesses.
5. Inspect relevant dependency/build manifests to confirm technologies. Capture only high-value features actually documented by the upstream project.
6. Add each repository to the corresponding company page and machine-readable index (JSON/CSV) in a later import step. Deduplicate repositories that appear under multiple source company lists.
7. Validate URLs, counts, README status, and company mapping before marking a company inventory complete.
8. Re-run periodically; repository inventories change. Keep dated snapshots or a clear last-checked timestamp.

## Scale

For organisations with thousands of projects, generate the initial inventory programmatically and perform README extraction in resumable batches. Store per-repository checkpoints so API interruptions or rate limits do not restart the entire scan. Rate-limit requests and retry transient failures with backoff.


## Multi-organization completeness

A company can publish through several official GitHub organizations. Keep each official account as a separate row in the mapping CSV and maintain a distinct account inventory. Completing one primary account does not establish company-wide completeness. Follow [ORGANIZATION-DISCOVERY.md](ORGANIZATION-DISCOVERY.md) before marking a company's account discovery complete.
