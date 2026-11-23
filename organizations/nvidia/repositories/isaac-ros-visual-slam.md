# Isaac ROS Visual SLAM

- **Company:** NVIDIA
- **GitHub account:** [NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- **Repository:** [NVIDIA-ISAAC-ROS/isaac_ros_visual_slam](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `a9cc0e703c6ace4d7324c0b97b1b834d71b6d392`

## Project overview

A GPU-accelerated ROS 2 package for visual simultaneous localization and mapping (VSLAM). It uses one or more stereo cameras and optionally an IMU to estimate robot odometry for navigation, particularly where GPS is unavailable or intermittent.

## Features and capabilities documented by the README

- Uses stereo image pairs to match key points and estimate depth from the camera baseline, then tracks key points across frames to estimate 3D camera motion and odometry.
- Combines visual odometry with IMU-based visual-inertial odometry when distinctive visual features are limited or absent.
- Builds a map of tracked key points and uses loop closure to recognize previously visited areas and reduce map-estimation uncertainty.
- Supports additional or differently oriented stereo cameras to provide concurrent visual odometry estimates that can complement LIDAR and wheel odometry.
- The README identifies the ROS 2 package `isaac_ros_cuvslam` and interface package `isaac_ros_visual_slam_interfaces`.
- Links to quickstart, examples, coordinate-frame, troubleshooting and API documentation.

## Technology stack

ROS 2 package; NVIDIA cuVSLAM; stereo camera input; optional IMU; GPU acceleration. The README names the `isaac_ros_cuvslam` and `isaac_ros_visual_slam_interfaces` packages but does not enumerate the implementation languages or all hardware/software dependencies. It lists Jetson AGX Xavier (aarch64) in its benchmark table.

## Getting started

Use the official Isaac ROS Visual SLAM documentation and package quickstart linked from the README. Check the version-specific Isaac ROS release documentation for supported camera, IMU, ROS 2, GPU and Jetson configurations before deployment.

## Lifecycle, compatibility and operational considerations

The README reports one KITTI benchmark comparison: VSLAM runtime 0.007 s, translation error 0.94%, rotation error 0.0019 deg/m on Jetson AGX Xavier aarch64, compared with ORB-SLAM2 at 0.06 s and 1.15% translation error on a different x86_64 platform. These are upstream-reported results, not an independently reproduced apples-to-apples benchmark. The inspected README includes an update dated 16 November 2026 for Isaac ROS 5.1.0 compatibility/integration.

## Evaluation guidance

Review the release-specific installation documentation, exact software/hardware requirements, dependency manifests, licence terms and security guidance before using the project in production. Benchmark claims should be tested on the actual target hardware and workload. This dossier is based on the upstream README; it is not a full source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam/releases)

*Evidence note: the README blob SHA identifies the upstream version inspected. Details not supported by the README are left unspecified or directed to version-specific documentation.*
