# NVIDIA/Model-Optimizer

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/Model-Optimizer/blob/main/README.md)
- README blob SHA: b15c2cc1f098d85ac7abbd1cb2f3912590eb1525
- README bytes captured: 20575
- README truncated at capture limit: False
- Repository ID: 790916393
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A unified library of SOTA model optimization techniques like quantization, distillation, pruning, neural architecture search, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:26:35+00:00

### Short excerpt (up to 300 words)

> To install stable release Model Optimizer follows a

### README headings

- NVIDIA Model Optimizer
- Latest News
- Install
- Clone the Model Optimizer repository
- Techniques
- Pre-Quantized Checkpoints
- Resources
- Model Support Matrix
- Deprecation Policy
- Citation
- Contributing
- AI Agents
- Claude Code
- Codex
- Top Contributors

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install

> To install stable release

### Limitations and security: Deprecation Policy

> Model Optimizer follows a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 17,426,032 |
| Shell | 182,897 |
| Cuda | 162,289 |
| Jinja | 40,517 |
| C++ | 30,599 |
| Standard ML | 11,090 |
| Jupyter Notebook | 5,071 |
| C | 2,748 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: PyYAML, accelerate, apache-tvm-ffi, autodoc_pydantic, bandit, coverage, cppimport, cupy-cuda12x, cupy-cuda13x, datasets, deepspeed, diffusers, fire, fla-core, httpx, huggingface_hub, hydra-core, immutabledict, lief, lru-dict
- examples/cnn_qat/requirements.txt (capture: captured) — dependency clues: torchvision
- examples/diffusers/requirements.txt (capture: captured) — dependency clues: nvtx, opencv-python
- examples/gpt-oss/requirements.txt (capture: captured) — dependency clues: kernels, trackio, trl
- examples/hf_ptq/requirements.txt (capture: captured) — dependency clues: compressed-tensors, fire, flash-attn, mlflow-skinny, psutil, transformers_stream_generator, zstandard
- examples/llm_distill/requirements.txt (capture: captured) — dependency clues: pyarrow, torchao, trl

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5654
- Forks at capture: 833
- Last updated: 2026-11-23T11:43:09Z
- Last pushed: 2026-11-23T19:16:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/Model-Optimizer)
- [README](https://github.com/NVIDIA/Model-Optimizer/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/Model-Optimizer/issues)
- [Releases](https://github.com/NVIDIA/Model-Optimizer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
