# capire/incidents-app

- Company: SAP
- GitHub account: [https://github.com/capire](https://github.com/capire)
- Mapping status: official-directory-listed
- Repository: [capire/incidents-app](https://github.com/capire/incidents-app)
- Default branch: main
- README: [Open upstream README](https://github.com/capire/incidents-app/blob/main/readme.md)
- README blob SHA: c87d39d190c7acdd6f46aebc50c0a00c3a912e2e
- Repository ID: 685533985
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:33+00:00

### Short excerpt (up to 100 words)

> Welcome to the Incident Management reference sample application for the SAP Cloud Application Programming Model (CAP). The application allows to create and process incidents on behalf of registered customers with the basic domain model is depicted below. Assumed you prepared for CAP development as documented in capire's *Initial Setup* section, ... Clone the repository and install dependencies: git clone https://github.com/capire/incidents cd incidents npm install Run the application locally: cds watch Then open http://localhost:4004 and navigate to /incidents/webapp. <br> (for testing with authorization, copy the file `xmpls/authorizations.cds` into the `srv` folder. Then, login as `alice`, no password required). If you get

### README headings

- Incident Management – CAP Reference Application
- Setup
- Run
- Test
- Add plugins
- Deploy

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 36,097 |
| CAP CDS | 10,567 |
| HTML | 4,967 |
| Dockerfile | 548 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/attachments, @cap-js/audit-logging, @cap-js/cds-test, @cap-js/change-tracking, @cap-js/sqlite, @sap/cds
- .devcontainer/Dockerfile (capture: captured)
- app/incidents/package.json (capture: captured)
- xmpls/messaging/package.json (capture: captured) — dependency clues: @cap-js/cds-test, @cap-js/sqlite, @sap-cloud-sdk/connectivity, @sap-cloud-sdk/http-client, @sap-cloud-sdk/resilience, @sap-cloud-sdk/util, @sap/cds, @sap/xb-msg-amqp-v100, express
- xmpls/remote-service/package.json (capture: captured) — dependency clues: @cap-js/cds-test, @cap-js/sqlite, @sap-cloud-sdk/connectivity, @sap-cloud-sdk/http-client, @sap-cloud-sdk/resilience, @sap-cloud-sdk/util, @sap/cds, express

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 61
- Forks at capture: 73
- Last updated: 2026-11-23T00:28:11Z
- Last pushed: 2026-10-29T16:09:29Z
- Topics: sample

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/capire/incidents-app)
- [README](https://github.com/capire/incidents-app/blob/main/readme.md)
- [Issues](https://github.com/capire/incidents-app/issues)
- [Releases](https://github.com/capire/incidents-app/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
