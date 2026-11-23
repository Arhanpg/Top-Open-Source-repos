# cap-js/audit-logging

- Company: SAP
- GitHub account: [https://github.com/cap-js](https://github.com/cap-js)
- Mapping status: official-directory-listed
- Repository: [cap-js/audit-logging](https://github.com/cap-js/audit-logging)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js/audit-logging/blob/main/README.md)
- README blob SHA: fe340f111941ff3a8f7b0341e039e78f478a88e1
- Repository ID: 653013549
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CDS plugin providing integration to the SAP Audit Log service as well as out-of-the-box personal data-related audit logging based on annotations.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:35:36+00:00

### Short excerpt (up to 100 words)

> `@cap-js/audit-logging` is a CDS plugin providing integration to the SAP Audit Log service as well as out-of-the-box personal data-related audit logging based on annotations. Documentation can be found at cap.cloud.sap. In this guide, we use the Incidents Management reference sample app as the base to add change tracking to. Clone the repository and apply the step-by-step instructions: git clone https://github.com/cap-js/incidents-app cd incidents-app npm i To enable audit logging, simply add this self-configuring plugin package to your project: npm add @cap-js/audit-logging Identify entities and elements (potentially) holding personal data using `@PersonalData` annotations. Create a `db/data-privacy.cds` file and add the following: using

### README headings

- Welcome to @cap-js/audit-logging
- Preliminaries
- Setup
- Annotate Personal Data
- Test-Drive Locally
- In Production
- Support, Feedback, Contributing
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 172,045 |
| CAP CDS | 21,160 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/cds-test, @cap-js/sqlite, @sap/cds, @sap/cds-lsp, @sap/cds-mtxs, express, jest
- test/integration/package.json (capture: captured) — dependency clues: @cap-js/audit-logging
- test/mtx/package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/sqlite, @sap/cds, @sap/cds-mtxs
- test/personal-data/package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/sqlite

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 15
- Forks at capture: 9
- Last updated: 2026-11-02T08:51:55Z
- Last pushed: 2026-11-20T16:13:59Z
- Topics: audit-logging, cap, cds, nodejs, plugin, sap-btp, sap-cap

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js/audit-logging)
- [README](https://github.com/cap-js/audit-logging/blob/main/README.md)
- [Issues](https://github.com/cap-js/audit-logging/issues)
- [Releases](https://github.com/cap-js/audit-logging/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
