# aws-robotics/cloudwatchlogs-ros1

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/cloudwatchlogs-ros1](https://github.com/aws-robotics/cloudwatchlogs-ros1)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-robotics/cloudwatchlogs-ros1/blob/master/README.md)
- README blob SHA: 0cbc0279b0d105a8491980fb71ea4e747c6668a4
- Repository ID: 154743369
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS packages for facilitating the use of AWS cloud services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:51+00:00

### Short excerpt (up to 100 words)

> The **`cloudwatch_logger`** node enables logs generated in a ROS system to get sent to AWS CloudWatch Logs. Out of the box, this node provides the ability to subscribe to the **`/rosout_agg`** (rosout aggregated) topic, which all logs using the ROS logging framework will be published to, and sends logs to the AWS CloudWatch Logs service. Logs can be sent to AWS CloudWatch Logs selectively based on log severity. The **`cloudwatch_logger`** node can also subscribe to other topics if logs are not sent to **`/rosout_agg`**, and it is able to unsubscribe to the rosout_agg topic for getting logs. The **`cloudwatch_logger`** node

### README headings

- cloudwatch_logger
- Overview
- License
- Supported ROS Distributions
- Installation
- AWS Credentials
- Building from Source
- Launch Files
- Usage
- Run the node
- Send a test log message
- Verify that the test log message was successfully sent to CloudWatch Logs
- Configuration File and Parameters
- Advanced Configuration Parameters
- Node
- cloudwatch_logger
- Subscribed Topics
- Published Topics
- Services

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 67,705 |
| CMake | 5,050 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- cloudwatch_logger/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 16
- Forks at capture: 9
- Last updated: 2026-01-20T02:29:23Z
- Last pushed: 2022-02-08T21:39:36Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/cloudwatchlogs-ros1)
- [README](https://github.com/aws-robotics/cloudwatchlogs-ros1/blob/master/README.md)
- [Issues](https://github.com/aws-robotics/cloudwatchlogs-ros1/issues)
- [Releases](https://github.com/aws-robotics/cloudwatchlogs-ros1/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
