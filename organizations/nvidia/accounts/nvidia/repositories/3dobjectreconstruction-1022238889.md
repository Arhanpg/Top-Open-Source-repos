# NVIDIA/3DObjectReconstruction

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/3DObjectReconstruction](https://github.com/NVIDIA/3DObjectReconstruction)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/3DObjectReconstruction/blob/main/README.md)
- README blob SHA: 59c66fb870073f530ea14bfb4c2eb49679fa8956
- Repository ID: 1022238889
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

3D Object Reconstruction project is a workflow that takes a set of stereo images and camera info and outputs a textured mesh (i.e., .OBJ file). The purpose is to translate physical items into the digital world in a photorealistic way

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:26:11+00:00

### Short excerpt (up to 100 words)

> - June, 2026: We release Commercial Version Of 3D Object Reconstruction Pipeline! 1. We use Theseus optimizers for pose optimization to replace BundleFusion. 2. Add optional config for color fusion across views to handle varying lighting conditions. (See Configuration for usage) 3. We now use commercial version FoundationStereo ONNX weight from NVIDIA TAO Toolkit. Now could be enabled through FoundationStereo configuration. 4. Add multi-architecture Docker support with automatic detection: deployment now automatically detects x86_64 vs ARM64 (tested on Jetson Orin) and uses the appropriate Dockerfile (`Dockerfile` or `Dockerfile.aarch64`) and upgrade to pytorch 2.7.0 for better compatiblity especially for newer architechures.

### README headings

- NVIDIA 3D Object Reconstruction Framework
- 🆕 Updates & News
- Framework Overview
- What is 3D Object Reconstruction?
- How to Use This Framework
- Preparing your data
- 1&ensp;–&ensp;Input data schema
- 2&ensp;–&ensp;Camera calibration
- data/configs/base.yaml
- 3&ensp;–&ensp;Data organization
- Real-World Results and What to Expect
- Additional Reading
- Quick Start (Recommended)
- Prerequisites
- 🎬 Complete Setup
- Clone the repository
- One-command setup: downloads weights, builds image
- Automatically detects your architecture (x86_64 or ARM64)
- Start the container and launch the jupyter notebook server
- Force ARM64 build
- Force x86_64 build
- 🎯 Interactive Experience
- Technical Details
- Software Components
- Technical Diagrams
- Minimum System Requirements
- Hardware Requirements
- Software Requirements
- Development Environment
- Use Cases and Applications

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 394,216 |
| Jupyter Notebook | 39,825 |
| Shell | 26,965 |
| Dockerfile | 12,604 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- docker/Dockerfile (capture: captured)
- src/pyproject.toml (capture: captured) — dependency clues: Pillow, black, flake8, imageio, iopath, ipympl, ipywidgets, isort, joblib, jupyter, jupyterlab, libigl, matplotlib, mypy, notebook, numpy, nvidia-3d-object-reconstruction, omegaconf, onnxruntime-gpu, open3d
- src/requirements.txt (capture: captured) — dependency clues: imageio, iopath, joblib, libigl, numpy, omegaconf, opencv-python, plyfile, pycuda, pytest, pytest-html, pytest-timeout, python-multipart, ruamel.yaml, scikit-learn, scipy, transformations, trimesh, xatlas

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 252
- Forks at capture: 26
- Last updated: 2026-11-20T00:58:37Z
- Last pushed: 2026-07-06T22:09:35Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/3DObjectReconstruction)
- [README](https://github.com/NVIDIA/3DObjectReconstruction/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/3DObjectReconstruction/issues)
- [Releases](https://github.com/NVIDIA/3DObjectReconstruction/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
