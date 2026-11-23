# cap-js/cds-federation-synonyms

- Company: SAP
- GitHub account: [https://github.com/cap-js](https://github.com/cap-js)
- Mapping status: official-directory-listed
- Repository: [cap-js/cds-federation-synonyms](https://github.com/cap-js/cds-federation-synonyms)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js/cds-federation-synonyms/blob/main/README.md)
- README blob SHA: 260cee9e02895c76ac6734585b85cb7767ee0340
- Repository ID: 1285084649
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CDS plugin for CAP-to-CAP Data Federation based on SAP HANA synonyms.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:35:45+00:00

### Short excerpt (up to 100 words)

> CDS plugin for SAP HANA synonym-based data federation. This plugin is still **experimental**. For CAP applications using SAP HANA as database, this plugin enables CAP-to-CAP data federation by integration on the database layer via synonyms. In the database schema of the application that consumes the data ("consumer"), the imported entities are represented as synonyms that point to the respective tables or views in the database schema of the application that provides the data ("provider"). Acess to the producer is read-only. Visit CAP-level Data Federation to learn about the basics. * @sap/cds-dk version 9.9 or higher. * For a multitenant consumer,

### README headings

- Welcome to @cap-js/cds-federation-synonyms
- About this project
- Requirements
- Usage
- Provider
- Consumer
- Schematic example
- Walkthrough
- Security considerations
- Provider and consumer share a trust boundary
- Cross-tenant federation via `provider_tenant`
- Extensions cannot reach synonym federation
- Audit logging
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 177,609 |
| CAP CDS | 16,125 |
| Shell | 2,960 |
| Java | 300 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/audit-logging, @cap-js/cds-federation-synonyms, @cap-js/cds-test, @cap-js/sqlite, @sap/cds, @sap/cds-dk, @sap/cds-mtxs
- test/ext-guard-it/package.json (capture: captured) — dependency clues: @sap/cds-mtxs
- test/scenarios/package.json (capture: captured) — dependency clues: @cap-js/cds-federation-synonyms, @sap/cds
- test/e2e/xflights/package.json (capture: captured) — dependency clues: @cap-js/cds-federation-synonyms, @cap-js/hana, @cap-js/sqlite, @sap/cds, @sap/cds-dk, @sap/cds-mtxs, @sap/xssec
- test/e2e/xtravels-j/package.json (capture: captured) — dependency clues: @cap-js/cds-federation-synonyms, @capire/xflights-data-syn, @sap/cds-dk, @sap/cds-mtxs
- test/e2e/xtravels-j/pom.xml (capture: captured) — dependency clues: cds-maven-plugin, cds-services-bom, flatten-maven-plugin, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, spring-boot-dependencies, spring-boot-maven-plugin, xtravels-j-parent

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 0
- Last updated: 2026-11-10T08:18:34Z
- Last pushed: 2026-11-23T10:08:13Z
- Topics: cap, cds, plugin, sap-cap, sap-hana

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js/cds-federation-synonyms)
- [README](https://github.com/cap-js/cds-federation-synonyms/blob/main/README.md)
- [Issues](https://github.com/cap-js/cds-federation-synonyms/issues)
- [Releases](https://github.com/cap-js/cds-federation-synonyms/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
