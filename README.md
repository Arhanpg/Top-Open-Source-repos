# Top Open-Source Repositories by Leading Companies

A structured research catalogue for discovering and understanding publicly available GitHub repositories associated with leading technology and technology-enabled companies.

The company universe currently comes from the supplied `Repos.docx`: **160 source entries across 151 unique companies**. The document groups companies into United States & Global, Europe, China and India. It does not provide a Russia list.

---

## Start here: catalogue tour

| Step | Where to go | What you will find |
|---|---|---|
| 1 | [Browse by region](#browse-by-region) | Company lists grouped by the source document |
| 2 | [Open an organization folder](#organization-folders) | Company overview, account mapping and repository index |
| 3 | Open a repository's Markdown page | A technical brief based on that project's README |
| 4 | [Read the research standards](#how-to-read-the-records) | What each status means and how evidence is recorded |
| 5 | [Run the inventory collector](#scaling-the-catalogue) | A resumable tool for large public repository inventories |

## Browse by region

| Region | Source entries | Index |
|---|---:|---|
| United States & Global | 50 | [Open index](companies/united-states-global/README.md) |
| Europe | 50 | [Open index](companies/europe/README.md) |
| China | 30 | [Open index](companies/china/README.md) |
| India | 30 | [Open index](companies/india/README.md) |

A company can appear in more than one source group. For example, companies repeated in the source document are consolidated into one organization directory, while the regional index preserves their source-group appearances.

## Organization folders

All company-level documentation is under [`organizations/`](organizations/). A typical folder looks like this:

```text
organizations/
  microsoft/
    README.md
    repositories/
      README.md
      markitdown.md
      playwright.md
      typescript.md
      ...
  apple/
    README.md
    repositories/
      README.md
      container.md
      foundationdb.md
```

Each company README records the candidate GitHub account, mapping status, inventory state and links to project records. Each repository index lists projects whose README has been reviewed. A company directory being present does **not** mean that its repository inventory is complete.

## What a repository page contains

The individual Markdown pages are intended to be compact technical briefs rather than just lists of links. As evidence becomes available, each page should document:

1. **Identity:** company, canonical repository URL, default branch and direct README URL.
2. **Purpose:** the problem the maintainers say the project solves.
3. **Capabilities:** features and workflows actually described by upstream documentation.
4. **Technology:** languages, frameworks, package managers, model runtimes, databases and infrastructure, with evidence for each.
5. **Getting started:** upstream installation / quick-start links or commands.
6. **Fit and limitations:** where the project may be useful, platform constraints, security warnings and lifecycle status.
7. **Evidence:** README blob SHA and links to manifests or relevant documentation.

Where a point is not supported by inspected sources, it should be left unknown or described as requiring further review. It should not be filled with assumptions based on the company sector or repository name.

## Initial README-reviewed project samples

These are the first documented examples in the catalogue, not a ranking of the companies' best projects:

| Company | Project | What it does |
|---|---|---|
| Microsoft | [MarkItDown](organizations/microsoft/repositories/markitdown.md) | Converts multiple document and media formats into Markdown for text / LLM workflows |
| Microsoft | [Playwright](organizations/microsoft/repositories/playwright.md) | Cross-browser automation and end-to-end testing |
| Microsoft | [Qlib](organizations/microsoft/repositories/qlib.md) | AI-oriented quantitative investment research and backtesting platform |
| Microsoft | [GraphRAG](organizations/microsoft/repositories/graphrag.md) | Research pipeline exploring graph-derived context for LLM question answering |
| Apple | [container](organizations/apple/repositories/container.md) | Runs Linux containers as lightweight VMs on Apple silicon Macs |
| Apple | [FoundationDB](organizations/apple/repositories/foundationdb.md) | Distributed transactional ordered key-value database |
| Google | [LangExtract](organizations/alphabet-google/repositories/langextract.md) | LLM-powered structured extraction with source-span grounding |
| NVIDIA | [Megatron-LM](organizations/nvidia/repositories/megatron-lm.md) | GPU-optimized transformer training and parallelism |
| NVIDIA | [TensorRT-LLM](organizations/nvidia/repositories/tensorrt-llm.md) | Optimized inference framework for LLMs and visual-generation models |
| Amazon / AWS | [AWS CDK](organizations/amazon/repositories/aws-cdk.md) | Infrastructure as Code framework using CloudFormation |

More reviewed records are listed in the relevant company repository indexes.

## How to read the records

### Company-account mapping

A company name and a similarly named GitHub account are not enough to establish ownership. A mapping should be confirmed through a company-controlled website, engineering blog, product documentation or reciprocal official link. Some companies publish software through multiple organizations, foundations, product teams or employee accounts; those should be recorded separately with the relationship explained.

### Repository review statuses

- **mapping unverified:** the GitHub account is a research lead, not a verified corporate account.
- **metadata only:** repository metadata has been captured, but the README has not been inspected.
- **README reviewed:** the README has been opened and summarized; the record includes a source link and evidence note.
- **README unavailable:** the repository exists but no usable README could be retrieved.
- **no public org found:** no official public GitHub account was verified after checking company-controlled sources.
- **inventory complete:** every page of the public repository listing for the verified account has been retrieved and the final page confirmed.

A README-reviewed project page is not a source-code audit, security review, dependency vulnerability scan or performance benchmark. Those are separate tasks.

## Scaling the catalogue

The catalogue includes a resumable public repository inventory collector:

- [Canonical collector](scripts/catalogue_audit.py)
- [Legacy compatibility entry point](scripts/audit_org_repos.py)
- [Collector usage guide](docs/INVENTORY-COLLECTOR.md)
- [Offline collector tests](tests/test_catalogue_audit.py)
- [GitHub Actions run history](https://github.com/Arhanpg/Top-Open-Source-repos/actions)
- [Company account mapping CSV](config/company_accounts.csv)
- [Repository entry schema](docs/REPOSITORY-ENTRY-SCHEMA.md)
- [Inventory process](docs/INVENTORY-PROCESS.md)
- [Research status definitions](docs/RESEARCH-STATUS.md)

The canonical collector resolves account_type=auto, follows repository pagination, writes tracked per-account inventory.json checkpoints, and captures README excerpts/headings, language-byte statistics and selected manifest paths in bounded batches. Automated captures remain pending human interpretation. It skips unverified company-account mappings by default.

For large organizations, run the collector in resumable batches with a GitHub token. Record the retrieval date, page count and final-page completion state. Do not label a company inventory complete merely because the first 100 results were returned.

## Project principles

- Prefer official upstream sources and link to the canonical repository.
- Preserve archived and fork status; do not silently discard records.
- Distinguish programming languages from frameworks, libraries, runtimes and infrastructure.
- Keep README-derived facts separate from interpretation and recommendations.
- Avoid copying large portions of upstream documentation; summarize and link to it.
- Revisit repository pages over time because dependencies, supported runtimes and project status change.

## Contributing research

When adding a new company or project, follow the shared [repository entry schema](docs/REPOSITORY-ENTRY-SCHEMA.md). If the README is unclear, inspect the relevant package manifests or official documentation. Record evidence and date of review, and leave unsupported information blank rather than guessing.

---

*This is an evolving research catalogue. Counts and review status describe only the work actually present in the repository at the time of the latest update.*


## Automated public inventory

The repository now includes a resumable auditor and a scheduled GitHub Actions workflow:

- [Canonical collector](scripts/catalogue_audit.py)
- [Legacy compatibility entry point](scripts/audit_org_repos.py)
- [Scheduled/manual workflow](.github/workflows/catalogue-inventory.yml)
- [Company/account discovery rules](docs/ORGANIZATION-DISCOVERY.md)
- [Collector usage and resume guide](docs/INVENTORY-COLLECTOR.md)
- [Account mapping CSV](config/company_accounts.csv)

The workflow enumerates public repositories through API pagination, then captures README, language and selected manifest evidence in bounded batches. It commits generated account indexes and per-repository Markdown dossiers directly to `main`. Daily runs include directly verified accounts and accounts explicitly listed in official company open-source directories; name-only candidates remain excluded. Manual dispatch can select one company and optionally include unverified candidates.

**Important:** a captured README is not the same as a fully interpreted technical audit, and a primary GitHub organization is not necessarily every organization owned by a company. See the discovery guide and review-status documentation.


## README review batch — 23 November 2026

A total of 28 additional repository dossiers have been added across Microsoft, Google, Apple, NVIDIA and AWS. See [the batch report](docs/README-REVIEW-BATCH-2026-11-23.md) for the full list and important lifecycle caveats. The five dated discovery JSON files each contain a first-page ranked search sample of up to 100 repositories. These samples are not exhaustive account inventories.


The follow-on review added six further projects, bringing the five starting account folders to 46 detailed README briefs. The project list and lifecycle findings are included in the [batch report](docs/README-REVIEW-BATCH-2026-11-23.md).


## Collector reliability update — 24 November 2026

The collector now uses tracked per-account checkpoints under organizations/<company>/accounts/<login>/, so interrupted inventory pages and README enrichment can resume across fresh GitHub Actions runners. See the [reliability report](docs/COLLECTOR-RELIABILITY-UPDATE-2026-11-24.md) and revised [collector guide](docs/INVENTORY-COLLECTOR.md). The five starting account folders currently contain 46 curated README-based briefs; this is separate from the automated inventory still to be collected.


The Actions workflow first runs Python compilation and the offline collector tests before attempting an inventory scan. The workflow is committed, but a successful live inventory still needs to be confirmed in the [Actions run history](https://github.com/Arhanpg/Top-Open-Source-repos/actions).


## Additional official AWS account coverage — 24 November 2026

The company-controlled [Open Source at AWS](https://aws.github.io/) website lists 30 GitHub organization links, including the primary `aws` account. The mapping now includes 29 additional directory-listed accounts under Amazon/AWS with explicit attribution caveats. This brings the inventory-eligible mappings to 34 accounts across five primary companies plus the AWS directory expansion; it does not make all 151 company inventories complete.

See [Amazon/AWS account discovery](organizations/amazon/ACCOUNT-DISCOVERY.md) and [the organization discovery method](docs/ORGANIZATION-DISCOVERY.md).


## First live inventory snapshot — 23 November 2026

The first live GitHub Actions run completed pagination for 34 configured accounts and committed 25,965 public repository metadata records. See the [live inventory snapshot](docs/LIVE-INVENTORY-SNAPSHOT-2026-11-23.md) and [Actions run #1](https://github.com/Arhanpg/Top-Open-Source-repos/actions/runs/45248026075). This is a metadata inventory; the first README evidence batch is partial and manual technical review remains outstanding.


## Inventory progress dashboard

The first live scan enumerated 25,965 public repository records across 34 configured accounts. [Open the detailed inventory and evidence progress dashboard](docs/INVENTORY-PROGRESS-2026-11-23.md) for per-account counts, README capture coverage, manifest evidence and pending work. The figures distinguish repository pagination from README interpretation.


## NVIDIA project-account expansion — 24 November 2026

The [official Open Source at NVIDIA hub](https://opensource.nvidia.com/llm-info/) links five additional GitHub project accounts beyond the primary `NVIDIA` organization. They are mapped as `official-project-linked` to distinguish project association from blanket legal ownership. See [NVIDIA account discovery](organizations/nvidia/ACCOUNT-DISCOVERY.md). The inventory-eligible account mapping now contains 39 accounts: five primary verified, 29 AWS directory-listed and five NVIDIA project-linked.


The first live inventory baseline covered 34 accounts and 25,965 repositories. Five NVIDIA project-linked accounts were added afterwards from the official NVIDIA open-source hub, bringing the configured inventory target to 39 accounts. Their own public-repository pagination must complete before a new combined repository total is reported.


## Latest manual README reviews — 24 November 2026

Five additional NVIDIA project repositories have now been documented from their upstream READMEs: [Isaac ROS Visual SLAM](organizations/nvidia/repositories/isaac-ros-visual-slam.md), [Cosmos-Predict2.5](organizations/nvidia/repositories/cosmos-predict2-5.md), [cuGraph](organizations/nvidia/repositories/cugraph.md), [Dynamo](organizations/nvidia/repositories/dynamo.md) and [Triton Inference Server](organizations/nvidia/repositories/triton-inference-server.md). The five company folders now contain **51 manually interpreted README-based project briefs** in total. This remains a curated subset of the much larger automated repository inventories.


[Account discovery and inventory coverage status](docs/ACCOUNT-DISCOVERY-STATUS-2026-11-24.md) tracks eligible accounts, candidate mappings and the separation between inventory completion and manual README documentation.


## Microsoft project-account expansion — 24 November 2026

Microsoft Learn's official contributor guide links repositories in three additional accounts: [MicrosoftDocs](https://github.com/MicrosoftDocs), [dotnet](https://github.com/dotnet) and [Azure](https://github.com/Azure). They are mapped with the distinct `official-project-linked` status. This raises the configured inventory target from 39 to **42 accounts**; these three accounts require their own pagination and are not included in the first 25,965-repository baseline.

See [Microsoft Account Discovery](organizations/microsoft/ACCOUNT-DISCOVERY.md). Microsoft's official Open Source Program says it has more than 100 GitHub organizations, so the wider discovery task remains incomplete.


## Automated enrichment cadence

The scheduled collector now runs four times per day (02:23, 08:23, 14:23 and 20:23 UTC) with a default batch of 10 repositories per eligible account per run. The 42 currently eligible mappings allow up to 1,680 enrichment candidates per day before API limits, retries and unavailable README states. See the [collector guide](docs/INVENTORY-COLLECTOR.md) for the exact run semantics.


## Apple project review and account expansion — 24 November 2026

Five additional Apple Open Source projects now have individual technical briefs: [Password Manager Resources](organizations/apple/repositories/password-manager-resources.md), [ServiceTalk](organizations/apple/repositories/servicetalk.md), [Containerization](organizations/apple/repositories/containerization.md), [Swift](organizations/apple/repositories/swift-language.md) and [MLX](organizations/apple/repositories/mlx.md). Apple's official project pages link Swift to the swiftlang GitHub account and MLX to ml-explore; both are mapped as project-linked accounts. The curated five-company total is now **56** README-based project briefs, while the inventory-eligible account target is **44**.


## SAP and Siemens account-family expansion — 24 November 2026

The account map now includes ten additional SAP organizations listed by SAP's verified GitHub profile and two Siemens product-specific organizations linked by Siemens's official open-source portal. SAP and Siemens primary accounts are also now directly verified. This adds 14 inventory-eligible account rows (including the two promoted primary mappings) and brings the configured eligible set to **58 accounts**. See [SAP](organizations/sap/ACCOUNT-DISCOVERY.md), [Siemens](organizations/siemens/ACCOUNT-DISCOVERY.md) and the [account discovery status](docs/ACCOUNT-DISCOVERY-STATUS-2026-11-24.md).


## Baidu and Tencent account verification — 24 November 2026

The primary [Baidu](https://github.com/baidu) and [Tencent](https://github.com/Tencent) GitHub organizations are now directly verified against their company open-source domains. Baidu's profile names three affiliated organizations—PaddlePaddle, ApolloAuto and XuperChain—which are mapped separately as project-linked accounts. The catalogue now has **63 inventory-eligible accounts**; their pagination must complete before any revised combined repository total is reported. See [Baidu Account Discovery](organizations/baidu/ACCOUNT-DISCOVERY.md) and [Tencent Account Discovery](organizations/tencent/ACCOUNT-DISCOVERY.md).


## Baidu and Tencent README review — 24 November 2026

Five additional detailed project dossiers are now indexed: [PaddleOCR](organizations/baidu/repositories/paddleocr.md), [Apollo](organizations/baidu/repositories/apollo.md), [XuperChain](organizations/baidu/repositories/xuperchain.md), [WeKnora](organizations/tencent/repositories/weknora.md) and [ncnn](organizations/tencent/repositories/ncnn.md). The curated company set now has **61 manually interpreted README-based project briefs** across seven company folders.


## Latest catalogue status — 24 November 2026

The company mapping now contains 205 rows and 63 inventory-eligible GitHub accounts. The first live inventory baseline is still 25,965 repositories across the original 34 accounts; additional accounts need their own committed pagination before a new combined total is stated. The manually interpreted catalogue now contains 61 project dossiers across Microsoft, Google, Apple, NVIDIA, Amazon/AWS, Baidu and Tencent. See [the account discovery and inventory status](docs/ACCOUNT-DISCOVERY-STATUS-2026-11-24.md).


## Google Cloud account expansion — 24 November 2026

Google Cloud's official documentation links language-specific sample repositories under the separate [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform) GitHub account. It is now mapped as `official-project-linked` and will be paginated independently from `google`. The inventory-eligible mapping has increased to **64 accounts**.


## SAP and Siemens README review — 24 November 2026

Five new detailed project dossiers now cover [Kyma](organizations/sap/repositories/kyma.md), [OpenUI5](organizations/sap/repositories/openui5.md), [Elektra](organizations/sap/repositories/elektra.md), [MindConnect NodeJS](organizations/siemens/repositories/mindconnect-nodejs.md) and the [Industrial Edge hands-on app](organizations/siemens/repositories/industrial-edge-hands-on-app.md). The curated catalogue now contains **66 manually interpreted README-based project briefs** across nine company folders.


## Current verified project and account totals — 24 November 2026

The manually interpreted catalogue now contains **66 README-based project dossiers** across nine companies. The mapping contains **206 rows**, with **64 inventory-eligible accounts** (9 verified, 39 official-directory-listed and 16 official-project-linked). The historical live inventory baseline remains 25,965 public repositories across the original 34 accounts; added accounts need their own committed pagination before a revised total is reported.


## Further SAP technical documentation — 24 November 2026

The SAP folder now includes [ABAP Cheat Sheets](organizations/sap/repositories/abap-cheat-sheets.md) and [SAPUI5 Documentation Source](organizations/sap/repositories/sapui5-docs.md). These bring the manually interpreted project dossier total to **68** across nine company folders.


## Live inventory milestone — 24 November 2026

Historical snapshot before the Google Gemini account was added: the successful collector run completed pagination for 64 accounts and enumerated **33,470 public repository records**. The later reconciliation covers 65 accounts and 33,522 repositories; see the current section below and [Live Inventory and Evidence Snapshot](docs/LIVE-INVENTORY-SNAPSHOT-2026-11-24.md). The 142 unresolved candidate/unverified company-account mappings still prevent a claim of exhaustive company-wide account discovery.


## Google Cloud and Gemini README review — 24 November 2026

Seven new project dossiers now cover [Online Boutique](organizations/alphabet-google/repositories/online-boutique.md), [Google Cloud Generative AI samples](organizations/alphabet-google/repositories/google-cloud-generative-ai-samples.md), [Terraformer](organizations/alphabet-google/repositories/terraformer.md), [kubectl-ai](organizations/alphabet-google/repositories/kubectl-ai.md), [Agent Starter Pack](organizations/alphabet-google/repositories/agent-starter-pack.md), [Agents CLI](organizations/alphabet-google/repositories/agents-cli.md) and the [Gemini API Cookbook](organizations/alphabet-google/repositories/gemini-api-cookbook.md). The curated catalogue now has **75 manually interpreted dossiers**. The separately linked `google-gemini` account has been added to the map; it is not included in the current 64-account / 33,470-repository pagination snapshot.


## Latest account reconciliation — 24 November 2026

The mapping contains **207 rows**: 65 inventory-eligible GitHub accounts and 142 unresolved candidates/unverified mappings. The 64-account / 33,470-repository figure is a historical baseline; the later 65-account / 33,522-repository reconciliation is shown in the current audit section. The curated technical catalogue is a separate manually interpreted subset.


## Microsoft account README review — 24 November 2026

Three new Microsoft project briefs are available: [Azure Documentation Source](organizations/microsoft/repositories/azure-docs.md), [.NET Documentation Source](organizations/microsoft/repositories/dotnet-docs.md) and [Azure SDK for .NET](organizations/microsoft/repositories/azure-sdk-for-net.md). They bring the selected manual catalogue to **78 project dossiers** across nine companies.


## Current 33,522-repository audit — 24 November 2026

All **65 configured inventory accounts** currently have completed public-repository pagination, representing **33,522 public repository records**. The automated evidence collector has captured 2,075 READMEs and reached terminal README/language/manifest evidence states for 2,137 records. **31,385 remain pending or errored**; these require more enrichment runs and retries. Human technical interpretation is a separate status and is not implied by these counts.

The pipeline now paces REST requests, rotates pending repositories fairly, uses raw public file retrieval for selected manifest/README bodies, performs four daily enrichment runs and refreshes account inventories weekly. See the [reconciled backlog and company totals](docs/COLLECTOR-RELIABILITY-UPDATE-2026-11-24.md), [collector guide](docs/INVENTORY-COLLECTOR.md), and [GitHub Actions](https://github.com/Arhanpg/Top-Open-Source-repos/actions).


## Latest collector validation

The latest collector update adds a 3.6-second REST request pace, short evidence snippets matched to README sections, and an updated daily-enrichment / weekly-inventory schedule. The latest 26-test preflight passed in [Actions run #17](https://github.com/Arhanpg/Top-Open-Source-repos/actions/runs/45324524032); the enrichment step was still in progress at the latest check. Repository totals will be updated after its checkpoints are committed.


The daily collector now uses a global fair batch of up to **1,200 repositories per run** across eligible accounts. It rotates one repository per account per round and reallocates unused capacity from completed queues to the accounts with larger backlogs.


## Per-repository technical audits

The catalogue now includes a second, resumable stage to generate one YAML technical record and one Markdown dossier per inventoried repository. Files are written beneath `organizations/<company>/accounts/<github-account>/technical-audits/`. Each account receives a `TECHNICAL-AUDIT-INDEX.md`; global status is tracked in [docs/TECHNICAL-AUDIT-PROGRESS.md](docs/TECHNICAL-AUDIT-PROGRESS.md).

- [Technical-audit pipeline and setup](docs/TECHNICAL-AUDIT-PIPELINE.md)
- [YAML technical-audit schema](docs/TECHNICAL-AUDIT-SCHEMA.md)
- [Technical-audit progress](docs/TECHNICAL-AUDIT-PROGRESS.md)
- [Technical-audit generator](scripts/repository_technical_audit.py)
- [Technical-audit tests](tests/test_repository_technical_audit.py)

The scheduled workflow defaults to 200 dossiers per run and interleaves accounts fairly. Configure repository secret `AUDIT_LLM_API_KEY` (or `OPENROUTER_API_KEY`) and variable `AUDIT_LLM_MODEL` for semantic interpretation of project purpose, features and technology stack. Without those settings, the generator still creates evidence-only records and leaves unsupported claims unknown. Neither generated status is a human sign-off or exhaustive code/security audit.
