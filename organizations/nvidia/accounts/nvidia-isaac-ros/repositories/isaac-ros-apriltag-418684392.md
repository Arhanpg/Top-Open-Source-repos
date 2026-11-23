# NVIDIA-ISAAC-ROS/isaac_ros_apriltag

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_apriltag](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag/blob/main/README.md)
- README blob SHA: e5ad16d8faa1d5a9a954dec0f7fd638dc2b1a616
- Repository ID: 418684392
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA-accelerated Apriltag detection and pose estimation.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:32:00+00:00

### Short excerpt (up to 100 words)

> NVIDIA-accelerated AprilTag detection and pose estimation. Isaac ROS AprilTag contains a ROS 2 package for detection of a type of fiducial marker that provides a point of reference or measure. AprilTag detections are NVIDIA-accelerated for high performance. A common graph of nodes connects from an input camera through rectify and resize to AprilTag. Rectify warps the input camera image into a rectified, undistorted output image; this node may not be necessary if the camera driver provides rectified camera images. Resize is often used to downscale higher resolution cameras into the desired resolution for AprilTags if needed. The input resolution to

### README headings

- Isaac ROS AprilTag
- Overview
- AprilTag Tag Families Supported by Backend
- ROS 2 Native `rosidl::Buffer` Acceleration
- Performance
- Documentation
- Packages
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 28,297 |
| CMake | 3,425 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- isaac_ros_apriltag/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 203
- Forks at capture: 34
- Last updated: 2026-10-13T14:02:16Z
- Last pushed: 2026-11-18T06:56:50Z
- Topics: apriltag, fiducial-marker, gpu, jetson, nvidia, ros, ros2, ros2-humble

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_apriltag/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
