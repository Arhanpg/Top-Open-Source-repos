# NVIDIA-ISAAC-ROS/f1tenth_system

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/f1tenth_system](https://github.com/NVIDIA-ISAAC-ROS/f1tenth_system)
- Default branch: foxy-devel
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/f1tenth_system/blob/foxy-devel/README.md)
- README blob SHA: ffc69eab1c42b3352caccf0a0dc0ed654227203c
- Repository ID: 650424906
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Drivers and system level code for the F1TENTH vehicles

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:57+00:00

### Short excerpt (up to 100 words)

> Drivers onboard f1tenth race cars. This branch is under development for migration to ROS2. See the documentation of F1TENTH on how to get started. On Logitech F-710 joysticks, the LB button is the deadman's switch for teleop, and the RB button is the deadman's switch for navigation. You can also remap buttons. See how on the readthedocs documentation. - `/drive`: Topic for autonomous navigation, uses `AckermannDriveStamped` messages. - `/scan`: Topic for `LaserScan` messages. - `/odom`: Topic for `Odometry` messages. - `/sensors/imu/raw`: Topic for `Imu` messages. - `/sensors/core`: Topic for telemetry data from the VESC 1. ackermann_msgs https://index.ros.org/r/ackermann_msgs/#foxy. 2. urg_node https://index.ros.org/p/urg_node/#foxy.

### README headings

- f1tenth_system
- Deadman's switch
- Topics
- Topics that the driver stack subscribe to
- Sensor topics published by the driver stack
- External Dependencies
- Package in this repo
- Nodes launched in bringup
- Parameters and topics for dependencies
- vesc_driver
- ackermann_to_vesc
- vesc_to_odom
- throttle_interpolator

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 15,759 |
| Shell | 781 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- f1tenth_stack/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 1
- Forks at capture: 2
- Last updated: 2025-02-28T14:46:56Z
- Last pushed: 2023-06-08T02:07:09Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/f1tenth_system)
- [README](https://github.com/NVIDIA-ISAAC-ROS/f1tenth_system/blob/foxy-devel/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/f1tenth_system/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/f1tenth_system/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
