# ApolloAuto/apollo-model-yolo3d

- Company: Baidu
- Account: ApolloAuto
- Repository: https://github.com/ApolloAuto/apollo-model-yolo3d
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:07:25+00:00

## Project purpose

YOLO3D is inspired by Mousavian et al. in their paper **3D Bounding Box Estimation Using Deep Learning and Geometry**. YOLO3D uses a different approach, we use 2d gt label result as the input of first stage detector, then use the 2d result as input to regressor model.

## Why this project is used

[Apollo] This is the implementation of yolox3d second stage, a camera 3D object detection for autonomous driving perception.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Makefile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: hydra-colorlog, hydra-core, hydra-optuna-sweeper, pre-commit, pyrootutils, pytest, pytorch-lightning, rich, sh, torch, torchmetrics, torchvision
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/__init__.py, src/datamodules/__init__.py, src/datamodules/components/__init__.py, src/datamodules/components/kitti_dataset.py

## Setup and usage

- Quickstart: git clone git@github.com:ApolloAuto/apollo-model-yolo3d.git

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/ApolloAuto/apollo-model-yolo3d/blob/main/README.md
- README SHA: 225913f9b8eb617ca4fbfaa837e67eeecf2a4885
- Manifests: Makefile, pyproject.toml, requirements.txt, setup.py
- Sampled source files: src/datamodules/components/kitti_dataset.py
- Git tree state: captured
- Evidence fingerprint: dc978cc07618c38066b6d3d5e12855aeb7311383bf52170a54ea19105f52a2e3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
