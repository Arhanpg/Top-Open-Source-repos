# NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference

- Company: NVIDIA
- Account: NVIDIA-ISAAC-ROS
- Repository: https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:59:28+00:00

## Project purpose

NVIDIA-accelerated DNN model inference ROS 2 packages using NVIDIA Triton/TensorRT for both Jetson and x86_64 with CUDA-capable GPU.

## Why this project is used

NVIDIA-accelerated DNN model inference ROS 2 packages using NVIDIA Triton/TensorRT for both Jetson and x86_64 with CUDA-capable GPU

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, CMake
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: isaac_ros_tensor_proc/src/image_tensor_normalize_node.cpp, isaac_ros_tensor_proc/src/image_to_tensor_node.cpp, isaac_ros_tensor_proc/src/interleaved_to_planar_node.cpp, isaac_ros_tensor_proc/src/normalize_node.cpp

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference/blob/main/README.md
- README SHA: 583a46b1f75ef067cdfdc32e0043c784a574b940
- Manifests: isaac_ros_dnn_image_encoder/CMakeLists.txt, isaac_ros_tensor_proc/CMakeLists.txt, isaac_ros_tensor_rt/CMakeLists.txt, isaac_ros_triton/CMakeLists.txt, tensorrt_conversions/CMakeLists.txt, triton_conversions/CMakeLists.txt
- Sampled source files: isaac_ros_tensor_proc/src/image_tensor_normalize_node.cpp, isaac_ros_tensor_proc/src/image_to_tensor_node.cpp, isaac_ros_tensor_proc/src/interleaved_to_planar_node.cpp, isaac_ros_tensor_proc/src/normalize_node.cpp
- Git tree state: captured
- Evidence fingerprint: f7dc72e1915bac6bc10a2abf910f8346c25dcf04eb84c6375b0c00f1ad158ddf

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
