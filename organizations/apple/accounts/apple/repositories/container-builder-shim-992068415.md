# apple/container-builder-shim

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/container-builder-shim](https://github.com/apple/container-builder-shim)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/container-builder-shim/blob/main/README.md)
- README blob SHA: 79229abdbb08d27d1ad4d7f7b8ae560a4fee7766
- Repository ID: 992068415
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Shim for connecting Swift host code to BuildKit running in a container. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:10:07+00:00

### Short excerpt (up to 100 words)

> **container-builder-shim** is a lightweight bridge that connects BuildKit's session protocol with containerization's Build API. It enables compatibility between BuildKit (the build engine behind Docker) and containerization by translating messages and file transfers between their respective APIs. - **Protocol Translation:** - Translates session protocol messages from BuildKit into requests understood by containerization. - **Session Management:** - Handles file synchronization, image resolution, build output streaming, and caching. - **FSSync:** Transfers local files required for builds. - **Resolver:** Resolves image references and tags. - **ContentStore:** Retrieves and caches build dependencies like base images and layers. - **Exporter:** Provides the final built image, including

### README headings

- container-builder-shim
- What It Does
- Key Components
- How It Works
- Build Context Transfer
- Responsibilities
- Primary data flow
- Context boundary rules
- `.dockerignore`
- `followpaths`
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 311,697 |
| Makefile | 6,234 |
| Shell | 2,847 |
| Dockerfile | 1,208 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/agext/levenshtein, github.com/cespare/xxhash/v2, github.com/containerd/console, github.com/containerd/containerd, github.com/containerd/containerd/api, github.com/containerd/containerd/v2, github.com/containerd/continuity, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/containerd/log, github.com/containerd/log/otel, github.com/containerd/platforms, github.com/containerd/ttrpc, github.com/containerd/typeurl/v2, github.com/distribution/reference, github.com/docker/cli, github.com/docker/docker-credential-helpers, github.com/docker/go-units
- Makefile (capture: captured)
- vendor/go.opentelemetry.io/otel/Makefile (capture: captured)
- vendor/go.opentelemetry.io/otel/requirements.txt (capture: captured) — dependency clues: codespell
- vendor/google.golang.org/grpc/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 137
- Forks at capture: 39
- Last updated: 2026-10-30T16:49:12Z
- Last pushed: 2026-10-30T16:49:07Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/container-builder-shim)
- [README](https://github.com/apple/container-builder-shim/blob/main/README.md)
- [Issues](https://github.com/apple/container-builder-shim/issues)
- [Releases](https://github.com/apple/container-builder-shim/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
