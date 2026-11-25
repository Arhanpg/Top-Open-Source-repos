# cap-java/cds-feature-data-inspector

- Company: SAP
- Account: cap-java
- Repository: https://github.com/cap-java/cds-feature-data-inspector
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:17:30+00:00

## Project purpose

cds-feature-data-inspector is a plugin to **view data** of CAP Java applications.

## Why this project is used

A CDS plugin designed to help support users and developers securely inspect raw database content in both local and production environments, ensuring compliance with security standards. It supports multiple data sources—including database entities and services—providing direct, auditable access for troubleshooting and analysis.

## Core features

- Exclude specific entities and elements from being exposed by the plugin. For more information, see Excluding Entities and Elements.: Exclude specific entities and elements from being exposed by the plugin. For more information, see Excluding Entities and Elements.
  - Evidence: README.md#Features
- Automatically log access to sensitive personal data using CAP Java's audit logging. For more information, see Audit Logging.: Automatically log access to sensitive personal data using CAP Java's audit logging. For more information, see Audit Logging.
  - Evidence: README.md#Features
- Provide xsuaa scope for access control. For more information, see Authorization.: Provide xsuaa scope for access control. For more information, see Authorization.
  - Evidence: README.md#Features

## Technology stack

- Languages: Java, CAP CDS
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js/data-inspector, @cap-js/sqlite, @sap/cds, @sap/cds-dk, assertj-core, cds-feature-auditlog-v2, cds-feature-data-inspector, cds-feature-data-inspector-coverage-report, cds-feature-data-inspector-root, cds-feature-data-inspector-test-app, cds-feature-jdbc, cds-maven-plugin, cds-services-api, cds-services-bom, cds-starter-spring-boot-odata, cds4j-runtime, central-publishing-maven-plugin, flatten-maven-plugin, jackson-datatype-jsr310, jacoco-maven-plugin, junit-bom, junit-jupiter, maven-compiler-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-failsafe-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-resources-plugin, maven-source-plugin, maven-surefire-plugin, spotless-maven-plugin, spring-boot-dependencies, spring-boot-maven-plugin, spring-boot-starter-security, spring-boot-starter-test, spring-security-test, sqlite-jdbc
- Build/package tools: npm-compatible manifest, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: test-app/src/main/java/com/sap/cds/feature/datainspector/testapp/Application.java, cds-feature-data-inspector/src/main/java/com/sap/cds/feature/datainspector/configuration/Registration.java, cds-feature-data-inspector/src/main/java/com/sap/cds/feature/datainspector/handler/DataInspectorConstants.java, cds-feature-data-inspector/src/main/java/com/sap/cds/feature/datainspector/handler/DataReader.java

## Setup and usage

- Installation: Add the plugin to your CAP Java project's srv/pom.xml:
- Installation: cds-feature-data-inspector
- Installation: Reference the plugin's CDS model with a using statement in one of your srv/*.cds files (opt-in — the plugin is not activated until you do this):
- Installation: using from 'com.sap.cds/cds-feature-data-inspector';
- Installation: To use the SAPUI5 app or cds add data-inspector, additionally install the Node.js @cap-js/data-inspector plugin as a devDependency in your host app's package.json:
- Installation: npm install --save-dev @cap-js/data-inspector
- Installation: Then disable the Node.js plugin's CDS model contribution by adding "@cap-js/data-inspector": false under the top-level requires in .cdsrc.json, or under cds.requires in package.json:
- Installation: "@cap-js/data-inspector": false

## Limitations and caveats

- Security / Disclosure: If you find a bug that might be a security problem, follow the instructions in our security policy to report it. Don't create GitHub issues for security-related questions or problems.

## Evidence and provenance

- README: https://github.com/cap-java/cds-feature-data-inspector/blob/main/README.md
- README SHA: 651f67d13e78f85c91785441ae49850af12747e7
- Manifests: pom.xml, cds-feature-data-inspector/package.json, cds-feature-data-inspector/pom.xml, coverage-report/pom.xml, test-app/package.json, test-app/pom.xml
- Sampled source files: test-app/src/main/java/com/sap/cds/feature/datainspector/testapp/Application.java, cds-feature-data-inspector/src/main/java/com/sap/cds/feature/datainspector/configuration/Registration.java, cds-feature-data-inspector/src/main/java/com/sap/cds/feature/datainspector/handler/DataInspectorConstants.java, cds-feature-data-inspector/src/main/java/com/sap/cds/feature/datainspector/handler/DataReader.java
- Git tree state: captured
- Evidence fingerprint: 98ce926f1c8ccf5aa9e4471685203a5fdd236a1b7c3c5dd6ae55c1a7f577d8ce

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
