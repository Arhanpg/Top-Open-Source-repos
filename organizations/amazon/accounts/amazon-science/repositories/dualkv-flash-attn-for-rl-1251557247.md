# amazon-science/dualkv-flash-attn-for-rl

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/dualkv-flash-attn-for-rl](https://github.com/amazon-science/dualkv-flash-attn-for-rl)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/dualkv-flash-attn-for-rl/blob/main/README.md)
- README blob SHA: d050702874f76e4311e53a7be71994d8a26a650a
- README bytes captured: 9430
- README truncated at capture limit: False
- Repository ID: 1251557247
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Implementation of DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T21:57:39+00:00

### Short excerpt (up to 300 words)

> cd flash-attention pip install pip install vllm==0.12.0 ray==2.55.0

### README headings

- DualKV: Shared-Prompt Flash-Attention for RL Training
- Repository Structure
- Hardware Requirements
- Software Environment
- Setup
- Install Flash Attention (with DualKV kernels)
- Install veRL (with DualKV integration)
- (Optional) Flash Attention 3
- (Optional) Prefix Grouper
- Remaining Dependencies
- Models and Data
- Models
- Data
- Reproducing Experiments
- Table 1: Kernel-Level Benchmarks (1x H100 or A100)
- Table 2: Single-Layer DualKV vs Prefix Grouper vs FA2 (1x H100)
- Single-Step Full-Model Benchmark (8x H100)
- Table 5: End-to-End GRPO (Qwen3-8B, 8x H100)
- Table 7: End-to-End DAPO (Qwen3-8B, 8x H100)
- Table 3: Multi-Node MoE (Mixture of Experts) (Qwen3-30B-A3B, 16x H100, 2 nodes)
- On node 0 (head):
- On node 1 (worker):
- Qwen3-14B Experiments
- Qwen3-8B QuALITY Experiments
- Memory Scaling Sweep (1x H100)
- Analytical Memory Model (Appendix B)
- DualKV + Ulysses Sequence Parallelism (8x H100)
- DualKV + SP=2 (DP=4, SP=2): combines prompt deduplication with head splitting
- Citation
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install Flash Attention (with DualKV kernels)

> cd flash-attention pip install

### Technology and requirements: Remaining Dependencies

> pip install vllm==0.12.0 ray==2.55.0

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 9,601,918 |
| C++ | 1,511,451 |
| Shell | 996,080 |
| Cuda | 483,925 |
| Jupyter Notebook | 67,077 |
| Jinja | 5,927 |
| Dockerfile | 4,996 |
| C | 1,848 |
| Makefile | 728 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- flash-attention/Makefile (capture: captured)
- flash-attention/setup.py (capture: captured)
- verl/pyproject.toml (capture: captured)
- verl/requirements.txt (capture: captured) — dependency clues: accelerate, codetiming, datasets, dill, fastapi, hydra-core, latex2sympy2_extended, liger-kernel, math_verify, numpy, packaging, pandas, peft, pre-commit, pyarrow, pybind11, pylatexenc, ray, tensorboard, tensordict
- verl/setup.py (capture: captured)
- flash-attention/flash_attn/pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 4
- Forks at capture: 5
- Last updated: 2026-07-13T22:12:01Z
- Last pushed: 2026-07-15T22:31:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/dualkv-flash-attn-for-rl)
- [README](https://github.com/amazon-science/dualkv-flash-attn-for-rl/blob/main/README.md)
- [Issues](https://github.com/amazon-science/dualkv-flash-attn-for-rl/issues)
- [Releases](https://github.com/amazon-science/dualkv-flash-attn-for-rl/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
