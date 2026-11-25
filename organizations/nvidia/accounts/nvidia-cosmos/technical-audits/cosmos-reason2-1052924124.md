# nvidia-cosmos/cosmos-reason2

- Company: NVIDIA
- Account: nvidia-cosmos
- Repository: https://github.com/nvidia-cosmos/cosmos-reason2
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:56:33+00:00

## Project purpose

> [!IMPORTANT] > ## 🚀 Cosmos 3 Has Arrived > > Cosmos 3 is NVIDIA's next-generation foundation model platform for Physical AI. Compared with Cosmos-Reason2, Cosmos 3 delivers substantially stronger physical reasoning capabilities while extending beyond reasoning to support world prediction, simulation, transfer, and action generation within a single unified model. > > Rather than relying on separate models for reasoning, prediction, transfer, and policy learning, a single Cosmos 3 model can understand the world, reason about physical interactions, predict future outcomes, transform observations across domains, and generate actions for embodied agents. This unified architecture enables stronger performance across a broad range of Physical AI applications, including robotics, autonomous vehicles, and smart spaces. > > This repository is no longer under active development and will receive o

## Why this project is used

Cosmos-Reason2 models understand the physical common sense and generate appropriate embodied decisions in natural language through long chain-of-thought reasoning processes.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Dockerfile, Just, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: accelerate, av, cosmos-reason2-utils, imageio-ffmpeg, matplotlib, numpy, pillow, pydantic, pyyaml, qwen-vl-utils, rich, transformers, tyro
- Build/package tools: Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: ci/uv_lock.sh, ci/uv_lock_script.sh, cosmos_reason2_utils/cosmos_reason2_utils/__init__.py, cosmos_reason2_utils/cosmos_reason2_utils/init.py

## Setup and usage

No setup information established.

## Limitations and caveats

- Tested Platforms: Cosmos-Reason2 works on Hopper and Blackwell. Additional hardware configurations may work but are not officially validated at the time of this release.
- Tested Platforms: Examples have been tested on the following devices:
- Tested Platforms: | GPU | CUDA Version | Functionality |
- Tested Platforms: | NVIDIA H100 | 12.8 | inference/post-training/quantization |
- Tested Platforms: | NVIDIA GB200 | 13.0 | inference |
- Tested Platforms: | NVIDIA DGX Spark | 13.0 | inference |
- Tested Platforms: | NVIDIA Jetson AGX Thor (Edge) | 13.0 | Transformers inference. vLLM inference is coming soon! |

## Evidence and provenance

- README: https://github.com/nvidia-cosmos/cosmos-reason2/blob/main/README.md
- README SHA: 3ba7733cb5a13a2f44ac9b510ea96ac63071e71d
- Manifests: Dockerfile, pyproject.toml, cosmos_reason2_utils/pyproject.toml, examples/cosmos_rl/pyproject.toml, examples/notebooks/pyproject.toml
- Sampled source files: ci/uv_lock.sh, ci/uv_lock_script.sh, cosmos_reason2_utils/cosmos_reason2_utils/__init__.py, cosmos_reason2_utils/cosmos_reason2_utils/init.py
- Git tree state: captured
- Evidence fingerprint: cbf73e0fcb7c8bb52a5dd3baa9ac887e6692d52ef7f31629e0271d08593ec8f3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
