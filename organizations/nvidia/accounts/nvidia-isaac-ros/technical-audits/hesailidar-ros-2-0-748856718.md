# NVIDIA-ISAAC-ROS/HesaiLidar_ROS_2.0

- Company: NVIDIA
- Account: NVIDIA-ISAAC-ROS
- Repository: https://github.com/NVIDIA-ISAAC-ROS/HesaiLidar_ROS_2.0
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:50:19+00:00

## Project purpose

This repository includes the ROS Driver for Hesai LiDAR sensor manufactured by Hesai Technology. Developed based on HesaiLidar_SDK_2.0, After launched, the project will monitor UDP packets from Lidar,parse data and publish point cloud frames into ROS topic

## Why this project is used

This repository includes the ROS Driver for Hesai LiDAR sensor manufactured by Hesai Technology. Developed based on HesaiLidar_SDK_2.0, After launched, the project will monitor UDP packets from Lidar,parse data and publish point cloud frames into ROS topic

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, CMake, Cuda, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/manager/node_manager.cc, src/manager/node_manager.h, src/manager/source_driver_ros1.hpp, src/manager/source_driver_ros2.hpp

## Setup and usage

- Installation dependencies: Install ROS related dependency libraries, please refer to: http://wiki.ros.org
- Installation dependencies: - Ubuntu 16.04 - ROS Kinetic desktop
- Installation dependencies: - Ubuntu 18.04 - ROS Melodic desktop
- Installation dependencies: - Ubuntu 20.04 - ROS Noetic desktop
- Installation dependencies: - Ubuntu 18.04 - ROS2 Dashing desktop
- Installation dependencies: - Ubuntu 20.04 - ROS2 Foxy desktop
- Installation dependencies: - Ubuntu 22.04 - ROS2 Humble desktop

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/NVIDIA-ISAAC-ROS/HesaiLidar_ROS_2.0/blob/master/README.md
- README SHA: bcb7b960bc5758e8535d8e1a30bb42f9eb888e04
- Manifests: CMakeLists.txt
- Sampled source files: src/manager/node_manager.cc, src/manager/node_manager.h, src/manager/source_driver_ros1.hpp, src/manager/source_driver_ros2.hpp
- Git tree state: captured
- Evidence fingerprint: f6826419680485c93c099f2c21257a8a18ad281ebfcb36cfa69c80752bed2194

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
