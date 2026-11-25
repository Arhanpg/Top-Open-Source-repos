# NVIDIA/MinkowskiEngine

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine)
- Default branch: master
- README: [Open upstream README](https://github.com/NVIDIA/MinkowskiEngine/blob/master/README.md)
- README blob SHA: 048588159eb474cfb511251fbf5294db35518176
- README bytes captured: 19943
- README truncated at capture limit: False
- Repository ID: 179401695
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Minkowski Engine is an auto-diff neural network library for high-dimensional sparse tensors

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:15:59+00:00

### Short excerpt (up to 300 words)

> Unlimited high-dimensional sparse tensor You can install the In some cases, you Ubuntu >= 14.04 CUDA

### README headings

- Minkowski Engine
- News
- Example Networks
- Sparse Tensor Networks: Neural Networks for Spatially Sparse Tensors
- Features
- Requirements
- Installation
- Pip
- For pip installation from the latest source
- pip install -U git+https://github.com/NVIDIA/MinkowskiEngine --no-deps
- Uncomment some options if things don't work
- export CXX=c++; # set this if you want to use a different C++ compiler
- export CUDA_HOME=/usr/local/cuda-11.1; # or select the correct cuda version on your system.
- \ # uncomment the following line if you want to force cuda installation
- --install-option="--force_cuda" \
- \ # uncomment the following line if you want to force no cuda installation. force_cuda supercedes cpu_only
- --install-option="--cpu_only" \
- \ # uncomment the following line to override to openblas, atlas, mkl, blas
- --install-option="--blas=openblas" \
- Anaconda
- CUDA 10.2
- Make sure `g++-7 --version` is at least 7.4.0
- Install MinkowskiEngine
- Uncomment the following line to specify the cuda home. Make sure `$CUDA_HOME/nvcc --version` is 10.2
- export CUDA_HOME=/usr/local/cuda-10.2
- Or if you want local MinkowskiEngine
- CUDA 11.X
- Install MinkowskiEngine
- Uncomment the following line to specify the cuda home. Make sure `$CUDA_HOME/nvcc --version` is 11.X
- export CUDA_HOME=/usr/local/cuda-11.1

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> Unlimited high-dimensional sparse tensor

### Getting started and usage: Installation

> You can install the

### Architecture and design: Specifying CUDA architecture list

> In some cases, you

### Technology and requirements: Requirements

> Ubuntu >= 14.04 CUDA

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 524,909 |
| Cuda | 462,152 |
| C++ | 434,706 |
| Makefile | 5,587 |
| Dockerfile | 959 |
| Shell | 533 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- requirements.txt (capture: captured) — dependency clues: numpy, torch
- setup.py (capture: captured)
- docker/Dockerfile (capture: captured)
- docs/Makefile (capture: captured)
- tests/cpp/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 2976
- Forks at capture: 492
- Last updated: 2026-11-23T17:30:14Z
- Last pushed: 2024-03-05T16:00:19Z
- Topics: 3d-convolutional-network, 3d-vision, 4d-convolutional-neural-network, auto-differentiation, computer-vision, convolutional-neural-networks, cuda, deep-learning, high-dimensional-data, high-dimensional-inference, minkowski-engine, neural-network, pytorch, semantic-segmentation, space-time, sparse-convolution, sparse-tensor-network, sparse-tensors, spatio-temporal-analysis, trilateral-filter

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/MinkowskiEngine)
- [README](https://github.com/NVIDIA/MinkowskiEngine/blob/master/README.md)
- [Issues](https://github.com/NVIDIA/MinkowskiEngine/issues)
- [Releases](https://github.com/NVIDIA/MinkowskiEngine/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
