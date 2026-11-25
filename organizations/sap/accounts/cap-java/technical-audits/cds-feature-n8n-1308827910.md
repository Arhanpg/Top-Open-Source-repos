# cap-java/cds-feature-n8n

- Company: SAP
- Account: cap-java
- Repository: https://github.com/cap-java/cds-feature-n8n
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:49:05+00:00

## Project purpose

CAP Plugin to automatically trigger and interact with n8n workflow automation tool - declaratively via @n8n.process.start annotations and programmatically via the n8n service.

## Why this project is used

Java Plugin for CAP Java Applications to trigger and interact with n8n workflows

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, CAP CDS
- Frameworks/libraries: Unknown / not established
- Dependency names: @sap/cds, @sap/cds-dk, @sap/eslint-plugin-cds, bcprov-jdk18on, cds-adapter-odata-v4, cds-feature-n8n, cds-feature-n8n-coverage-report, cds-feature-n8n-root, cds-maven-plugin, cds-services-bom, cds-services-utils, cds-starter-spring-boot, central-publishing-maven-plugin, cloudplatform-connectivity, commons-codec, eslint, flatten-maven-plugin, h2, httpcore5, httpcore5-h2, integration-tests, integration-tests-parent, jackson-core, jackson-databind, jacoco-maven-plugin, maven-checkstyle-plugin, maven-compiler-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-resources-plugin, maven-source-plugin, maven-surefire-plugin, opentelemetry-api, opentelemetry-common, opentelemetry-context, sdk-bom, slf4j-api, spotless-maven-plugin, spring-boot-dependencies, spring-boot-maven-plugin, spring-boot-starter-test, spring-security-test, tomcat-embed-core, tomcat-embed-el, tomcat-embed-websocket, wiremock-standalone
- Build/package tools: npm-compatible manifest, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: integration-tests/srv/src/main/java/app/Application.java, samples/bookshop/srv/src/main/java/customer/bookshop/Application.java, cds-feature-n8n/src/main/java/com/sap/cds/feature/n8n/configuration/N8nAutoConfiguration.java, cds-feature-n8n/src/main/java/com/sap/cds/feature/n8n/handlers/N8nAnnotationValidator.java

## Setup and usage

- Quick Start: Follow these steps to get a fully working local environment from scratch.
- Quick Start: 1. Build and install the plugin locally:
- Quick Start: 2. Add the dependency to your CAP Java application's pom.xml:
- Quick Start: 3. Annotate an entity in your CDS model:
- Quick Start: annotate AdminService.Books with @n8n.process.start: [
- Quick Start: {on: 'DELETE', path: 'book-deleted'}
- Quick Start: 4. Configure the n8n base URL in application.yaml:
- Quick Start: base-url: ${N8N_BASE_URL:http://localhost:5678}

## Limitations and caveats

- Security / Disclosure: If you find any bug that may be a security problem, please follow our instructions at in our security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/cap-java/cds-feature-n8n/blob/main/README.md
- README SHA: 8ddf3eec309df18a15547ba20022b1644a8df07c
- Manifests: package.json, pom.xml, cds-feature-n8n/pom.xml, coverage-report/pom.xml, integration-tests/package.json, integration-tests/pom.xml
- Sampled source files: integration-tests/srv/src/main/java/app/Application.java, samples/bookshop/srv/src/main/java/customer/bookshop/Application.java, cds-feature-n8n/src/main/java/com/sap/cds/feature/n8n/configuration/N8nAutoConfiguration.java, cds-feature-n8n/src/main/java/com/sap/cds/feature/n8n/handlers/N8nAnnotationValidator.java
- Git tree state: captured
- Evidence fingerprint: c2f93a6ef4403c9877b5bca0c9f61690a36e1ee7acc0d8f08546537621659105

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
