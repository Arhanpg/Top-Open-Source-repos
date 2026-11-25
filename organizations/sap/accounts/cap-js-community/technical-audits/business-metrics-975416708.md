# cap-js-community/business-metrics

- Company: SAP
- Account: cap-js-community
- Repository: https://github.com/cap-js-community/business-metrics
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:50:59+00:00

## Project purpose

**Business-metrics** is an extension library for **@cap-js/telemetry** designed for CAP (Cloud Application Programming) applications. It allows you to effortlessly track usage and performance by integrating Counter and Gauge metrics directly into your CAP service entities and actions. These metrics enable better observability and can be exported to telemetry tools for monitoring.

## Why this project is used

**Business-metrics** is an extension library for **@cap-js/telemetry** designed for CAP (Cloud Application Programming) applications. It allows you to effortlessly track usage and performance by integrating Counter and Gauge metrics directly into your CAP service entities and actions. These metrics enable better observability and can be exported to telemetry tools for monitoring.

## Core features

- **Counter Metrics**: Track the number of times specific events occur for service entities or actions (e.g., READ, DELETE or custom actions like releaseSalesOrde: **Counter Metrics**: Track the number of times specific events occur for service entities or actions (e.g., READ, DELETE or custom actions like releaseSalesOrder).
  - Evidence: README.md#Features
- **Gauge Metrics**: Monitor and observe specific fields of entities, such as stock levels or other numeric values.: **Gauge Metrics**: Monitor and observe specific fields of entities, such as stock levels or other numeric values.
  - Evidence: README.md#Features

## Technology stack

- Languages: JavaScript, CAP CDS
- Frameworks/libraries: Unknown / not established
- Dependency names: @cap-js/cds-test, @cap-js/cds-types, @cap-js/sqlite, @cap-js/telemetry, @opentelemetry/api, @sap/cds, @sap/cds-dk, @sap/cds-mtxs, business-metrics, eslint, jest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/metrics/entity-metrics.js, cds-plugin.js, jest.config.js

## Setup and usage

- Installation: 1. Add business-metrics to your dependencies via npm add @cap-js-community/business-metrics
- Installation: npm add @cap-js-community/business-metrics
- Installation: 2. Enable business metrics in package.json under the cds.requires.telemetry.metrics section:
- Installation: "enableBusinessMetrics": true

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/cap-js-community/business-metrics/blob/main/README.md
- README SHA: 2fc09b186288ab116cc51c6d57e7f97b2691a27f
- Manifests: package.json, test/bookshop/package.json
- Sampled source files: lib/metrics/entity-metrics.js, cds-plugin.js, jest.config.js
- Git tree state: captured
- Evidence fingerprint: 1515cd3a0f853e2b5643b5da425005fe597c4eb80159e409954af61db0eafdb9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
