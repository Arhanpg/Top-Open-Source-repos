# GoogleCloudPlatform/aef-orchestration-framework

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/aef-orchestration-framework](https://github.com/GoogleCloudPlatform/aef-orchestration-framework)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/aef-orchestration-framework/blob/main/README.md)
- README blob SHA: 52a3b8c573839f8b437090fafdee9b9efb1682af
- Repository ID: 819071328
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:44:18+00:00

### Short excerpt (up to 100 words)

> ***Note:*** For a comprehensive installation guide of all the AEF repositories together, please look here. Data orchestration plays a vital role in enabling efficient data access and analysis, this repository deploys the core artifacts of a streamlined serverless data orchestration framework using generic executors as Google Cloud Functions. And deployed via Terraform. This Orchestration Framework is the core integrator of the Analytics Engineering Framework comprised of: 1. **(This repository) Orchestration Framework**: Maintained by Analytics Engineers to provide seamless, extensible orchestration and execution infrastructure. 1. Data Model: Directly used by end data practitioners to manage data models, schemas, and Dataplex metadata.

### README headings

- Analytics Engineering Framework - Orchestration Framework
- Concepts
- Domain-Based vs. Central Orchestration
- Cloud Workflows Orchestration implementation:
- Scheduling and execution
- Repository
- Usage
- Terraform

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 67,596 |
| Shell | 46,241 |
| HCL | 14,445 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- functions/data-processing-engines/bq-saved-query-executor/requirements.txt (capture: captured) — dependency clues: functions-framework, google-api-python-client, google-auth, google-cloud-bigquery, google-cloud-dataform, google-cloud-logging, google-cloud-resource-manager, grpcio, grpcio-tools
- functions/data-processing-engines/dataflow-flextemplate-job-executor/requirements.txt (capture: captured) — dependency clues: functions-framework, google-api-python-client, google-auth, google-cloud-storage
- functions/data-processing-engines/dataform-tag-executor/requirements.txt (capture: captured) — dependency clues: functions-framework, google-api-python-client, google-auth, google-cloud-bigquery, google-cloud-dataform, google-cloud-logging, google-cloud-resource-manager, google-cloud-secret-manager, google-cloud-storage, grpcio, grpcio-tools
- functions/data-processing-engines/dataproc-serverless-job-executor/requirements.txt (capture: captured) — dependency clues: functions-framework, google-api-python-client, google-auth, google-cloud-bigquery, google-cloud-dataform, google-cloud-logging, google-cloud-resource-manager, google-cloud-storage, grpcio, grpcio-tools
- functions/orchestration-helpers/intermediate/requirements.txt (capture: captured) — dependency clues: functions-framework, google-cloud-bigquery, google-cloud-error-reporting, google-cloud-logging
- functions/orchestration-helpers/pipeline-executor/requirements.txt (capture: captured) — dependency clues: functions-framework, google-cloud-bigquery, google-cloud-error-reporting, google-cloud-logging, google-cloud-workflows

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 22
- Last updated: 2026-07-13T16:40:44Z
- Last pushed: 2025-05-07T17:27:56Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/aef-orchestration-framework)
- [README](https://github.com/GoogleCloudPlatform/aef-orchestration-framework/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/aef-orchestration-framework/issues)
- [Releases](https://github.com/GoogleCloudPlatform/aef-orchestration-framework/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
