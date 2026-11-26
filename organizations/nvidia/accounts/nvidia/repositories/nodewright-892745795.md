# NVIDIA/nodewright

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nodewright](https://github.com/NVIDIA/nodewright)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nodewright/blob/main/README.md)
- README blob SHA: 8ce10cf1c31c9257118e022c5a6e007c0c97d07e
- README bytes captured: 13687
- README truncated at capture limit: False
- Repository ID: 892745795
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Kubernetes Operator to manage Node OS customizations.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:07:11+00:00

### Short excerpt (up to 300 words)

> NodeWright functions like a **Interruption Budget:** percent of See the examples/ directory Please report security vulnerabilities

### README headings

- NodeWright (formerly Skyhook)
- Why NodeWright?
- What is NodeWright?
- Where and When to use NodeWright
- Benefits
- Key Features
- Pre-built Packages
- Installation
- Replace <chart-version> with a published chart version from
- https://github.com/NVIDIA/nodewright/pkgs/container/nodewright%2Fcharts%2Fnodewright
- Monitoring and Troubleshooting
- Watch NodeWright apply packages
- Check NodeWright resource status
- Check overall status
- Get detailed status of a specific NodeWright
- Check node annotations for package state
- View node state annotations for a specific NodeWright
- Stages
- Packages
- Examples
- Kyverno Policy Examples
- [NodeWright Operator](operator/README.md)
- [NodeWright Agent](agent/README.md)
- [NodeWright CLI](docs/user-guide/cli.md)
- Quick Install
- Verify installation
- Contributing
- Governance & Maintainers
- Security
- Support

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: What is NodeWright?

> NodeWright functions like a

### Features and capabilities: Key Features

> **Interruption Budget:** percent of

### Getting started and usage: Examples

> See the examples/ directory

### Limitations and security: Security

> Please report security vulnerabilities

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 3,283,670 |
| Shell | 161,907 |
| JavaScript | 104,631 |
| Makefile | 68,674 |
| Python | 37,193 |
| Go Template | 19,005 |
| Dockerfile | 6,302 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- agent/go.mod (capture: captured) — dependency clues: github.com/Masterminds/semver/v3, github.com/go-logr/logr, github.com/go-task/slim-sprig/v3, github.com/google/go-cmp, github.com/google/pprof, github.com/onsi/ginkgo/v2, github.com/onsi/gomega, github.com/santhosh-tekuri/jsonschema/v6, github.com/stretchr/objx, github.com/stretchr/testify, go.yaml.in/yaml/v3, golang.org/x/mod, golang.org/x/net, golang.org/x/sync, golang.org/x/sys, golang.org/x/text, golang.org/x/tools
- agent/Makefile (capture: captured)
- chart/Chart.yaml (capture: captured)
- operator/go.mod (capture: captured) — dependency clues: cel.dev/expr, github.com/Azure/go-ansiterm, github.com/Masterminds/semver/v3, github.com/antlr4-go/antlr/v4, github.com/beorn7/perks, github.com/blang/semver/v4, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/emicklei/go-restful/v3, github.com/evanphx/json-patch, github.com/evanphx/json-patch/v5, github.com/felixge/httpsnoop, github.com/fsnotify/fsnotify, github.com/fxamacker/cbor/v2, github.com/go-errors/errors, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-logr/zapr, github.com/go-openapi/jsonpointer
- operator/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 79
- Forks at capture: 44
- Last updated: 2026-11-21T06:29:00Z
- Last pushed: 2026-11-23T17:04:10Z
- Topics: kubernetes, linux, os, package-manager

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nodewright)
- [README](https://github.com/NVIDIA/nodewright/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nodewright/issues)
- [Releases](https://github.com/NVIDIA/nodewright/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
