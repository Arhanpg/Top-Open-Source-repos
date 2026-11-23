# NVIDIA-ISAAC-ROS/isaac-ros-cli

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac-ros-cli](https://github.com/NVIDIA-ISAAC-ROS/isaac-ros-cli)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac-ros-cli/blob/main/README.md)
- README blob SHA: 2fb01d0fbd74cd78498c19217ab8d3b07cf3f6ab
- Repository ID: 1090935175
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

 A command-line interface for managing Isaac ROS development environments.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:16:07+00:00

### Short excerpt (up to 100 words)

> A command-line interface for managing Isaac ROS development environments. sudo apt-get install isaac-ros-cli isaac-ros --help sudo isaac-ros init <docker|venv|baremetal> isaac-ros status isaac-ros status --output json isaac-ros activate isaac-ros activate --config docker.run.container_name=foo isaac-ros activate --config docker.run.container_name=foo -c docker.run.platform=x86_64 isaac-ros activate -c docker.image.push=true isaac-ros activate --push isaac-ros activate --no-push To build a new local copy: make build

### README headings

- Isaac ROS CLI
- Installation
- Usage
- Show help
- Initialize environment (pick a mode)
- Show configured mode and current activation state
- Activate environment
- Override config keys for one invocation (see config/config.yaml for available keys)
- Override the configured image push default for one invocation
- Rebuilding Debian Package

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 267,320 |
| Shell | 25,440 |
| Makefile | 4,394 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 13
- Forks at capture: 16
- Last updated: 2026-10-07T06:37:03Z
- Last pushed: 2026-11-18T06:56:48Z
- Topics: docker, gpu, jetson, nvidia, ros, ros2, ros2-jazzy, ubuntu

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac-ros-cli)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac-ros-cli/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac-ros-cli/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac-ros-cli/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
