# NVIDIA-ISAAC-ROS/isaac_ros_nvblox

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_nvblox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox/blob/main/README.md)
- README blob SHA: 373aced912394de78a0f1eb55c95cc73b3c9c127
- Repository ID: 472930182
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA-accelerated 3D scene reconstruction and Nav2 local costmap provider using nvblox

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:29+00:00

### Short excerpt (up to 100 words)

> Nvblox ROS 2 integration for local 3D scene reconstruction and mapping. Isaac ROS Nvblox contains ROS 2 packages for 3D reconstruction and cost maps for navigation. `isaac_ros_nvblox` processes depth and pose to reconstruct a 3D scene in real-time and outputs a 2D costmap for used in planning during navigation as a vision-based solution to avoid obstacles. `isaac_ros_nvblox` is designed to work with depth-cameras and/or 3D LiDAR. The package uses GPU acceleration to compute a 3D reconstruction and 2D costmaps using framework-independent C++ library. Above is a typical graph that uses `isaac_ros_nvblox`. Nvblox takes a depth image, a color image, and

### README headings

- Isaac ROS Nvblox
- Overview
- Performance
- Documentation
- Packages
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 470,021 |
| CMake | 39,516 |
| Cuda | 36,548 |
| Shell | 6,035 |
| TypeScript | 5,045 |
| GLSL | 3,958 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- isaac_ros_nvblox/CMakeLists.txt (capture: captured)
- nvblox_foxglove/package.json (capture: captured) — dependency clues: @foxglove/eslint-plugin, @foxglove/schemas, @foxglove/studio, @types/react, @types/react-dom, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, create-foxglove-extension, eslint, eslint-config-prettier, eslint-plugin-es, eslint-plugin-filenames, eslint-plugin-import, eslint-plugin-jest, eslint-plugin-prettier, eslint-plugin-react, eslint-plugin-react-hooks, prettier, react, react-dom
- nvblox_message_adapters/CMakeLists.txt (capture: captured)
- nvblox_msgs/CMakeLists.txt (capture: captured)
- nvblox_nav2/CMakeLists.txt (capture: captured)
- nvblox_ros/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 772
- Forks at capture: 151
- Last updated: 2026-11-17T07:29:28Z
- Last pushed: 2026-11-18T06:57:15Z
- Topics: 3d-reconstruction, gpu, jetson, nvidia, robotics, ros, ros2-humble

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
