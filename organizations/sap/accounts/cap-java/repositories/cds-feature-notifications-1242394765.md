# cap-java/cds-feature-notifications

- Company: SAP
- GitHub account: [https://github.com/cap-java](https://github.com/cap-java)
- Mapping status: official-directory-listed
- Repository: [cap-java/cds-feature-notifications](https://github.com/cap-java/cds-feature-notifications)
- Default branch: main
- README: [Open upstream README](https://github.com/cap-java/cds-feature-notifications/blob/main/README.md)
- README blob SHA: 3b1e7e21c01d8291d92a19a7a18fc6a4ddbc82bd
- Repository ID: 1242394765
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CAP Java plugin that integrates SAP Alert Notification service (ANS) with the SAP Cloud Application Programming Model (CAP) for sending business notifications.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:36:04+00:00

### Short excerpt (up to 100 words)

> A CAP Java plugin that integrates SAP Alert Notification service (ANS) with the SAP Cloud Application Programming Model (CAP) for sending business notifications. The `cds-feature-notifications` plugin enables out-of-the-box notification handling for CAP Java applications. Annotate CDS events with `@notification`, emit them from a handler or annotate entities with `@notifications` for automatic delivery triggered by CRUD events, actions, or functions. The plugin takes care of the rest and delivers notifications via SAP Alert Notification service (ANS). In **local mode**, notifications are logged to the console with no ANS binding required. In **production mode**, notifications are delivered through Web (SAP Build Work

### README headings

- cds-feature-notifications
- About this project
- Table of Contents
- Getting Started
- Create a Project
- Add Maven Dependency
- Define and Emit a Notification
- Step 1: Define a Notification Type
- Step 2: Add i18n Translations (Optional)
- Step 3: Add Email HTML Template (Optional)
- Option 1: External HTML File
- Option 2: Inline HTML
- Step 4: Compile
- Step 5: Emit the Notification
- Option 1: Emit from Java Code
- Option 2: Declarative via CDS Entity Annotations
- Step 6: Run in Local Mode
- Production Mode
- Enable Production Mode
- Connect to ANS
- Option 1: ANS Service Binding
- Option 2: Work Zone Notification Credentials
- Deep Dive
- Recipient Formats
- Case 1: Single String
- Case 2: Array of Strings
- Dynamic Priority
- Navigation Target Parameters
- Storing Notifications to DB
- Cooldown Mechanism

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 324,064 |
| CAP CDS | 38,037 |
| HTML | 4,045 |
| JavaScript | 408 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @sap/cds-dk, @sap/eslint-plugin-cds, eslint
- pom.xml (capture: captured) — dependency clues: assertj-core, cds-feature-notifications, cds-feature-notifications-root, cds-maven-plugin, cds-services-api, cds-services-bom, central-publishing-maven-plugin, flatten-maven-plugin, jacoco-maven-plugin, junit-bom, junit-jupiter, logback-classic, logback-core, maven-clean-plugin, maven-compiler-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-failsafe-plugin, maven-gpg-plugin, maven-javadoc-plugin
- cds-feature-notifications/pom.xml (capture: captured) — dependency clues: build-helper-maven-plugin, cds-adapter-api, cds-feature-jdbc, cds-feature-notifications, cds-feature-notifications-root, cds-feature-remote-odata, cds-maven-plugin, cds-services-bom, cds-services-impl, cds-services-utils, cloudplatform-connectivity, cloudplatform-core, commons-io, commons-lang3, connectivity-destination-service, jacoco-maven-plugin, logback-classic, maven-javadoc-plugin, maven-source-plugin, spotbugs-annotations
- coverage-report/pom.xml (capture: captured) — dependency clues: cds-feature-notifications, cds-feature-notifications-coverage-report, cds-feature-notifications-root, integration-tests, jacoco-maven-plugin, maven-deploy-plugin, maven-pmd-plugin, maven-resources-plugin
- integration-tests/package.json (capture: captured) — dependency clues: @sap/cds-dk
- integration-tests/pom.xml (capture: captured) — dependency clues: cds-feature-notifications-root, cds-maven-plugin, cds-services-bom, flatten-maven-plugin, integration-tests-parent, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, spring-boot-dependencies, spring-boot-maven-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-10-02T15:30:31Z
- Last pushed: 2026-11-23T15:36:59Z
- Topics: btp, cap, java, notifications, plugin

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cap-java/cds-feature-notifications)
- [README](https://github.com/cap-java/cds-feature-notifications/blob/main/README.md)
- [Issues](https://github.com/cap-java/cds-feature-notifications/issues)
- [Releases](https://github.com/cap-java/cds-feature-notifications/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
