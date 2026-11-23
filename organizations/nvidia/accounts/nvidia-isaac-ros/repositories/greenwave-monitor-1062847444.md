# NVIDIA-ISAAC-ROS/greenwave_monitor

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/greenwave_monitor](https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor/blob/main/README.md)
- README blob SHA: e0f1160f22fb86d151a7275bddb57424004d382b
- Repository ID: 1062847444
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS 2 Topic Monitoring

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:16:00+00:00

### Short excerpt (up to 100 words)

> Greenwave monitor is a tool for runtime monitoring of ROS 2 topics. It provides the following features: 1. A node similar to a C++ based ros2 topic hz. i.e. subscribes to topics to determine the frame rate and latency. Compared to ros2 topic hz the greenwave node is more performant, publishes Diagnostics, and offers services to manage topics and expected frequencies. 2. A terminal based dashboard that displays the topic rates, latency, and status, and allows you to add/remove topics and set expected frequencies. 3. A header only C++ library so you can calculate and publish compatible diagnostics directly from

### README headings

- Greenwave Monitor
- Compatibility
- Installation
- Usage
- ncurses Dashboard
- Rich TUI (r2s integration) - Optional
- Manual Launch (ros2 topic hz mode)
- Inline Integration Example Node

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 101,852 |
| C++ | 91,923 |
| Shell | 16,122 |
| CMake | 7,477 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- greenwave_monitor/CMakeLists.txt (capture: captured)
- greenwave_monitor_interfaces/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 265
- Forks at capture: 20
- Last updated: 2026-11-14T10:14:45Z
- Last pushed: 2026-09-08T15:37:27Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor)
- [README](https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/greenwave_monitor/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
