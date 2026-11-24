# SAP/cloud-security-services-integration-library

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/cloud-security-services-integration-library](https://github.com/SAP/cloud-security-services-integration-library)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/cloud-security-services-integration-library/blob/main/README.md)
- README blob SHA: 2192bee8ffe58abb64b3f3b722394378dfb3dd5f
- README bytes captured: 51570
- README truncated at capture limit: False
- Repository ID: 147522483
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Integration libraries and samples for authenticating users and clients bound to XSUAA authentication and authorization service or Identity authentication service.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:28:28+00:00

### Short excerpt (up to 300 words)

> Typical web applications consist Before you can use This repository offers a

### README headings

- SAP BTP Security Services Integration Libraries
- :mega: What's New in 4.x
- Table of Contents
- Prerequisites
- Usage
- 2.1. Token Validation
- 2.1.1. Jakarta EE web applications
- 2.1.2. Spring Boot web applications
- Spring Boot Version Support
- Spring Boot 3.x Compatibility
- Migrating from spring-xsuaa
- 2.2. Token Flows for token retrievals
- 2.3 Testing utilities
- 2.4 Token Exchange for Hybrid Authentication
- Important Constraints
- How Token Exchange Works
- Token Exchange Modes
- Prerequisites for Token Exchange
- 2.4.1 Jakarta Example: Using [`HybridTokenAuthenticator`](java-security/src/main/java/com/sap/cloud/security/servlet/HybridTokenAuthenticator.java)
- 2.4.2 Spring Boot Example: Using [`HybridJwtDecoder`](spring-security/src/main/java/com/sap/cloud/security/spring/token/authentication/HybridJwtDecoder.java)
- Troubleshooting
- 2.5 Distributed Caching (since 4.2.0)
- Recommendation: when do I need a distributed cache?
- How the caches behave
- The SPI and shipped adapters
- Enabling on Spring Boot
- Enabling on plain Java
- Configuration reference
- Cache keys and entry content
- Bring your own cache

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage

> Typical web applications consist

### Technology and requirements: Prerequisites

> Before you can use

### Limitations and security: SAP BTP Security Services Integration Libraries

> This repository offers a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,586,810 |
| PowerShell | 4,705 |
| Shell | 2,968 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: assertj-core, caffeine, central-publishing-maven-plugin, commons-io, hamcrest-all, impsort-maven-plugin, jackson-core-asl, jackson-mapper-asl, jacoco-maven-plugin, jakarta.annotation-api, jakarta.servlet-api, java-bom, jetty-bom, json, junit, junit-bom, log4j-api, log4j-to-slf4j, maven-gpg-plugin, maven-javadoc-plugin
- bom/pom.xml (capture: captured) — dependency clues: central-publishing-maven-plugin, env, java-api, java-bom, java-security, java-security-core, java-security-test, maven-gpg-plugin, maven-javadoc-plugin, maven-source-plugin, resourceserver-security-spring-boot-3-starter, resourceserver-security-spring-boot-starter, spring-security, spring-security-3, token-client, token-client-spring, token-client-spring-3
- env/pom.xml (capture: captured) — dependency clues: assertj-core, commons-io, env, jacoco-maven-plugin, jakarta.annotation-api, java-access-api, java-api, java-consumption-api, java-sap-service-operator, java-sap-vcap-services, json, junit-jupiter-engine, junit-jupiter-params, logcaptor, maven-javadoc-plugin, maven-pmd-plugin, maven-source-plugin, maven-surefire-plugin, mockito-core, parent
- java-api/pom.xml (capture: captured) — dependency clues: assertj-core, commons-io, jacoco-maven-plugin, jakarta.annotation-api, jakarta.servlet-api, java-api, junit-jupiter-engine, junit-jupiter-params, maven-javadoc-plugin, maven-pmd-plugin, maven-source-plugin, maven-surefire-plugin, mockito-core, parent, slf4j-api, slf4j-simple, spotbugs-annotations, spotbugs-maven-plugin
- java-security-core/pom.xml (capture: captured) — dependency clues: assertj-core, commons-io, env, jacoco-maven-plugin, jakarta.annotation-api, java-api, java-security-core, junit-jupiter-engine, junit-jupiter-params, logback-classic, maven-javadoc-plugin, maven-pmd-plugin, maven-source-plugin, maven-surefire-plugin, mockito-core, mockito-junit-jupiter, parent, spotbugs-maven-plugin, token-client
- java-security-it/pom.xml (capture: captured) — dependency clues: assertj-core, httpclient, java-security-it, java-security-test, junit-jupiter-params, junit-vintage-engine, maven-failsafe-plugin, maven-surefire-plugin, mockito-core, parent, slf4j-simple, spring-security, spring-security-oauth2-jose

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 176
- Forks at capture: 140
- Last updated: 2026-11-06T12:49:49Z
- Last pushed: 2026-11-23T06:11:23Z
- Topics: open-source

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/cloud-security-services-integration-library)
- [README](https://github.com/SAP/cloud-security-services-integration-library/blob/main/README.md)
- [Issues](https://github.com/SAP/cloud-security-services-integration-library/issues)
- [Releases](https://github.com/SAP/cloud-security-services-integration-library/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
