# NVIDIA-ISAAC-ROS/dope_training

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/dope_training](https://github.com/NVIDIA-ISAAC-ROS/dope_training)
- Default branch: master
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/dope_training/blob/master/README.md)
- README blob SHA: e627b401be2f0ac15b9a6d8b2069e395bba90a59
- Repository ID: 1429022171
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Training, Inference, and Evaluation Scripts for Deep Object Pose 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:55+00:00

### Short excerpt (up to 100 words)

> This repo contains a simplified version of the **training** script for DOPE. The original repo for DOPE can be found here. In addition, this repo contains scripts for inference, evaluation, and data visualization. More instructions can be found in the subdirectories `/evaluate` and `/inference`. ***Note*** It is highly recommended to install these dependencies in a virtual environment. You can create and activate a virtual environment by running: python -m venv ./output/dope_training source ./output/dope_training/bin/activate To install the required dependencies, run: pip install -r requirements.txt We use `torchrun` to run the training script. At minimum, the ``--data`` and ``--object`` flags must be

### README headings

- Deep Object Pose Estimation (DOPE) - Training
- Installing Dependencies
- Training
- Loading Data from `s3`
- Multi-GPU Training
- Debugging
- Common Issues
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 121,224 |
| Dockerfile | 1,519 |
| Shell | 276 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: Pillow, PyWavelets, PyYAML, albumentations, boto3, botocore, certifi, charset-normalizer, idna, imageio, jmespath, joblib, networkx, numpy, opencv-python-headless, packaging, protobuf, pyparsing, pyrr, python-dateutil
- docker/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-10-21T23:10:52Z
- Last pushed: 2024-07-31T18:48:28Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/dope_training)
- [README](https://github.com/NVIDIA-ISAAC-ROS/dope_training/blob/master/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/dope_training/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/dope_training/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
