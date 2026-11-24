# capire/xtravels-java

- Company: SAP
- GitHub account: [https://github.com/capire](https://github.com/capire)
- Mapping status: official-directory-listed
- Repository: [capire/xtravels-java](https://github.com/capire/xtravels-java)
- Default branch: main
- README: [Open upstream README](https://github.com/capire/xtravels-java/blob/main/README.md)
- README blob SHA: 5eb3df07df7a53fd6faca17aaed1d5d348ccd897
- Repository ID: 1071471240
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Travel booking app using master data from xflights built with CAP Java

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:41:41+00:00

### Short excerpt (up to 100 words)

> A travel booking application built with CAP Java using master data provided by capire/xflights-java. git clone https://github.com/capire/xtravels-java cd xtravels-java mvn package The package has dependencies to other `capire` packages, including _`sap.capire/xflights-data`_, that can be pulled from GitHub Packages or from a local workspace setup as follows... Reuse packages among the *capire samples* are published to the GitHub Packages registry. This includes Maven packages as well as NPM packages. Authenticate to GitHub's Maven repository by adding the following to your `~/.m2/settings.xml`: As password you're using a Personal Access Token (classic) with `read:packages` scope. Read more about it in Authenticating to GitHub

### README headings

- @capire/xtravels-java
- Get it
- Using GitHub Packages
- Authenticate for Maven
- Authenticate for NPM
- Using Workspaces
- Run it
- With xflights
- Additional Examples
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 40,227 |
| CAP CDS | 28,818 |
| HTML | 1,214 |
| Clean | 863 |
| JavaScript | 255 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @capire/common, @sap/ams, @sap/cds, @sap/cds-dk
- pom.xml (capture: captured) — dependency clues: cds-maven-plugin, cds-services-bom, flatten-maven-plugin, java-bom, langchain4j-bom, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, sdk-modules-bom, spotless-maven-plugin, spring-boot-dependencies, spring-boot-maven-plugin, xtravels-parent
- app/package.json (capture: captured) — dependency clues: @sap/approuter
- db/package.json (capture: captured) — dependency clues: @sap/hdi-deploy, hdb
- srv/pom.xml (capture: captured) — dependency clues: cds-adapter-agent, cds-adapter-odata-v4, cds-feature-flow, cds-maven-plugin, cds-starter-cloudfoundry, cds-starter-spring-boot, dcl-compiler-plugin, h2, langchain4j-ollama, spring-boot-devtools, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-cap-ams, spring-boot-starter-cap-ams-test, spring-boot-starter-security, spring-boot-starter-security-test, spring-boot-starter-test, spring-boot-starter-webmvc-test, xflights-data, xtravels
- app/travels/package.json (capture: captured) — dependency clues: @sap/ux-ui5-tooling

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2026-11-02T09:15:03Z
- Last pushed: 2026-11-20T13:03:14Z
- Topics: cap, cds, data, federation, flights, java, reuse

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/capire/xtravels-java)
- [README](https://github.com/capire/xtravels-java/blob/main/README.md)
- [Issues](https://github.com/capire/xtravels-java/issues)
- [Releases](https://github.com/capire/xtravels-java/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
