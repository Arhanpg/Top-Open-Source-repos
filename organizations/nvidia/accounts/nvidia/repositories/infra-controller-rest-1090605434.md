# NVIDIA/infra-controller-rest

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/infra-controller-rest](https://github.com/NVIDIA/infra-controller-rest)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/infra-controller-rest/blob/main/README.md)
- README blob SHA: fa3e34be2c48468ff482038e46191e25646df9b4
- README bytes captured: 11541
- README truncated at capture limit: False
- Repository ID: 1090605434
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA Infra Controller - Hardware Lifecycle Management (REST API)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T07:31:46+00:00

### Short excerpt (up to 300 words)

> SPDX-FileCopyrightText: Copyright (c) 2026 make pre-commit-install This will: Supporting modules: **common** - Go 1.25.4 or later Versions older than v1.3.0

### README headings

- NVIDIA Infrastructure Controller (NICo) REST API
- Prerequisites
- Core Compatibility Matrix
- Quick Start
- Run Unit Tests
- Option A: Local Development with Kind
- Option B: Bare-Metal Cluster with helm-prereqs
- 1. Build and push images to your registry
- 2. Set environment variables
- 3. Clone infra-controller-core (if not already present as a sibling directory)
- 4. Run setup from the infra-controller-core repo
- Option C: Manual / Kustomize Production Deployment
- CLI
- Using the API
- Get an Access Token
- Example API Requests
- Health check
- Get current tenant (auto-creates on first access)
- List sites
- Test Users
- Building Docker Images
- Build All Images
- Build with Custom Registry and Tag
- Push to Your Registry
- Docker Hub
- AWS ECR
- Google Container Registry
- Azure Container Registry
- Available Images
- Architecture

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> SPDX-FileCopyrightText: Copyright (c) 2026

### Getting started and usage: Install pre-commit hooks (first time setup)

> make pre-commit-install This will:

### Architecture and design: Architecture

> Supporting modules: **common** -

### Technology and requirements: Prerequisites

> Go 1.25.4 or later

### Limitations and security: Core Compatibility Matrix

> Versions older than v1.3.0

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 15,527,065 |
| HTML | 237,127 |
| Shell | 87,781 |
| Makefile | 37,217 |
| Mustache | 15,348 |
| Python | 12,196 |
| Go Template | 7,421 |
| Dockerfile | 783 |
| PLpgSQL | 435 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: connectrpc.com/connect, connectrpc.com/grpchealth, connectrpc.com/grpcreflect, connectrpc.com/otelconnect, dario.cat/mergo, github.com/Azure/go-ansiterm, github.com/DATA-DOG/go-sqlmock, github.com/Microsoft/go-winio, github.com/NVIDIA/infra-controller-rest/sdk/standard, github.com/Nerzal/gocloak/v13, github.com/PagerDuty/go-pagerduty, github.com/asaskevich/govalidator, github.com/avast/retry-go/v4, github.com/beorn7/perks, github.com/buger/jsonparser, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/containerd/log
- Makefile (capture: captured)
- flow/Dockerfile (capture: captured)
- flow/Makefile (capture: captured)
- nvswitch-manager/Makefile (capture: captured)
- powershelf-manager/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 38
- Forks at capture: 38
- Last updated: 2026-11-06T00:32:09Z
- Last pushed: 2026-06-02T04:30:02Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/infra-controller-rest)
- [README](https://github.com/NVIDIA/infra-controller-rest/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/infra-controller-rest/issues)
- [Releases](https://github.com/NVIDIA/infra-controller-rest/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
