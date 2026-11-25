# ApolloAuto/Apollo-Vision-Net-Deployment

- Company: Baidu
- Account: ApolloAuto
- Repository: https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:57:24+00:00

## Project purpose

This repository is a deployment project of Apollo Vision Network on TensorRT.

## Why this project is used

Apollo BEV+OCC model deployment

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Cuda, C++, Dockerfile, CMake, C, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Pillow, Shapely, matplotlib, netron, numba, numpy, nuscenes_devkit, nvidia-pyindex, opencv_python, pycocotools, pycuda, pyquaternion, pytorch_quantization, scipy, setuptools, terminaltables, thop, tqdm, trimesh
- Build/package tools: CMake configuration, Docker build configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: ci/check/run_py_format.py, configs/_base_/default_runtime.py, configs/_base_/det2trt.py, configs/_base_/schedules/schedule_1x.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/ApolloAuto/Apollo-Vision-Net-Deployment/blob/main/README.md
- README SHA: c919521b6a05f55d6c1c832c1dc1cf47b1277cfd
- Manifests: requirements.txt, docker/Dockerfile, TensorRT/CMakeLists.txt, third_party/bev_mmdet3d/setup.py
- Sampled source files: ci/check/run_py_format.py, configs/_base_/default_runtime.py, configs/_base_/det2trt.py, configs/_base_/schedules/schedule_1x.py
- Git tree state: captured
- Evidence fingerprint: 1bfac21e1f9a2338b5823802ee41ce237219bf3253b681097fbe0002de5bac4d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
