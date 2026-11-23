# aws-robotics/health-metrics-collector-ros2

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/health-metrics-collector-ros2](https://github.com/aws-robotics/health-metrics-collector-ros2)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-robotics/health-metrics-collector-ros2/blob/master/README.md)
- README blob SHA: 41d8ad8c6e578a0b8e26655b7f42ce23fe67cadb
- Repository ID: 200933258
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS2 node that collects metrics about system resource consumption and publishes them to a topic to be emitted to CloudWatch Metrics.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:10+00:00

### Short excerpt (up to 100 words)

> This `health_metric_collector` ROS node collects system metrics and publishes them to `/metrics` topic. The `cloudwatch_metrics_collector` node is subscribed to this topic and will publish the metrics to AWS CloudWatch when it is instantiated. **Keywords**: ROS, ROS2, AWS, CloudWatch, Metrics The source code is released under an [Apache 2.0]. **Author**: AWS RoboMaker<br/> **Affiliation**: [Amazon Web Services (AWS)]<br/> RoboMaker cloud extensions rely on third-party software licensed under open-source licenses and are provided for demonstration purposes only. Incorporation or use of RoboMaker cloud extensions in connection with your production workloads or commercial product(s) or devices may affect your legal rights or obligations under

### README headings

- health_metric_collector
- Overview
- License
- Supported ROS Distributions
- Installation
- AWS Credentials
- Building from Source
- Launch Files
- Usage
- Run the node
- Running the sample application
- Configuration file and Parameters
- Supported Metrics Types
- Node
- health_metric_collector
- Published Topics
- Subscribed Topics
- Services

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 22,920 |
| CMake | 2,957 |
| Python | 2,940 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- health_metric_collector/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 16
- Forks at capture: 1
- Last updated: 2024-01-21T04:26:22Z
- Last pushed: 2022-02-08T21:43:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/health-metrics-collector-ros2)
- [README](https://github.com/aws-robotics/health-metrics-collector-ros2/blob/master/README.md)
- [Issues](https://github.com/aws-robotics/health-metrics-collector-ros2/issues)
- [Releases](https://github.com/aws-robotics/health-metrics-collector-ros2/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
