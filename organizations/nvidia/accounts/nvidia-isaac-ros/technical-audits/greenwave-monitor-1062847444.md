# NVIDIA-ISAAC-ROS/greenwave_monitor

- Company: NVIDIA
- Account: NVIDIA-ISAAC-ROS
- Repository: https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:16:39+00:00

## Project purpose

Greenwave monitor is a tool for runtime monitoring of ROS 2 topics.

## Why this project is used

ROS 2 Topic Monitoring

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, C++, Shell, CMake
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: greenwave_monitor/src/example_greenwave_publisher_main.cpp, greenwave_monitor/src/example_greenwave_publisher_node.cpp, greenwave_monitor/src/greenwave_monitor.cpp, greenwave_monitor/src/greenwave_monitor_main.cpp

## Setup and usage

- Installation: > **Note:** Make sure ROS_DISTRO is set to your ROS 2 distribution, for example by
- Installation: > running source /opt/ros/ /setup.bash.
- Installation: sudo apt install ros-${ROS_DISTRO}-greenwave-monitor
- Installation: From source, for development:
- Installation: git clone https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor.git
- Installation: colcon build --packages-up-to greenwave_monitor
- Installation: source install/setup.bash
- Usage: Greenwave monitor provides a lightweight ncurses dashboard for monitoring topics. An optional rich TUI (r2s integration) with additional features is also available as a separate package.

## Limitations and caveats

- Compatibility: Greenwave monitor is a standalone package tested on Humble, Iron, Jazzy, Lyrical, Kilted, and Rolling ROS 2 releases, under Ubuntu 22.04, Ubuntu 24.04, and Ubuntu 26.04. It does not depend on Isaac ROS. It does however play nicely with Isaac ROS NITROS diagnostics, see docs/DESIGN_AND_IMPLEMENTATION.md for more.

## Evidence and provenance

- README: https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor/blob/main/README.md
- README SHA: e0f1160f22fb86d151a7275bddb57424004d382b
- Manifests: greenwave_monitor/CMakeLists.txt, greenwave_monitor_interfaces/CMakeLists.txt
- Sampled source files: greenwave_monitor/src/example_greenwave_publisher_main.cpp, greenwave_monitor/src/example_greenwave_publisher_node.cpp, greenwave_monitor/src/greenwave_monitor.cpp, greenwave_monitor/src/greenwave_monitor_main.cpp
- Git tree state: captured
- Evidence fingerprint: df6ccb71604c5ba39e48eced7a470451ca13af1f37ea7ec01522115b40b1193a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
