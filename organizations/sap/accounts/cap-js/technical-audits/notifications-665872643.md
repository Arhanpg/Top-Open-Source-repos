# cap-js/notifications

- Company: SAP
- Account: cap-js
- Repository: https://github.com/cap-js/notifications
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:41:37+00:00

## Project purpose

The @cap-js/notifications package is a CDS plugin that provides support for publishing business notifications in SAP Build Work Zone.

## Why this project is used

CDS Plugin that provides support for publishing business notifications in SAP Build WorkZone.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, CAP CDS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js/cds-test, @cap-js/cds-types, @cap-js/hana, @cap-js/notifications, @cap-js/sqlite, @sap-cloud-sdk/connectivity, @sap-cloud-sdk/http-client, @sap-cloud-sdk/resilience, @sap-cloud-sdk/util, @sap/cds, @sap/cds-dk, @sap/xssec, express, jest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/build.js, lib/compile.js, lib/notificationTypes.js, lib/utils.js

## Setup and usage

- Getting Started: After installing the plugin, you can send notifications in two ways:
- Quick start: Direct notification: Send a simple notification using notify():
- Quick start: Direct notification: const alert = await cds.connect.to("notifications")
- Quick start: Direct notification: recipients: ["user@example.com"],
- Quick start: Direct notification: title: "Book Order Received",
- Quick start: Direct notification: description: 'Your order for "Wuthering Heights" is being processed.'

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/cap-js/notifications/blob/main/README.md
- README SHA: 5e901732b518537455702ad0f51f5013b1c88c37
- Manifests: package.json, tests/bookshop/package.json
- Sampled source files: lib/build.js, lib/compile.js, lib/notificationTypes.js, lib/utils.js
- Git tree state: captured
- Evidence fingerprint: 61e470e58ecde8ccaed7fd79b4260abb02a7625352372e36970daf7caf06595a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
