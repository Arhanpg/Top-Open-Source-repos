# GoogleCloudPlatform/dpi-accelerator-beckn-onix

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/dpi-accelerator-beckn-onix](https://github.com/GoogleCloudPlatform/dpi-accelerator-beckn-onix)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/dpi-accelerator-beckn-onix/blob/main/README.md)
- README blob SHA: 42a9e15610abe4a5c65aa761458ec08447b9b396
- README bytes captured: 23157
- README truncated at capture limit: False
- Repository ID: 1059877887
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T20:27:03+00:00

### Short excerpt (up to 300 words)

> **Automated Deployment**: A simple, The recommended way to Beckn-Onix is a cloud-native, **Backend Services**: Go **Installer**: The installer supports advanced

### README headings

- DPI Accelerator - BECKN-ONIX
- Key Features
- Security Features (Cloud Armor & Outbound Proxy)
- Getting Started
- Repository Structure
- High-Level Architecture
- Onix Architecture Diagrams
- Technology Stack
- Core Services & API Endpoints
- 1. Gateway
- 2. Registry
- 3. Registry Admin
- 4. Subscriber
- 5. Adapter (BAP/BPP)
- The Onix Installer can also deploy these adapters (along with their configured plugins), which can be configured to act as a BAP (Buyer App), a BPP (Provider App), or both, depending on the user's needs during the installation process.
- Configuration
- `onixctl`: The Build & Packaging Tool
- Plugin Architecture
- Deployment (BECKN Onix GCP Installer)
- Security and Authentication
- Inbound Authentication (Calling Adapter or Subscriber)
- Protected APIs
- Target Audience Values
- Client-Side Token Generation
- 1. Calling from GCP (or other clouds via Workload Identity Federation)
- Go
- Python
- Automatically loads from GOOGLE_APPLICATION_CREDENTIALS or Metadata Server
- Generate ID token for specific audience
- Create a request object to communicate with the auth server

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Key Features

> **Automated Deployment**: A simple,

### Getting started and usage: Getting Started

> The recommended way to

### Architecture and design: High-Level Architecture

> Beckn-Onix is a cloud-native,

### Technology and requirements: Technology Stack

> **Backend Services**: Go **Installer**:

### Limitations and security: Security Features (Cloud Armor & Outbound Proxy)

> The installer supports advanced

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 1,053,517 |
| TypeScript | 337,173 |
| Python | 325,650 |
| HCL | 247,128 |
| Shell | 82,447 |
| HTML | 70,509 |
| CSS | 49,131 |
| Jinja | 32,345 |
| PLpgSQL | 11,046 |
| Go Template | 9,270 |
| JavaScript | 5,359 |
| Makefile | 259 |
| Smarty | 227 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cel.dev/expr, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/cloudsqlconn, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/monitoring, cloud.google.com/go/pubsub, cloud.google.com/go/secretmanager, cloud.google.com/go/storage, dario.cat/mergo, github.com/DATA-DOG/go-sqlmock, github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/Microsoft/go-winio, github.com/ProtonMail/go-crypto, github.com/alicebob/miniredis/v2, github.com/beckn-one/beckn-onix
- deploy/onix_installer/makefile (capture: captured)
- deploy/onix_installer/backend/requirements.txt (capture: captured) — dependency clues: absl-py, annotated-types, anyio, certifi, cffi, charset-normalizer, click, cryptography, fastapi, google-api-core, google-auth, google-cloud-resource-manager, googleapis-common-protos, grpc-google-iam-v1, grpcio, grpcio-status, h11, httpcore, httpx, idna
- deploy/onix_installer/frontend/package.json (capture: captured) — dependency clues: @angular/animations, @angular/build, @angular/cdk, @angular/cli, @angular/common, @angular/compiler, @angular/compiler-cli, @angular/core, @angular/forms, @angular/material, @angular/platform-browser, @angular/platform-browser-dynamic, @angular/router, @types/jasmine, @types/js-yaml, jasmine-core, js-yaml, karma, karma-chrome-launcher, karma-coverage
- deploy/onix_installer/backend/installer_kit/terraform/helm_charts/onix_adapter/Chart.yaml (capture: captured)
- deploy/onix_installer/backend/installer_kit/terraform/helm_charts/onix_gateway/Chart.yaml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 8
- Last updated: 2026-11-13T10:51:23Z
- Last pushed: 2026-11-13T10:51:22Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/dpi-accelerator-beckn-onix)
- [README](https://github.com/GoogleCloudPlatform/dpi-accelerator-beckn-onix/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/dpi-accelerator-beckn-onix/issues)
- [Releases](https://github.com/GoogleCloudPlatform/dpi-accelerator-beckn-onix/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
