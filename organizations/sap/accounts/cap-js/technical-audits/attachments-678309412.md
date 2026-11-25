# cap-js/attachments

- Company: SAP
- Account: cap-js
- Repository: https://github.com/cap-js/attachments
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:25:54+00:00

## Project purpose

The @cap-js/attachments package is a CDS plugin that provides out-of-the box asset storage and handling by using an _aspect_ called Attachments. It also provides a CAP-level, easy-to-use integration of the SAP Object Store.

## Why this project is used

The @cap-js/attachments package is a CDS plugin that provides out-of-the box asset storage and handling by using an aspect Attachments. It also provides a CAP-level, easy to use integration of the SAP Object Store.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, CAP CDS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-sdk/client-s3, @aws-sdk/lib-storage, @azure/storage-blob, @cap-js/attachments, @cap-js/audit-logging, @cap-js/cds-test, @cap-js/hana, @cap-js/postgres, @cap-js/sqlite, @google-cloud/storage, @sap/cds
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/mtx/server.js, lib/csn-runtime-extension.js, lib/generic-handlers.js, lib/helper.js

## Setup and usage

- Quick Start: For a quick local development setup with in-memory storage:
- Quick Start: - The plugin is self-configuring as described, see the following details section. To enable attachments, simply add the plugin package to your project:
- Quick Start: npm add @cap-js/attachments
- Quick Start: The attachments plugin needs to be referenced in the package.json of the consuming CAP NodeJS application:
- Quick Start: "@cap-js/attachments": " ",
- Quick Start: In addition, different profiles can be found in package.json as well, such as:
- Quick Start: - To use Attachments, extend a CDS model by adding an element that refers to the pre-defined Attachments type (see Changes in the CDS Models for more details):
- Quick Start: using { Attachments } from '@cap-js/attachments';

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/cap-js/attachments/blob/main/README.md
- README SHA: e1a9521ba3c14fe2344a24e0530c2753aa8fd568
- Manifests: package.json, tests/incidents-app/package.json, tests/incidents-app/app/incidents/package.json
- Sampled source files: lib/mtx/server.js, lib/csn-runtime-extension.js, lib/generic-handlers.js, lib/helper.js
- Git tree state: captured
- Evidence fingerprint: 64c176f64c8ad096601fbe6480244b0258fc5ab77c267f6c2c8b1c8b9f495993

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
