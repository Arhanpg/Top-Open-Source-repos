# NVIDIA/Audio2Face-3D-SDK

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/Audio2Face-3D-SDK](https://github.com/NVIDIA/Audio2Face-3D-SDK)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/Audio2Face-3D-SDK/blob/main/README.md)
- README blob SHA: 78dd7a9c75e1842f76e2321a2cdba7248c5bbf00
- Repository ID: 1034647520
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

High-performance C++/CUDA SDK for running Audio2Emotion and Audio2Face inference with integrated post-processing.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:40:59+00:00

### Short excerpt (up to 100 words)

> The Audio2X SDK is a comprehensive toolkit for fast audio-driven animation and emotion detection. It consists of two main components: - **Audio2Emotion SDK**: Analyzes audio (speech) input to detect and classify emotional states - **Audio2Face SDK**: Generates facial animations from audio (speech) input, supporting both regression and diffusion-based approaches The SDK is designed for high-performance applications requiring fast audio processing and animation generation. It leverages NVIDIA's GPU computing capabilities through CUDA and TensorRT for optimal performance. - **Faster Than Real-time Processing**: Faster than 60 FPS frame generation - **Multi-track Support**: Process multiple audio streams simultaneously - **GPU Acceleration**: Full CUDA/TensorRT

### README headings

- Audio2X SDK
- Key Features
- Build
- Prerequisites
- System Requirements
- Building Audio2X SDK
- Windows
- Linux
- Windows
- Linux
- Build Output Structure
- Downloading Models and Generating Test Data
- License-protected models (Gated Models)
- Create venv
- Run these scripts in venv
- Generate unit test data
- Convert downloaded models to TensorRT format
- Create venv
- Run these scripts in venv
- Generate unit test data
- Convert downloaded models to TensorRT format
- Running Audio2X SDK Unit Tests and Samples
- Run samples (Please ensure that the environment variables CUDA_PATH and TENSORRT_ROOT_DIR are set)
- By default, the script runs a release build. To run a debug build, pass the debug argument.
- Run benchmarks
- Run benchmarks with a default set of filters
- Run samples (Please ensure that the environment variables CUDA_PATH and TENSORRT_ROOT_DIR are set)
- By default, the script runs a release build. To run a debug build, pass the debug argument.
- Run benchmarks
- Run benchmarks with a default set of filters

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 2,273,001 |
| Cuda | 177,411 |
| CMake | 84,984 |
| Python | 73,376 |
| Roff | 37,208 |
| Batchfile | 22,168 |
| PowerShell | 21,730 |
| Shell | 17,533 |
| C | 5,809 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- audio2emotion-sdk/CMakeLists.txt (capture: captured)
- audio2face-sdk/CMakeLists.txt (capture: captured)
- audio2x-common/CMakeLists.txt (capture: captured)
- audio2x-sdk/CMakeLists.txt (capture: captured)
- deps/requirements.txt (capture: captured) — dependency clues: Jinja2, MarkupSafe, PyYAML, certifi, charset-normalizer, colorama, filelock, fsspec, huggingface-hub, idna, inquirerpy, mpmath, networkx, numpy, onnx, packaging, pfzy, prompt_toolkit, protobuf, pydub

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 239
- Forks at capture: 58
- Last updated: 2026-11-22T01:29:48Z
- Last pushed: 2025-08-28T14:22:28Z
- Topics: cuda, gpu-acceleration, nvidia, tensorrt

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/Audio2Face-3D-SDK)
- [README](https://github.com/NVIDIA/Audio2Face-3D-SDK/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/Audio2Face-3D-SDK/issues)
- [Releases](https://github.com/NVIDIA/Audio2Face-3D-SDK/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
