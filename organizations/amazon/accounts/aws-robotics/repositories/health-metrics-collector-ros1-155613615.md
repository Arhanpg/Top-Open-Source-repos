# aws-robotics/health-metrics-collector-ros1

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/health-metrics-collector-ros1](https://github.com/aws-robotics/health-metrics-collector-ros1)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-robotics/health-metrics-collector-ros1/blob/master/README.md)
- README blob SHA: 497e8fec103b9e3d68e7f54ff93dd6b22e4f1a7e
- Repository ID: 155613615
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This is a node for ROS1 that collects metrics about cpu usage and publishes them to a topic to be pushed to CloudWatch Metrics.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:57+00:00

### Short excerpt (up to 100 words)

> This `health_metric_collector` ROS node collects system metrics and publishes them to `/metrics` topic. The `cloudwatch_metrics_collector` node is subscribed to this topic and will publish the metrics to AWS CloudWatch when it is instantiated. **Keywords**: ROS, AWS, CloudWatch, Metrics The source code is released under an [Apache 2.0]. **Author**: AWS RoboMaker<br/> **Affiliation**: [Amazon Web Services (AWS)]<br/> RoboMaker cloud extensions rely on third-party software licensed under open-source licenses and are provided for demonstration purposes only. Incorporation or use of RoboMaker cloud extensions in connection with your production workloads or commercial product(s) or devices may affect your legal rights or obligations under the

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
- Performance and Benchmark Results
- Node
- health_metric_collector
- Published Topics
- Subscribed Topics
- Services

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 22,348 |
| CMake | 2,699 |

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
- Stars at capture: 10
- Forks at capture: 9
- Last updated: 2023-01-28T03:11:18Z
- Last pushed: 2022-02-08T21:42:47Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/health-metrics-collector-ros1)
- [README](https://github.com/aws-robotics/health-metrics-collector-ros1/blob/master/README.md)
- [Issues](https://github.com/aws-robotics/health-metrics-collector-ros1/issues)
- [Releases](https://github.com/aws-robotics/health-metrics-collector-ros1/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
