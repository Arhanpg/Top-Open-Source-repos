# NVIDIA-ISAAC-ROS/isaac_ros_object_detection

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_object_detection](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection/blob/main/README.md)
- README blob SHA: e64e84fae148ae056f7ab86374368308fff5ad8c
- Repository ID: 472931232
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA-accelerated, deep learned model support for image space object detection

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:31+00:00

### Short excerpt (up to 100 words)

> NVIDIA-accelerated, deep learned model support for object detection including DetectNet. Isaac ROS Object Detection contains ROS 2 packages to perform object detection. `isaac_ros_rtdetr`, `isaac_ros_detectnet`, `isaac_ros_yolov8`, and `isaac_ros_grounding_dino` each provide a method for spatial classification using bounding boxes with an input image. Classification is performed by a GPU-accelerated model of the appropriate architecture: - `isaac_ros_rtdetr`: RT-DETR models - `isaac_ros_detectnet`: DetectNet models - `isaac_ros_yolov8`: YOLOv8 models - `isaac_ros_grounding_dino`: Grounding DINO models The output prediction can be used by perception functions to understand the presence and spatial location of an object in an image. Each Isaac ROS Object Detection package is used in

### README headings

- Isaac ROS Object Detection
- Overview
- ROS 2 Native `rosidl::Buffer` Acceleration
- Performance
- Documentation
- Packages
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 160,457 |
| C | 21,357 |
| CMake | 18,800 |
| Shell | 15,115 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- isaac_ros_detectnet/CMakeLists.txt (capture: captured)
- isaac_ros_grounding_dino/CMakeLists.txt (capture: captured)
- isaac_ros_grounding_dino_interfaces/CMakeLists.txt (capture: captured)
- isaac_ros_grounding_dino_models_install/CMakeLists.txt (capture: captured)
- isaac_ros_peoplenet_models_install/CMakeLists.txt (capture: captured)
- isaac_ros_rtdetr/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 206
- Forks at capture: 51
- Last updated: 2026-11-19T04:42:23Z
- Last pushed: 2026-11-18T06:57:16Z
- Topics: deep-learning, gpu, inference, jetson, machine-learning, nvidia, object-detection, ros, ros2, ros2-humble, tensorrt, triton

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
