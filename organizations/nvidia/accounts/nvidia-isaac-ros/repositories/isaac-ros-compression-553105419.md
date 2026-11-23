# NVIDIA-ISAAC-ROS/isaac_ros_compression

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS)
- Mapping status: official-project-linked
- Repository: [NVIDIA-ISAAC-ROS/isaac_ros_compression](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_compression)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_compression/blob/main/README.md)
- README blob SHA: 680fc924e10274da13051349953c0ca33225dad9
- Repository ID: 553105419
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

NVIDIA-accelerated data compression

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:32:12+00:00

### Short excerpt (up to 100 words)

> NVIDIA-accelerated data compression. Isaac ROS Compression provides H.264 image encoder and decoder that leverages the specialized hardware in NVIDIA GPUs and the The `isaac_ros_h264_encoder` package can compress an image into H.264 data using the NVENC. The `isaac_ros_h264_decoder` package can decode the H.264 data into original images using the NVDEC. Image compression reduces the data footprint of images when written to storage or transmitted between computers. A 1080p camera at 30fps produces 177MB/s of data; image compression reduces this by approximately 10 times to 17MB/s of data, reducing the throughput needed to send this to another computer or write out to

### README headings

- Isaac ROS Compression
- Overview
- Performance
- Documentation
- Packages
- Latest

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 188,460 |
| C++ | 127,198 |
| CMake | 13,569 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- codec/CMakeLists.txt (capture: captured)
- isaac_ros_h264_decoder/CMakeLists.txt (capture: captured)
- isaac_ros_h264_encoder/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 73
- Forks at capture: 16
- Last updated: 2026-09-22T02:12:42Z
- Last pushed: 2026-11-18T06:56:55Z
- Topics: compression, gpu, jetson, nvidia, ros2, ros2-humble

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_compression)
- [README](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_compression/blob/main/README.md)
- [Issues](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_compression/issues)
- [Releases](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_compression/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
