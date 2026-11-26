# cap-js/cds-intellij

- Company: SAP
- Account: cap-js
- Repository: https://github.com/cap-js/cds-intellij
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:01:32+00:00

## Project purpose

Welcome to **SAP CDS Language Support for IntelliJ**. It is a plugin for IntelliJ IDEs that provides editing and development support for the CDS language as used in the SAP Cloud Application Programming Model (CAP).

## Why this project is used

SAP CDS Language Support for IntelliJ

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Shell, JavaScript, Kotlin, CAP CDS
- Frameworks/libraries: Unknown / not established
- Dependency names: @sap/cds-lsp
- Build/package tools: Gradle build file, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/js/codestyle/patchJavaSrc.js, src/js/usersettings/patchUserSettingsJavaSrc.js, src/js/util/string.js, src/main/java/com/sap/cap/cds/intellij/CdsFileType.java

## Setup and usage

- Download and Installation: Prepare your environment:
- Download and Installation: 1. Install [](https://nodejs.org/en/)
- Download and Installation: on your computer if not already present.
- Download and Installation: 2. Register the new Node.js installation in your IntelliJ IDE by going to *File > Settings > Languages & Frameworks > CDS*.
- Download and Installation: 3. If you have installed the SAP CDS Language Support for IntelliJ plugin from a ZIP file before, uninstall it.
- Download and Installation: - Note: we have reset the current plugin version to 1.0.0 for the first JetBrains Marketplace release, to clarify that the feature set is still incomplete.
- Download and Installation: Install or update the plugin:
- Download and Installation: 1. In your IntelliJ IDE, go to *File > Settings > Plugins*.

## Limitations and caveats

- Known Compatibility Issues: | Symptom | Solution |
- Known Compatibility Issues: |------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
- Known Compatibility Issues: | SAP CDS Language Support for IntelliJ is not enabled in the IDE. | 1.x versions of the plugin are not compatible with the **free** IntelliJ **Community** Edition. Make sure you are using a version ≥ 2.x of the plugin. |
- Known Compatibility Issues: | CDS file icons are missing and/or no syntax highlighting | Uninstall any previous versions of the plugin *(File > Settings > Plugins)*. Remove the 'cds' TextMate Bundle *(File > Settings > Editor > TextMate Bundles)*. Restart the IDE. Install the latest plugin version. |

## Evidence and provenance

- README: https://github.com/cap-js/cds-intellij/blob/main/README.md
- README SHA: 8b48cb2b5bddc4cd7406d9e0f27c2151ef19b06f
- Manifests: build.gradle, lsp/package.json
- Sampled source files: src/js/codestyle/patchJavaSrc.js, src/js/usersettings/patchUserSettingsJavaSrc.js, src/js/util/string.js, src/main/java/com/sap/cap/cds/intellij/CdsFileType.java
- Git tree state: captured
- Evidence fingerprint: d034477f3af72d936db86ab157032a5dbff5edac4f9ebe5da0a9e8b2780c8f72

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
