# cap-js-community/odata-v2-adapter

- Company: SAP
- Account: cap-js-community
- Repository: https://github.com/cap-js-community/odata-v2-adapter
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:57:22+00:00

## Project purpose

Exposes a full-fledged OData V2 service, converting OData V2 requests to CDS OData V4 service calls and responses back. Runs in the context of the SAP Cloud Application Programming Model (CAP) using CDS Node.js module @sap/cds or CDS Java modules com.sap.cds.

## Why this project is used

OData V2 adapter for CDS. Exposes a full-fledged OData V2 service, converting OData V2 requests to CDS OData V4 service calls and responses back.

## Core features

- GET, POST, PUT / MERGE / PATCH, DELETE: GET, POST, PUT / MERGE / PATCH, DELETE
  - Evidence: README.md#Features
- Batch support: Batch support
  - Evidence: README.md#Features
- Actions, Functions: Actions, Functions
  - Evidence: README.md#Features
- Analytical Annotations: Analytical Annotations
  - Evidence: README.md#Features
- Deep Expands/Selects: Deep Expands/Selects
  - Evidence: README.md#Features
- JSON, Atom (XML) format: JSON, Atom (XML) format
  - Evidence: README.md#Features
- Deep Structures: Deep Structures
  - Evidence: README.md#Features
- Data Type Mapping: Data Type Mapping
  - Evidence: README.md#Features
- IEEE754Compatible: IEEE754Compatible
  - Evidence: README.md#Features
- Messages / Error Handling: Messages / Error Handling
  - Evidence: README.md#Features
- Location Header: Location Header
  - Evidence: README.md#Features
- $inlinecount / $count / \$value: $inlinecount / $count / \$value
  - Evidence: README.md#Features
- Entity with Parameters: Entity with Parameters
  - Evidence: README.md#Features
- File Upload (binary, multipart/form-data): File Upload (binary, multipart/form-data)
  - Evidence: README.md#Features
- Stream Support (Octet and Url): Stream Support (Octet and Url)
  - Evidence: README.md#Features

## Technology stack

- Languages: JavaScript, CAP CDS, HTML, TypeScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js-community/odata-v2-adapter, @cap-js/cds-test, @cap-js/hana, @cap-js/postgres, @cap-js/sqlite, @eslint/js, @sap/cds, @sap/cds-dk, @sap/hdi-deploy, @types/express, @vitest/coverage-v8, @vitest/eslint-plugin, body-parser, body-parser-xml, compression, eslint, eslint-config-prettier, eslint-plugin-n, express, express-fileupload, http-proxy-middleware, node-fetch, prettier, supertest, typescript, typescript-eslint, vitest, xml2js
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: test-hana/_env/srv/server.js, src/build.js, src/index.d.ts, test-hana/_env/app/parameters/webapp/Component.js

## Setup and usage

- Getting Started: - Run npm add @cap-js-community/odata-v2-adapter in @sap/cds project
- Getting Started: - Execute cds-serve to start server
- Getting Started: - OData V2 service is available at http://localhost:4004/odata/v2/
- Getting Started: - OData V4 service is available at http://localhost:4004/odata/v4/

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/cap-js-community/odata-v2-adapter/blob/main/README.md
- README SHA: 22824b8ca3e731447015182e92a8d8c8d310fa7c
- Manifests: package.json, test-hana/_env/package.json, test-postgres/_env/package.json, test/_env/package.json, test-hana/_env/db/package.json
- Sampled source files: test-hana/_env/srv/server.js, src/build.js, src/index.d.ts, test-hana/_env/app/parameters/webapp/Component.js
- Git tree state: captured
- Evidence fingerprint: 3aff216f262b3127c40565359bdae9f87fdefbf1f6810314086280b0d3afc752

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
