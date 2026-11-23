# aws-deepracer/aws-deepracer-webserver-pkg

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/aws-deepracer-webserver-pkg](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg/blob/main/README.md)
- README blob SHA: 1338f89b262f96b2ca7c3fd07e59b706e1ae3bf9
- Repository ID: 341985928
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The DeepRacer Web Server ROS package creates the web_publisher_node which launches a Flask application as a background thread and creates service clients and subscribers for all the services and topics that are required by the APIs called from the DeepRacer vehicle console.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:23+00:00

### Short excerpt (up to 100 words)

> The AWS DeepRacer web server ROS package creates the `webserver_publisher_node`, which is part of the core AWS DeepRacer application and launches from the `deepracer_launcher`. For more details about the application and its components, see the `aws-deepracer-launcher` repository. This node launches a Flask application as a background thread and creates service clients and subscribers for all the services and topics required by the APIs called from the AWS DeepRacer vehicle console. This node acts as an interface between the AWS DeepRacer device console and the backend ROS services. The source code is released under Apache 2.0. Follow these steps to install

### README headings

- AWS DeepRacer web server package
- Overview
- License
- Installation
- Prerequisites
- Downloading and building
- Usage
- Running the node
- Launch files
- Node details
- `webserver_publisher_node`
- Subscribed topics
- Published topics
- Service clients
- Resources

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 163,314 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- webserver_pkg/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 7
- Last updated: 2021-10-30T02:34:47Z
- Last pushed: 2021-07-28T21:16:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg)
- [README](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg/issues)
- [Releases](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
