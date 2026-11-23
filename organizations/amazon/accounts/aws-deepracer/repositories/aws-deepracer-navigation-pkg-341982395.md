# aws-deepracer/aws-deepracer-navigation-pkg

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/aws-deepracer-navigation-pkg](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg/blob/main/README.md)
- README blob SHA: 3fa9b6795344782a461978798b26411506ad21f3
- Repository ID: 341982395
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DeepRacer Navigation ROS package creates the deepracer_navigation_node that is responsible for collecting the RL model inference results and mapping it to the servo message based on the action space for the particular model selected.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:09:01+00:00

### Short excerpt (up to 100 words)

> The AWS DeepRacer navigation ROS package creates the `deepracer_navigation_node`, which is part of the core AWS DeepRacer application and launches from the `deepracer_launcher`. For more information about the application and the components, see the aws-deepracer-launcher repository. This node is responsible for collecting the reinforcement learning model inference results and mapping them to the servo message with throttle and steering angle values based on the action space for the particular model selected. The source code is released under Apache 2.0. Follow these instructions to install the AWS DeepRacer navigation package. The AWS DeepRacer device comes with all the prerequisite packages and

### README headings

- AWS DeepRacer navigation package
- Overview
- License
- Installation
- Prerequisites
- Downloading and building
- Usage
- Run the node
- Launch files
- Node details
- `deepracer_navigation_node`
- Subscribed topics
- Published topics
- Services
- Resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 30,036 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deepracer_navigation_pkg/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 4
- Forks at capture: 6
- Last updated: 2025-03-01T16:30:31Z
- Last pushed: 2021-05-27T18:25:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg)
- [README](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg/issues)
- [Releases](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
