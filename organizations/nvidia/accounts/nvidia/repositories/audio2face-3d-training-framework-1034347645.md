# NVIDIA/Audio2Face-3D-Training-Framework

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/Audio2Face-3D-Training-Framework](https://github.com/NVIDIA/Audio2Face-3D-Training-Framework)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/Audio2Face-3D-Training-Framework/blob/main/README.md)
- README blob SHA: 96e0055bd9c6a3030aa974cd6cfd864abad608a4
- Repository ID: 1034347645
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Audio2Face-3D Training Framework for creating custom neural networks that generate realistic facial animations from audio input

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:41:01+00:00

### Short excerpt (up to 100 words)

> **Resources:** - Audio2Face-3D Example Dataset: https://huggingface.co/datasets/nvidia/Audio2Face-3D-Dataset-v1.0.0-claire - Maya-ACE plugin: https://github.com/NVIDIA/Maya-ACE - Research Paper: https://arxiv.org/abs/2508.16401 **Audio2Face-3D** generates high-fidelity facial animations from an audio source. The technology is capable of producing detailed and realistic articulation, including precise motion for the skin, jaw, tongue, and eyes, to achieve accurate lip-sync and lifelike character expression, including emotions. **Audio2Face-3D Training Framework** is the core tool for training high-fidelity facial animation models within the Audio2Face-3D ecosystem. It supports both NVIDIA's prebuilt models and custom models tailored to specific characters, languages, or artistic styles. Training these models requires extensive datasets of synchronized facial animation and corresponding audio,

### README headings

- Audio2Face-3D Training Framework
- Audio2Face-3D
- Documentation Navigation
- This README
- Detailed Guides
- Prerequisites
- System Requirements
- Quick Start
- 1. Clone Repository
- Create audio2face directory and navigate to it
- Clone the repository
- 2. Setup Workspace
- Create datasets and workspace directories
- 3. Configure Environment
- Navigate to the repository directory
- Copy environment file template
- 4. Download Example Dataset
- Navigate to the datasets directory
- Make sure git LFS is installed
- Clone Claire dataset in the datasets directory using https
- Or alternatively clone Claire dataset in the datasets directory using SSH
- 5. Setup Permissions and Build Docker
- Navigate to the repository directory
- Add executable permissions
- Build Docker container
- 6. Run Example Training
- Step 1: Preprocess the Dataset
- Run preprocessing with example config
- Step 2: Train
- Run training example

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 643,036 |
| Shell | 11,246 |
| Dockerfile | 1,123 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- docker/Dockerfile (capture: captured)
- docker/pyproject.toml (capture: captured) — dependency clues: SoundFile, audiomentations, cupy-cuda12x, numpy, onnx, praatio, protobuf, scikit-learn, scipy, tensorboard, timm, torch, torchaudio, tqdm, transformers
- tools/requirements.txt (capture: captured) — dependency clues: black, flake8, markdown2

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 125
- Forks at capture: 26
- Last updated: 2026-11-07T14:10:18Z
- Last pushed: 2025-10-15T19:23:37Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/Audio2Face-3D-Training-Framework)
- [README](https://github.com/NVIDIA/Audio2Face-3D-Training-Framework/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/Audio2Face-3D-Training-Framework/issues)
- [Releases](https://github.com/NVIDIA/Audio2Face-3D-Training-Framework/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
