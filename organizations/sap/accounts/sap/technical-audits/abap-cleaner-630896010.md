# SAP/abap-cleaner

- Company: SAP
- Account: SAP
- Repository: https://github.com/SAP/abap-cleaner
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:17:35+00:00

## Project purpose

While there is no lack of guidelines and rules on what clean ABAP code should look like...

## Why this project is used

ABAP cleaner applies 100+ cleanup rules to ABAP code at a single keystroke

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, TypeScript, ABAP, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @types/node, @types/vscode, @vscode/vsce, build-helper-maven-plugin, com.sap.adt.abapcleaner.app, maven-antrun-plugin, org.junit, parent, target-platform-configuration, tycho-maven-plugin, tycho-p2-director-plugin, tycho-p2-repository-plugin, tycho-surefire-plugin, tycho-versions-plugin, typescript
- Build/package tools: npm-compatible manifest, Maven project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundJob.java, com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundTask.java, com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java, com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplayColors.java

## Setup and usage

No setup information established.

## Limitations and caveats

- Limitations and Known Issues: In ABAP development tools for Eclipse (ADT), the ABAP cleaner plug-in (as any other plug-in) can only be installed
- Limitations and Known Issues: from extensible versions of ADT, in which menu 'Help / Install New Software...' is available.
- Limitations and Known Issues: Since ABAP cleaner does not perform additional backend calls, cleanup is restricted to what can be done within the current code document,
- Limitations and Known Issues: without retrieving additional DDIC information, signatures, includes etc.
- Limitations and Known Issues: ABAP cleaner strives to offer cleanup rules that automatically detect what can be improved in the given ABAP code,
- Limitations and Known Issues: so after some initial configuration, users shall be able to apply "everything everywhere" with just one keystroke.
- Limitations and Known Issues: ABAP cleaner is therefore restricted to cleanup rules that keep functionality unchanged and can be applied without
- Limitations and Known Issues: any additional user interaction, or need for subsequent inspection of changes.

## Evidence and provenance

- README: https://github.com/SAP/abap-cleaner/blob/main/README.md
- README SHA: a47f8a0d14d486d947f623456e4c4e37f38550fb
- Manifests: pom.xml, com.sap.adt.abapcleaner.app/pom.xml, vscode-extension/package.json
- Sampled source files: com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundJob.java, com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundTask.java, com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java, com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplayColors.java
- Git tree state: captured
- Evidence fingerprint: 1437a259eef6c13bab31a452e250fdc4c394d341f0f3efd9f37810cdcf316358

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
