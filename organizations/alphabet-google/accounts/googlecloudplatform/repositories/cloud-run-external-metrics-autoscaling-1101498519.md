# GoogleCloudPlatform/cloud-run-external-metrics-autoscaling

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-run-external-metrics-autoscaling](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/blob/main/README.md)
- README blob SHA: f9f6daf49b7f2717a9b13c94960d71e4e30df5f9
- README bytes captured: 17802
- README truncated at capture limit: False
- Repository ID: 1101498519
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Cloud Run External Metrics Autoscaling (CREMA) leverages KEDA to provide autoscaling for Cloud Run services and worker pools based on external metrics (such as Kafka lag, Pub/Sub queue depth, or Prometheus)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:38:08+00:00

### Short excerpt (up to 300 words)

> CREMA can be deployed 1. **Google Cloud SDK:** This project currently depends

### README headings

- Cloud Run External Metrics Autoscaling
- Architecture
- How it works
- Compatibility
- Setup
- Prerequisites
- Create a GCP Service Account
- Configure
- For a service
- For a worker pool
- Deploy
- Verify
- Cloud Logging Logs
- Optional: Build the container image from source
- Metrics
- Image Versioning
- Known Issues
- Support

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: How it works

> CREMA can be deployed

### Technology and requirements: Prerequisites

> 1. **Google Cloud SDK:**

### Limitations and security: Compatibility

> This project currently depends

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 304,947 |
| HCL | 7,202 |
| Dockerfile | 1,637 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- metric-provider/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/logging, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/parametermanager, cloud.google.com/go/secretmanager, cloud.google.com/go/spanner, cloud.google.com/go/storage, dario.cat/mergo, filippo.io/edwards25519, github.com/Azure/azure-amqp-common-go/v4, github.com/Azure/azure-kusto-go/azkustodata, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 57
- Forks at capture: 8
- Last updated: 2026-10-30T19:51:54Z
- Last pushed: 2026-10-30T19:51:51Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling)
- [README](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
