# siemens/LightweightCmpRa

- Company: Siemens
- Account: Siemens
- Repository: https://github.com/siemens/LightweightCmpRa
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:44:37+00:00

## Project purpose

Copyright (c) 2019 - 2024 Siemens AG -->

## Why this project is used

CLI-based Registration Authority application PoC

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: CmpRaComponent, LightweightCmpRa, californium-core, commons-cli, cyclonedx-maven-plugin, dependency-check-maven, file-management, jackson-databind, jackson-jaxrs-yaml-provider, jacoco-maven-plugin, jakarta.xml.bind-api, jaxb-api, jaxb-runtime, maven-dependency-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-source-plugin, maven-surefire-plugin, slf4j-api, slf4j-simple, spotless-maven-plugin
- Build/package tools: Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/java/com/siemens/pki/lightweightcmpclient/configuration/CertProfileScopedList.java, src/main/java/com/siemens/pki/lightweightcmpclient/configuration/ClientConfiguration.java, src/main/java/com/siemens/pki/lightweightcmpclient/configuration/ClientContextImpl.java, src/main/java/com/siemens/pki/lightweightcmpclient/configuration/EnrollmentContextImpl.java

## Setup and usage

No setup information established.

## Limitations and caveats

- Known issues: With JDK 11, revocation checking has some issues:
- Known issues: * A CRL provided as CRLDP extension is not always used in path validation
- Known issues: for CMP and TLS trust chains.
- Known issues: * An OCSP AIA extension is not always used in path validation
- Known issues: for TLS trust chains.

## Evidence and provenance

- README: https://github.com/siemens/LightweightCmpRa/blob/main/README.md
- README SHA: 248be77d2604a0d4f4ece436094f29f5768f4680
- Manifests: pom.xml
- Sampled source files: src/main/java/com/siemens/pki/lightweightcmpclient/configuration/CertProfileScopedList.java, src/main/java/com/siemens/pki/lightweightcmpclient/configuration/ClientConfiguration.java, src/main/java/com/siemens/pki/lightweightcmpclient/configuration/ClientContextImpl.java, src/main/java/com/siemens/pki/lightweightcmpclient/configuration/EnrollmentContextImpl.java
- Git tree state: captured
- Evidence fingerprint: 462465896896ad17fb9e15a025dbff96143a36925789f1a16338b53d965f649b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
