# Account discovery and inventory coverage — 24 November 2026

## Current mapping totals

The mapping CSV contains **205 account rows**:

| Mapping class | Accounts | Meaning |
|---|---:|---|
| Directly verified primary accounts | 9 | Five initial primary accounts plus SAP, Siemens, Baidu and Tencent, whose GitHub organizations are verified |
| Official-directory-listed | 39 | 29 AWS accounts plus 10 dedicated SAP organizations named by SAP's verified GitHub profile |
| Official-project-linked | 15 | Five NVIDIA, three Microsoft, two Apple, two Siemens and three Baidu-affiliated project accounts |
| Candidate / unverified / relationship pending | 146 | Remaining source-list mappings that require company-controlled evidence |
| **Total mapping rows** | **205** | Includes the 151 original company-source rows plus 34 secondary-account rows |

**Inventory-eligible mappings:** 63 accounts (9 directly verified + 39 official-directory-listed + 15 official-project-linked).

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


## SAP and Siemens expansion — 24 November 2026

The verified SAP profile names ten dedicated project organizations, and Siemens's official open-source portal names two product-specific organizations. SAP and Siemens primary account rows have been promoted to directly verified. Ten SAP rows use `official-directory-listed`, and two Siemens rows use `official-project-linked`. The mapping now has 202 rows and 58 inventory-eligible accounts. Their pagination is not included in the historic 25,965-repository baseline.


## Baidu and Tencent verification amendment — 24 November 2026

Baidu and Tencent primary organizations were promoted to directly verified using their GitHub verified-organization pages. Baidu's profile also lists PaddlePaddle, ApolloAuto and XuperChain as affiliated organizations; those three accounts were added with `official-project-linked`. Baidu AI Cloud is not mapped as an independent account because no standalone public GitHub login was confirmed. The mapping now contains 205 rows and 63 inventory-eligible accounts.


## Manual README interpretation update — 24 November 2026

Five further READMEs were manually interpreted from Baidu-affiliated and Tencent repositories: PaddleOCR, Apollo, XuperChain, WeKnora and ncnn. The curated project-dossier total is now **61**. This is a selected technical-documentation set, not a manual audit of all enumerated repositories.
