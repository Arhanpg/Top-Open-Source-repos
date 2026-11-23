# cap-js/data-privacy

- Company: SAP
- GitHub account: [https://github.com/cap-js](https://github.com/cap-js)
- Mapping status: official-directory-listed
- Repository: [cap-js/data-privacy](https://github.com/cap-js/data-privacy)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js/data-privacy/blob/main/README.md)
- README blob SHA: f643e9268f1e8918d3e24fd18ceeb48b915a1252
- Repository ID: 1198538392
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SAP Cloud Application Programing Model (CAP) plugin for integrating into the SAP BTP Data Privacy Integration service which helps implementing data privacy requirements, like data retention management to compliantly delete personal data and personal data information retrieval for when users request their personal data.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:22+00:00

### Short excerpt (up to 100 words)

> The `@cap-js/data-privacy` plugin provides an out of box integration for CAP based applications with the SAP Data Privacy Integration (DPI) service. In particular based on `@PersonalData` and `@ILM` annotations in the data model, the plugin automatically provides a `/dpp/information` endpoint and a `/dpp/retention` endpoint via which the SAP DPI service can request personal data to show it in its `Manage Personal Data` app and block and delete data based on retention rules defined in SAP DPI. More information about how to use the plugin, can be found in the Data Privacy guide - Retention and Data Privacy guide - Information.

### README headings

- CDS plugin for SAP Data Privacy Integration
- About this project
- Requirements and Setup
- Test the plugin locally
- Local Testing
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 436,156 |
| CAP CDS | 131,869 |
| Handlebars | 4,258 |
| HTML | 1,099 |
| Clean | 1,051 |
| TypeScript | 430 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/cds-test, @cap-js/cds-types, @cap-js/sqlite, @eslint/js, @sap/cds, @sap/cds-common-content, @sap/cds-dk, @sap/cds-lsp, @sap/xsenv, eslint, jest, patch-package, prettier
- tests/bookshop-app/package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/data-privacy, @cap-js/hana, @cap-js/sqlite, @sap/ams, @sap/ams-dev, @sap/cds, @sap/cds-common-content, @sap/cds-dk, @sap/ux-specification, @sap/xsenv, @sap/xssec, express, path
- tests/incidents-mgmt/package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/data-privacy, @cap-js/hana, @cap-js/sqlite, @sap/cds, @sap/cds-dk, @sap/cds-mtxs, @sap/ux-specification, @sap/xssec, cds-launchpad-plugin, cds-plugin-ui5, express, passport
- tests/information/extend-information-endpoint/package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/data-privacy, @cap-js/hana, @cap-js/sqlite, @sap/cds, @sap/cds-dk, express
- tests/retention/extend-retention-endpoint/package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/data-privacy, @cap-js/hana, @cap-js/sqlite, @sap/cds, @sap/cds-dk, express
- tests/bookshop-app/app/router/package.json (capture: captured) — dependency clues: @sap/approuter

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 6
- Last updated: 2026-10-28T05:29:02Z
- Last pushed: 2026-11-05T05:22:11Z
- Topics: btp, cap, cds, data-privacy, nodejs, personal-data-handling, plugin, sap-btp, sap-cap

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js/data-privacy)
- [README](https://github.com/cap-js/data-privacy/blob/main/README.md)
- [Issues](https://github.com/cap-js/data-privacy/issues)
- [Releases](https://github.com/cap-js/data-privacy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
