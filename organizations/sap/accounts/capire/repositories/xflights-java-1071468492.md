# capire/xflights-java

- Company: SAP
- GitHub account: [https://github.com/capire](https://github.com/capire)
- Mapping status: official-directory-listed
- Repository: [capire/xflights-java](https://github.com/capire/xflights-java)
- Default branch: main
- README: [Open upstream README](https://github.com/capire/xflights-java/blob/main/README.md)
- README blob SHA: eb1fd10841b3c263cc9d807a0dab320a9f004145
- Repository ID: 1071468492
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Master data service for flights, airlines, airports built with CAP Java

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:41:37+00:00

### Short excerpt (up to 100 words)

> This is a CAP Java application that manages master data like Airlines, Airports, and Flights. It provides a reuse package for clients to consume this data. It is used in the xtravels-java application. To start the `xflights` application, run the `Application` class in your preferred IDE. Alternatively, execute `mvn spring-boot:run` on the command line. You can reuse the client package by adding it to your dependencies in your app's `pom.xml`: The reuse package is published to the GitHub Packages registry, which requires you to authenticate to GitHub's Maven repository by adding the following to your `~/.m2/settings.xml`: As password you're using

### README headings

- capire/xflights-java
- Run
- Reuse
- Usage
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| CAP CDS | 4,453 |
| JavaScript | 3,063 |
| Java | 303 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @cap-js/sqlite, @sap/cds-dk
- pom.xml (capture: captured) — dependency clues: cds-maven-plugin, cds-services-bom, flatten-maven-plugin, java-bom, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, spotless-maven-plugin, spring-boot-dependencies, spring-boot-maven-plugin, xflights-parent
- db/package.json (capture: captured) — dependency clues: @sap/hdi-deploy, hdb
- srv/pom.xml (capture: captured) — dependency clues: cds-adapter-hcql, cds-adapter-odata-v4, cds-maven-plugin, cds-starter-cloudfoundry, cds-starter-spring-boot, h2, spring-boot-devtools, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-test, xflights, xflights-parent
- apis/data-service/pom.xml (capture: captured) — dependency clues: cds-feature-remote-hcql, cds-maven-plugin, flatten-maven-plugin, maven-clean-plugin, xflights-data, xflights-parent

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-03T08:25:58Z
- Last pushed: 2026-11-20T12:53:41Z
- Topics: cap, cds, flights, java, reuse

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/capire/xflights-java)
- [README](https://github.com/capire/xflights-java/blob/main/README.md)
- [Issues](https://github.com/capire/xflights-java/issues)
- [Releases](https://github.com/capire/xflights-java/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
