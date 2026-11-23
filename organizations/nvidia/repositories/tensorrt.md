# TensorRT Open Source Software

- **Company:** NVIDIA
- **GitHub organization:** [NVIDIA](https://github.com/NVIDIA)
- **Repository:** [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT)
- **Default branch:** main
- **README:** [Open upstream README](https://github.com/NVIDIA/TensorRT/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `90832acea678dd070b5904366a05d07925b612eb`
- **Lifecycle:** Check current upstream release and support status before adoption

## Project overview

The repository contains the open-source software components of NVIDIA TensorRT, including plugin sources, the ONNX parser and sample applications demonstrating TensorRT platform capabilities. The README describes these components as a subset of the TensorRT GA release with extensions and bug fixes.

## Features and capabilities

- Includes source code for TensorRT plugins and the ONNX parser.
- Provides sample applications and import workflows for ONNX, Torch-TensorRT, Hugging Face/Optimum and the Network Definition API.
- Links a supported-model matrix across LLM, encoder/NLP, vision, audio, diffusion and multimodal workloads.
- Offers a prebuilt TensorRT Python package installable through pip.
- The inspected README announces TensorRT 11.x API changes and migration away from weakly typed networks, implicit quantization and IPluginV2 toward newer APIs.

## Technology stack

TensorRT OSS; Python package; CUDA Toolkit; optional cuDNN; GNU Make and CMake build tools. The inspected README lists TensorRT 11.5.0.63 as a GA build prerequisite and recommends CUDA 13.5.1 or 12.9.0 in its build guidance.

## Getting started

For the Python package workflow, the README documents pip install tensorrt. To build TensorRT-OSS, install the required TensorRT GA build and system dependencies, then follow the repository's build instructions.

## Lifecycle, compatibility and operational considerations

The README includes a TensorRT 11.x migration notice: weakly typed APIs, implicit quantization and IPluginV2-related APIs have been removed in favour of strongly typed networks, explicit quantization and IPluginV3. Python bindings for Python 3.9 and older have also been removed. Confirm exact release compatibility before upgrading.

## Evaluation guidance

Review the exact driver/model/runtime versions, hardware compatibility, licence, security guidance and maintenance state before using this project. Performance or deployment assumptions should be validated on the actual target hardware and software stack. This dossier summarizes the README; it is not a source-code, security or benchmark audit.

## Upstream references

- [Repository](https://github.com/NVIDIA/TensorRT)
- [README](https://github.com/NVIDIA/TensorRT/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/TensorRT/issues)
- [Releases](https://github.com/NVIDIA/TensorRT/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. The technology and lifecycle claims above are limited to the README evidence; source-level dependency validation is a separate task.*
