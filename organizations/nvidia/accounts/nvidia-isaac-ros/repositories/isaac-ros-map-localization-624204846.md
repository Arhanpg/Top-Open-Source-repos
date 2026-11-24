# NVIDIA-ISAAC-ROS/isaac_ros_map_localization

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_map_localization](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_map_localization)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_map_localization/blob/main/README.md)
- README blob SHA: dc1dc36a28b04ebcdd21c16e283323c662eab5a6
- Repository ID: 624204846
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA-accelerated global localization

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:17+00:00

### Short excerpt (up to 100 words)

> NVIDIA-accelerated Map localization. The Isaac ROS Map Localization module contains ROS 2 packages for lidar processing to estimate poses relative to a map. The Occupancy Grid Localizer processes a planar range scan to estimate pose in an occupancy grid map; this occurs in less than 1 second for most maps. This initial pose can be used to bootstrap navigation for mobile robots and has been integrated and tested with Nav2. This can remove the need for upwards of 30 seconds to [manually estimate the position and direction](https://youtu.be/IrJmuow1r7g?t=1029) of a robot with RViz, for example. The Occupancy Grid Localizer is designed

### README headings

- Isaac ROS Map Localization
- Overview
- Isaac ROS NITROS Acceleration
- Performance
- Documentation
- Packages
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 44,928 |
| CMake | 5,995 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- isaac_ros_occupancy_grid_localizer/CMakeLists.txt (capture: captured)
- isaac_ros_pointcloud_utils/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 83
- Forks at capture: 10
- Last updated: 2026-11-12T00:47:06Z
- Last pushed: 2025-12-11T06:15:42Z
- Topics: gpu, jetson, localization, nvidia, occupancy-grid-map, ros2, ros2-humble

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_map_localization)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_map_localization/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_map_localization/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_map_localization/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
