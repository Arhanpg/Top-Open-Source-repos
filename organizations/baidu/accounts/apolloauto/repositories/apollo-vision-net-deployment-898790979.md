# ApolloAuto/Apollo-Vision-Net-Deployment

- Company: Baidu
- GitHub account: [https://github.com/ApolloAuto](https://github.com/ApolloAuto)
- Mapping status: official-project-linked
- Repository: [ApolloAuto/Apollo-Vision-Net-Deployment](https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment)
- Default branch: main
- README: [Open upstream README](https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment/blob/main/README.md)
- README blob SHA: c919521b6a05f55d6c1c832c1dc1cf47b1277cfd
- Repository ID: 898790979
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Apollo BEV+OCC model deployment

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:46+00:00

### Short excerpt (up to 100 words)

> This repository is a deployment project of Apollo Vision Network on TensorRT. git clone xxxx cd xxxx PROJECT_DIR=$(pwd) Download nuScenes V1.0 full dataset data and CAN bus expansion data HERE as `/path/to/nuscenes` and `/path/to/can_bus`. Prepare nuscenes data like BEVFormer. cd ${PROJECT_DIR}/data ln -s /path/to/nuscenes nuscenes ln -s /path/to/can_bus can_bus cd ${PROJECT_DIR} sh samples/bevformer/create_data.sh ${PROJECT_DIR}/data/. ├── can_bus │ ├── scene-0001_meta.json │ ├── scene-0001_ms_imu.json │ ├── scene-0001_pose.json │ └── ... └── nuscenes ├── maps ├── samples ├── sweeps └── v1.0-trainval Download and install the `CUDA-11.6/cuDNN-8.6.0/TensorRT-8.5.1.7` following NVIDIA. Install PyTorch and TorchVision following the official instructions. pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1+cu116 --extra-index-url https://download.pytorch.org/whl/cu116

### README headings

- Deployment of Apollo Vision Network on TensorRT
- Benchmarks
- Clone
- Data Preparation
- NuScenes and CAN bus (For BEVFormer)
- Tree
- Install
- CUDA/cuDNN/TensorRT
- PyTorch
- MMCV-full
- MMDetection
- "-v" means verbose, or more output
- "-e" means installing a project in editable mode,
- thus any local modifications made to the code will take effect without reinstallation.
- MMDeploy
- go back to third_party directory and git clone pybind11
- Build TensorRT Plugins of MMDeploy
- Install MMDeploy
- "-v" means verbose, or more output
- "-e" means installing a project in editable mode,
- thus any local modifications made to the code will take effect without reinstallation.
- Install this Project
- Build and Install Custom TensorRT Plugins
- Build and Install Part of Ops in MMDetection3D
- Prepare the Checkpoints
- Run
- Acknowledgement

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 633,363 |
| Cuda | 321,925 |
| C++ | 175,790 |
| Dockerfile | 4,697 |
| CMake | 1,297 |
| C | 1,074 |
| Shell | 89 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: Pillow, Shapely, matplotlib, netron, numba, numpy, nuscenes_devkit, nvidia-pyindex, opencv_python, pycocotools, pycuda, pyquaternion, pytorch_quantization, scipy, setuptools, terminaltables, thop, tqdm, trimesh
- docker/Dockerfile (capture: captured)
- TensorRT/CMakeLists.txt (capture: captured)
- third_party/bev_mmdet3d/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 10
- Forks at capture: 7
- Last updated: 2026-11-20T08:57:54Z
- Last pushed: 2024-12-05T05:07:42Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment)
- [README](https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment/blob/main/README.md)
- [Issues](https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment/issues)
- [Releases](https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
