# aws-deepracer/aws-deepracer-i2c-pkg

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/aws-deepracer-i2c-pkg](https://github.com/aws-deepracer/aws-deepracer-i2c-pkg)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/aws-deepracer-i2c-pkg/blob/main/README.md)
- README blob SHA: a2d9aa4b16de6d0a5cd51274fa9c4d4380f543a9
- Repository ID: 341983985
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DeepRacer I2C ROS package creates the battery_node that is responsible for providing the vehicle battery level information.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:39+00:00

### Short excerpt (up to 100 words)

> The AWS DeepRacer I2C ROS package creates the `battery_node`, which is part of the core AWS DeepRacer application and launches from the `deepracer_launcher`. For more information about the application and the components, see the `aws-deepracer-launcher` repository This node is responsible for providing the vehicle battery level information. It provides functions to read the battery level values from the I2C bus and return the corresponding level information. The source code is released under Apache 2.0 (https://aws.amazon.com/apache-2-0/). Follow these steps to install the AWS DeepRacer I2C package. The AWS DeepRacer device comes with all the prerequisite packages and libraries installed to run

### README headings

- AWS DeepRacer I2C package
- Overview
- License
- Installation
- Prerequisites
- Downloading and building
- Usage
- Run the node
- Launch files
- Node details
- `battery_node`
- Services
- Resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 11,100 |
| Python | 1,538 |
| CMake | 1,504 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- i2c_pkg/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 4
- Last updated: 2021-10-30T02:38:59Z
- Last pushed: 2024-04-14T16:53:14Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/aws-deepracer-i2c-pkg)
- [README](https://github.com/aws-deepracer/aws-deepracer-i2c-pkg/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/aws-deepracer-i2c-pkg/issues)
- [Releases](https://github.com/aws-deepracer/aws-deepracer-i2c-pkg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
