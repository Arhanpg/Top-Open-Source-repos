# NVIDIA-ISAAC-ROS/realsense-ros

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/realsense-ros](https://github.com/NVIDIA-ISAAC-ROS/realsense-ros)
- Default branch: ros2-development
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/realsense-ros/blob/ros2-development/README.md)
- README blob SHA: 3d89df1fed985abc804ae94d8502a571a33f31ec
- README bytes captured: 23062
- README truncated at capture limit: False
- Repository ID: 588762756
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Intel(R) RealSense(TM) ROS Wrapper for D400 series, SR300 Camera and T265 Tracking Module

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T05:23:06+00:00

### Short excerpt (up to 300 words)

> #### Ubuntu 22.04: ROS2 Start the component: ros2 sudo apt-get install python3-rosdep Node components are currently

### README headings

- ROS2 Wrapper for Intel&reg; RealSense&trade; Devices
- For LibRS ROS1 Wrapper please refer to [ROS1-legacy branch](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy)
- Please notice: if you are moving from RealSense [ROS2-legacy branch](https://github.com/IntelRealSense/realsense-ros/tree/ros2-legacy) to ROS2-development:
- Installation Instructions
- Step 2: Install the latest Intel&reg; RealSense&trade; SDK 2.0
- Step 3: Install Intel&reg; RealSense&trade; ROS2 wrapper from sources
- Step 4: Install dependencies
- Step 5: Build
- Step 6: Terminal environment
- Usage Instructions
- Start the camera node
- Published Topics
- The metadata topic:
- Post processing blocks - i.e. filters:
- Sensor Parameters:
- Available Parameters:
- Parameters that can be modified during runtime:
- Parameters that cannot be changed in runtime:
- Available services:
- Using T265 ##
- Start the camera node
- Efficient intra-process communication:
- Example
- Manually loading multiple components into the same process
- Limitations
- Latency test tool and launch file
- Still in the pipeline:
- Unit tests:
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Step 1: Install the ROS2 distribution

> #### Ubuntu 22.04: ROS2

### Architecture and design: Manually loading multiple components into the same process

> Start the component: ros2

### Technology and requirements: Step 4: Install dependencies

> sudo apt-get install python3-rosdep

### Limitations and security: Limitations

> Node components are currently

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 209,172 |
| Python | 115,401 |
| CMake | 9,100 |
| Shell | 5,336 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- realsense2_camera/CMakeLists.txt (capture: captured)
- realsense2_camera_msgs/CMakeLists.txt (capture: captured)
- realsense2_description/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 6
- Last updated: 2026-06-22T10:23:21Z
- Last pushed: 2024-09-16T22:23:28Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/realsense-ros)
- [README](https://github.com/NVIDIA-ISAAC-ROS/realsense-ros/blob/ros2-development/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/realsense-ros/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/realsense-ros/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
