# cap-java/cds-feature-attachments

- Company: SAP
- Account: cap-java
- Repository: https://github.com/cap-java/cds-feature-attachments
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:59:16+00:00

## Project purpose

The com.sap.cds:cds-feature-attachments dependency is a CAP Java plugin that provides out-of-the box attachments storage and handling by using an aspect Attachments.

## Why this project is used

Support for attachments

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, CAP CDS
- Frameworks/libraries: Unknown / not established
- Dependency names: @sap/cds-dk, assertj-core, awaitility, cds-adapter-api, cds-feature-attachments, cds-feature-attachments-coverage-report, cds-feature-attachments-fs, cds-feature-attachments-integration-tests-generic, cds-feature-attachments-integration-tests-mtx-local, cds-feature-attachments-integration-tests-parent, cds-feature-attachments-oss, cds-feature-attachments-root, cds-maven-plugin, cds-services-api, cds-services-bom, cds-services-impl, cds-services-utils, cds4j-core, central-publishing-maven-plugin, cloudplatform-core, commons-io, commons-lang3, connectivity-apache-httpclient4, flatten-maven-plugin, guava, jacoco-maven-plugin, junit-bom, junit-jupiter, logback-classic, maven-clean-plugin, maven-compiler-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-failsafe-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-pmd-plugin, maven-resources-plugin, maven-source-plugin, maven-surefire-plugin, mockito-bom, mockito-core, netty-bom, pmd-rules, sdk-bom, spotbugs-annotations, spotbugs-maven-plugin, spotless-maven-plugin, spring-boot-dependencies, tools, vavr, wiremock-spring-boot
- Build/package tools: npm-compatible manifest, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: integration-tests/generic/src/main/java/com/sap/cds/feature/attachments/integrationtests/Application.java, integration-tests/mtx-local/srv/src/main/java/com/sap/cds/feature/attachments/integrationtests/mt/Application.java, samples/bookshop/srv/src/main/java/customer/bookshop/Application.java, cds-feature-attachments/src/main/java/com/sap/cds/feature/attachments/configuration/Registration.java

## Setup and usage

- Quick Start: For a quick setup with in-memory storage:
- Quick Start: - Add the cds-feature-attachments Maven dependency to the srv/pom.xml and configure the cds-maven-plugin with the resolve goal as described in MVN Setup.
- Quick Start: - Extend the CDS model with the Attachments aspect and annotate the service for UI integration as explained in Changes in the CDS Models and for the UI.
- Quick Start: For a complete working example, see the bookshop sample.
- Quick Start: The incidents app provides a demonstration of how to use this plugin.
- Quick Start: For object store integration, see Amazon, Azure, and Google Object Stores.

## Limitations and caveats

- Security: To secure the endpoint, security annotations can be used. For example:
- Security: using {Attachments} from com.sap.cds/cds-feature-attachments;
- Security: entity Items : cuid {
- Security: attachments : Composition of many Attachments;
- Security: annotate RestoreAttachments with @(requires: 'internal-user');
- Security: Here the RestoreAttachments service is annotated with the requires annotation to secure the service.
- Security: Various other annotations can be used to secure the service.
- Security: More information about the CAP Java security concept can be found in

## Evidence and provenance

- README: https://github.com/cap-java/cds-feature-attachments/blob/main/README.md
- README SHA: 210e8f25f3c46d2d5ffdf263bafeb4abbb33ecde
- Manifests: pom.xml, cds-feature-attachments/package.json, cds-feature-attachments/pom.xml, coverage-report/pom.xml, integration-tests/package.json, integration-tests/pom.xml
- Sampled source files: integration-tests/generic/src/main/java/com/sap/cds/feature/attachments/integrationtests/Application.java, integration-tests/mtx-local/srv/src/main/java/com/sap/cds/feature/attachments/integrationtests/mt/Application.java, samples/bookshop/srv/src/main/java/customer/bookshop/Application.java, cds-feature-attachments/src/main/java/com/sap/cds/feature/attachments/configuration/Registration.java
- Git tree state: captured
- Evidence fingerprint: 374e9248547f7ac2282b02bfe3023f15ac634f55ce2aca80c12c9670486879a4

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
