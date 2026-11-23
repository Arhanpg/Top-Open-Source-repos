# Account discovery and inventory coverage — 24 November 2026

## Current mapping totals

The mapping CSV contains **190 account rows**:

| Mapping class | Accounts | Meaning |
|---|---:|---|
| Directly verified primary accounts | 5 | One starting account each for Microsoft, Google, Apple, NVIDIA and AWS |
| Official-directory-listed | 29 | Additional accounts linked by the official Open Source at AWS directory |
| Official-project-linked | 10 | Five NVIDIA project accounts, three Microsoft documentation-linked accounts and two Apple project-linked accounts |
| Candidate / unverified / relationship pending | 146 | Remaining source-list mappings that require company-controlled evidence |
| **Total mapping rows** | **190** | Includes the 151 original company-source rows plus 34 secondary-account rows |

**Inventory-eligible mappings:** 44 accounts (5 directly verified + 29 AWS directory-listed + 5 NVIDIA project-linked + 3 Microsoft documentation-linked + 2 Apple project-linked).

## Inventory completion state

The first live scan completed public repository pagination for 34 configured accounts and committed 25,965 repository metadata records. Those accounts were:
- Microsoft: 1 account
- Google: 1 account
- Apple: 1 account
- NVIDIA primary account: 1 account
- Amazon/AWS: 30 accounts

Five NVIDIA, three Microsoft and two Apple project-linked accounts were added after that first scan and are not included in the 25,965 baseline. Their pagination must finish before an updated combined repository count is reported.

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


## Microsoft mapping amendment — 24 November 2026

Three additional Microsoft project-linked accounts (`MicrosoftDocs`, `dotnet`, `Azure`) were added from Microsoft Learn contributor guidance. The total is now 42 inventory-eligible mappings and 188 CSV rows. Microsoft itself states that it maintains more than 100 GitHub organizations, so this is not a complete Microsoft account directory.


## Apple mapping amendment — 24 November 2026

Two additional Apple project-linked accounts, swiftlang and ml-explore, were added from direct links on Apple's official Open Source project pages. The catalogue now has 190 account mapping rows and 44 inventory-eligible accounts. These account inventories are not included in the 25,965-repository first-run baseline.
