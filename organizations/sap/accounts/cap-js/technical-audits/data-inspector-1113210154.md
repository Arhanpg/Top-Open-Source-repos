# cap-js/data-inspector

- Company: SAP
- Account: cap-js
- Repository: https://github.com/cap-js/data-inspector
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:02:40+00:00

## Project purpose

@cap-js/data-inspector is a plugin to **view data** of CAP Node.js applications. It comes with an SAPUI5 app consumable out of the box.

## Why this project is used

A CDS plugin designed to help support users and developers securely inspect raw database content in both local and production environments, ensuring compliance with security standards. It supports multiple data sources—including database entities and services—providing direct, auditable access for troubleshooting and analysis.

## Core features

- Exclude specific entities and elements from being exposed by the plugin. See Excluding Entities and Elements.: Exclude specific entities and elements from being exposed by the plugin. See Excluding Entities and Elements.
  - Evidence: README.md#Features
- Automatically log access to sensitive personal data using @cap-js/audit-logging. See Audit Logging.: Automatically log access to sensitive personal data using @cap-js/audit-logging. See Audit Logging.
  - Evidence: README.md#Features
- Provide xsuaa scope for access control. See Authorization.: Provide xsuaa scope for access control. See Authorization.
  - Evidence: README.md#Features

## Technology stack

- Languages: TypeScript, JavaScript, CAP CDS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js/audit-logging, @cap-js/cds-test, @cap-js/cds-typer, @cap-js/cds-types, @cap-js/data-inspector, @cap-js/sqlite, @sap/cds, @sap/cds-dk, @sap/ux-ui5-tooling, @types/mocha, @types/node, @ui5/cli, c8, chai, cross-env, eslint, eslint-config-prettier, mocha, prettier, rimraf, ts-node, tsx, typescript, typescript-eslint, ui5-task-zipper, yaml
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/configurators/index.ts, app/data-inspector-ui/webapp/Component.js, app/data-inspector-ui/webapp/controller/App.controller.js, app/data-inspector-ui/webapp/controller/columnview.controller.js

## Setup and usage

- Installation: Install the plugin in your CAP Node.js project:
- Installation: npm install @cap-js/data-inspector

## Limitations and caveats

- Security / Disclosure: If you find a bug that might be a security problem, follow the instructions in our security policy to report it. Don't create GitHub issues for security-related questions or problems.

## Evidence and provenance

- README: https://github.com/cap-js/data-inspector/blob/main/README.md
- README SHA: e065c372c0c205e51f017836bde28d2bd34839f5
- Manifests: package.json, test/package.json, app/data-inspector-ui/package.json
- Sampled source files: lib/configurators/index.ts, app/data-inspector-ui/webapp/Component.js, app/data-inspector-ui/webapp/controller/App.controller.js, app/data-inspector-ui/webapp/controller/columnview.controller.js
- Git tree state: captured
- Evidence fingerprint: 4733607a1f46ed16cd5c0002b05b9d941bd943676824602acad9696e9e5279e9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
