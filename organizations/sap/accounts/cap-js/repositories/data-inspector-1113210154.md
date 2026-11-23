# cap-js/data-inspector

- Company: SAP
- GitHub account: [https://github.com/cap-js](https://github.com/cap-js)
- Mapping status: official-directory-listed
- Repository: [cap-js/data-inspector](https://github.com/cap-js/data-inspector)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js/data-inspector/blob/main/README.md)
- README blob SHA: e065c372c0c205e51f017836bde28d2bd34839f5
- Repository ID: 1113210154
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CDS plugin designed to help support users and developers securely inspect raw database content in both local and production environments, ensuring compliance with security standards. It supports multiple data sources—including database entities and services—providing direct, auditable access for troubleshooting and analysis.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:19+00:00

### Short excerpt (up to 100 words)

> `@cap-js/data-inspector` is a plugin to **view data** of CAP Node.js applications. It comes with an SAPUI5 app consumable out of the box. Install the plugin in your CAP Node.js project: npm install @cap-js/data-inspector Run it with cds watch - The Data Inspector OData service is served at `http://localhost:4004/odata/v4/data-inspector/`. - When asked for a user, use `alice` without password. The SAPUI5 app is **not** served by the CAP server (see Accessing the UI Locally). - Exclude specific entities and elements from being exposed by the plugin. See Excluding Entities and Elements. - Automatically log access to sensitive personal data using `@cap-js/audit-logging`.

### README headings

- SAP Cloud Application Programming Model Data Inspector Plugin for Node.js
- About this Project
- Quick Start
- Installation
- Run
- Features
- The UI at a Glance
- Accessing the UI Locally
- Excluding Entities and Elements
- Setup for BTP
- Prerequisites
- Setup with `cds add data-inspector`
- Authorization
- Audit Logging
- UI Configuration for SAP BTP
- CDS Build Plugin
- Application ID (multi-service deployment)
- UI Build Output Folder
- OData Service Base Path
- Custom Destination Name
- Authentication Type
- sap.cloud.service Configuration
- Local Server URL (ui5 serve proxy)
- MTA Deployment
- @sap/html5-app-deployer
- Cloud Portal Service Configuration
- SAP Build Work Zone Configuration
- (Optional) flpSandbox.html Configuration for Data Inspector Plugin's SAPUI5 App Tile for Local Testing
- Support, Feedback, and Contribution
- Development Setup

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 236,305 |
| JavaScript | 40,303 |
| CAP CDS | 6,248 |
| HTML | 4,213 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/cds-test, @cap-js/cds-typer, @cap-js/cds-types, @cap-js/sqlite, @sap/cds, @sap/cds-dk, @types/mocha, @types/node, c8, chai, cross-env, eslint, eslint-config-prettier, mocha, prettier, rimraf, ts-node, tsx, typescript
- test/package.json (capture: captured) — dependency clues: @cap-js/data-inspector
- app/data-inspector-ui/package.json (capture: captured) — dependency clues: @sap/ux-ui5-tooling, @ui5/cli, rimraf, ui5-task-zipper

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 1
- Last updated: 2026-10-14T05:43:54Z
- Last pushed: 2026-11-16T17:45:14Z
- Topics: btp, cap, cap-plugin, cds, cds-plugin, data, database, db, hana, javascript, nodejs, plugin, sap-btp, sap-cap, typescript

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js/data-inspector)
- [README](https://github.com/cap-js/data-inspector/blob/main/README.md)
- [Issues](https://github.com/cap-js/data-inspector/issues)
- [Releases](https://github.com/cap-js/data-inspector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
