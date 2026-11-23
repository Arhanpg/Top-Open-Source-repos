# NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation/blob/main/README.md)
- README blob SHA: cd60a0c5692835c271efd3c478b9fc8e1ac17f64
- Repository ID: 620539588
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA-accelerated, deep-learned freespace segmentation

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:58+00:00

### Short excerpt (up to 100 words)

> NVIDIA-accelerated, deep-learned freespace segmentation Isaac ROS Freespace Segmentation contains an ROS 2 package to produce occupancy grids for navigation. By processing a freespace segmentation mask with the pose of the robot relative to the ground, Bi3D Freespace produces an occupancy grid for avoid obstacles during navigation. This package is GPU accelerated to provide real-time, low latency results in a robotics application. Bi3D Freespace provides an additional occupancy grid source for mobile robots (ground based). `isaac_ros_bi3d` is used in a graph of nodes to provide a freespace segmentation mask as one output from a time-synchronized input left and right stereo image

### README headings

- Isaac ROS Freespace Segmentation
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
| C++ | 31,162 |
| CMake | 5,557 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- gxf_isaac_occupancy_grid_projector/CMakeLists.txt (capture: captured)
- isaac_ros_bi3d_freespace/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 44
- Forks at capture: 6
- Last updated: 2026-10-15T11:07:15Z
- Last pushed: 2025-12-11T06:15:39Z
- Topics: deep-learning, deep-neural-networks, freespace, gpu, jetson, nvidia, ros2, ros2-humble

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_freespace_segmentation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
