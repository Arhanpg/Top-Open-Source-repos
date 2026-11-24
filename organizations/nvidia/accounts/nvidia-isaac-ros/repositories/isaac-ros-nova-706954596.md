# NVIDIA-ISAAC-ROS/isaac_ros_nova

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_nova](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nova)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nova/blob/main/README.md)
- README blob SHA: b7b581da182e36d720a1fd27cd494e507fd7b862
- Repository ID: 706954596
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS 2 support packages for Nova.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:27+00:00

### Short excerpt (up to 100 words)

> Optimized Isaac ROS packages for Isaac Nova Orin. Isaac ROS Nova provides a set of optimized packages and tools to interface with the Nova sensor suite. These packages integrate with hardware timestamp synchronization on Jetson Orin platforms to enable high-quality sensor fusion. Sensor data streams through Isaac ROS graphs using NITROS for NVIDIA-accelerated processing. * Hesai Pandar XT32 3D LiDAR * Leopard Imaging HAWK stereo camera * Leopard Imaging OWL monocular camera * Bosch BMI088 IMU It is recommended to use Nova through the Isaac ROS Nova meta-package. This package will launch all the sensor drivers for your defined Nova

### README headings

- Isaac ROS Nova
- Overview
- Quickstart
- Isaac ROS NITROS Acceleration
- Performance
- Documentation
- Packages
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 335,168 |
| C++ | 103,825 |
| CMake | 37,778 |
| Shell | 6,784 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- hawk_description/CMakeLists.txt (capture: captured)
- isaac_ros_correlated_timestamp_driver/CMakeLists.txt (capture: captured)
- isaac_ros_data_recorder/CMakeLists.txt (capture: captured)
- isaac_ros_data_replayer/CMakeLists.txt (capture: captured)
- isaac_ros_data_validation/requirements.txt (capture: captured) — dependency clues: matplotlib, numpy, pandas, rosbags
- isaac_ros_data_validation/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 16
- Forks at capture: 3
- Last updated: 2026-08-03T23:18:34Z
- Last pushed: 2026-05-01T02:31:49Z
- Topics: nvidia, robotics, robots, ros, ros2

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nova)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nova/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nova/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nova/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
