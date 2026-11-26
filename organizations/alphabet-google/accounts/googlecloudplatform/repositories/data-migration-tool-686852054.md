# GoogleCloudPlatform/data-migration-tool

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/data-migration-tool](https://github.com/GoogleCloudPlatform/data-migration-tool)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/data-migration-tool/blob/main/README.md)
- README blob SHA: 57902801db99b17fe0b54c4458f165e8b1a3929c
- README bytes captured: 13300
- README truncated at capture limit: False
- Repository ID: 686852054
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

DMT is an end to end automation of data warehouse migration, focused on extraction, SQL translation, data migration, data validation, etc. The main goal is to reduce migration delivery time

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:19:36+00:00

### Short excerpt (up to 300 words)

> For Installation user guide, The following design proposes

### README headings

- Data Migration Tool Introduction
- Why you want to use Data Migration Tool
- What Data Migration Tool can provide you
- Supported Sources
- User Story
- Extract and translate DDL from on-prem data warehouses into BigQuery DDL syntax.
- Create tables in BigQuery.
- Validate Schema in BigQuery
- Transfer data from on-premise to BigQuery.
- Translate SQL SELECT statements into BigQuery syntax.
- Validate SQL SELECT statements in BigQuery.
- Translate DML statements into BigQuery syntax.
- Validate DML statements in BigQuery.
- Design
- Overview
- Controller
- DAG Overview
- Infrastructure/Services
- Cloud Composer
- Cloud Run
- Cloud Pub/Sub
- Cloud Storage
- Batch SQL Translator
- BigQuery
- Data Validation Tool
- Looker Studio
- Appendix
- DAG Parallelization & Composer Sizing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Data Migration Tool Introduction

> For Installation user guide,

### Architecture and design: Design

> The following design proposes

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 422,264 |
| HCL | 124,877 |
| Shell | 25,807 |
| Dockerfile | 3,697 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/translation/dvt/Dockerfile (capture: captured)
- src/translation/dvt/requirements.txt (capture: captured) — dependency clues: Flask, Werkzeug, cx_Oracle, google-cloud-secret-manager, google-pso-data-validator, gunicorn, hdfs, teradata, teradatasql, thrift-sasl
- src/translation/event_listener/Dockerfile (capture: captured)
- src/translation/event_listener/requirements.txt (capture: captured) — dependency clues: Flask, Werkzeug, google-api-python-client, google-auth, google-cloud-logging, gunicorn, jsonpath-ng
- src/datamigration/scripts/teradata/agent_controller/requirements.txt (capture: captured) — dependency clues: PyYAML, google-cloud-pubsub

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 45
- Forks at capture: 18
- Last updated: 2026-06-19T22:52:41Z
- Last pushed: 2026-04-13T23:39:46Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/data-migration-tool)
- [README](https://github.com/GoogleCloudPlatform/data-migration-tool/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/data-migration-tool/issues)
- [Releases](https://github.com/GoogleCloudPlatform/data-migration-tool/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
