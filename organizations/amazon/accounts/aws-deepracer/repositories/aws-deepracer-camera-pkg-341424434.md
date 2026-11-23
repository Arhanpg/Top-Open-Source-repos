# aws-deepracer/aws-deepracer-camera-pkg

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/aws-deepracer-camera-pkg](https://github.com/aws-deepracer/aws-deepracer-camera-pkg)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/aws-deepracer-camera-pkg/blob/main/README.md)
- README blob SHA: f68a5a5566115627733ba83d618f4cef34de8e96
- Repository ID: 341424434
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DeepRacer Camera ROS package creates the camera_node that is responsible for reading the raw data from the one/two cameras connected to the USB slots at the front of the AWS DeepRacer device and publishing them as CameraMsg.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:32+00:00

### Short excerpt (up to 100 words)

> The AWS DeepRacer camera ROS package creates the `camera_node`, which is part of the core AWS DeepRacer application and launches from the `deepracer_launcher`. For more information about the application and the components, see the `aws-deepracer-launcher` repository. This node is responsible for reading the raw data from the one or two cameras connected to the USB slots at the front of the device and publishing them as `CameraMsg` at the rate at which they are read. The source code is released under Apache 2.0 (https://aws.amazon.com/apache-2-0/). Follow these steps to install the AWS DeepRacer camera package. The AWS DeepRacer device comes with

### README headings

- AWS DeepRacer camera package
- Overview
- License
- Installation
- Prerequisites
- Downloading and building
- Usage
- Run the node
- Activating the camera image publisher using the CLI
- Launch files
- Configuration file and parameters
- Node details
- `camera_node`
- Published topics
- Services
- Resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 11,360 |
| CMake | 1,795 |
| Python | 1,622 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- camera_pkg/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 6
- Last updated: 2025-08-22T11:36:51Z
- Last pushed: 2022-10-28T18:16:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/aws-deepracer-camera-pkg)
- [README](https://github.com/aws-deepracer/aws-deepracer-camera-pkg/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/aws-deepracer-camera-pkg/issues)
- [Releases](https://github.com/aws-deepracer/aws-deepracer-camera-pkg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
