# Azure/AzFilesAutoValidator

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/AzFilesAutoValidator](https://github.com/Azure/AzFilesAutoValidator)
- Default branch: master
- README: [Open upstream README](https://github.com/Azure/AzFilesAutoValidator/blob/master/README.md)
- README blob SHA: b85e11cba72ab23dbdd0a1538ed5f71233ffc2ce
- README bytes captured: 27594
- README truncated at capture limit: False
- Repository ID: 1250277126
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

To gain access, please finish setting up this repository now at: 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:33:58+00:00

### Short excerpt (up to 300 words)

> The three phases share python3 -m venv .venv GitHub Actions cron (03:30 For each image Phase

### README headings

- Automated Validation for AzNFS on Linux Distribution
- Pipeline overview
- The three workflows
- Phase 1 — `.github/workflows/scan-marketplace.yml`
- Phase 2 — `.github/workflows/phase2-publish.yml`
- Phase 3 — `.github/workflows/phase3-validate.yml`
- Phase 1 — Scan
- Runtime architecture
- Current scope
- Repository layout
- Data model
- Classification per scan
- Phase 1 output
- Email
- Phase 2 — the three gates and the AzNFS support policy
- Phase 3 — LISA validation
- Exit codes (Phase 1)
- GitHub Actions configuration
- Logs
- Find recent runs of a workflow
- Full log of one run -- contains every INFO line the scripts emit
- Only the failed steps -- fastest for troubleshooting
- Live-follow a run in progress (the `tail -f` equivalent)
- Local development
- 1. Clone, create venv, install deps
- 2. Authenticate to Azure
- 3. Configure
- 4. Run Phase 1
- Phase 2 (against the public prod content server)
- Tests

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Pipeline overview

> The three phases share

### Getting started and usage: 1. Clone, create venv, install deps

> python3 -m venv .venv

### Architecture and design: Runtime architecture

> GitHub Actions cron (03:30

### Limitations and security: Phase 2 — the three gates and the AzNFS support policy

> For each image Phase

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 454,521 |
| Shell | 7,319 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: azure-communication-email, azure-identity, azure-mgmt-compute, pytest
- requirements.txt (capture: captured) — dependency clues: PyYAML, azure-communication-email, azure-identity, azure-mgmt-compute, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-09-30T11:16:45Z
- Last pushed: 2026-11-03T13:01:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/AzFilesAutoValidator)
- [README](https://github.com/Azure/AzFilesAutoValidator/blob/master/README.md)
- [Issues](https://github.com/Azure/AzFilesAutoValidator/issues)
- [Releases](https://github.com/Azure/AzFilesAutoValidator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
