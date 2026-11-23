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
