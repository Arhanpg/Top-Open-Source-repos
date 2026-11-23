# ApolloAuto/apollo-model-yolo3d

- Company: Baidu
- GitHub account: [https://github.com/ApolloAuto](https://github.com/ApolloAuto)
- Mapping status: official-project-linked
- Repository: [ApolloAuto/apollo-model-yolo3d](https://github.com/ApolloAuto/apollo-model-yolo3d)
- Default branch: main
- README: [Open upstream README](https://github.com/ApolloAuto/apollo-model-yolo3d/blob/main/README.md)
- README blob SHA: 225913f9b8eb617ca4fbfaa837e67eeecf2a4885
- Repository ID: 715954375
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

[Apollo] This is the implementation of yolox3d second stage, a camera 3D object detection for autonomous driving perception.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:51:16+00:00

### Short excerpt (up to 100 words)

> YOLO3D is inspired by Mousavian et al. in their paper **3D Bounding Box Estimation Using Deep Learning and Geometry**. YOLO3D uses a different approach, we use 2d gt label result as the input of first stage detector, then use the 2d result as input to regressor model. git clone git@github.com:ApolloAuto/apollo-model-yolo3d.git cd apollo-model-yolo3d conda create -n apollo_yolo3d python=3.8 numpy conda activate apollo_yolo3d pip install -r requirements.txt here we use KITTI data to train. You can download KITTI dataset from official website. After that, extract dataset to `data/KITTI`. ln -s /your/KITTI/path data/KITTI ├── data │ └── KITTI │ ├── calib │ ├──

### README headings

- YOLO3D: 3D Object Detection with YOLO
- Introduction
- Quickstart
- creat env for YOLO3D
- datasets
- train
- covert
- inference
- evaluate
- Acknowledgement

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 291,923 |
| Makefile | 1,169 |
| Shell | 440 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured)
- requirements.txt (capture: captured) — dependency clues: hydra-colorlog, hydra-core, hydra-optuna-sweeper, pre-commit, pyrootutils, pytest, pytorch-lightning, rich, sh, torch, torchmetrics, torchvision
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 18
- Forks at capture: 3
- Last updated: 2026-03-20T11:45:34Z
- Last pushed: 2023-11-13T02:07:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ApolloAuto/apollo-model-yolo3d)
- [README](https://github.com/ApolloAuto/apollo-model-yolo3d/blob/main/README.md)
- [Issues](https://github.com/ApolloAuto/apollo-model-yolo3d/issues)
- [Releases](https://github.com/ApolloAuto/apollo-model-yolo3d/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
