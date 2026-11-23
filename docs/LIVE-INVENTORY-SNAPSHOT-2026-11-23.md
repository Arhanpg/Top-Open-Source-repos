# Live repository inventory snapshot — 23 November 2026

## Scope

This snapshot is based on generated `ACCOUNT-INVENTORY.md` files committed after the first live GitHub Actions scan.

- Source run: [GitHub Actions run #1](https://github.com/Arhanpg/Top-Open-Source-repos/actions/runs/45248026075)
- Workflow commit scanned: `a01827a5c7582b3274687458b40ab1581815f809`
- Generated checkpoint commit: `99eda9e7bda00126f553b889a420a98314346008`
- Inventory date: 23 November 2026
- Accounts: 34
- Repository metadata records: 25,965
- Accounts with completed public-repository pagination: 34
- Manually README-reviewed repositories from this automated run: 0

## Per-company results

| Company group | Accounts | Repository records | Inventory pagination |
|---|---:|---:|---|
| Microsoft | 1 | 8,500 | Complete |
| Alphabet / Google | 1 | 2,947 | Complete |
| Apple | 1 | 194 | Complete |
| NVIDIA | 1 | 850 | Complete |
| Amazon / AWS directory | 30 | 13,474 | Complete |
| **Total** | **34** | **25,965** | **Complete for configured accounts** |

## Meaning of completion

For every configured account, the collector followed GitHub's public repository pagination until no next-page link remained. The generated account index reports `Pagination complete: True`.

This does not mean every relevant company-controlled account has been discovered, every README has been captured, every README has been interpreted, or every repository has undergone a source-code, security, licence, dependency or performance audit.

The AWS account set consists of the primary `aws` login and 29 logins in the Open Source at AWS directory. The directory-listed status records a documented relationship without claiming legal ownership or authorship of every repository.

## First README evidence batch

The workflow was configured for up to 10 enrichment candidates per account. The committed account summaries show that evidence capture began, but many repositories remain pending. README captured means the default-branch README was downloaded; README unavailable means GitHub returned no README; evidence captured means README/language/manifest data reached terminal states. Manual interpretation remains zero in the automated summaries.

Further runs must continue enrichment in bounded batches. Complete account inventories should be reused rather than paginated unnecessarily.

## Run status and empty repositories

The workflow's overall conclusion is `failure`, although pagination completed and the checkpoint commit succeeded. The two capture failures were:

- `aws-ia/.announcements`
- `NVIDIA/ADLR`

Both have no Git repository tree; GitHub returns HTTP 409 with `Git Repository is empty`. This exact response is now classified as terminal manifest unavailability. Other HTTP 409 responses remain errors.

## Account inventory links

- [Microsoft](../organizations/microsoft/ACCOUNT-INVENTORY.md)
- [Google](../organizations/alphabet-google/ACCOUNT-INVENTORY.md)
- [Apple](../organizations/apple/ACCOUNT-INVENTORY.md)
- [NVIDIA](../organizations/nvidia/ACCOUNT-INVENTORY.md)
- [Amazon / AWS](../organizations/amazon/ACCOUNT-INVENTORY.md)

## Next steps

1. Re-run after the empty-repository handling fix; the two affected repositories should reach terminal evidence states.
2. Continue README/language/manifest enrichment in small batches, preserving checkpoints.
3. Maintain an account-level evidence progress dashboard.
4. Expand official account discovery for Microsoft, Google, Apple and NVIDIA, then the remaining company mappings.
5. Interpret captured README evidence and update the curated human-reviewed dossiers separately.


See the [inventory and evidence progress dashboard](INVENTORY-PROGRESS-2026-11-23.md) for the complete 34-account table. In the first run, 286 README files were captured, 30 were unavailable, 314 repositories reached terminal README/language/manifest evidence states, 25,649 remained pending/error, and no automated records had a manual technical review.
