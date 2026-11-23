# NVIDIA-ISAAC-ROS/isaac_ros_deploy

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_deploy](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_deploy)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_deploy/blob/main/README.md)
- README blob SHA: febfd380977a6c8907d278d71d60063d5f2be358
- Repository ID: 1225085755
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Deploy neural network policies trained in NVIDIA Isaac Lab on real and simulated robots

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:32:21+00:00

### Short excerpt (up to 100 words)

> ROS 2 packages for deploying LEAPP-exported neural-network policies on real and simulated robots. Isaac ROS Deploy provides ROS 2 packages for deploying neural-network policies on real and simulated robots. It can support a variety of robot-control policies, including policies derived from and vision-language-action (VLA) policies exported through as long as the policy can be exported as a Isaac ROS Deploy bridges the gap between a Python training stack and a robot control system: it loads LEAPP bundles, runs ONNX inference through NVIDIA Triton, maps policy terms onto ROS topics or `ros2_control` interfaces, and optionally gates outputs through a safety controller.

### README headings

- Isaac ROS Deploy
- Overview
- Documentation
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 880,507 |
| Python | 481,839 |
| CMake | 53,391 |
| Shell | 757 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- isaac_ros_deploy/CMakeLists.txt (capture: captured)
- isaac_deploy/isaac_deploy_core/CMakeLists.txt (capture: captured)
- isaac_deploy/isaac_ros_deploy_bringup/CMakeLists.txt (capture: captured)
- isaac_deploy/isaac_ros_deploy_converters/CMakeLists.txt (capture: captured)
- isaac_deploy/isaac_ros_deploy_interfaces/CMakeLists.txt (capture: captured)
- isaac_deploy/isaac_ros_deploy_isaac_sim_extension/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 5
- Last updated: 2026-11-12T10:10:24Z
- Last pushed: 2026-11-18T06:56:59Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_deploy)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_deploy/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_deploy/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_deploy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
