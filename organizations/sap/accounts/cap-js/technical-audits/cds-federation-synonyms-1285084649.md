# cap-js/cds-federation-synonyms

- Company: SAP
- Account: cap-js
- Repository: https://github.com/cap-js/cds-federation-synonyms
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:05:14+00:00

## Project purpose

CDS plugin for SAP HANA synonym-based data federation.

## Why this project is used

CDS plugin for CAP-to-CAP Data Federation based on SAP HANA synonyms.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, CAP CDS, Shell, Java
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js/audit-logging, @cap-js/cds-federation-synonyms, @cap-js/cds-test, @cap-js/hana, @cap-js/sqlite, @capire/xflights-data-syn, @sap/cds, @sap/cds-dk, @sap/cds-mtxs, @sap/xssec, cds-maven-plugin, cds-services-bom, flatten-maven-plugin, maven-compiler-plugin, maven-enforcer-plugin, maven-surefire-plugin, spring-boot-dependencies, spring-boot-maven-plugin, xtravels-j-parent
- Build/package tools: npm-compatible manifest, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/server.js, lib/audit-log.js, lib/build-plugin.js, lib/config-helper.js

## Setup and usage

- Usage: Install the plugin both in the provider and in the consumer app.
- Usage: If the consumer uses multi-tenancy, install the plugin in the consumer's MTX sidecar, too.
- Usage: npm install git+https://github.com/cap-js/cds-federation-synonyms.git

## Limitations and caveats

- Security / Disclosure: If you find any bug that may be a security problem, please follow the instructions found in our security policy on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Evidence and provenance

- README: https://github.com/cap-js/cds-federation-synonyms/blob/main/README.md
- README SHA: 260cee9e02895c76ac6734585b85cb7767ee0340
- Manifests: package.json, test/ext-guard-it/package.json, test/scenarios/package.json, test/e2e/xflights/package.json, test/e2e/xtravels-j/package.json, test/e2e/xtravels-j/pom.xml
- Sampled source files: lib/server.js, lib/audit-log.js, lib/build-plugin.js, lib/config-helper.js
- Git tree state: captured
- Evidence fingerprint: 21181687d9760db045422d92169a6866b74da779a996370dfeb2a45e19e6115a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
