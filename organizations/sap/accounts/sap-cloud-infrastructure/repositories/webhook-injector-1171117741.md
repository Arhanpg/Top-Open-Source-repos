# SAP-cloud-infrastructure/webhook-injector

- Company: SAP
- GitHub account: [https://github.com/SAP-cloud-infrastructure](https://github.com/SAP-cloud-infrastructure)
- Mapping status: official-directory-listed
- Repository: [SAP-cloud-infrastructure/webhook-injector](https://github.com/SAP-cloud-infrastructure/webhook-injector)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-cloud-infrastructure/webhook-injector/blob/main/README.md)
- README blob SHA: d84d08ea5f41ab5de7428a796b4b6e3492917797
- Repository ID: 1171117741
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Kubernetes controller that runs as a sidecar to webhook servers, managing the lifecycle of webhook configurations and TLS certificates for remote or local clusters.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:49:35+00:00

### Short excerpt (up to 100 words)

> SPDX-FileCopyrightText: 2026 SAP SE or an SAP affiliate company SPDX-License-Identifier: Apache-2.0 --> A Kubernetes controller that runs as a sidecar to webhook servers, managing webhook configurations and TLS certificates for remote or local clusters. - **Automatic Certificate Management**: Generates and rotates self-signed certificates with dynamic SANs. - **Smart Rotation**: Time-based (20% remaining validity threshold), config-based (SAN changes), or manual (annotation). - **Remote Cluster Support**: Manage webhooks in clusters where the webhook server doesn't run. - **Language Agnostic**: Works with any webhook server that can watch certificate files for changes. - **High Availability**: Leader election with multi-replica support, zero-downtime rotation. -

### README headings

- webhook-injector
- Features
- Architecture
- Quick Start
- Prerequisites
- Build
- Sidecar Deployment
- Certificate Management
- Configuration
- Gardener Seed Deployment
- Direct-Apply (GRM-free) Patch Mode
- Metrics
- Alerts
- Certificate expiry (alertable signal: time-to-expiry of the live cert)
- Propagation chain (alertable signal: caBundle is not reaching the consumer)
- Configuration safety
- Testing
- Unit tests
- E2E integration tests (creates kind clusters, tests multi-cluster setup)
- Manual E2E workflow
- Development
- Docker
- Deployment
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 438,039 |
| Makefile | 15,813 |
| Shell | 5,482 |
| Dockerfile | 3,003 |
| Nix | 375 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/andybalholm/brotli, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/gardener/gardener/pkg/apis, github.com/go-logr/logr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/google/btree, github.com/google/gnostic-models, github.com/google/go-cmp, github.com/google/uuid, github.com/josharian/intern
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-05T12:34:08Z
- Last pushed: 2026-11-07T22:50:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-cloud-infrastructure/webhook-injector)
- [README](https://github.com/SAP-cloud-infrastructure/webhook-injector/blob/main/README.md)
- [Issues](https://github.com/SAP-cloud-infrastructure/webhook-injector/issues)
- [Releases](https://github.com/SAP-cloud-infrastructure/webhook-injector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
