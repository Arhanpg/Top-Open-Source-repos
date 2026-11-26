# ApolloAuto/apollo-model-yolox

- Company: Baidu
- Account: ApolloAuto
- Repository: https://github.com/ApolloAuto/apollo-model-yolox
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:15:11+00:00

## Project purpose

YOLOX is an anchor-free version of YOLO, with a simpler design but better performance! It aims to bridge the gap between research and industrial communities. For more details, please refer to our report on Arxiv.

## Why this project is used

[Apollo] This is the implementation of yolox3d first stage, a camera 2D object detection for autonomous driving perception.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, C++
- Frameworks/libraries: Unknown / not established
- Dependency names: loguru, ninja, numpy, onnx, onnx-simplifier, opencv_python, psutil, pycocotools, tabulate, tensorboard, thop, torch, torchvision, tqdm
- Build/package tools: Gradle build file, CMake configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: demo/ncnn/android/app/src/main/java/com/megvii/yoloXncnn/MainActivity.java, demo/ncnn/android/app/src/main/java/com/megvii/yoloXncnn/yoloXncnn.java, demo/ncnn/android/app/src/main/jni/yoloXncnn_jni.cpp, yolox/core/__init__.py

## Setup and usage

- Quick Start: Step1. Install YOLOX from source.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/ApolloAuto/apollo-model-yolox/blob/main/README.md
- README SHA: 96e387d2541653d1427b147bebb38b261bc1ba6e
- Manifests: requirements.txt, setup.py, docs/Makefile, demo/ncnn/android/build.gradle, demo/OpenVINO/cpp/CMakeLists.txt, demo/TensorRT/cpp/CMakeLists.txt
- Sampled source files: demo/ncnn/android/app/src/main/java/com/megvii/yoloXncnn/MainActivity.java, demo/ncnn/android/app/src/main/java/com/megvii/yoloXncnn/yoloXncnn.java, demo/ncnn/android/app/src/main/jni/yoloXncnn_jni.cpp, yolox/core/__init__.py
- Git tree state: captured
- Evidence fingerprint: a3e84c6930d488f2e2391409876e51929764bd18984c286a48c47d19fbf2e879

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
