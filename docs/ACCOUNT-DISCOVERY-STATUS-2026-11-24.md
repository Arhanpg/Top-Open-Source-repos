# Account discovery and inventory coverage — 24 November 2026

## Current mapping totals

The mapping CSV contains **206 account rows**:

| Mapping class | Accounts | Meaning |
|---|---:|---|
| Directly verified primary accounts | 9 | Five initial primary accounts plus SAP, Siemens, Baidu and Tencent, whose GitHub organizations are verified |
| Official-directory-listed | 39 | 29 AWS accounts plus 10 dedicated SAP organizations named by SAP's verified GitHub profile |
| Official-project-linked | 16 | Five NVIDIA, three Microsoft, two Apple, two Siemens, three Baidu-affiliated and one Google Cloud project accounts |
| Candidate / unverified / relationship pending | 146 | Remaining source-list mappings that require company-controlled evidence |
| **Total mapping rows** | **206** | Includes the 151 original company-source rows plus 34 secondary-account rows |

**Inventory-eligible mappings:** 64 accounts (9 directly verified + 39 official-directory-listed + 16 official-project-linked).

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


## Google Cloud account amendment — 24 November 2026

Google Cloud's company-controlled documentation links multiple language sample repositories under the separate `GoogleCloudPlatform` GitHub account. It has been added with `official-project-linked`. The mapping now contains 206 rows and 64 inventory-eligible accounts; the first 34-account repository total does not include this account.


## Manual README review update — 24 November 2026

Five additional manually interpreted project briefs were added for SAP (Kyma, OpenUI5, Elektra) and Siemens (MindConnect NodeJS, Industrial Edge Hands-on App). The curated technical dossier total is now **66** across nine company folders. The account mapping remains 206 rows and 64 eligible accounts; repository inventory completeness is a separate measure.


## Current verified mapping and manual-dossier reconciliation — 24 November 2026

The current CSV has 206 data rows and 64 inventory-eligible accounts:

- 9 directly verified primary GitHub accounts
- 39 official-directory-listed accounts
- 16 official-project-linked accounts

The curated technical catalogue contains 66 manually interpreted README-based project dossiers across nine company folders: Microsoft 18, Google 8, Apple 12, NVIDIA 13, Amazon/AWS 5, Baidu 3, Tencent 2, SAP 3 and Siemens 2.

The first live repository pagination snapshot is still 25,965 metadata rows across the original 34 accounts. Subsequent account additions are excluded from that historical total until their own pagination checkpoints have been committed.


## Manual README review update — 24 November 2026

Two more SAP project READMEs have been interpreted: ABAP Cheat Sheets and SAPUI5 Documentation Source. The manually interpreted dossier total is now **68**, across Microsoft 18, Google 8, Apple 12, NVIDIA 13, Amazon/AWS 5, Baidu 3, Tencent 2, SAP 5 and Siemens 2. Account mapping remains 206 rows / 64 inventory-eligible accounts; no repository count is inferred from manual review work.


## Live inventory progress — 24 November 2026

Successful Actions run #45259910014 has produced complete pagination for all 64 eligible accounts and **33,470 repository metadata records**. The latest committed account summaries report 1,688 README captures, 54 unavailable README states, 1,742 terminal README/language/manifest evidence captures and 31,728 pending/error records. README capture coverage is 5.04%; terminal evidence coverage is 5.20%.

The curated catalogue separately contains 68 manually interpreted project dossiers. The autogenerated per-account manual-review metric remains zero, so these two measures must not be conflated. See [Live Inventory and Evidence Snapshot](LIVE-INVENTORY-SNAPSHOT-2026-11-24.md).
