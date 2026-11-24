# NVIDIA/compute-eval

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/compute-eval](https://github.com/NVIDIA/compute-eval)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/compute-eval/blob/main/README.md)
- README blob SHA: 0243738b2bf2768a4820701a45d85bcf824f0c82
- README bytes captured: 34444
- README truncated at capture limit: False
- Repository ID: 959472680
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Evaluating Large Language Models for CUDA Code Generation ComputeEval is a framework designed to generate and evaluate CUDA code from Large Language Models.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:33:39+00:00

### Short excerpt (up to 300 words)

> **Note:** This repository executes min_cuda_toolkit: "13.1" # Minimum

### README headings

- ComputeEval
- Benchmark Structure and Evaluation
- Problem Organization
- Problem Groups
- Problem Specification Format
- Build and test configuration
- Optional: override the container image used by the Podman evaluator.
- Defaults to null (use localhost/compute-eval:<CTK_VERSION>).
- Ignored by the local evaluator.
- Requirements
- Optional metadata
- Evaluation Rules of Engagement
- Continuous Integration Validation
- Performance Measurement
- Opting In
- Functional correctness (required)
- Performance measurement (optional)
- Timing Modes
- Default: total application wall-clock time
- (timing_mode defaults to "process" if omitted)
- Only count specific kernels
- NVTX region kernel time (time_type defaults to "kernel")
- NVTX region wall-clock time (overrides the default time_type)
- Total GPU time (kernels + memory transfers)
- Self-reported timing from STDOUT
- Region Timing with NVTX
- As a context manager:
- Or as a decorator:
- Custom Timing
- Profiling Modes

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage

> **Note:** This repository executes

### Technology and requirements: Requirements

> min_cuda_toolkit: "13.1" # Minimum

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 315,456 |
| C++ | 45,074 |
| Cuda | 9,197 |
| Dockerfile | 5,858 |
| Makefile | 1,557 |
| C | 1,140 |
| Shell | 286 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: anthropic, fire, harbor, huggingface_hub, litellm, numpy, nvidia-compute-eval, nvidia-ml-py, openai, psutil, pydantic, python-dotenv, pyyaml, requests, tqdm, tree-sitter, tree-sitter-language-pack
- compute_eval/cuda_tools/Makefile (capture: captured)
- docker/harbor-agent/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 150
- Forks at capture: 19
- Last updated: 2026-11-01T21:38:24Z
- Last pushed: 2026-11-19T00:03:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/compute-eval)
- [README](https://github.com/NVIDIA/compute-eval/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/compute-eval/issues)
- [Releases](https://github.com/NVIDIA/compute-eval/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
