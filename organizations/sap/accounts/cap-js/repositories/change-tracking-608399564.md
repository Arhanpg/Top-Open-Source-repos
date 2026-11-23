# cap-js/change-tracking

- Company: SAP
- GitHub account: [https://github.com/cap-js](https://github.com/cap-js)
- Mapping status: official-directory-listed
- Repository: [cap-js/change-tracking](https://github.com/cap-js/change-tracking)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-js/change-tracking/blob/main/README.md)
- README blob SHA: 0a0dd7b2b5ad10c95a7abdbe239c9ea7efaaccc9
- Repository ID: 608399564
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CDS plugin providing out-of-the box support for automatic capturing, storing, and viewing of the change records of modeled entities.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:17+00:00

### Short excerpt (up to 100 words)

> A CDS plugin for automatic capturing, storing, and viewing of change records for modelled entities. This plugin is implemented as a **CDS plugin** — a Node.js package that hooks into CDS's build pipeline. During the build, it generates **native database triggers** (SQL DDL) directly from the CDS model. Because the triggers run at the database level, they are completely independent of the application runtime: neither CAP Node.js nor CAP Java needs to do anything special at request time to capture changes. The annotations (`@changelog`) are interpreted once at build time by the plugin, and the resulting triggers are then deployed

### README headings

- Change Tracking Plugin for SAP Cloud Application Programming Model (CAP)
- Why This Plugin Works for Both CAP Node.js and CAP Java
- Table of Contents
- Try it Locally
- Annotations
- Testing
- Change History View
- Detailed Explanation
- Human-readable Types and Fields
- Human-readable IDs
- ObjectID fallback for NULL values
- Human-readable Values
- Human-readable IDs for Composition Entries
- Composition of one
- Composition of many
- Expression-based labels
- Localized values
- Tracing any kind of change
- Tracking datetime fields with a fixed time zone
- Advanced Options
- Altered table view
- Disable lazy loading
- Disable UI Facet generation
- Disable Association to Changes Generation
- Disabling Change Tracking
- Select types of changes to track
- Preserve change logs of deleted data
- Adjust the depth of the entity hierarchy tracking
- Disable Children Change Linking
- Examples

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 725,444 |
| CAP CDS | 67,677 |
| Java | 9,580 |
| HTML | 2,945 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/cds-test, @cap-js/cds-types, @sap/cds
- tests/bookshop-mtx/package.json (capture: captured) — dependency clues: @cap-js/change-tracking, @cap-js/hana, @cap-js/sqlite, @sap/cds-dk, @sap/cds-mtxs, @sap/xssec, better-sqlite3
- tests/bookshop/package.json (capture: captured) — dependency clues: @cap-js/attachments, @cap-js/change-tracking, @cap-js/hana, @cap-js/postgres, @cap-js/sqlite, @sap/cds-dk, better-sqlite3, puppeteer, ui5-test-runner
- tests/bookshop/pom.xml (capture: captured) — dependency clues: cds-maven-plugin, cds-services-bom, flatten-maven-plugin, incidents-java-parent, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, spring-boot-dependencies, spring-boot-maven-plugin
- tests/bookshop/srv/pom.xml (capture: captured) — dependency clues: cds-adapter-hcql, cds-adapter-odata-v4, cds-maven-plugin, cds-starter-spring-boot, h2, incidents-java, incidents-java-parent, spring-boot-devtools, spring-boot-maven-plugin, spring-boot-starter-security, spring-boot-starter-test
- tests/performance/perf-bookshop/package.json (capture: captured) — dependency clues: @cap-js/change-tracking, @cap-js/hana, @cap-js/sqlite, @sap/cds, @sap/xssec

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 43
- Forks at capture: 16
- Last updated: 2026-11-12T13:48:43Z
- Last pushed: 2026-11-19T13:34:35Z
- Topics: btp, cap, cds, change-tracking, nodejs, plugin, sap-btp, sap-cap

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-js/change-tracking)
- [README](https://github.com/cap-js/change-tracking/blob/main/README.md)
- [Issues](https://github.com/cap-js/change-tracking/issues)
- [Releases](https://github.com/cap-js/change-tracking/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
