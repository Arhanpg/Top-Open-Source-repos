# GoogleCloudPlatform/document-intake-accelerator

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/document-intake-accelerator](https://github.com/GoogleCloudPlatform/document-intake-accelerator)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/document-intake-accelerator/blob/main/README.md)
- README blob SHA: 5bf3b1e22b84013dfcde52f001e240c6a1886cc5
- README bytes captured: 15586
- README truncated at capture limit: False
- Repository ID: 532043924
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T20:17:27+00:00

### Short excerpt (up to 300 words)

> End-to-end workflow management: document export PROJECT_ID=<GCP Project ID>

### README headings

- Document Intake Accelerator
- Key features
- Getting Started to Deploy the DocAI Workflow
- Prerequisites
- A custom domain like your-domain.com, or leave it blank for using the Ingress IP address instead.
- Tested with gcloud v400.0.0
- GCP Orgnization policy
- GCP foundation - Terraform
- Create Terraform Statefile in GCS bucket.
- enabling GCP services first.
- Run the rest of Terraform
- ...
- Enter yes at the promopt to apply Terraform changes.
- in terraform/environments/dev folder
- Enable Firebase Auth
- Deploying Kubernetes Microservices
- Update DNS with custom Domain (Optional)
- Deployment Troubleshoot
- Terraform Troubleshoot
- App Engine already exists
- CloudRun Troubleshoot
- Frontend Web App
- Development
- Prerequisites
- Initial setup for local development
- Build and run all microservices in the default GKE cluster
- Build and run all microservices in Develompent mode with live reload
- Build and run with a specific microservice
- Build and run microservices with a custom Source Repository path
- Run with local minikube cluster

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Key features

> End-to-end workflow management: document

### Technology and requirements: Prerequisites

> export PROJECT_ID=<GCP Project ID>

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 508,562 |
| JavaScript | 171,699 |
| HCL | 56,547 |
| Shell | 20,506 |
| CSS | 20,025 |
| Dockerfile | 4,235 |
| HTML | 2,967 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- common/Dockerfile (capture: captured)
- common/requirements.txt (capture: captured) — dependency clues: fireo, google-cloud-bigquery, google-cloud-logging, google-cloud-pubsub, google-cloud-secret-manager, jsonschema, neo4j, pandas
- e2e/requirements.txt (capture: captured) — dependency clues: google-cloud-bigquery, mock, pylint, pytest, requests
- utils/requirements.txt (capture: captured) — dependency clues: faker, firebase_admin, fireo, google-cloud-bigquery, google-cloud-logging, google-cloud-pubsub, google-cloud-secret-manager, neo4j, pandas, pyarrow, pyyaml
- cloudrun/queue/Dockerfile (capture: captured)
- cloudrun/queue/requirements.txt (capture: captured) — dependency clues: fastapi, firebase_admin, gunicorn, pytest, uvicorn

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 23
- Forks at capture: 14
- Last updated: 2026-11-12T23:51:31Z
- Last pushed: 2026-10-30T21:02:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/document-intake-accelerator)
- [README](https://github.com/GoogleCloudPlatform/document-intake-accelerator/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/document-intake-accelerator/issues)
- [Releases](https://github.com/GoogleCloudPlatform/document-intake-accelerator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
