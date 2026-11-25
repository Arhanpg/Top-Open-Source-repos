# ApolloAuto/apollo-model-centerpoint

- Company: Baidu
- Account: ApolloAuto
- Repository: https://github.com/ApolloAuto/apollo-model-centerpoint
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:03:14+00:00

## Project purpose

该项目提供了开源自动驾驶平台Apollo中Lidar 3D目标检测算法CenterPoint的训练和部署代码。

## Why this project is used

该项目提供了开源自动驾驶平台Apollo中Lidar 3D目标检测算法CenterPoint的训练和部署代码。

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, C++, Cuda, CMake, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: colorlog, easydict, filelock, h5py, numba, numpy, nuscenes-devkit, opencv-python, paddledet, paddleseg, pandas, pillow, pyquaternion, pyyaml, rarfile, scikit-image, scikit-learn, visualdl
- Build/package tools: CMake configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: deploy/caddn/cpp/compile.sh, deploy/caddn/cpp/custom_ops/grid_sample_3d.cc, deploy/caddn/cpp/custom_ops/grid_sample_3d.h, deploy/caddn/cpp/custom_ops/iou3d_cpu.cpp

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/ApolloAuto/apollo-model-centerpoint/blob/master/README.md
- README SHA: 7624954e301c10615586efae948ce1ece611b909
- Manifests: requirements.txt, setup.py, paddle3d/ops/setup.py, deploy/caddn/cpp/CMakeLists.txt, deploy/centerpoint/cpp/CMakeLists.txt, deploy/iassd/cpp/CMakeLists.txt
- Sampled source files: deploy/caddn/cpp/compile.sh, deploy/caddn/cpp/custom_ops/grid_sample_3d.cc, deploy/caddn/cpp/custom_ops/grid_sample_3d.h, deploy/caddn/cpp/custom_ops/iou3d_cpu.cpp
- Git tree state: captured
- Evidence fingerprint: d20eadf686fc5945aef40e36aa19228a5f9cd1d5fa30b0533e8ec8a37a3a2a3d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
