# ApolloAuto/apollo-model-yolox

- Company: Baidu
- GitHub account: [https://github.com/ApolloAuto](https://github.com/ApolloAuto)
- Mapping status: official-project-linked
- Repository: [ApolloAuto/apollo-model-yolox](https://github.com/ApolloAuto/apollo-model-yolox)
- Default branch: main
- README: [Open upstream README](https://github.com/ApolloAuto/apollo-model-yolox/blob/main/README.md)
- README blob SHA: 96e387d2541653d1427b147bebb38b261bc1ba6e
- Repository ID: 715954255
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

[Apollo] This is the implementation of yolox3d first stage, a camera 2D object detection for autonomous driving perception.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:51:19+00:00

### Short excerpt (up to 100 words)

> YOLOX is an anchor-free version of YOLO, with a simpler design but better performance! It aims to bridge the gap between research and industrial communities. For more details, please refer to our report on Arxiv. This repo is an implementation of PyTorch version YOLOX, there is also a MegEngine implementation. * 【2023/10/23】 We employ YOLOX(commit id ac58e0a5e68e57454b7b9ac822aced493b553c53) as the first stage in Apollo camera_detection_multi_stage component. * 【2023/02/28】 We support assignment visualization tool, see doc here. * 【2022/04/14】 We support jit compile op. * 【2021/08/19】 We optimize the training process with **2x** faster training and **~1%** higher performance! See notes for

### README headings

- Introduction
- Updates!!
- Quick Start
- clone code
- creat conda env
- install requirements
- Deployment
- Cite YOLOX

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 304,023 |
| C++ | 24,802 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: loguru, ninja, numpy, onnx, onnx-simplifier, opencv_python, psutil, pycocotools, tabulate, tensorboard, thop, torch, torchvision, tqdm
- setup.py (capture: captured)
- docs/Makefile (capture: captured)
- demo/ncnn/android/build.gradle (capture: captured)
- demo/OpenVINO/cpp/CMakeLists.txt (capture: captured)
- demo/TensorRT/cpp/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 3
- Last updated: 2026-06-30T02:40:27Z
- Last pushed: 2023-12-07T09:08:36Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ApolloAuto/apollo-model-yolox)
- [README](https://github.com/ApolloAuto/apollo-model-yolox/blob/main/README.md)
- [Issues](https://github.com/ApolloAuto/apollo-model-yolox/issues)
- [Releases](https://github.com/ApolloAuto/apollo-model-yolox/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
