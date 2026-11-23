# cap-java/incidents-app

- Company: SAP
- GitHub account: [https://github.com/cap-java](https://github.com/cap-java)
- Mapping status: official-directory-listed
- Repository: [cap-java/incidents-app](https://github.com/cap-java/incidents-app)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-java/incidents-app/blob/main/README.md)
- README blob SHA: 080831f591c380cb41150cf1a02512fe393d40d3
- Repository ID: 919974179
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:36:09+00:00

### Short excerpt (up to 100 words)

> Welcome to the Incident Management reference sample application for CAP and development recommendations provided by the SAP BTP Developer Guide. The application support team members to create and process incidents on behalf of registered customers. The basic domain model is depicted below. Assumed you prepared for CAP development as documented in capire's *Getting Started > Jumpstart* page, ... Clone the repository and install dependencies: git clone https://github.com/cap-java/incidents-app cd incidents-app mvn clean compile Run the application locally: cd srv mvn cds:watch Then open http://localhost:8080/ . You can see all the default services and UI endpoints listed in the CAP default landing

### README headings

- Incident Management
- Domain Model
- Setup
- Run
- Deploy
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 9,828 |
| CAP CDS | 8,411 |
| HTML | 7,129 |
| JavaScript | 3,113 |
| Dockerfile | 548 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @sap/cds-dk
- pom.xml (capture: captured) — dependency clues: cds-services-bom, flatten-maven-plugin, incident-management-parent, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, spring-boot-dependencies, spring-boot-maven-plugin
- .devcontainer/Dockerfile (capture: captured)
- db/package.json (capture: captured) — dependency clues: @sap/hdi-deploy, hdb
- srv/pom.xml (capture: captured) — dependency clues: cds-adapter-odata-v4, cds-feature-attachments, cds-maven-plugin, cds-starter-cloudfoundry, cds-starter-spring-boot, h2, incident-management, incident-management-parent, spring-boot-devtools, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-test, spring-security-test
- app/incidents/package.json (capture: captured) — dependency clues: @sap/ux-ui5-tooling, @ui5/cli

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 3
- Last updated: 2026-11-11T11:12:14Z
- Last pushed: 2026-11-11T10:12:09Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-java/incidents-app)
- [README](https://github.com/cap-java/incidents-app/blob/main/README.md)
- [Issues](https://github.com/cap-java/incidents-app/issues)
- [Releases](https://github.com/cap-java/incidents-app/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
