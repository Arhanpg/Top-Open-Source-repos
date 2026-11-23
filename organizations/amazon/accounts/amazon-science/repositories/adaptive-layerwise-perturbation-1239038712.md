# amazon-science/adaptive-layerwise-perturbation

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/adaptive-layerwise-perturbation](https://github.com/amazon-science/adaptive-layerwise-perturbation)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/adaptive-layerwise-perturbation/blob/main/README.md)
- README blob SHA: 7327980a404a9a876e25ad627329b382084cc8d7
- Repository ID: 1239038712
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:43+00:00

### Short excerpt (up to 100 words)

> **Chenlu Ye\*, Xuanchang Zhang\*, Yifan Hao, Zhou Yu, Ziji Zhang, Abhinav Gullapalli, Hao Chen, Jing Huang, Tong Zhang** University of Illinois Urbana-Champaign, Amazon Policy staleness and training-inference mismatch are key challenges in LLM reinforcement learning. Modern RL pipelines use separate systems for rollout generation (e.g., BF16 vLLM) and policy training (e.g., FP32 FSDP), introducing distributional gaps between the behavior policy and the training policy. These gaps destabilize training through inflated importance sampling ratios and noisy gradient estimates. **Adaptive Layerwise Perturbation (ALP)** addresses this by injecting learnable Gaussian perturbations into transformer hidden states across all layers during policy updates. The perturbed

### README headings

- Adaptive Layerwise Perturbation (ALP)
- Introduction
- Repository Structure
- Method
- Results
- Multi-Turn Tool-Integrated Reasoning (Qwen2.5-7B)
- Ablation: Layer Range for ALP
- ALP Configuration
- Key Parameters
- Enabling Learnable Coefficients
- Noise Seed Mechanism
- Multi-Turn Experiments
- Prerequisites
- Build and Start Container
- Start Sandbox Service
- Running Multi-Turn Experiments
- Multi-Turn Datasets
- Multi-Turn Environment Variables
- Single-Turn Experiments
- Supported Models
- Datasets
- Running Single-Turn Experiments
- Baseline
- Bypass
- Perturbation (ALP)
- TIS
- Quick Examples
- Single-Turn Environment Variables
- Evaluation
- Single-Turn Evaluation

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 5,999,726 |
| Shell | 971,904 |
| Jupyter Notebook | 67,077 |
| Jinja | 5,927 |
| Dockerfile | 3,130 |
| Makefile | 602 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- single-turn/pyproject.toml (capture: captured)
- single-turn/requirements.txt (capture: captured) — dependency clues: accelerate, codetiming, datasets, dill, fastapi, hydra-core, latex2sympy2_extended, liger-kernel, math_verify, numpy, packaging, pandas, peft, pre-commit, pyarrow, pybind11, pylatexenc, ray, tensorboard, tensordict
- single-turn/setup.py (capture: captured)
- single-turn/docker/Dockerfile (capture: captured)
- single-turn/docs/Makefile (capture: captured)
- single-turn/eval_benchmark/qwen_evaluation/requirements.txt (capture: captured) — dependency clues: Pebble, antlr4-python3-runtime, datasets, flash_attn, python_dateutil, sympy, timeout-decorator, torch, tqdm, transformers, vllm, word2number

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 1
- Last updated: 2026-09-24T22:50:52Z
- Last pushed: 2026-09-02T01:19:14Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/adaptive-layerwise-perturbation)
- [README](https://github.com/amazon-science/adaptive-layerwise-perturbation/blob/main/README.md)
- [Issues](https://github.com/amazon-science/adaptive-layerwise-perturbation/issues)
- [Releases](https://github.com/amazon-science/adaptive-layerwise-perturbation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
