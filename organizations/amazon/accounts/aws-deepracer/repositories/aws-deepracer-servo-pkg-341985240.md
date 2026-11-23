# aws-deepracer/aws-deepracer-servo-pkg

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/aws-deepracer-servo-pkg](https://github.com/aws-deepracer/aws-deepracer-servo-pkg)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/aws-deepracer-servo-pkg/blob/main/README.md)
- README blob SHA: 388451b780d8bd96e7ceb2dee841ccc4cb4b6aae
- Repository ID: 341985240
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DeepRacer Servo ROS package creates the servo_node that is responsible to map the input servo throttle and steering angle messages to raw PWM values to move the car.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:09:08+00:00

### Short excerpt (up to 100 words)

> The AWS DeepRacer servo ROS package creates the `servo_node`, which is part of the core AWS DeepRacer application and launches from the `deepracer_launcher`. For more information about the application and the components, see the aws-deepracer-launcher repository. This node is responsible for mapping the input servo throttle and steering angle ratios to raw PWM values and writing that to the buffer so that car moves accordingly. It also sets and gets the [min, mid, max, polarity] calibration values for steering and throttle and the tail light LED PWM values. The source code is released under Apache 2.0. Follow these steps to

### README headings

- AWS DeepRacer servo package
- Overview
- License
- Installation
- Prerequisites
- Downloading and building
- Usage
- Run the node
- Launch files
- Node details
- servo_node
- Subscribed topics
- Services
- Resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 57,572 |
| CMake | 1,693 |
| Python | 1,538 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- servo_pkg/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 7
- Last updated: 2024-10-02T09:16:59Z
- Last pushed: 2021-11-08T22:39:51Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/aws-deepracer-servo-pkg)
- [README](https://github.com/aws-deepracer/aws-deepracer-servo-pkg/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/aws-deepracer-servo-pkg/issues)
- [Releases](https://github.com/aws-deepracer/aws-deepracer-servo-pkg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
