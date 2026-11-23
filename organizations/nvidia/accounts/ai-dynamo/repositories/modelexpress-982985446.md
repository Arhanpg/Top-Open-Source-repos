# ai-dynamo/modelexpress

- Company: NVIDIA
- GitHub account: [https://github.com/ai-dynamo](https://github.com/ai-dynamo)
- Mapping status: official-project-linked
- Repository: [ai-dynamo/modelexpress](https://github.com/ai-dynamo/modelexpress)
- Default branch: main
- README: [Open upstream README](https://github.com/ai-dynamo/modelexpress/blob/main/README.md)
- README blob SHA: ed58461846eec02042c607e53eaee95fb4e3a203
- Repository ID: 982985446
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Model Express is a Rust-based component meant to be placed next to existing model inference systems to speed up their startup times and improve overall performance.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:32:59+00:00

### Short excerpt (up to 100 words)

> SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved. SPDX-License-Identifier: Apache-2.0 --> ModelExpress (MX) starts with a simple question: before loading a model, where does a compatible copy of its weights already live? Rather than treating every replica as an independent cold start, ModelExpress discovers available sources and selects the fastest supported path into GPU memory. Deploy it standalone or alongside vLLM, SGLang, NVIDIA Dynamo, and other inference runtimes. At startup, ModelExpress probes the capabilities available in the environment and tries the fixed loading strategy chain documented in Configuration: 1. **Serving peer → GPU** — Transfer post-processed weights

### README headings

- Overview
- Runtime path selection
- Features
- Integrations
- ModelExpress Architecture
- Benchmarks
- Cold-start loading paths
- NIXL memory registration
- Weight and kernel-artifact transfer
- Quick Start
- Deployment
- Kubernetes (Helm)
- P2P GPU Transfer (vLLM)
- ModelStreamer on Kubernetes
- Docker
- Configuration
- CLI
- Testing
- Documentation
- Known Issues
- Roadmap
- Priorities Under Development
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 5,583,258 |
| Rust | 1,923,033 |
| Shell | 54,994 |
| Lua | 39,137 |
| C++ | 20,409 |
| Dockerfile | 9,033 |
| Go Template | 4,297 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- .devcontainer/Dockerfile (capture: captured)
- ci/pyproject.toml (capture: captured) — dependency clues: aiperf, grpcio, grpcio-tools, pytest
- docker/Dockerfile (capture: captured)
- helm/Chart.yaml (capture: captured)
- modelexpress_client/Cargo.toml (capture: captured) — dependency clues: anyhow, clap, colored, futures, modelexpress-common, serde, serde_json, tempfile, thiserror, tokio, tonic, tracing, tracing-subscriber, uuid

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 205
- Forks at capture: 121
- Last updated: 2026-11-18T17:06:15Z
- Last pushed: 2026-11-23T18:10:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ai-dynamo/modelexpress)
- [README](https://github.com/ai-dynamo/modelexpress/blob/main/README.md)
- [Issues](https://github.com/ai-dynamo/modelexpress/issues)
- [Releases](https://github.com/ai-dynamo/modelexpress/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
