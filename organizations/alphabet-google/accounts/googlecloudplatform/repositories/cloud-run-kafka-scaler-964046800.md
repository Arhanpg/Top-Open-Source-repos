# GoogleCloudPlatform/cloud-run-kafka-scaler

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-run-kafka-scaler](https://github.com/GoogleCloudPlatform/cloud-run-kafka-scaler)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-run-kafka-scaler/blob/main/README.md)
- README blob SHA: c367e444a469d1eb3ca15cd55e26d3c4bf3f32f8
- README bytes captured: 22194
- README truncated at capture limit: False
- Repository ID: 964046800
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Buildable container image for horizontally scaling Kafka consumers running on Cloud Run

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:45:20+00:00

### Short excerpt (up to 300 words)

> The following diagram provides

### README headings

- Cloud Run Kafka Autoscaler
- Architecture
- Building the Kafka Autoscaler
- Setting up and Deploying the Autoscaler
- Prerequisites
- 1. Kafka Cluster
- 2. Deployed Cloud Run Consumer
- 3. Required Roles
- 4. Create Required Secrets
- a) Kafka Admin Client Secret (`ADMIN_CLIENT_SECRET`)
- b) Scaler Configuration Secret (`SCALER_CONFIG_SECRET`)
- Create the secret
- Deployment Options
- Option 1: Manual Deployment (`gcloud` / Shell Script)
- Set Environment Variables
- GCP Project ID
- GCP Region
- Fully qualified name of the deployed Cloud Run service or worker pool to scale
- Example: projects/my-project/locations/us-central1/workerpools/my-kafka-consumer
- Email of the Service Account used by the consumer workload. The setup script
- will grant the scaler service account permission to use consumer service
- account.
- Example: my-consumer-service-account@my-project.iam.gserviceaccount.com
- Kafka consumer group ID to monitor
- Name for the scaler Cloud Run service to be created
- Full Artifact Registry path to the scaler image built in the previous step
- Example: us-central1-docker.pkg.dev/my-project/my-repo/my_kafka_autoscaler
- Fully qualified name of the existing secret which contains scaling
- configuration
- Example: projects/my-project/secrets/scaler-config

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> The following diagram provides

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 329,094 |
| Starlark | 24,854 |
| HCL | 21,418 |
| Shell | 10,915 |
| Dockerfile | 872 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- examples/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 45
- Forks at capture: 10
- Last updated: 2026-10-20T22:53:05Z
- Last pushed: 2026-08-19T18:38:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-run-kafka-scaler)
- [README](https://github.com/GoogleCloudPlatform/cloud-run-kafka-scaler/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-run-kafka-scaler/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-run-kafka-scaler/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
