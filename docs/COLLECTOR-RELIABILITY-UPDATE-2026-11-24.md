# Collector reliability update — 24 November 2026

## Findings from the previous collector setup

A code review identified several mismatches between the documented collector, the GitHub Actions workflow and the verified account mapping:

1. The verified mapping rows use account_type=auto, while the older audit_org_repos.py accepted only org or user.
2. The Actions workflow passed --phase, --enrich-limit and --manifest-limit, but the older collector did not define those arguments.
3. The older collector stored its main resume state in .catalogue-state.json, which is ignored by Git. A fresh Actions runner therefore could not rely on that file being present.
4. Previously completed repositories were skipped for enrichment, while inventory output was rebuilt from current-run in-memory rows. That made cross-run inventory continuity difficult.
5. The root README linked the legacy collector while the workflow invoked a different loader.

## Changes made

- Replaced scripts/catalogue_audit.py with a readable, standard-library-only canonical implementation.
- Added automatic account-type resolution through the public GitHub profile endpoint.
- Added explicit inventory, enrichment, export and combined phases.
- Followed GitHub's pagination Link header rather than assuming one page or a search result represents a complete inventory.
- Persisted account pagination state and repository evidence to tracked inventory.json files after every page and each enrichment.
- Added bounded README excerpts, README heading capture, language-byte statistics and selected manifest-path capture.
- Kept automated evidence capture distinct from manual README review.
- Retained scripts/audit_org_repos.py as a compatibility wrapper to the canonical collector.
- Updated GitHub Actions and collector documentation to use the same CLI.

## Local verification performed

The replacement script passed Python bytecode compilation. Offline mocked tests passed for automatic organization detection, README/language/manifest evidence capture, dossier and account-index generation, skipping a fully paginated account when no refresh is requested, and stopping at a page cap before resuming from the saved next page through the final page.

These are local mocked tests, not a live GitHub Actions run. The workflow still needs an execution in the repository's Actions environment.

## Remaining work

The collector now provides a coherent base for large inventory runs, but company-wide completion still requires discovery and verification of secondary official GitHub accounts, full pagination for each verified account, repeated enrichment batches and eventual human interpretation of the captured evidence.


## Follow-on hardening

- Scheduled refreshes preserve and resume an interrupted scan's next-page checkpoint. A new scheduled scan begins only after the previous pagination run completed.
- Empty organizations remain complete after their first successful empty page and are not mistaken for uninitialized checkpoints.
- Selected small manifests are fetched with a 256 KB per-file cap, and conservative dependency-name clues are extracted for common package formats.
- Per-manifest errors create a partial evidence state instead of being represented as a successful manifest capture.


## Evidence freshness

Inventory refreshes compare the default branch and last-pushed timestamp with the previous metadata snapshot. When either changes, the collector invalidates cached README, language and manifest evidence so that the next enrichment batch captures the current source. A previously manually reviewed page is marked as requiring a fresh manual review rather than silently retaining a current-review label.


## Automated test suite and live-run status

The standard-library unittest suite is stored at tests/test_catalogue_audit.py and is wired into the workflow before repository collection. It now contains 18 offline test cases covering manifest dependency clues, automatic account-type resolution, pagination checkpoints/resume, interrupted scheduled refresh, empty repositories, stale-evidence invalidation and mapping eligibility.

The first live GitHub Actions run (#1) has since completed inventory pagination for 34 configured accounts and committed 25,965 repository metadata records; see docs/LIVE-INVENTORY-SNAPSHOT-2026-11-23.md. A subsequent run is validating empty-repository handling and continuing enrichment. The automated account summaries are still far from fully enriched, and none of those generated records has been manually interpreted.


## Live inventory run — 23 November 2026

The first automated run ([Actions run #1](https://github.com/Arhanpg/Top-Open-Source-repos/actions/runs/45248026075)) completed repository pagination and committed account checkpoints. The five primary starting accounts and the 30 AWS-directory-listed accounts all reported complete pagination.

Verified inventory snapshot from the committed company-level account indexes:

| Company group | Accounts | Public repository records |
|---|---:|---:|
| Microsoft | 1 | 8,500 |
| Google | 1 | 2,947 |
| Apple | 1 | 194 |
| NVIDIA | 1 | 850 |
| Amazon / AWS directory | 30 | 13,474 |
| **Total** | **34** | **25,965** |

The run's overall conclusion was failure because two empty repositories returned GitHub HTTP 409 during tree inspection: `aws-ia/.announcements` and `NVIDIA/ADLR`. This did not invalidate their completed public-repository pagination. The collector now classifies the exact `Git Repository is empty` response as terminal manifest unavailability, while retaining other HTTP 409 responses as errors.

The first run captured README/language/manifest evidence for a bounded batch of up to 10 repositories per account. It did not manually interpret those READMEs: automated dossiers remain `manual technical interpretation pending`. Further enrichment batches are required for the remaining repositories.


## Additional NVIDIA account discovery — 24 November 2026

After the 34-account inventory snapshot, five further NVIDIA project-linked accounts were added from direct links on NVIDIA's official Open Source at NVIDIA hub: `NVIDIA-ISAAC-ROS`, `nvidia-cosmos`, `rapidsai`, `ai-dynamo` and `triton-inference-server`. They use the separate `official-project-linked` status to avoid implying blanket legal ownership. The configured inventory target is therefore now 39 accounts, but the original 25,965-repository snapshot does not include these five new account inventories. See [NVIDIA Account Discovery](../organizations/nvidia/ACCOUNT-DISCOVERY.md).


## Empty README response — 24 November 2026

The second live enrichment run identified `boto/requestbuilder` as a repository with a zero-byte file named `README`. GitHub's README endpoint returned metadata but no Base64 body, which the collector incorrectly treated as an evidence-capture error. The collector now classifies only a verified zero-byte README as terminal `unavailable`; non-empty README metadata without content remains an error. Two offline tests cover both paths.


## Current 65-account / 33,522-repository reconciliation — 24 November 2026

A fresh reconciliation of all 65 committed account-level README summaries gives the following inventory/evidence totals:

| Measure | Count |
|---|---:|
| Accounts with committed inventory checkpoints | 65 |
| Public repository metadata records | **33,522** |
| README captures | 2,075 |
| README unavailable | 62 |
| Terminal README/language/manifest evidence | 2,137 |
| Pending/error evidence | **31,385** |

README capture coverage is **6.19%** (2,075 / 33,522). Terminal evidence coverage is **6.37%** (2,137 / 33,522). These are automated evidence states, not human technical-review counts.

| Company group | Accounts | Repositories | README captures | README unavailable | Evidence terminal | Pending/error |
|---|---:|---:|---:|---:|---:|---:|
| Alphabet / Google | 3 | 4,546 | 87 | 3 | 90 | 4,456 |
| Amazon / AWS | 30 | 13,474 | 1,065 | 33 | 1,098 | 12,376 |
| Apple | 3 | 287 | 94 | 7 | 101 | 186 |
| Baidu | 4 | 298 | 75 | 5 | 80 | 218 |
| Microsoft | 4 | 12,242 | 177 | 3 | 180 | 12,062 |
| NVIDIA | 6 | 1,121 | 201 | 5 | 206 | 915 |
| SAP | 11 | 910 | 271 | 2 | 273 | 637 |
| Siemens | 3 | 327 | 85 | 4 | 89 | 238 |
| Tencent | 1 | 317 | 20 | 0 | 20 | 297 |
| **Total** | **65** | **33,522** | **2,075** | **62** | **2,137** | **31,385** |

### Highest remaining account backlogs

| Account | Repositories pending/error |
|---|---:|
| aws-samples | 9,510 |
| microsoft | 8,440 |
| google | 2,887 |
| azure | 2,720 |
| GoogleCloudPlatform | 1,527 |
| awslabs | 993 |
| NVIDIA | 791 |
| MicrosoftDocs | 661 |
| aws | 516 |
| amazon-science | 470 |

The top ten account backlogs represent approximately 90.9% of the remaining pending/error records. Thirty of the 65 account summaries currently show zero pending/error; the largest accounts dominate the remaining workload.

### Throughput and rate-limit changes

- Every GitHub REST request is spaced at 4-second intervals, targeting approximately 900 requests/hour against the documented GITHUB_TOKEN primary REST budget of 1,000 requests/hour/repository in Actions.
- Four daily Actions runs execute enrichment only. They do not re-fetch every account's repository pagination before processing README evidence.
- A separate weekly Sunday run refreshes inventory metadata and resumes interrupted pagination from tracked checkpoints.
- The daily scheduler uses a global ceiling of 1,200 repositories per run, distributed round-robin across eligible accounts. Exhausted small-account queues are reallocated to the largest remaining backlogs; each account retains its own repository cursor.
- Selected manifest contents are retrieved from raw.githubusercontent.com with a 256 KB cap. Non-empty README files without inline API content can fall back to their public raw URL with a 2 MB cap. These reduce REST Contents requests.
- Automated evidence capture remains separate from human interpretation. No company is marked complete while company account discovery and manual technical interpretation remain outstanding.


## Latest live validation — 24 November 2026

- Main commit: 8b7df8eca70f7a3af87e6ab23ad15a545d0501c3 added README section evidence extraction and the REST pacing test.
- GitHub Actions run #17 checked out that commit and passed its preflight validation step, which compiles the collector and runs the 26-test offline suite.
- At the latest status check, the inventory/evidence enrichment step was still running. No additional repository captures are included in the 33,522 baseline until the run commits its account checkpoints.
- [View Actions run #17](https://github.com/Arhanpg/Top-Open-Source-repos/actions/runs/45324524032).

The current count of 33,522 records and 31,385 pending/error is therefore a pre-enrichment-run baseline, not the result of run #17.


### Global batch distribution

The daily workflow now passes a global 1,200-repository cap to the collector. The collector interleaves accounts instead of reserving a fixed quota for each account. This is important for the 31,385-record backlog: accounts with only a few pending records no longer leave unused per-account slots while very large accounts still have thousands of outstanding repositories.

The global 1,200 is an upper ceiling. Theoretical best-case capture throughput is 4,800 repositories per day across four runs, before accounting for README-unavailable states, API retries, rate limits, and repositories that need re-capture after source changes. This is a capacity estimate, not a completion promise.
