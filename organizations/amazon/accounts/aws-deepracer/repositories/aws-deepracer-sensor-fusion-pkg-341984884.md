# aws-deepracer/aws-deepracer-sensor-fusion-pkg

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/aws-deepracer-sensor-fusion-pkg](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg/blob/main/README.md)
- README blob SHA: b74854d5685020fe5cc7517fd353925a41eaf2f5
- Repository ID: 341984884
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DeepRacer Sensor Fusion ROS package creates the sensor_fusion_node that is responsible for collecting the messages from all the sensors (Camera+LiDAR) and publish the combined sensor message.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:09:07+00:00

### Short excerpt (up to 100 words)

> The AWS DeepRacer sensor fusion ROS package creates the `sensor_fusion_node`, which is part of the core AWS DeepRacer application and launches from the `deepracer_launcher`. For more information about the application and the components, see the aws-deepracer-launcher repository. This node is responsible for collecting the messages from all the sensors and publishing the combined sensor message. It provides services and functions to subscribe to the LiDAR and camera messages, configure LiDAR, publish a combined sensor message, and publish an overlay message with the LiDAR data overlaid on top of the camera image. The source code is released under Apache 2.0. Follow

### README headings

- AWS DeepRacer sensor fusion package
- Overview
- License
- Installation
- Prerequisites
- Downloading and building
- Usage
- Run the node
- Launch files
- Node details
- `sensor_fusion_node`
- Subscribed topics
- Published topics
- Services
- Resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 55,450 |
| CMake | 1,766 |
| Python | 1,570 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- sensor_fusion_pkg/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 10
- Last updated: 2024-12-19T10:57:20Z
- Last pushed: 2022-10-28T18:22:03Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg)
- [README](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg/issues)
- [Releases](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
