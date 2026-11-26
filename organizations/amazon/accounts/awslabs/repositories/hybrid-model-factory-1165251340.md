# awslabs/hybrid-model-factory

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/hybrid-model-factory](https://github.com/awslabs/hybrid-model-factory)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/hybrid-model-factory/blob/main/README.md)
- README blob SHA: e326eddda6a689ba97c77d0613456f96b1e1db6f
- README bytes captured: 29545
- README truncated at capture limit: False
- Repository ID: 1165251340
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Open-source toolkit for training, Priming, and serving next generation Hybrid architectures

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T22:29:03+00:00

### Short excerpt (up to 300 words)

> If you want to Hybrid Model Factory extends Initializes a **fused Hybrid

### README headings

- Hybrid Model Factory
- Features
- Primed Model Zoo
- 8B Models (Primed from Qwen3-8B)
- 32B Models (Primed from Qwen3-32B)
- Getting Started
- Inference
- Training
- End-to-End Pipeline Scripts
- Training Decision Models
- Priming Pipeline Overview
- Stage 0: Initialize a Hybrid architecture using the pre-trained Transformer's weights
- Stage 1: Attention → SSM Distillation
- Stage 2: Fine-tuning
- Single node
- Multi-node (run on each node)
- Single node
- Multi-node (run on each node)
- Training-Free Context Length Extension
- Decision Models
- Supported Architectures
- Base Models
- Hybrid Layer Types
- Performance
- 8B Long-context Instruct Models (Primed from Qwen3-8B)
- Long-Context Benchmarks
- Short-Context NLP Benchmarks
- 8B Long-context Reasoning Models (Primed from Qwen3-8B)
- 32B Long-context Instruct Models (Primed from Qwen3-32B)
- Long-Context Benchmarks

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Priming Pipeline Overview

> If you want to

### Features and capabilities: Features

> Hybrid Model Factory extends

### Architecture and design: Stage 0: Initialize a Hybrid architecture using the pre-trained Transformer's weights

> Initializes a **fused Hybrid

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 4,519,045 |
| Shell | 10,324 |
| Dockerfile | 2,568 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- training/pyproject.toml (capture: captured) — dependency clues: accelerate, av, datasets, einops, fastapi, fire, gradio, hf-transfer, matplotlib, modelscope, numpy, omegaconf, packaging, pandas, peft, protobuf, pydantic, pyyaml, safetensors, scipy
- vllm-inference/Dockerfile (capture: captured)
- vllm-inference/setup.py (capture: captured)
- training/docker/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 97
- Forks at capture: 9
- Last updated: 2026-11-20T03:08:19Z
- Last pushed: 2026-11-17T22:01:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/hybrid-model-factory)
- [README](https://github.com/awslabs/hybrid-model-factory/blob/main/README.md)
- [Issues](https://github.com/awslabs/hybrid-model-factory/issues)
- [Releases](https://github.com/awslabs/hybrid-model-factory/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
