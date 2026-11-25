# ApolloAuto/Apollo-Vision-Net

- Company: Baidu
- Account: ApolloAuto
- Repository: https://github.com/ApolloAuto/Apollo-Vision-Net
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:48:51+00:00

## Project purpose

This repository introduces the Apollo Vision Network, a new 3D detection and occupancy prediction network for autonomous driving.

## Why this project is used

Apollo BEV+OCC network training

## Core features

- Image backbone: Replacing ResNet-50 with pre-trained DLA-34 using depth estimation data (Toyota DDAD15M) reduces model complexity while improving performance.: Image backbone: Replacing ResNet-50 with pre-trained DLA-34 using depth estimation data (Toyota DDAD15M) reduces model complexity while improving performance.
  - Evidence: README.md#Highlights
- Image neck: Replacing the single scale FPN network with a SecondFPN network improves the performance of the model.: Image neck: Replacing the single scale FPN network with a SecondFPN network improves the performance of the model.
  - Evidence: README.md#Highlights
- Detection head: Using GroupDETR instead of DETR significantly improves object detection performance without increasing time consumption.: Detection head: Using GroupDETR instead of DETR significantly improves object detection performance without increasing time consumption.
  - Evidence: README.md#Highlights
- Occ head: Using low resolution bev queries (50 * 50) in the Transformer encoder, then upsampling to high resolution (200 * 200) in the occ head, significantly i: Occ head: Using low resolution bev queries (50 * 50) in the Transformer encoder, then upsampling to high resolution (200 * 200) in the occ head, significantly improve inference speed.
  - Evidence: README.md#Highlights
- OCC loss: Increase the weight of OCC focal loss from 1.0 to 10.0, introduce affinity loss and lovasz softmax loss, and significantly improve the miou of OCC det: OCC loss: Increase the weight of OCC focal loss from 1.0 to 10.0, introduce affinity loss and lovasz softmax loss, and significantly improve the miou of OCC detection.
  - Evidence: README.md#Highlights

## Technology stack

- Languages: Python, Cuda, C++, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/cpu/dcnv3_cpu.cpp, projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/cpu/dcnv3_cpu.h, projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/cuda/dcnv3_cuda.h, projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/dcnv3.h

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/ApolloAuto/Apollo-Vision-Net/blob/main/README.md
- README SHA: 8617913b7f168856ed347609fffcf0a9d54d1f83
- Manifests: projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/setup.py
- Sampled source files: projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/cpu/dcnv3_cpu.cpp, projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/cpu/dcnv3_cpu.h, projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/cuda/dcnv3_cuda.h, projects/mmdet3d_plugin/bevformer/backbones/ops_dcnv3/src/dcnv3.h
- Git tree state: captured
- Evidence fingerprint: d26ddeb24f409b60cba2ee7f297a21c63628e0959917196b7d67308766fae4fc

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
