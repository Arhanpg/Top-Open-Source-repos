# aws-deepracer/aws-deepracer

- Company: Amazon
- Account: aws-deepracer
- Repository: https://github.com/aws-deepracer/aws-deepracer
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:45:48+00:00

## Project purpose

The AWS DeepRacer Evo vehicle is a 1/18th scale Wi-Fi enabled 4-wheel ackermann steering platform that features two RGB cameras and a LiDAR sensor. This repository contains the configuration and launch files to enable ROS Navigation Stack on AWS DeepRacer and control the vehicle using teleop-twist-keyboard, along with the core components to integrate AWS DeepRacer with ROS Navigation stack. For detailed information, see Introduction to the ROS Navigation stack using AWS DeepRacer Evo.

## Why this project is used

Simulation artifacts, core components and configuration files to integrate AWS DeepRacer device with ROS Navigation stack.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, C++, CMake, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: deepracer_gazebo/src/gazebo_ros_deepracer_drive.cpp, deepracer_bringup/launch/deepracer.launch.py, deepracer_bringup/launch/deepracer_navigation_dr.launch.py, deepracer_bringup/launch/deepracer_navigation_sim.launch.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-deepracer/aws-deepracer/blob/main/README.md
- README SHA: d4f0d705b4a9bc456049258e9f92b21f2ccba2c6
- Manifests: deepracer_bringup/CMakeLists.txt, deepracer_description/CMakeLists.txt, deepracer_gazebo/CMakeLists.txt, deepracer_nodes/cmdvel_to_servo_pkg/setup.py, deepracer_nodes/deepracer_interfaces_pkg/CMakeLists.txt, deepracer_nodes/enable_deepracer_nav_pkg/setup.py
- Sampled source files: deepracer_gazebo/src/gazebo_ros_deepracer_drive.cpp, deepracer_bringup/launch/deepracer.launch.py, deepracer_bringup/launch/deepracer_navigation_dr.launch.py, deepracer_bringup/launch/deepracer_navigation_sim.launch.py
- Git tree state: captured
- Evidence fingerprint: f8fe206bf864cc50323d21f0d08a012a014dbe660dd48ac0ad9a064a97238110

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
