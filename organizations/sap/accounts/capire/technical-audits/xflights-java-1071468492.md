# capire/xflights-java

- Company: SAP
- Account: capire
- Repository: https://github.com/capire/xflights-java
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:41:46+00:00

## Project purpose

This is a CAP Java application that manages master data like Airlines, Airports, and Flights. It provides a reuse package for clients to consume this data. It is used in the xtravels-java application.

## Why this project is used

Master data service for flights, airlines, airports built with CAP Java

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: CAP CDS, JavaScript, Java
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js/sqlite, @sap/cds-dk, @sap/hdi-deploy, cds-adapter-hcql, cds-adapter-odata-v4, cds-feature-remote-hcql, cds-maven-plugin, cds-services-bom, cds-starter-cloudfoundry, cds-starter-spring-boot, flatten-maven-plugin, h2, hdb, java-bom, maven-clean-plugin, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, spotless-maven-plugin, spring-boot-dependencies, spring-boot-devtools, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-test, xflights, xflights-data, xflights-parent
- Build/package tools: npm-compatible manifest, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: srv/src/main/java/sap/capire/xflights/Application.java

## Setup and usage

- Usage: Then you can import and use the entities in your CDS models like this:
- Usage: using { sap.capire.flights.data.Flights } from 'capire/xflights-data';
- Usage: // mashup with your own entities ...
- Usage: Find examples for that in the _xtravels-java_ application.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/capire/xflights-java/blob/main/README.md
- README SHA: eb1fd10841b3c263cc9d807a0dab320a9f004145
- Manifests: package.json, pom.xml, db/package.json, srv/pom.xml, apis/data-service/pom.xml
- Sampled source files: srv/src/main/java/sap/capire/xflights/Application.java
- Git tree state: captured
- Evidence fingerprint: eb5ba55328c4953030f0758d68763f66fe4db0a3278775977b4cbfe030c84ce9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
