# ai-dynamo/aiconfigurator

- Company: NVIDIA
- Account: ai-dynamo
- Repository: https://github.com/ai-dynamo/aiconfigurator
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:58:28+00:00

## Project purpose

SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved. SPDX-License-Identifier: Apache-2.0 -->

## Why this project is used

Offline optimization of your disaggregated Dynamo graph

## Core features

- Support using huggingface model id if falls into these model family and not MoE models.: Support using huggingface model id if falls into these model family and not MoE models.
  - Evidence: README.md#Supported Features
- **Operations**:: **Operations**:
  - Evidence: README.md#Supported Features
- MHA/GQA (FP8, BF16): MHA/GQA (FP8, BF16)
  - Evidence: README.md#Supported Features
- MLA (FP8, BF16): MLA (FP8, BF16)
  - Evidence: README.md#Supported Features
- KV Cache (BF16, FP8, INT8): KV Cache (BF16, FP8, INT8)
  - Evidence: README.md#Supported Features
- GEMM (BF16, FP8, FP8-Block, FP8-OOTB, SQ, INT8 WO, INT4 WO, NVFP4): GEMM (BF16, FP8, FP8-Block, FP8-OOTB, SQ, INT8 WO, INT4 WO, NVFP4)
  - Evidence: README.md#Supported Features
- CustomAllReduce (BF16): CustomAllReduce (BF16)
  - Evidence: README.md#Supported Features
- NCCL (all_reduce, all_gather, all-to-all, reduce_scatter): NCCL (all_reduce, all_gather, all-to-all, reduce_scatter)
  - Evidence: README.md#Supported Features
- MoE (BF16, FP8, FP8-Block, W4A-FP8, INT4 WO, NVFP4): MoE (BF16, FP8, FP8-Block, W4A-FP8, INT4 WO, NVFP4)
  - Evidence: README.md#Supported Features
- MLA BMM (BF16, FP8): MLA BMM (BF16, FP8)
  - Evidence: README.md#Supported Features
- **Parallel modes**:: **Parallel modes**:
  - Evidence: README.md#Supported Features
- Tensor-parallel: Tensor-parallel
  - Evidence: README.md#Supported Features
- Pipeline-parallel: Pipeline-parallel
  - Evidence: README.md#Supported Features
- Expert Tensor-parallel/Expert-parallel: Expert Tensor-parallel/Expert-parallel
  - Evidence: README.md#Supported Features
- Attention DP (for DEEPSEEK and MoE): Attention DP (for DEEPSEEK and MoE)
  - Evidence: README.md#Supported Features

## Technology stack

- Languages: Python, Rust, Shell, Jinja, Jupyter Notebook, HTML, Dockerfile, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: aiconfigurator-core, bincode, bokeh, jinja2, log, matplotlib, munch, numpy, nvidia-ml-py, packaging, pandas, parquet, pep440_rs, plotext, plotly, prettytable, pyarrow, pydantic, pyo3, pyyaml, quick_cache, scipy, serde, serde_json, serde_yaml, sha2, tempfile, thiserror, tqdm
- Build/package tools: Cargo manifest, Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: aic-core/rust/aiconfigurator-core/src/common/mod.rs, aic-core/rust/aiconfigurator-core/src/engine/mod.rs, aic-core/rust/aiconfigurator-core/src/fpm/mod.rs, aic-core/rust/aiconfigurator-core/src/lib.rs

## Setup and usage

No setup information established.

## Limitations and caveats

- Compatibility install from PyPI: New development and new integrations should target AISimulate. Until the
- Compatibility install from PyPI: stable AISimulate 0.12 artifacts are published, existing AIC users may continue
- Compatibility install from PyPI: installing the latest supported AIC release:
- Compatibility install from PyPI: > **Public PyPI support: Linux x86-64 only.** The required
- Compatibility install from PyPI: > aiconfigurator-core wheel bundles a native Rust/PyO3 extension and is
- Compatibility install from PyPI: > published to PyPI as a manylinux_2_28_x86_64 wheel (Linux x86-64,
- Compatibility install from PyPI: > **Release wheel coverage:** The
- Compatibility install from PyPI: > platform-wheel workflow also

## Evidence and provenance

- README: https://github.com/ai-dynamo/aiconfigurator/blob/main/README.md
- README SHA: 77e625823b2524b7767298db438fee1d712c4ae9
- Manifests: Cargo.toml, pyproject.toml, aic-core/pyproject.toml, docker/Dockerfile, aic-core/rust/aiconfigurator-core/Cargo.toml, aic-core/rust/tests/public-api/Cargo.toml
- Sampled source files: aic-core/rust/aiconfigurator-core/src/common/mod.rs, aic-core/rust/aiconfigurator-core/src/engine/mod.rs, aic-core/rust/aiconfigurator-core/src/fpm/mod.rs, aic-core/rust/aiconfigurator-core/src/lib.rs
- Git tree state: captured
- Evidence fingerprint: e6c99bc713410a6eea5959d8b9ddd282fb8cce15e60dd57d4536cf3a4e0ed525

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
