# GoogleCloudPlatform/cloud-run-pubsub-pull

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-run-pubsub-pull](https://github.com/GoogleCloudPlatform/cloud-run-pubsub-pull)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-run-pubsub-pull/blob/master/README.md)
- README blob SHA: 0492b794e546a57b753a05992d48a2d717c8c692
- README bytes captured: 21181
- README truncated at capture limit: False
- Repository ID: 980805327
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Example code for autoscaling a Cloud Run service or worker pool that consumes messages from a Cloud Pub/Sub topic using a pull subscription based on utilization reported by the consumer instances.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:03:58+00:00

### Short excerpt (up to 300 words)

> This directory contains example Usage and billing can The example has three

### README headings

- Cloud Run Pub/Sub Pull Example
- Overview
- Architecture
- Consumer: Application business logic
- Worker sidecar/library
- Sidecar vs. library
- Directly exporting metrics from application business logic
- Scaler
- Worker-Scaler Metrics API {#api}
- Code Structure
- Deploying
- Configuration variables {#config}
- Example: "us-central1-docker.pkg.dev/<project ID>/<repo name>"
- Project number is used to construct Cloud Run's default URLs for routing
- requests from the worker to the scaler.
- The Pub/Sub subscription project ID. Defaults to the same project as
- $PROJECT_ID, but can be a different project.
- Build container images
- Deploy using Terraform
- Worker as a Cloud Run worker pool
- Worker as a Cloud Run service
- Deploy using `gcloud`
- Create service accounts and grant permissions
- Deploy worker
- Deploy in sidecar mode {#deploy}
- As a worker pool
- As a service
- Deploy scaler
- Resource type of the worker deployment. Set to "services" if the worker is
- deployed as a service.

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> This directory contains example

### Getting started and usage: Shutting down usage to stop billing

> Usage and billing can

### Architecture and design: Architecture

> The example has three

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 127,160 |
| HCL | 10,882 |
| Dockerfile | 1,488 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/pubsub, github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/golang/glog, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, go.opencensus.io, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc, go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp, go.opentelemetry.io/otel

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 28
- Forks at capture: 2
- Last updated: 2026-09-15T17:32:08Z
- Last pushed: 2026-09-15T17:34:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-run-pubsub-pull)
- [README](https://github.com/GoogleCloudPlatform/cloud-run-pubsub-pull/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-run-pubsub-pull/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-run-pubsub-pull/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
