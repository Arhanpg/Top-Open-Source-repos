# Account discovery and inventory coverage — 24 November 2026

## Current mapping totals

The mapping CSV contains **185 account rows**:

| Mapping class | Accounts | Meaning |
|---|---:|---|
| Directly verified primary accounts | 5 | One starting account each for Microsoft, Google, Apple, NVIDIA and AWS |
| Official-directory-listed | 29 | Additional accounts linked by the official Open Source at AWS directory |
| Official-project-linked | 5 | Additional NVIDIA project accounts linked by NVIDIA's official open-source hub |
| Candidate / unverified / relationship pending | 146 | Remaining source-list mappings that require company-controlled evidence |
| **Total mapping rows** | **185** | Includes the 151 original company-source rows plus 34 secondary-account rows |

**Inventory-eligible mappings:** 39 accounts (5 directly verified + 29 AWS directory-listed + 5 NVIDIA project-linked).

## Inventory completion state

The first live scan completed public repository pagination for 34 configured accounts and committed 25,965 repository metadata records. Those accounts were:
- Microsoft: 1 account
- Google: 1 account
- Apple: 1 account
- NVIDIA primary account: 1 account
- Amazon/AWS: 30 accounts

Five NVIDIA project-linked accounts were added after that first scan and are not included in the 25,965 baseline. Their pagination must finish before an updated combined repository count is reported.

- [First live inventory snapshot](LIVE-INVENTORY-SNAPSHOT-2026-11-23.md)
- [First-run evidence progress dashboard](INVENTORY-PROGRESS-2026-11-23.md)
- [GitHub Actions run history](https://github.com/Arhanpg/Top-Open-Source-repos/actions)

## Manual README documentation

The curated company folders contain **51 manually interpreted README-based dossiers**:

| Company | Manually reviewed project dossiers |
|---|---:|
| Microsoft | 18 |
| Google | 8 |
| Apple | 7 |
| NVIDIA | 13 |
| Amazon / AWS | 5 |
| **Total** | **51** |

These are selected technical briefs, not a full manual audit of all 25,965 inventoried repositories.

## Company-wide completeness

No company is yet marked company-wide complete. The current verified/linked accounts are an expanding starting set, not a complete list of every product, engineering, research, cloud, subsidiary or acquired-business account. The remaining source-list account mappings require verification against company-controlled sources before they should be attributed to those companies.
