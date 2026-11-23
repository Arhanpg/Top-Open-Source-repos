# ncnn — High-Performance Neural Network Inference Framework

- Company association: Tencent
- Upstream GitHub account: [Tencent](https://github.com/Tencent)
- Repository: [Tencent/ncnn](https://github.com/Tencent/ncnn)
- Default branch: master
- README: [Open upstream README](https://github.com/Tencent/ncnn/blob/master/README.md)
- Review status: README inspected and summarized
- README blob SHA: 687f43a983f95fccbcc352cd85905286feeae2d9
- Account relationship: The repository is hosted under Tencent's verified primary public GitHub organization.

## Project overview

A high-performance neural-network inference framework optimized for mobile and edge deployment. The README highlights lightweight CPU/GPU inference, broad device coverage and conversion/deployment tooling for neural-network models.

## Features and capabilities documented by the README

- Provides a lightweight C++ inference runtime optimized for mobile and embedded devices.
- Uses CPU optimizations and SIMD/vectorization, and supports GPU acceleration through Vulkan where the target device and build permit it.
- Includes the pnnx model-conversion tool and workflows for bringing models from frameworks/formats such as PyTorch and ONNX into ncnn.
- Offers C++ APIs and platform-specific build/distribution packages.
- The README lists build and deployment paths for Android, HarmonyOS, iOS, macOS, watchOS, tvOS, visionOS, Linux, Windows, Raspberry Pi, NVIDIA Jetson and WebAssembly.
- Provides separate Vulkan and CPU-only release packages for several platforms.
- Publishes CI build workflows and platform-specific build instructions for reproducible native builds.

## Technology stack

C++; CMake-oriented native build tooling; Vulkan GPU backend; CPU-only inference path; pnnx model converter; model import from supported PyTorch/ONNX workflows; cross-platform toolchains for Android, iOS, macOS, HarmonyOS, Linux, Windows and embedded devices. The README recommends following its platform-specific build guide.

## Getting started

Choose the target platform and follow the matching build instructions in the ncnn wiki. Download the corresponding release package or build from source. Decide explicitly whether the deployment uses Vulkan or CPU-only inference, and validate the model-conversion path with pnnx for the source framework.

## Lifecycle, compatibility and operational considerations

Vulkan support depends on the target driver and GPU; CPU-only packages are available for platforms where Vulkan is unsuitable. Model conversion and operator support should be validated against the specific model. The README lists many platforms but that does not guarantee identical operator/performance support across every device.

## Evaluation guidance

Check the exact upstream release, source manifests, platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a complete source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/Tencent/ncnn)
- [README](https://github.com/Tencent/ncnn/blob/master/README.md)
- [Issues](https://github.com/Tencent/ncnn/issues)
- [Releases](https://github.com/Tencent/ncnn/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Technical claims are limited to README-supported material; details not established by the README are left unspecified.
