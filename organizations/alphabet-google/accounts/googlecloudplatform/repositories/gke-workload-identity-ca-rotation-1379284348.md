# GoogleCloudPlatform/gke-workload-identity-ca-rotation

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/gke-workload-identity-ca-rotation](https://github.com/GoogleCloudPlatform/gke-workload-identity-ca-rotation)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/gke-workload-identity-ca-rotation/blob/main/README.md)
- README blob SHA: 68c1f9c1917e73a2cd4d42d6c98e8c357674ac7e
- README bytes captured: 21630
- README truncated at capture limit: False
- Repository ID: 1379284348
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:59:54+00:00

### Short excerpt (up to 300 words)

> The system uses a

### README headings

- GKE MWLID Automated CA Lifecycle Management
- Architecture
- Project Structure
- Getting Started
- 1. Build and Push Image
- Default build (us-central1 only)
- Multi-region build
- 2. Deploy Infrastructure
- Map your regional Subordinate pools
- ca_count (optional, default 1) = the expected number of active intermediate
- CAs in the pool; the rotator alerts when the pool doesn't match.
- 3. Update Jobs (Manual Code Push)
- Update Subordinate jobs
- Update Root transition jobs
- Root CA Rotation Orchestration
- Manual Orchestration Steps:
- Operations & "Break Glass"
- Bootstrapping Initial Infrastructure (Initial Seeding)
- 1. Bootstrap the Root CA
- 2. Bootstrap Regional Subordinates
- 3. Expected CA Count (Alerting on Drift)
- Manual Rotation
- Emergency Rotation (Disable Only)
- Task Management & Orchestration
- Centralized Orchestration Architecture
- Resiliency and The Two-Layer Retry System
- The Paused Queue Safety Net
- Managing Tasks Manually
- Configuration (terraform.tfvars)
- Testing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> The system uses a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 82,627 |
| HCL | 19,998 |
| Dockerfile | 340 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/cloudtasks, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/longrunning, cloud.google.com/go/security, github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/s2a-go, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, go.opentelemetry.io/auto/sdk, go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc, go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp, go.opentelemetry.io/otel, go.opentelemetry.io/otel/metric

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 3
- Last updated: 2026-09-23T12:38:01Z
- Last pushed: 2026-11-14T01:38:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/gke-workload-identity-ca-rotation)
- [README](https://github.com/GoogleCloudPlatform/gke-workload-identity-ca-rotation/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/gke-workload-identity-ca-rotation/issues)
- [Releases](https://github.com/GoogleCloudPlatform/gke-workload-identity-ca-rotation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
