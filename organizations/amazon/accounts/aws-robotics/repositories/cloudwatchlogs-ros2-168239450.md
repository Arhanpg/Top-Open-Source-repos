# aws-robotics/cloudwatchlogs-ros2

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/cloudwatchlogs-ros2](https://github.com/aws-robotics/cloudwatchlogs-ros2)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-robotics/cloudwatchlogs-ros2/blob/master/README.md)
- README blob SHA: 8dd768634f603acf26444fefa8a912373dec3773
- Repository ID: 168239450
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS packages for facilitating the use of AWS cloud services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:52+00:00

### Short excerpt (up to 100 words)

> The **`cloudwatch_logger`** node enables logs generated in a ROS system to get sent to AWS CloudWatch Logs. Out of the box, this node provides the ability to subscribe to the **`/rosout`** topic, which all logs using the ROS logging framework will be published to by default, and sends logs to the AWS CloudWatch Logs service. Logs can be sent to AWS CloudWatch Logs selectively based on log severity. The **`cloudwatch_logger`** node can also subscribe to other topics if logs are not sent to **`/rosout`**, and it is able to unsubscribe from the **`/rosout`** topic if desired. The **`cloudwatch_logger`** node wraps

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
| C++ | 63,553 |
| CMake | 3,899 |
| Python | 2,540 |

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
- Stars at capture: 7
- Forks at capture: 4
- Last updated: 2024-01-17T07:17:53Z
- Last pushed: 2022-02-08T21:40:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/cloudwatchlogs-ros2)
- [README](https://github.com/aws-robotics/cloudwatchlogs-ros2/blob/master/README.md)
- [Issues](https://github.com/aws-robotics/cloudwatchlogs-ros2/issues)
- [Releases](https://github.com/aws-robotics/cloudwatchlogs-ros2/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
