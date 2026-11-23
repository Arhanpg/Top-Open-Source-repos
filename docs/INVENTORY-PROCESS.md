# Inventory and README audit process

1. Verify the GitHub account through a company-controlled website, engineering blog or official documentation. Record the exact login, account type, source URL and scope limitation.
2. Keep every official GitHub organization or user account for a company as a separate mapping row. A primary organization is not necessarily the whole company.
3. Enumerate public repositories using complete GitHub REST API pagination. Continue until the response contains no next-page link. Store page count, retrieval time, repository count and completion status.
4. Preserve public forks, archived repositories, templates and mirrors, while labelling each accurately. Do not silently filter them.
5. Retrieve README evidence for each repository. Record README-unavailable results explicitly; never infer purpose from a repository name.
6. Capture GitHub language-byte statistics and selected build/dependency manifest paths. Do not infer frameworks from language statistics or filenames alone.
7. Generate an individual evidence dossier and inventory row for each repository. Automated capture remains distinct from a human README review.
8. Manually interpret the README's purpose, features, stack and limitations before assigning the README-reviewed status.
9. Validate account ownership evidence, repository links, counts, README states and pagination before marking an account inventory complete.
10. Re-run inventories periodically and preserve dated snapshots or a last-checked timestamp.

## Checkpoints and scale

The canonical collector writes each account's pagination state to the tracked file organizations/<company>/accounts/<login>/inventory.json after every page and each repository enrichment. This makes the process resumable across fresh GitHub Actions runners. A bounded max-pages test is never reported as complete. A completed account is not re-enumerated unless refresh-inventory is requested.

For large accounts, enrich repositories in controlled batches. Keep API retry/backoff enabled, and monitor rate limits. A README capture is not the same as a completed technical interpretation.

## Company-wide completeness

Company-wide completeness requires both:
- a documented discovery pass for the company's relevant official GitHub organizations/users, including product teams, cloud divisions, research groups, subsidiaries and acquired businesses; and
- complete public-repository pagination for each verified account.

Completing one account must never be presented as completing the whole company.
