# aws-deepracer/aws-deepracer-ctrl-pkg

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/aws-deepracer-ctrl-pkg](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg/blob/main/README.md)
- README blob SHA: 94742cd1e111c6edd6c2522cfdd993ace31b7044
- Repository ID: 341981469
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DeepRacer Control ROS package creates the ctrl_node that manages the different mode of operation of the device [manual, autonomous, calibration].

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:33+00:00

### Short excerpt (up to 100 words)

> The AWS DeepRacer control ROS package creates the `ctrl_node`, which is part of the core AWS DeepRacer application and launches from the `deepracer_launcher`. More details about the application and the components can be found in the `aws-deepracer-launcher` repository. This is a main node with services exposed to be used by webserver backend API calls. This node manages the device's different modes [manual, autonomous, calibration]. It allows us to maintain the device in a single mode at any point of time so that the overlapping functionalities (such as servo messages) do not conflict with each other. Also, this can be extended

### README headings

- AWS DeepRacer control package
- Overview
- License
- Installation
- Prerequisites
- Downloading and building
- Usage
- Run the node
- Launch files
- Node Details
- `ctrl_node`
- Subscribed topics
- Published topics
- Service clients
- Services
- Resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 81,447 |
| Python | 1,534 |
| CMake | 1,497 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- ctrl_pkg/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 5
- Last updated: 2023-12-01T15:10:42Z
- Last pushed: 2021-06-12T23:23:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg)
- [README](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg/issues)
- [Releases](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
