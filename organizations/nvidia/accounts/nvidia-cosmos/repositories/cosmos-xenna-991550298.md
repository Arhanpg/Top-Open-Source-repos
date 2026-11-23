# nvidia-cosmos/cosmos-xenna

- Company: NVIDIA
- GitHub account: [https://github.com/nvidia-cosmos](https://github.com/nvidia-cosmos)
- Mapping status: official-project-linked
- Repository: [nvidia-cosmos/cosmos-xenna](https://github.com/nvidia-cosmos/cosmos-xenna)
- Default branch: main
- README: [Open upstream README](https://github.com/nvidia-cosmos/cosmos-xenna/blob/main/README.md)
- README blob SHA: 86a8663476b0c2bb2d33431afeae83312f345824
- Repository ID: 991550298
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Python library for building and running distributed data pipelines using Ray

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:32:26+00:00

### Short excerpt (up to 100 words)

> Cosmos-xenna is a Python library for building and running distributed data pipelines using Ray. It has a heavy focus on pipelines which are a series of inference steps using AI models. For example, a pipeline which downloads an image, runs a VLM on it to produce a caption, and then runs an embedding model to produce a text embedding and uploads the resulting data. Cosmos-xenna simplifies the development of distributed AI pipelines by providing: - A simple interface - Autoscaling/autobalancing of stages - Stateful actors which allow the user to load/download weights before running processing - Large model support via

### README headings

- Cosmos-xenna
- Introduction
- What is Xenna?
- How Pipelines Work
- Stage 1: Download videos from S3
- Stage 2: Run VLM to caption videos
- Stage 3: Upload captions to S3 and write metadata to Postgres
- Connect the stages and run
- Pipeline Monitoring
- SPMD support
- What is SPMD mode?
- How SPMD is implemented
- Data flow in SPMD mode
- Example: Large model inference with vLLM
- Use the stage in a pipeline
- Key differences from regular stages
- P2P artifact downloading
- Using with Pipelines
- Configure S3 authentication and download behavior
- Run the pipeline with distributed downloads
- Standalone Usage
- Configure object store access
- Specify what to download
- Run the distributed download
- Multi-Profile Authentication
- Reference profiles in download requests
- Installing
- Quick Start
- Ray cluster requirements
- Needed to give Xenna control over setting CUDA environment variables. Without this, Ray will overwrite the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,315,110 |
| Rust | 607,464 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured) — dependency clues: approx, axum, comfy-table, crossbeam-channel, env_logger, fixed, futures, good_lp, itertools, log, object_store, portpicker, pyo3, rand, reqwest, retry, serde, serde_json, tempfile, thiserror
- pyproject.toml (capture: captured) — dependency clues: attrs, cattrs, gpustat, huggingface-hub, jinja2, loguru, obstore, pillow, portpicker, pulp, pynvml, ray, requests, tabulate, torch, torchvision, transformers

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 89
- Forks at capture: 27
- Last updated: 2026-11-20T06:34:09Z
- Last pushed: 2026-11-09T16:30:55Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/nvidia-cosmos/cosmos-xenna)
- [README](https://github.com/nvidia-cosmos/cosmos-xenna/blob/main/README.md)
- [Issues](https://github.com/nvidia-cosmos/cosmos-xenna/issues)
- [Releases](https://github.com/nvidia-cosmos/cosmos-xenna/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
