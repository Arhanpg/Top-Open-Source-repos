# ApolloAuto/apollo-model-radar4d

- Company: Baidu
- Account: ApolloAuto
- Repository: https://github.com/ApolloAuto/apollo-model-radar4d
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T06:59:32+00:00

## Project purpose

Prepare your own dataset, and modify the dataset path in "tools/cfgs/dataset_configs/radar4d_dataset.yaml"

## Why this project is used

Prepare your own dataset, and modify the dataset path in "tools/cfgs/dataset_configs/radar4d_dataset.yaml"

## Core features

- [x] Support both one-stage and two-stage 3D object detection frameworks: [x] Support both one-stage and two-stage 3D object detection frameworks
  - Evidence: README.md#Currently Supported Features
- [x] Support distributed training & testing with multiple GPUs and multiple machines: [x] Support distributed training & testing with multiple GPUs and multiple machines
  - Evidence: README.md#Currently Supported Features
- [x] Support multiple heads on different scales to detect different classes: [x] Support multiple heads on different scales to detect different classes
  - Evidence: README.md#Currently Supported Features
- [x] Support stacked version set abstraction to encode various number of points in different scenes: [x] Support stacked version set abstraction to encode various number of points in different scenes
  - Evidence: README.md#Currently Supported Features
- [x] Support Adaptive Training Sample Selection (ATSS) for target assignment: [x] Support Adaptive Training Sample Selection (ATSS) for target assignment
  - Evidence: README.md#Currently Supported Features
- [x] Support RoI-aware point cloud pooling & RoI-grid point cloud pooling: [x] Support RoI-aware point cloud pooling & RoI-grid point cloud pooling
  - Evidence: README.md#Currently Supported Features
- [x] Support GPU version 3D IoU calculation and rotated NMS: [x] Support GPU version 3D IoU calculation and rotated NMS
  - Evidence: README.md#Currently Supported Features

## Technology stack

- Languages: Python, Cuda, C++, C, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: easydict, numba, numpy, pyyaml, scikit-image, tensorboardX, torch, tqdm
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: pcdet/ops/iou3d_nms/src/iou3d_cpu.cpp, pcdet/ops/iou3d_nms/src/iou3d_cpu.h, pcdet/ops/iou3d_nms/src/iou3d_nms.cpp, pcdet/ops/iou3d_nms/src/iou3d_nms.h

## Setup and usage

- Installation: Please refer to INSTALL.md for the installation of OpenPCDet.
- Getting Started: Please refer to GETTING_STARTED.md to learn more usage about this project.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/ApolloAuto/apollo-model-radar4d/blob/master/README.md
- README SHA: 5a5cc63ed25e61256dd6dd52f6501ab746b770ba
- Manifests: requirements.txt, setup.py
- Sampled source files: pcdet/ops/iou3d_nms/src/iou3d_cpu.cpp, pcdet/ops/iou3d_nms/src/iou3d_cpu.h, pcdet/ops/iou3d_nms/src/iou3d_nms.cpp, pcdet/ops/iou3d_nms/src/iou3d_nms.h
- Git tree state: captured
- Evidence fingerprint: 3b393a99db99b9880737459e90a60d9d87f837c22910b5a3f9ec8c7de92d6186

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
