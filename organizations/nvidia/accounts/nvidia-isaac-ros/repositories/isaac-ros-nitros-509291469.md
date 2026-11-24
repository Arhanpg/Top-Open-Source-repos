# NVIDIA-ISAAC-ROS/isaac_ros_nitros

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_nitros](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros/blob/main/README.md)
- README blob SHA: 1929723dc9ce71b7420387bdbda43252d72d67b3
- Repository ID: 509291469
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA Isaac Transport for ROS package for hardware-acceleration friendly movement of messages

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:21+00:00

### Short excerpt (up to 100 words)

> NVIDIA Isaac Transport for ROS package for hardware-acceleration friendly movement of messages. **NITROS is deprecated.** Isaac ROS nodes now use ROS 2 messages with `rosidl::Buffer` fields and the CUDA buffer backend, which are native ROS 2 Lyrical features. NITROS type adaptation and negotiation, Managed NITROS, CUDA with NITROS, PyNITROS, and the NITROS Bridge APIs will be removed in a future Isaac ROS release. Node-level compatibility is maintained, but applications that call NITROS APIs directly require source-level migration. Refer to guide, and rosidl::Buffer and Buffer Backends for the replacement architecture. packages that distribute NVIDIA’s precompiled SDKs to other Isaac ROS repositories,

### README headings

- Isaac ROS NITROS
- Overview
- Documentation
- Packages
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 802,705 |
| CMake | 24,465 |
| C | 7,214 |
| Shell | 494 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- cuapriltags_vendor/CMakeLists.txt (capture: captured)
- cumotion_vendor/CMakeLists.txt (capture: captured)
- cuvslam_vendor/CMakeLists.txt (capture: captured)
- isaac_ros_nitros_bridge/isaac_ros_nitros_bridge_ros2/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 224
- Forks at capture: 54
- Last updated: 2026-11-17T02:44:36Z
- Last pushed: 2026-11-18T06:57:13Z
- Topics: gpu, hardware-acceleration, jetson, nvidia, ros, ros2-humble

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nitros/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
