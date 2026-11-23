# MLX

- Company association: Apple
- Upstream GitHub account: [ml-explore](https://github.com/ml-explore)
- Repository: [ml-explore/mlx](https://github.com/ml-explore/mlx)
- Default branch: main
- README: [Open upstream README](https://github.com/ml-explore/mlx/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: fb30a24f2ce87d6f81822fc51e01c9fb6d38de28
- Relationship note: Apple's official Open Source project catalogue links this project and its separate GitHub account; the mapping is project-linked, not blanket legal ownership of every repository in the account.

## Project overview

An array framework for machine-learning research on Apple silicon, brought to you by Apple machine-learning research. Its README emphasizes a NumPy-like Python API, unified memory and a deliberately simple design for efficient experimentation.

## Features and capabilities documented by the README

- Python APIs that closely follow NumPy and higher-level packages such as mlx.nn and mlx.optimizers with APIs inspired by PyTorch.
- C++, C and Swift APIs that mirror the Python API.
- Composable transformations for automatic differentiation, vectorization and computation-graph optimization.
- Lazy computation and dynamic graph construction.
- CPU/GPU execution using shared unified memory on Apple silicon, avoiding explicit device-to-device transfers for MLX arrays.
- Examples for transformer-language-model training, Llama generation, LoRA fine-tuning, Stable Diffusion and Whisper.

## Technology stack

Python; C++; C; Swift; NumPy-like array API; mlx.nn and mlx.optimizers; PyPI; unified-memory CPU/GPU execution on Apple silicon. README lists Linux CUDA and CPU-only installation variants.

## Getting started

On macOS, install with pip install mlx. On Linux, the README documents pip install mlx[cuda] for CUDA and pip install mlx[cpu] for CPU-only use. Follow the official quickstart and installation docs for source builds and supported configurations.

## Lifecycle, compatibility and operational considerations

The README identifies Apple silicon as the framework's primary target; Linux CUDA/CPU packages are separate installation paths. The project is hosted under ml-explore, which Apple's official Open Source MLX project page links directly. This is a project association, not blanket ownership of all repositories in the account.

## Evaluation guidance

Check the current upstream release, dependency manifests, exact platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/ml-explore/mlx)
- [README](https://github.com/ml-explore/mlx/blob/main/README.md)
- [Issues](https://github.com/ml-explore/mlx/issues)
- [Releases](https://github.com/ml-explore/mlx/releases)

Evidence note: the README blob SHA identifies the upstream README revision inspected. Technology details not established by the README or official project page are left unspecified.
