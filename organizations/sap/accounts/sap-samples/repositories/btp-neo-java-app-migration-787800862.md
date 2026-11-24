# SAP-samples/btp-neo-java-app-migration

- Company: SAP
- GitHub account: [https://github.com/SAP-samples](https://github.com/SAP-samples)
- Mapping status: official-directory-listed
- Repository: [SAP-samples/btp-neo-java-app-migration](https://github.com/SAP-samples/btp-neo-java-app-migration)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-samples/btp-neo-java-app-migration/blob/main/README.md)
- README blob SHA: b1a0841a62dcb62f679ab3ffbf16f99f48cd309a
- README bytes captured: 25400
- README truncated at capture limit: False
- Repository ID: 787800862
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Code sample and documentation for migrating SAP BTP Java applications from NEO to Cloud Foundry, showcasing step-by-step processes and best practices.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:34:16+00:00

### Short excerpt (up to 300 words)

> The skills guide your To run a guided Check if there is

### README headings

- Migration Guide for Java Applications from the Neo Environment to the Cloud Foundry Environment
- Table of Contents
- 🚀 AI-Assisted Migration (Recommended)
- Overview & Supported AI Tools
- AI Skills Folder & Catalog
- Quick Start
- 1. Purpose
- 2. Prerequisites
- 2.1 Install the Migration Tools
- 3. Gather All Application Sources
- 3.1 Clone the Repo Containing the Source Code
- 3.2 Make Sure Your Code Compiles
- 3.3 Analyze the Dependencies of Your Java Applications
- 4. Migrate to Jakarta EE 10 and Java 25
- 5. Replace the Neo Java Web API with the SAP Cloud SDK
- 5.1 **Remove** the following dependency from the `pom.xml` file: <br>
- 5.2 If you find the following dependency in the `pom.xml`, **removed** it:
- 5.3 **Add** the following dependencies in the `<dependencyManagement>` section:<br>
- 5.4 **Add** the versions of the dependencies in the `<properties>` section:<br>
- 5.5 **Add** the following dependency in the `<dependencies>` section:<br>
- 6. Set Up Authentication and Authorization
- Related Information
- 7. Additional Scenarios
- 8. Deploy the Java Application
- 8.1 Prepare the MTA Deployment Descriptor File
- 8.2 Deploy the Java Application to the Cloud Foundry Environment
- 9. Access the Java Application
- 10. AI Assisted Migration Reference

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview & Supported AI Tools

> The skills guide your

### Getting started and usage: Quick Start

> To run a guided

### Technology and requirements: 3.3 Analyze the Dependencies of Your Java Applications

> Check if there is

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 258,442 |
| Python | 54,907 |
| Shell | 16,816 |
| JavaScript | 8,581 |
| CSS | 7,301 |
| HTML | 2,856 |
| Dockerfile | 106 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- scenarios/authentication-and-authorization-scenario2/neo/pom.xml (capture: captured) — dependency clues: javax.servlet-api, javax.servlet.jsp-api, json, maven-compiler-plugin, maven-war-plugin, neo-authn-authz-demo, neo-java-web-api, slf4j-api
- scenarios/authentication-and-authorization/cf/pom.xml (capture: captured) — dependency clues: authentication, cf-tomcat-bom, jakarta.servlet-api, java-api, maven-war-plugin, scp-cf, sdk-modules-bom
- scenarios/authentication-and-authorization/neo/pom.xml (capture: captured) — dependency clues: authentication, neo-java-web-api
- scenarios/connectivity/cf/pom.xml (capture: captured) — dependency clues: cf-tomcat-bom, connectivity, jakarta.servlet-api, maven-war-plugin, scp-cf, sdk-modules-bom
- scenarios/connectivity/integration-test/pom.xml (capture: captured) — dependency clues: connectivity-integration-test, httpunit, junit, maven-enforcer-plugin, maven-failsafe-plugin, maven-surefire-plugin
- scenarios/connectivity/neo/pom.xml (capture: captured) — dependency clues: connectivity, maven-war-plugin, neo-java-web-api

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 0
- Last updated: 2026-09-29T13:19:43Z
- Last pushed: 2026-11-19T13:46:21Z
- Topics: btp-cloud-foundry, btp-neo, connectivity, destinations, document-serivce, hana-cloud, xsuaa

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-samples/btp-neo-java-app-migration)
- [README](https://github.com/SAP-samples/btp-neo-java-app-migration/blob/main/README.md)
- [Issues](https://github.com/SAP-samples/btp-neo-java-app-migration/issues)
- [Releases](https://github.com/SAP-samples/btp-neo-java-app-migration/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
