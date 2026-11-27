# industrial-edge/archiving-and-visualization

- Company: Siemens
- Account: industrial-edge
- Repository: https://github.com/industrial-edge/archiving-and-visualization
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:10:40+00:00

## Project purpose

Archiving and visualization demo application for Industrial Edge

## Why this project is used

The Industrial Edge Application "Archiving & Visualization Demo" is based on a bottle filling process application from which data values are collected, stored in an Influxdb database and visualized with a Grafana dashboard.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @influxdata/influxdb-client, cors, influx, mqtt
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/mqtt-service/server.js, src/mqtt-service/data-collector.js, src/mqtt-service/global.js, src/mqtt-service/metadata.js

## Setup and usage

- Installation: You can find the further information about the following steps in the docs
- Installation: - Upload application to Industrial Edge Management
- Installation: - Configure and install application to Industrial Edge Device

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/industrial-edge/archiving-and-visualization/blob/main/README.md
- README SHA: 79f1641d83daa2f6cc9c2cddce8d18d17276e19e
- Manifests: src/mqtt-service/package.json
- Sampled source files: src/mqtt-service/server.js, src/mqtt-service/data-collector.js, src/mqtt-service/global.js, src/mqtt-service/metadata.js
- Git tree state: captured
- Evidence fingerprint: 4d909d73df1f247da070d69edc95b1be1f3989adb2640eac28f9630585315bbb

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
