# GoogleCloudPlatform/key-protection-module

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/key-protection-module](https://github.com/GoogleCloudPlatform/key-protection-module)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/key-protection-module/blob/main/README.md)
- README blob SHA: 1ed3717f3d47de025532ad8c55aa29b04f43d985
- README bytes captured: 3219
- README truncated at capture limit: False
- Repository ID: 1218915838
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:37:20+00:00

### Short excerpt (up to 300 words)

> KPM consists of two Go 1.24+ Rust 2024

### README headings

- Key Protection Module (KPM)
- Project Overview
- Architecture
- Component Breakdown
- Building and Running
- Prerequisites
- Build Steps
- Docker Build
- Development Conventions
- Code Style
- Testing
- How to Contribute

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Project Overview

> KPM consists of two

### Technology and requirements: Prerequisites

> Go 1.24+ Rust 2024

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 233,258 |
| Rust | 154,584 |
| Shell | 32,412 |
| Python | 14,989 |
| C | 5,495 |
| Dockerfile | 2,635 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go, buf.build/go/protovalidate, cel.dev/expr, github.com/antlr4-go/antlr/v4, github.com/davecgh/go-spew, github.com/google/cel-go, github.com/google/uuid, github.com/pmezard/go-difflib, go.yaml.in/yaml/v3, golang.org/x/exp, golang.org/x/net, golang.org/x/sys, golang.org/x/text, google.golang.org/genproto/googleapis/api, google.golang.org/genproto/googleapis/rpc, google.golang.org/grpc, google.golang.org/protobuf
- km_common/Cargo.toml (capture: captured) — dependency clues: bssl-crypto, clear_on_drop, hex, libc, memmap2, prost, prost-build, protoc-bin-vendored, secrecy, strum, thiserror, tracing, tracing-subscriber, uuid, zeroize
- tests/requirements.txt (capture: captured) — dependency clues: jsonschema, pyhpke, pytest, requests, requests-unixsocket
- key_protection_service/key_custody_core/Cargo.toml (capture: captured) — dependency clues: km_common, prost, uuid, zeroize

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 13
- Last updated: 2026-10-28T20:39:06Z
- Last pushed: 2026-11-14T00:35:09Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/key-protection-module)
- [README](https://github.com/GoogleCloudPlatform/key-protection-module/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/key-protection-module/issues)
- [Releases](https://github.com/GoogleCloudPlatform/key-protection-module/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
