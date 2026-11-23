# nvidia-cosmos/cosmos-reason1

- Company: NVIDIA
- GitHub account: [https://github.com/nvidia-cosmos](https://github.com/nvidia-cosmos)
- Mapping status: official-project-linked
- Repository: [nvidia-cosmos/cosmos-reason1](https://github.com/nvidia-cosmos/cosmos-reason1)
- Default branch: main
- README: [Open upstream README](https://github.com/nvidia-cosmos/cosmos-reason1/blob/main/README.md)
- README blob SHA: 699c5a32e220bc2d177b98bc66e57cfa05746673
- Repository ID: 941558026
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Cosmos-Reason1 models understand the physical common sense and generate appropriate embodied decisions in natural language through long chain-of-thought reasoning processes.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:16:19+00:00

### Short excerpt (up to 100 words)

> NVIDIA Cosmos Reason – an open, customizable, 7B-parameter reasoning vision language model (VLM) for physical AI and robotics - enables robots and vision AI agents to reason like humans, using prior knowledge, physics understanding and common sense to understand and act in the real world. This model understands space, time, and fundamental physics, and can serve as a planning model to reason what steps an embodied agent might take next. Cosmos Reason excels at navigating the long tail of diverse scenarios of the physical world with spatial-temporal understanding. Cosmos Reason is post-trained with physical common sense and embodied reasoning data

### README headings

- [Paper](https://arxiv.org/abs/2503.15558) | [Website](https://research.nvidia.com/labs/dir/cosmos-reason1/) | [HuggingFace](https://huggingface.co/collections/nvidia/cosmos-reason1-67c9e926206426008f1da1b7) | [Cosmos Cookbook](https://github.com/nvidia-cosmos/cosmos-cookbook)
- News
- Model
- Setup
- Inference
- Tutorials
- Post-Training
- Additional Resources
- Post-Training quantization
- License and Contact

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 45,451 |
| Shell | 1,359 |
| Just | 307 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: accelerate, qwen-vl-utils, torch, torchcodec, transformers
- cosmos_reason1_utils/pyproject.toml (capture: captured) — dependency clues: matplotlib, numpy, pillow, pydantic, torch, torchvision
- examples/benchmark/pyproject.toml (capture: captured) — dependency clues: attrs, datasets, ffmpeg-python, huggingface-hub, numpy, opencv-python, pillow, pyyaml, qwen_vl_utils, tensorflow_datasets, torch, tqdm, transformers, vllm
- examples/post_training/pyproject.toml (capture: captured) — dependency clues: cosmos-reason1-utils, cosmos-rl, datasets, toml, torch, torchcodec, transformers, wandb
- examples/post_training_hf/pyproject.toml (capture: captured) — dependency clues: cosmos-reason1-utils, cosmos-rl, datasets, pydantic, rich, toml, torch, torchcodec, transformers, wandb
- examples/post_training_llava/pyproject.toml (capture: captured) — dependency clues: cosmos-reason1-utils, cosmos-rl, datasets, pydantic, rich, toml, torch, torchcodec, transformers, wandb

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 965
- Forks at capture: 84
- Last updated: 2026-11-20T05:54:13Z
- Last pushed: 2026-06-07T17:18:24Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/nvidia-cosmos/cosmos-reason1)
- [README](https://github.com/nvidia-cosmos/cosmos-reason1/blob/main/README.md)
- [Issues](https://github.com/nvidia-cosmos/cosmos-reason1/issues)
- [Releases](https://github.com/nvidia-cosmos/cosmos-reason1/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
