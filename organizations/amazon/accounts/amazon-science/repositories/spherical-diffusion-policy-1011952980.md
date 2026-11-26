# amazon-science/Spherical_Diffusion_Policy

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/Spherical_Diffusion_Policy](https://github.com/amazon-science/Spherical_Diffusion_Policy)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/Spherical_Diffusion_Policy/blob/main/README.md)
- README blob SHA: 0f0354813dec401ab3b3af29ced3d6684cecea68
- README bytes captured: 12456
- README truncated at capture limit: False
- Repository ID: 1011952980
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

[ICML 2025] Official implementation of Spherical Diffusion Policy: A SE(3) Equivariant Visuomotor Policy with Spherical Fourier Representation

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T02:59:46+00:00

### Short excerpt (up to 300 words)

> 1. Install the following

### README headings

- Spherical Diffusion Policy
- Step1: Installation
- Step2: Preparing Dataset
- Download Dataset for 12 MimicGen tasks (with SE(2) initialization, _d1 and _d2 tasks):
- Download all datasets
- Alternatively, download one (or several) datasets of interest, e.g.,
- [Optional] Preparing tasks and generate dataset for 8 MimicGen tasks with SE(3) initialization (_d3 and _d4 tasks):
- Generating Point Cloud and Voxel Observation
- Template
- Replace [dataset] and [n_worker] with your choices.
- E.g., use 24 workers to generate point cloud and voxel observation for stack_d1
- Convert Action Space in Dataset
- Template
- Replace [dataset] and [n_worker] with your choices.
- E.g., convert stack_d1_pc with 12 workers
- Step3: Training SDP
- to train with batch size of 64 and hidden dimension of 64
- Citation
- License
- Acknowledgement
- Gotcha
- Setting up a new instance in AWS EC2:
- Multi-GPU Training

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Step1: Installation

> 1. Install the following

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,475,551 |
| Shell | 17,319 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: accelerate, boto3, cffi, click, diffusers, dill, e3nn, einops, escnn, h5py, hydra-core, imagecodecs, imageio, imageio-ffmpeg, matplotlib, numba, numcodecs, numpy, opencv-python, psutil
- setup.py (capture: captured)
- sdp/model/detr/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 46
- Forks at capture: 8
- Last updated: 2026-10-24T00:50:06Z
- Last pushed: 2026-11-19T15:54:22Z
- Topics: machine-learning, robotics

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/Spherical_Diffusion_Policy)
- [README](https://github.com/amazon-science/Spherical_Diffusion_Policy/blob/main/README.md)
- [Issues](https://github.com/amazon-science/Spherical_Diffusion_Policy/issues)
- [Releases](https://github.com/amazon-science/Spherical_Diffusion_Policy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
