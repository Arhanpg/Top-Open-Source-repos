# ai-dynamo/modelexpress

- Company: NVIDIA
- Account: ai-dynamo
- Repository: https://github.com/ai-dynamo/modelexpress
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:42:29+00:00

## Project purpose

SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved. SPDX-License-Identifier: Apache-2.0 -->

## Why this project is used

Model Express is a Rust-based component meant to be placed next to existing model inference systems to speed up their startup times and improve overall performance.

## Core features

- **Cold start reduction** — GPU-to-GPU P2P transfer over InfiniBand instead of disk load: **Cold start reduction** — GPU-to-GPU P2P transfer over InfiniBand instead of disk load
  - Evidence: README.md#Features
- **Capability-driven loading** — Fixed priority chain: P2P RDMA → server cache → InstantTensor → ModelStreamer → GDS → native loader, with safe fallback: **Capability-driven loading** — Fixed priority chain: P2P RDMA → server cache → InstantTensor → ModelStreamer → GDS → native loader, with safe fallback
  - Evidence: README.md#Features
- **HuggingFace caching** — PVC-backed cache, HF_HUB_OFFLINE, ignore_weights, get_model_path for Dynamo: **HuggingFace caching** — PVC-backed cache, HF_HUB_OFFLINE, ignore_weights, get_model_path for Dynamo
  - Evidence: README.md#Features
- **P2P GPU transfer** — vLLM modelexpress loader, SGLang remote_instance loader with the modelexpress backend, and TRT-LLM checkpoint_format="MX" with NVIDIA NIX: **P2P GPU transfer** — vLLM modelexpress loader, SGLang remote_instance loader with the modelexpress backend, and TRT-LLM checkpoint_format="MX" with NVIDIA NIXL over InfiniBand, RoCE, NVLink, EFA, and other supported fabrics
  - Evidence: README.md#Features
- **JIT cache transfer** — Reuse compatible vLLM and SGLang NIXL compilation caches when replicas scale out: **JIT cache transfer** — Reuse compatible vLLM and SGLang NIXL compilation caches when replicas scale out
  - Evidence: README.md#Features
- **Metadata backends** — Redis, Kubernetes CRD, or decentralized Kubernetes Service routing: **Metadata backends** — Redis, Kubernetes CRD, or decentralized Kubernetes Service routing
  - Evidence: README.md#Features
- **Kubernetes** — Helm chart, CRDs/Redis for P2P, no-shared-storage support: **Kubernetes** — Helm chart, CRDs/Redis for P2P, no-shared-storage support
  - Evidence: README.md#Features
- **CLI** — Health, download, list, validate, clear; init-container support for pre-warming: **CLI** — Health, download, list, validate, clear; init-container support for pre-warming
  - Evidence: README.md#Features
- **ModelStreamer integration** — Pipeline concurrent reads from S3, Azure Blob, GCS, or local storage into vLLM and SGLang: **ModelStreamer integration** — Pipeline concurrent reads from S3, Azure Blob, GCS, or local storage into vLLM and SGLang
  - Evidence: README.md#Features
- **Expanded model pull providers**: NGC catalog and Google Cloud Storage in addition to Hugging Face: **Expanded model pull providers**: NGC catalog and Google Cloud Storage in addition to Hugging Face
  - Evidence: README.md#Features
- **GDS (GPUDirect Storage)**: load model weights directly from NVMe into GPU memory, bypassing the CPU/DRAM copy path: **GDS (GPUDirect Storage)**: load model weights directly from NVMe into GPU memory, bypassing the CPU/DRAM copy path
  - Evidence: README.md#Features
- **Lower NIXL registration overhead** — Opt in to allocation-level pool registration or a single VMM arena registration: **Lower NIXL registration overhead** — Opt in to allocation-level pool registration or a single VMM arena registration
  - Evidence: README.md#Features

## Technology stack

- Languages: Python, Rust, Shell, Lua, C++, Dockerfile, Go Template
- Frameworks/libraries: Unknown / not established
- Dependency names: aiperf, anyhow, async-trait, chrono, clap, colored, config, crc32c, fd-lock, futures, google-cloud-auth, google-cloud-gax, google-cloud-storage, grpcio, grpcio-tools, hf-hub, jiff, modelexpress-common, object-store-reqwest, object_store, openssl, prost, pytest, reqwest, rustls, serde, serde_json, serde_yaml, sha2, tempfile, thiserror, tokio, tonic, tonic-build, tracing, tracing-subscriber, uuid, wiremock
- Build/package tools: Cargo manifest, Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: modelexpress_client/src/lib.rs, modelexpress_common/src/lib.rs, modelexpress_server/src/lib.rs, modelexpress_server/src/main.rs

## Setup and usage

- Quick Start: This Quick Start sets up the P2P path, which is what the benchmarks above measure, so it needs the full NIXL and metadata-backend prerequisites listed below. For a local single-machine setup instead, docker compose -f docker/docker-compose.yml up --build brings up the server with a Redis backend and no NIXL, and the modelexpress-cli commands in CLI
- Quick Start: **Requirements:** vLLM 0.23.0+, the ModelExpress Python package, NIXL-compatible GPU nodes, and a reachable metadata backend.
- Quick Start: git clone https://github.com/ai-dynamo/modelexpress.git
- Quick Start: python -m pip install ./modelexpress_client/python
- Quick Start: export MX_SERVER_ADDRESS=modelexpress-server:8001
- Quick Start: export MX_P2P_METADATA=1
- Quick Start: export MX_ARTIFACT_TRANSFER=1
- Quick Start: export MX_ARTIFACT_BACKEND=nixl

## Limitations and caveats

- Known Issues: - **GDS loader does not scale with TP** — Each TP rank reads full checkpoint tensors and vLLM shards them afterward, so GDS/disk reads scale with TP degree. This can reduce or reverse expected GDS speedups versus the default mmap-based disk loader; TP-aware range reads are needed for a full fix. See GDS Reads Full Checkpoint Tensors Under TP.
- Known Issues: - **P2P source wedges after a reader is torn down (UCX/InfiniBand)** — Once a reader that pulled from a source is removed, the source can stop serving new readers: their RDMA reads stall to the transfer timeout and fall back to disk, while the source keeps advertising Ready and serving inference normally. Loading stays correct, but P2P is effective

## Evidence and provenance

- README: https://github.com/ai-dynamo/modelexpress/blob/main/README.md
- README SHA: ed58461846eec02042c607e53eaee95fb4e3a203
- Manifests: Cargo.toml, .devcontainer/Dockerfile, ci/pyproject.toml, docker/Dockerfile, modelexpress_client/Cargo.toml, modelexpress_common/Cargo.toml
- Sampled source files: modelexpress_client/src/lib.rs, modelexpress_common/src/lib.rs, modelexpress_server/src/lib.rs, modelexpress_server/src/main.rs
- Git tree state: captured
- Evidence fingerprint: 711122db90cdf796ebf385d8a401bd1ac3d9c85890bdccfc5dbcd7302dd05497

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
