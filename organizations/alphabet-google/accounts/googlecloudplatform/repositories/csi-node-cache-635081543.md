# GoogleCloudPlatform/csi-node-cache

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/csi-node-cache](https://github.com/GoogleCloudPlatform/csi-node-cache)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/csi-node-cache/blob/main/README.md)
- README blob SHA: d5b281131efbe2e078b5dc9f73ee7be157f42826
- README bytes captured: 7421
- README truncated at capture limit: False
- Repository ID: 635081543
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:47:36+00:00

### Short excerpt (up to 300 words)

> This repository deploys a CSI ephemeral driver for a shared node volume. All pods that use it see the same volume, and this volume outlives

### README headings

- Kubernetes Node Cache
- Note
- Set Up
- Artifact Registry
- Workload Identity
- Deployment
- Use
- PD Caches
- Workload Identity Setup

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Kubernetes Node Cache

> This repository deploys a CSI ephemeral driver for a shared node volume. All pods that use it see the same volume, and this volume outlives

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 100,587 |
| Shell | 8,385 |
| Dockerfile | 4,486 |
| Makefile | 1,784 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, github.com/beorn7/perks, github.com/cespare/xxhash/v2, github.com/container-storage-interface/spec, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch/v5, github.com/felixge/httpsnoop, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/swag, github.com/google/gnostic-models, github.com/google/go-cmp
- Makefile (capture: captured)
- cmd/controller/Dockerfile (capture: captured)
- cmd/driver/Dockerfile (capture: captured)
- vendor/go.opentelemetry.io/otel/Makefile (capture: captured)
- vendor/go.opentelemetry.io/otel/requirements.txt (capture: captured) — dependency clues: codespell

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 2
- Last updated: 2026-08-19T17:07:03Z
- Last pushed: 2026-11-14T03:29:03Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/csi-node-cache)
- [README](https://github.com/GoogleCloudPlatform/csi-node-cache/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/csi-node-cache/issues)
- [Releases](https://github.com/GoogleCloudPlatform/csi-node-cache/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
