# cap-java/cds-feature-auditlog-ng

- Company: SAP
- Account: cap-java
- Repository: https://github.com/cap-java/cds-feature-auditlog-ng
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:09:09+00:00

## Project purpose

The CDS plugin for SAP Audit Log service enables Java CAP applications to emit audit log events in a standardized way. It is fully compatible with the Audit Log Event Catalog, ensuring standardized event semantics and compatibility.

## Why this project is used

Emit standardized audit log events from Java CAP applications with the Audit Log Service NG Java CAP plugin.  The plugin ensures compatibility with the Audit Log Event Catalog, aligning emitted events with shared semantic conventions for consistency across systems.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java
- Frameworks/libraries: Unknown / not established
- Dependency names: bcpkix-jdk18on, bcprov-jdk18on, cds-feature-auditlog-ng, cds-feature-auditlog-ng-root, cds-services-api, cds-services-bom, cds-services-impl, cds-services-utils, central-publishing-maven-plugin, flatten-maven-plugin, jacoco-maven-plugin, json-schema-validator, junit-jupiter, maven-clean-plugin, maven-compiler-plugin, maven-deploy-plugin, maven-enforcer-plugin, maven-gpg-plugin, maven-javadoc-plugin, maven-pmd-plugin, maven-source-plugin, maven-surefire-plugin, mockito-bom, mockito-core, sdk-bom, slf4j-api, spotbugs-maven-plugin
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNG.java, cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNGCommunicator.java, cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNGConfiguration.java, cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNGHandler.java

## Setup and usage

No setup information established.

## Limitations and caveats

- Security / Disclosure: If you find any bug that may be a security problem, please follow our instructions at in our security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/cap-java/cds-feature-auditlog-ng/blob/main/README.md
- README SHA: 62dd42c478e8ca2612ae45057865e9ff06d78821
- Manifests: pom.xml, cds-feature-auditlog-ng/pom.xml
- Sampled source files: cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNG.java, cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNGCommunicator.java, cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNGConfiguration.java, cds-feature-auditlog-ng/src/main/java/com/sap/cds/feature/auditlog/ng/AuditLogNGHandler.java
- Git tree state: captured
- Evidence fingerprint: b18d287d931949a9b910f5819216e2ab01abb75e820711d1b5954d1136ec8224

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
