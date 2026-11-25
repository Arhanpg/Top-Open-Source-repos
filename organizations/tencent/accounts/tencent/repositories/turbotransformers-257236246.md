# Tencent/TurboTransformers

- Company: Tencent
- GitHub account: [https://github.com/Tencent](https://github.com/Tencent)
- Mapping status: verified
- Repository: [Tencent/TurboTransformers](https://github.com/Tencent/TurboTransformers)
- Default branch: master
- README: [Open upstream README](https://github.com/Tencent/TurboTransformers/blob/master/README.md)
- README blob SHA: e84f3e6205ea8cf94013251305452dd502cbe7cd
- README bytes captured: 11876
- README truncated at capture limit: False
- Repository ID: 257236246
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

a fast and user-friendly runtime for transformer inference (Bert, Albert, GPT2, Decoders, etc) on CPU and GPU.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T07:09:45+00:00

### Short excerpt (up to 300 words)

> Note that the building 1. The results of

### README headings

- TurboTransformers: a fast and user-friendly runtime for transformer inference on CPU and GPU
- Supported Models
- Boost BERT Inference in 2 Lines of Python Code
- Installation
- CPU
- optional: If you want to compare the performance of onnxrt-mkldnn during benchmark, you need to set BUILD_TYPE=dev to compile onnxruntime into the docker image, as follows
- you can switch between Openblas and MKL by modifying this line in CMakeList.txt
- set(BLAS_PROVIDER "mkl" CACHE STRING "Set the blas provider library, in [openblas, mkl, blis]")
- The conda package will be in /workspace/dist/*.tar.bz2
- When using turbo_transformers in other environments outside this container: conda install your_root_path/dist/*.tar.bz2
- GPU
- You can modify the environment variables in the script to specify the cuda version and operating system version
- for example: nvidia-docker run --gpus all --net=host --rm -it -v $PWD:/workspace -v /etc/passwd:/etc/passwd --name=turbo_gpu_env thufeifeibear:0.1.1-cuda9.0-ubuntu16.04-gpu-dev
- Using Tensor Core (FP16)
- Usage
- Pretrained Model Loading
- APIs
- python APIs
- C++ APIs
- Smart Batching (Minimize Zero-Padding Overhead in Batching)
- How to contribute new models
- TODO
- License
- Known Issues
- History
- Cite us
- Contact us

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> Note that the building

### Limitations and security: Known Issues

> 1. The results of

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 418,382 |
| Python | 403,330 |
| Cuda | 52,640 |
| CMake | 28,725 |
| Shell | 14,409 |
| C | 1,189 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- requirements.txt (capture: captured) — dependency clues: contexttimer, future, onnx, transformers
- 3rd/CMakeLists.txt (capture: captured)
- benchmark/CMakeLists.txt (capture: captured)
- example/CMakeLists.txt (capture: captured)
- turbo_transformers/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 1551
- Forks at capture: 208
- Last updated: 2026-11-19T21:47:20Z
- Last pushed: 2025-07-18T03:51:18Z
- Topics: albert, bert, decoder, gpt2, gpu, huggingface-transformers, inference, machine-translation, nlp, pytorch, roberta, transformer

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Tencent/TurboTransformers)
- [README](https://github.com/Tencent/TurboTransformers/blob/master/README.md)
- [Issues](https://github.com/Tencent/TurboTransformers/issues)
- [Releases](https://github.com/Tencent/TurboTransformers/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
