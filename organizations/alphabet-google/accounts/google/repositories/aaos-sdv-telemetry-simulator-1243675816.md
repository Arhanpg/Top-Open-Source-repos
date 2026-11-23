# google/aaos-sdv-telemetry-simulator

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/aaos-sdv-telemetry-simulator](https://github.com/google/aaos-sdv-telemetry-simulator)
- Default branch: develop
- README: [Open upstream README](https://github.com/google/aaos-sdv-telemetry-simulator/blob/develop/README.md)
- README blob SHA: c8a535706fe9b8a7b9e135a2be6a9234d39a1a40
- Repository ID: 1243675816
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:25:47+00:00

### Short excerpt (up to 100 words)

> Copyright 2025 Google LLC Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. --> This project sets up a Google Cloud Platform (GCP) infrastructure and orchestrator for running simulations. It includes

### README headings

- SDV Telemetry Cloud Simulation
- GCP Simulation Infrastructure and Orchestrator
- Infrastructure and Orchestration Prerequisites
- Project Structure
- Infrastructure (/infrastructure)
- Orchestrator (/orchestrator)
- Pipeline Scripts (../pipeline_scripts)
- Key Components
- Terraform Configuration
- Backend Configuration
- Key Variables
- Cloud Function Configuration
- Service Accounts
- Firestore
- Cloud Storage
- Environment Variables
- Example terraform.tfvars
- Deployment
- Automated Deployment Configuration
- Input files
- Output files
- API Requests
- Create a Simulation Request
- Delete a Simulation
- Read Simulation Data
- Firestore Indexes
- Response Format
- Simulation Agent
- Key Features
- Agent Prerequisites

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 257,048 |
| Dart | 41,265 |
| Starlark | 36,806 |
| HCL | 34,292 |
| Shell | 9,518 |
| Python | 8,644 |
| Dockerfile | 1,612 |
| HTML | 1,214 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- tools/go.mod (capture: captured) — dependency clues: github.com/bazelbuild/buildtools, github.com/golang/protobuf, google.golang.org/protobuf
- cloud_simulation/orchestrator/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute, cloud.google.com/go/compute/metadata, cloud.google.com/go/firestore, cloud.google.com/go/iam, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/pubsub, cloud.google.com/go/pubsub/v2, cloud.google.com/go/storage, github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/envoyproxy/go-control-plane/envoy, github.com/envoyproxy/protoc-gen-validate
- cloud_simulation/simulation-agent/Dockerfile (capture: captured)
- pipeline_scripts/deployment_validation/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute, cloud.google.com/go/compute/metadata, cloud.google.com/go/firestore, cloud.google.com/go/functions, cloud.google.com/go/iam, cloud.google.com/go/longrunning, cloud.google.com/go/monitoring, cloud.google.com/go/storage, github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/bazelbuild/rules_go, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/envoyproxy/go-control-plane/envoy, github.com/envoyproxy/protoc-gen-validate
- cloud_simulation/simulation-agent/agent/go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/monitoring, cloud.google.com/go/storage, github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/envoyproxy/go-control-plane/envoy, github.com/envoyproxy/protoc-gen-validate, github.com/felixge/httpsnoop, github.com/go-jose/go-jose/v4, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/google/s2a-go
- cloud_simulation/web_demo/backend/requirements.txt (capture: captured) — dependency clues: Flask, Flask-Cors, google-auth, google-cloud-storage, gunicorn, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 3
- Last updated: 2026-11-11T10:50:45Z
- Last pushed: 2026-11-14T03:27:41Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/aaos-sdv-telemetry-simulator)
- [README](https://github.com/google/aaos-sdv-telemetry-simulator/blob/develop/README.md)
- [Issues](https://github.com/google/aaos-sdv-telemetry-simulator/issues)
- [Releases](https://github.com/google/aaos-sdv-telemetry-simulator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
