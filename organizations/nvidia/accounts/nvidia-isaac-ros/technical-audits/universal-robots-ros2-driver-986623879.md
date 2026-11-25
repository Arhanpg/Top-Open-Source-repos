# NVIDIA-ISAAC-ROS/Universal_Robots_ROS2_Driver

- Company: NVIDIA
- Account: NVIDIA-ISAAC-ROS
- Repository: https://github.com/NVIDIA-ISAAC-ROS/Universal_Robots_ROS2_Driver
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:48:41+00:00

## Project purpose

Universal Robots has become a dominant supplier of lightweight, robotic manipulators for industry, as well as for scientific research and education.

## Why this project is used

Universal Robots ROS2 driver supporting CB3 and e-Series

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Python, CMake, Shell, Batchfile, Emacs Lisp
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: ur_calibration/src/calibration.cpp, ur_calibration/src/calibration_consumer.cpp, ur_calibration/src/calibration_correction.cpp, ur_controllers/src/force_mode_controller.cpp

## Setup and usage

- Getting Started: For getting started, you'll basically need three steps:
- Getting Started: 1. **Install the driver**
- Getting Started: sudo apt-get install ros-rolling-ur
- Getting Started: See the installation instructions for more details and source-build instructions.
- Getting Started: 2. **Start & Setup the robot**. Once you've installed the driver, [setup the
- Getting Started: robot](https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_robot_driver/ur_robot_driver/doc/installation/robot_setup.html)
- Getting Started: to be able to communicate with this driver correctly.
- Getting Started: Please do this step carefully and extract the calibration as explained

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/NVIDIA-ISAAC-ROS/Universal_Robots_ROS2_Driver/blob/main/README.md
- README SHA: 7f6d8ce6e555be87401348ceb41a0976e3f94e85
- Manifests: ur/CMakeLists.txt, ur_calibration/CMakeLists.txt, ur_controllers/CMakeLists.txt, ur_dashboard_msgs/CMakeLists.txt, ur_moveit_config/CMakeLists.txt, ur_robot_driver/CMakeLists.txt
- Sampled source files: ur_calibration/src/calibration.cpp, ur_calibration/src/calibration_consumer.cpp, ur_calibration/src/calibration_correction.cpp, ur_controllers/src/force_mode_controller.cpp
- Git tree state: captured
- Evidence fingerprint: 7f754d399ab77efe50de2cc978b0e76395e80cfe1288225148eedba97aa2b34f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
