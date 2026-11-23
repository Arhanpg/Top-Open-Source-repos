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

- [Collector script](scripts/audit_org_repos.py)
- [Collector usage guide](docs/INVENTORY-COLLECTOR.md)
- [Company account mapping CSV](config/company_accounts.csv)
- [Repository entry schema](docs/REPOSITORY-ENTRY-SCHEMA.md)
- [Inventory process](docs/INVENTORY-PROCESS.md)
- [Research status definitions](docs/RESEARCH-STATUS.md)

The collector uses GitHub's public repositories API with pagination, captures repository metadata and language-byte statistics, and caches README text locally for later review. It does not invent summaries or automatically claim that a downloaded README has been manually reviewed. It skips unverified company-account mappings by default.

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

- [Auditor loader](scripts/catalogue_audit.py)
- [Compressed implementation payload](scripts/catalogue_audit.py.gz.b64)
- [Scheduled/manual workflow](.github/workflows/catalogue-inventory.yml)
- [Company/account discovery rules](docs/ORGANIZATION-DISCOVERY.md)
- [Collector usage and resume guide](docs/INVENTORY-COLLECTOR.md)
- [Account mapping CSV](config/company_accounts.csv)

The workflow enumerates public repositories through API pagination, then captures README, language and selected manifest evidence in bounded batches. It commits generated account indexes and per-repository Markdown dossiers directly to `main`. Daily runs currently include only verified starting accounts. Manual dispatch can select one company and optionally include unverified candidates.

**Important:** a captured README is not the same as a fully interpreted technical audit, and a primary GitHub organization is not necessarily every organization owned by a company. See the discovery guide and review-status documentation.
