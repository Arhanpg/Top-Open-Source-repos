# Public GitHub repository inventory collector

The canonical collector is scripts/catalogue_audit.py. It uses only the Python 3.12 standard library and GitHub's REST API. The compatibility entry point scripts/audit_org_repos.py delegates to the same implementation.

## Requirements

- Python 3.11 or newer.
- A GitHub token in GITHUB_TOKEN (recommended for authenticated API limits).
- A company/account row in config/company_accounts.csv.
- A verified, official-directory-listed or official-project-linked mapping status for normal scheduled collection. Name-based candidate mappings are skipped unless explicitly included.

## Quick start

PowerShell:

~~~powershell
$env:GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
python scripts/catalogue_audit.py --company Microsoft --phase inventory --max-pages 1
python scripts/catalogue_audit.py --company Microsoft --phase all --enrich-limit 50
~~~

Bash:

~~~bash
export GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
python3 scripts/catalogue_audit.py --company Microsoft --phase all --enrich-limit 50
~~~

The first command is a bounded test: it deliberately does not mark the inventory complete. The second command resumes from the saved next-page checkpoint and begins README enrichment.

## Account type and repository pagination

The mapping CSV currently uses account_type=auto for the five verified starting accounts. The collector resolves account type from the public GitHub profile endpoint and then uses the correct public repository endpoint:

- Organization: /orgs/{login}/repos with public repositories.
- User: /users/{login}/repos with repositories owned by that user.

It requests 100 records per page and follows GitHub's Link: rel="next" header. Every retrieved page is written immediately to the tracked inventory.json checkpoint. If the default branch or pushed commit changes, README/language/manifest evidence is invalidated and queued for re-capture; a previous manual README review is marked as requiring refresh. When an account is interrupted, rerunning the collector continues at the saved next_page; it does not start from page one unless --refresh-inventory is requested.

Archived repositories and forks are retained and labelled. Only public repositories are collected. A primary company account is not proof that all product, research, cloud or subsidiary accounts have been discovered.

## Phases and command-line options

| Option | Meaning |
|---|---|
| --phase inventory | Enumerate public repository metadata and save page checkpoints. |
| --phase enrich | Capture README, language statistics and selected manifest paths for pending repositories. |
| --phase export | Rebuild the account inventory Markdown and company account summary from saved checkpoint data. |
| --phase all | Inventory (or resume), enrich a bounded batch, and export. |
| --company Microsoft | Filter by a case-insensitive company name or GitHub login. |
| --enrich-limit 50 | Capture evidence for up to 50 repositories per account in per-account mode. |
| --total-enrich-limit 1200 | Use a global fair batch of up to 1,200 repositories across the selected accounts. |
| --enrich-limit 0 | Process every pending repository for the selected account(s). |
| --manifest-limit 6 | Maximum number of representative manifest paths recorded per repository. |
| --max-pages 1 | Test cap for inventory pages; a capped scan remains incomplete. |
| --refresh-inventory | Rescan from page one and retain previously captured README evidence. |
| --force-enrich | Re-fetch README, language and manifest evidence for previously enriched repositories. |
| --include-unverified | Include candidate mappings; the resulting account records retain the unverified warning. |

A complete account inventory is only reported after GitHub pagination returns no next page. Search results and a first page of 100 repositories are not completion evidence.

## Tracked output and resume behaviour

Generated files live under:

~~~text
organizations/<company-slug>/
  ACCOUNT-INVENTORY.md
  accounts/<github-login>/
    README.md
    INVENTORY.md
    inventory.json
    repositories/
      <repository-name>-<github-repository-id>.md
~~~

- inventory.json stores all repository metadata, pagination state, next page and per-repository evidence status. It is tracked by Git, so a fresh GitHub Actions runner can resume.
- README.md summarizes account-level counts and distinguishes captured evidence from manual review.
- INVENTORY.md lists all enumerated repositories and links to generated dossiers.
- Each dossier includes GitHub metadata, the README blob SHA, up to 25 words of evidence excerpts selected from matching README sections, README headings, language-byte statistics, selected build/dependency manifest paths, conservative dependency-name clues where the manifest parser supports them, lifecycle fields and the exact upstream README link. Manifest files larger than 256 KB are not downloaded.
- The existing curated company-level repositories/ pages are preserved; automated evidence is written below the separate accounts/<login>/ directory.

The collector does not cache whole upstream READMEs in the Git repository. It keeps a brief excerpt and source SHA/link so later reviewers can open the canonical source.

## Review-state meanings

- metadata only: repository metadata is present; evidence capture has not completed.
- evidence captured; manual review pending: README section excerpts/headings, language metadata and manifest-tree inspection reached terminal states. A person still needs to interpret purpose, features, stack and limitations.
- README unavailable: GitHub returned 404 for the README endpoint.
- evidence capture incomplete: one or more API capture operations failed and should be retried.
- README reviewed: reserved for a human technical interpretation; the automated collector never assigns this state.

GitHub language statistics are byte counts, not framework detection. Manifest filenames help locate evidence but are not by themselves proof that a repository uses a particular framework. Dependency names are recorded as clues only and still require human interpretation. Recursive trees may be marked truncated for very large repositories.

## Rate limits and recovery

The collector retries transient HTTP errors, rate-limit responses and network failures with bounded backoff. Each page and each enriched repository is checkpointed before the next unit of work. If an account fails, the workflow commits whatever checkpoint files were already written, then reports the run as failed so it can be retried.

Do not remove organizations/<company>/accounts/<login>/inventory.json while an inventory is in progress. Use --refresh-inventory for a deliberate fresh enumeration. Manual README review status is separate from automated capture status.

## GitHub Actions

The workflow .github/workflows/catalogue-inventory.yml:
- Runs daily against verified mappings and refreshes repository pagination from page one.
- Supports manual execution for one company or all verified mappings.
- Supports a bounded enrichment batch size and an optional inventory refresh.
- Commits account checkpoints and generated evidence directly to main.
- Commits checkpoint changes even when the scan step reports an error, then surfaces that failure.

Direct pushes must be allowed by the repository's branch rules and the workflow's token must have contents write permission. A successful workflow file commit does not prove a scan itself has run successfully; check the Actions run history separately.

## Current scope and limitations

At the time this guide was updated, five primary accounts are marked directly verified (Microsoft, Google, Apple, NVIDIA and AWS), and 29 additional AWS-related accounts are listed by the official Open Source at AWS directory. These 34 mappings are eligible for automated inventory. Other name-based mappings remain research candidates until corroborated by official company sources. The collector inventories only the configured GitHub account; it does not discover every secondary organization automatically.

README evidence capture is not a completed architecture, security, dependency-vulnerability or performance audit. The separate project dossiers in the curated company folders remain manually interpreted records.


## Offline tests

Run the standard-library unit tests before a large scan:

~~~bash
python -m py_compile scripts/catalogue_audit.py scripts/audit_org_repos.py
python -m unittest discover -s tests -v
~~~

The suite checks dependency-name parsing for common manifest formats, automatic organization account resolution, REST request pacing, README section evidence extraction, page-cap checkpoint/resume behaviour, an interrupted scheduled refresh and empty organization handling. These tests use mocked GitHub responses and do not make live API calls.


## Official-directory-listed account eligibility

The collector treats `official-directory-listed` as an inventory-eligible mapping status. This is separate from direct ownership verification and should remain visible in the account dossier. The AWS list is sourced from the official [Open Source at AWS](https://aws.github.io/) website. The exact handles and relationship caveat are documented in [Amazon/AWS Account Discovery](../organizations/amazon/ACCOUNT-DISCOVERY.md).


## Empty and source-less repositories

GitHub can return HTTP 409 with the message `Git Repository is empty` when a public repository exists but has no commit/tree. The collector records manifest evidence as `unavailable` with an explicit reason; this is a terminal repository state, not a transient API failure. Other HTTP 409 responses remain errors and are surfaced for review.


## Official-project-linked mappings

An account may be linked as a named project from a company-controlled open-source hub without being described as a wholly owned company organization. Such rows use the status `official-project-linked`, remain eligible for public inventory, and preserve the source-specific attribution caveat. The current NVIDIA examples are documented in [NVIDIA Account Discovery](../organizations/nvidia/ACCOUNT-DISCOVERY.md).


## Microsoft documentation-linked accounts

Microsoft Learn's contributor guide directly links to repositories under `MicrosoftDocs`, `dotnet` and `Azure`. These mappings use `official-project-linked` and remain distinct from the primary `microsoft` account. The relationship proves that Microsoft documentation points contributors to projects in those accounts; it is not a claim that every repository in those accounts is Microsoft-authored. See [Microsoft Account Discovery](../organizations/microsoft/ACCOUNT-DISCOVERY.md).


## Empty README files

Some existing repositories contain a zero-byte file named `README` (without a Markdown extension). GitHub can return README metadata with no Base64 content for such a file. The collector records this as `README unavailable` with the explicit reason `README file is present but zero bytes`. A non-empty file whose content is unexpectedly absent remains a capture error.


## Scheduled enrichment cadence

The scheduled workflow runs four times per day at 02:23, 08:23, 14:23 and 20:23 UTC. Each daily run executes the enrichment phase only, with a default ceiling of 20 repositories per eligible account. With 65 mapped accounts, the theoretical batch ceiling is 1,300 repositories per run (5,200/day) before retry and rate-limit effects. GitHub REST calls are paced at approximately one request every 3.6 seconds. A separate Sunday run at 01:23 UTC refreshes repository metadata and pagination. Actual throughput is lower when README, language, or manifest capture fails or a GitHub API retry is required.


## Apple project-linked accounts

Apple's official Open Source catalogue links two separate GitHub accounts for Swift and MLX: swiftlang and ml-explore. They use official-project-linked and are inventoried independently from the primary apple organization. See [Apple Account Discovery](../organizations/apple/ACCOUNT-DISCOVERY.md).


## SAP and Siemens account families

SAP's verified GitHub profile lists ten additional dedicated organizations; these are mapped as `official-directory-listed`. Siemens's official Open Source portal lists `mindsphere` and `industrial-edge` as product-specific organizations; these are mapped as `official-project-linked`. Both groups are inventoried separately from their parent accounts. See the [SAP](../organizations/sap/ACCOUNT-DISCOVERY.md) and [Siemens](../organizations/siemens/ACCOUNT-DISCOVERY.md) discovery registers.


## Baidu and Tencent account verification

Baidu and Tencent primary GitHub organizations have now been verified by GitHub against their company open-source domains. Baidu's verified profile explicitly names PaddlePaddle, ApolloAuto and XuperChain as affiliated organizations; these use the separate `official-project-linked` status. Baidu AI Cloud is not mapped as a standalone GitHub login because a public account handle could not be confirmed. Tencent's primary account is verified; further product or subsidiary accounts still require explicit source links.


## Google Cloud project account

Google Cloud documentation links to code samples in a separate GitHub account, `GoogleCloudPlatform`. It is mapped with `official-project-linked` and inventoried separately from the primary `google` account. See [Google Account Discovery](../organizations/alphabet-google/ACCOUNT-DISCOVERY.md).


## Gemini API project-linked account

Google Cloud's official Generative AI sample README links `google-gemini/cookbook`. The separate `google-gemini` login is now mapped with `official-project-linked` and must be inventoried separately from `google` and `GoogleCloudPlatform`. The initial 64-account pagination snapshot does not contain this newly added account.


## High-volume enrichment and rate limits — 24 November 2026

The GitHub Actions workflow separates repository enumeration from README evidence enrichment:

- Four daily runs (02:23, 08:23, 14:23 and 20:23 UTC) run the enrichment phase only. They do not re-enumerate already complete account inventories.
- A separate Sunday run (01:23 UTC) refreshes repository metadata and pagination. If interrupted, the tracked next-page checkpoint resumes the scan.
- The daily workflow uses a global limit of up to 1,200 repositories per run across all selected accounts. It rotates one repository per account per round and redistributes slots when an account queue is exhausted. A persisted per-account cursor keeps repeated failures from blocking later repositories.

GitHub documents a primary limit of 1,000 REST API requests per hour for the repository GITHUB_TOKEN in Actions, plus secondary rate limits. The collector spaces REST requests at approximately 4 seconds, honours GitHub Retry-After and rate-reset headers, and fetches selected public manifest/README bodies through raw.githubusercontent.com rather than additional REST Contents requests. This is a conservative operating target, not a guarantee that every batch completes.

Each generated dossier keeps source metadata, language-byte statistics, manifest-path/dependency clues, a bounded README excerpt and an upstream source link. It remains labelled as requiring human interpretation. It is not an automated claim that purpose, feature completeness or architecture has been fully audited.


## README section evidence

The automated collector identifies relevant upstream README headings (project overview, features, getting started/usage, architecture, technology/requirements and limitations/security). It stores no more than 25 quoted words per README, split across matching sections, plus heading names, blob SHA and the canonical source link. These excerpts are evidence for human reviewers, not automatically generated summaries or a completed technical audit.


## README section evidence excerpts

For each README, the collector identifies relevant headings for project overview, features, getting started/usage, architecture/design, technology/requirements and limitations/security. It stores no more than 25 quoted words per README, split across matching sections, as short source excerpts linked to the original heading. Full README text is not copied into the inventory. These snippets support manual review; they are not generated project summaries.


## Global enrichment scheduler

The daily workflow uses total-enrich-limit instead of a fixed per-account quota. The collector builds a pending queue for each eligible account, starts with one repository from each account in sorted order, then takes a second round, continuing until the global cap is reached or no queue has pending items. When a smaller account is exhausted, its slot is naturally reallocated to accounts with more remaining work. Each account still stores its own enrichment cursor and repository checkpoints.

The global limit is set to 1,200 per run in GitHub Actions. At roughly three REST calls per repository (README metadata, language statistics and recursive Git tree), that represents up to 3,600 REST requests, around four hours at a four-second start-to-start pace. This leaves part of the six-hour job window for API retries, raw file downloads, exports and commits. The 1,200 value is a ceiling, not a guaranteed completion count.
