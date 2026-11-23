# cap-java/cds-feature-data-inspector

- Company: SAP
- GitHub account: [https://github.com/cap-java](https://github.com/cap-java)
- Mapping status: official-directory-listed
- Repository: [cap-java/cds-feature-data-inspector](https://github.com/cap-java/cds-feature-data-inspector)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-java/cds-feature-data-inspector/blob/main/README.md)
- README blob SHA: 651f67d13e78f85c91785441ae49850af12747e7
- Repository ID: 1314885901
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CDS plugin designed to help support users and developers securely inspect raw database content in both local and production environments, ensuring compliance with security standards. It supports multiple data sources—including database entities and services—providing direct, auditable access for troubleshooting and analysis.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:35:57+00:00

### Short excerpt (up to 100 words)

> `cds-feature-data-inspector` is a plugin to **view data** of CAP Java applications. This plugin focuses on the CAP Java runtime: it provides the Data Inspector OData **service definition and handler implementations**. The SAPUI5 app and the `cds add data-inspector` command are provided by the Node.js `@cap-js/data-inspector` plugin. A CAP Java consumer therefore gets the full experience by combining the two: - This CAP Java plugin (added as a Maven dependency) for the runtime - `@cap-js/data-inspector` (as a **devDependency**) for the UI using `cds build` and the project wiring using `cds add`. For more information, see Setup for SAP BTP and Accessing

### README headings

- SAP Cloud Application Programming Model Data Inspector Plugin for Java
- About this Project
- Quick Start
- Installation
- Run
- Features
- Accessing the UI Locally
- Excluding Entities and Elements
- Setup for SAP BTP
- Prerequisites
- Setup with `cds add data-inspector`
- Authorization
- Audit Logging
- UI Configuration for SAP BTP
- Support, Feedback, and Contribution
- Development Setup
- Minimum Versions
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 173,727 |
| CAP CDS | 9,228 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: cds-feature-data-inspector-root, cds-maven-plugin, cds-services-bom, central-publishing-maven-plugin, flatten-maven-plugin, jacoco-maven-plugin, junit-bom, maven-compiler-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-failsafe-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, maven-surefire-plugin, spotless-maven-plugin, spring-boot-maven-plugin
- cds-feature-data-inspector/package.json (capture: captured) — dependency clues: @sap/cds-dk
- cds-feature-data-inspector/pom.xml (capture: captured) — dependency clues: assertj-core, cds-feature-data-inspector, cds-feature-data-inspector-root, cds-maven-plugin, cds-services-api, cds4j-runtime, jackson-datatype-jsr310, jacoco-maven-plugin, junit-jupiter
- coverage-report/pom.xml (capture: captured) — dependency clues: cds-feature-data-inspector, cds-feature-data-inspector-coverage-report, cds-feature-data-inspector-root, cds-feature-data-inspector-test-app, jacoco-maven-plugin, maven-deploy-plugin, maven-resources-plugin
- test-app/package.json (capture: captured) — dependency clues: @cap-js/data-inspector, @cap-js/sqlite, @sap/cds, @sap/cds-dk
- test-app/pom.xml (capture: captured) — dependency clues: cds-feature-auditlog-v2, cds-feature-data-inspector, cds-feature-data-inspector-root, cds-feature-data-inspector-test-app, cds-feature-jdbc, cds-maven-plugin, cds-starter-spring-boot-odata, jacoco-maven-plugin, maven-deploy-plugin, maven-failsafe-plugin, maven-surefire-plugin, spring-boot-dependencies, spring-boot-maven-plugin, spring-boot-starter-security, spring-boot-starter-test, spring-security-test, sqlite-jdbc

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-10-29T09:07:56Z
- Last pushed: 2026-11-17T15:06:09Z
- Topics: btp, cap, cap-plugin, cds, cds-plugin, data, database, db, hana, java, plugin, sap-btp, sap-cap

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-java/cds-feature-data-inspector)
- [README](https://github.com/cap-java/cds-feature-data-inspector/blob/main/README.md)
- [Issues](https://github.com/cap-java/cds-feature-data-inspector/issues)
- [Releases](https://github.com/cap-java/cds-feature-data-inspector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
