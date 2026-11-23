# NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline/blob/main/README.md)
- README blob SHA: 0a8e4ee2133a742e453abaf6aa45537ac2905a92
- Repository ID: 418710869
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA-accelerated ROS 2 packages for camera image processing.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:46:02+00:00

### Short excerpt (up to 100 words)

> NVIDIA-accelerated Image Pipeline. Isaac ROS Image Pipeline is a metapackage of functionality for image processing. Camera output often needs pre-processing to meet the input requirements of multiple different perception functions. This can include cropping, resizing, mirroring, correcting for lens distortion, and color space conversion. For stereo cameras, additional processing is required to produce disparity between left + right images and a point cloud for depth perception. This package is accelerated using the GPU and specialized hardware engines for image computation, replacing the CPU-based Considerable effort has been made to ensure that replacing `image_pipeline` with `isaac_ros_image_pipeline` on a Jetson or GPU

### README headings

- Isaac ROS Image Pipeline
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
| C++ | 417,107 |
| CMake | 35,847 |
| Cuda | 26,428 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- cvcuda_conversions/CMakeLists.txt (capture: captured)
- isaac_ros_cvcuda_utils/CMakeLists.txt (capture: captured)
- isaac_ros_depth_image_proc/CMakeLists.txt (capture: captured)
- isaac_ros_image_pipeline/CMakeLists.txt (capture: captured)
- isaac_ros_image_proc/CMakeLists.txt (capture: captured)
- isaac_ros_stereo_image_proc/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 195
- Forks at capture: 37
- Last updated: 2026-11-08T19:25:51Z
- Last pushed: 2026-11-18T06:57:06Z
- Topics: cv, gpu, image-processing, jetson, nvidia, ros, ros2, ros2-humble, stereo-vision

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_image_pipeline/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
