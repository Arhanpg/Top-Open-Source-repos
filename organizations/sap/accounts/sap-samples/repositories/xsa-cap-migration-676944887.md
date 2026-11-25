# SAP-samples/xsa-cap-migration

- Company: SAP
- GitHub account: [https://github.com/SAP-samples](https://github.com/SAP-samples)
- Mapping status: official-directory-listed
- Repository: [SAP-samples/xsa-cap-migration](https://github.com/SAP-samples/xsa-cap-migration)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-samples/xsa-cap-migration/blob/main/README.md)
- README blob SHA: 448b2b1d5a2932f040a6c1dbb9c57b0f1262e07b
- README bytes captured: 33339
- README truncated at capture limit: False
- Repository ID: 676944887
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A sample application that demonstrates the migration of XSA-based application to SAP Cloud Application Programming model and Hana Cloud.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:11:47+00:00

### Short excerpt (up to 300 words)

> SAP HANA Interactive Education In this step, we 1. SAP HANA 2.0 Part of XSJS Javascript

### README headings

- XS Advanced Programming Model To SAP Cloud Application Programming Model Migration Guide
- Introduction
- Decision Table
- Requirements
- Where to Start
- **Note:**
- 1. The migration steps should be tested in a development environment before production.
- 2. This guide is directed at single-tenant-applications.
- Steps
- Step-1: Preparing XS Advanced Source and CAP Target Applications
- 1.1: Clone and Deploy the XS Advanced Source Application:
- 1.2: Creation and Setup of the Target CAP Application
- Step-2: Rename the HANA Artifacts in the Source SAP HANA 2.0/XSA HDI Container
- Step-3: CAP Application Deployment with hdbcds and hdbtable format to the Source SAP HANA 2.0/XSA HDI Container.
- Step-4: Migration of SAP HANA 2.0 HDI Container using Self-Service Migration for SAP HANA Cloud and Connect the CAP application to the migrated container.
- Step-5: Migration of SRV and UI layers.
- Known Issues
- Learning Resources
- How to obtain support
- Contributing
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> SAP HANA Interactive Education

### Features and capabilities: 1.2.2: Remove or Modify the Unsupported database features:

> In this step, we

### Technology and requirements: Requirements

> 1. SAP HANA 2.0

### Limitations and security: Known Issues

> Part of XSJS Javascript

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 1,148,708 |
| CAP CDS | 50,232 |
| HTML | 33,699 |
| XSLT | 13,190 |
| CSS | 12,695 |
| Smarty | 1,060 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- hana-shine-cap/package.json (capture: captured) — dependency clues: @cap-js-community/odata-v2-adapter, @cap-js/sqlite, @sap/cds, @sap/cds-dk, @sap/cds-hana, @sap/jobs-client, @sap/xsenv, @sap/xssec, eslint, exceljs, express, hdb, jszip, passport
- migration-script/package.json (capture: captured) — dependency clues: @sap/cds, child_process, fs, fs-extra, glob, path, readline, saxon-js, shelljs, xslt3
- hana-shine-cap/app/package.json (capture: captured) — dependency clues: @sap/approuter
- hana-shine-cap/db/package.json (capture: captured) — dependency clues: @sap/hdi-deploy
- hana-shine-cap/user-db/package.json (capture: captured) — dependency clues: @sap/hdi-deploy
- hana-shine-xsa/core-db/package.json (capture: captured) — dependency clues: @sap/hana-client, @sap/hdi-deploy

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 7
- Last updated: 2026-06-03T10:18:05Z
- Last pushed: 2026-11-23T11:45:19Z
- Topics: migration, sample, sample-code, sap-cap, sap-hana-cloud, xsa, xsa-cap

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-samples/xsa-cap-migration)
- [README](https://github.com/SAP-samples/xsa-cap-migration/blob/main/README.md)
- [Issues](https://github.com/SAP-samples/xsa-cap-migration/issues)
- [Releases](https://github.com/SAP-samples/xsa-cap-migration/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
