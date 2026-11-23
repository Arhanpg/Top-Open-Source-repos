# SAP-cloud-infrastructure/opensearch-fortlogs

- Company: SAP
- GitHub account: [https://github.com/SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- Mapping status: official-directory-listed
- Repository: [SAP-cloud-infrastructure/opensearch-fortlogs](https://github.com/SAP-cloud-infrastructure/opensearch-fortlogs)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-cloud-infrastructure/opensearch-fortlogs/blob/main/README.md)
- README blob SHA: dc6fc645df064cf2b7cf51292a9fb414320619ef
- Repository ID: 1262721884
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Custom OpenSearch Docker image for FortLogs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:49:22+00:00

### Short excerpt (up to 100 words)

> Custom OpenSearch Docker image that replaces the bundled `opensearch-security-analytics` and `opensearch-alerting` plugins with patched builds containing upstream fixes not yet merged. Upstream PRs with critical fixes are open but unmerged. This image ships those fixes by installing plugin ZIPs built from source branches before the patches land in an official release. `opensearchproject/opensearch:3.8.0` (linux/amd64) 1. Removes the stock `opensearch-security-analytics` and `opensearch-alerting` plugins. 2. Installs custom-built plugin ZIPs that include the patches listed below. - PRs by thecodingshrimp - PRs by carmeroa - PRs by thecodingshrimp - PRs by carmeroa - PRs by NelTdS Images are built and pushed to ghcr.io by

### README headings

- opensearch-fortlogs
- Why
- Base image
- What this image does
- Upstream PRs included
- opensearch-project/alerting
- opensearch-project/security-analytics
- Open upstream issues
- Published image
- Building locally
- Removing a patch
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Dockerfile | 1,530 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-12T14:59:51Z
- Last pushed: 2026-11-19T09:59:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-cloud-infrastructure/opensearch-fortlogs)
- [README](https://github.com/SAP-cloud-infrastructure/opensearch-fortlogs/blob/main/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/opensearch-fortlogs/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/opensearch-fortlogs/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
