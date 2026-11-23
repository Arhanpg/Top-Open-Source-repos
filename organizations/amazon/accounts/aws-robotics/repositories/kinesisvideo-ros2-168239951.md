# aws-robotics/kinesisvideo-ros2

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/kinesisvideo-ros2](https://github.com/aws-robotics/kinesisvideo-ros2)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-robotics/kinesisvideo-ros2/blob/master/README.md)
- README blob SHA: 4b4401581a7c7f9d9e32d13bc9b7a7db4bfac958
- Repository ID: 168239951
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS packages for facilitating the use of AWS cloud services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:17+00:00

### Short excerpt (up to 100 words)

> The Kinesis Video Streams ROS package enables robots to stream video to the cloud for analytics, playback, and archival use. Out of the box, the nodes provided make it possible to encode & stream image data (e.g. video feeds and LIDAR scans) from a ROS “Image” topic to the cloud, enabling you to view the live video feed through the Kinesis Video Console, consume the stream via other applications, or perform intelligent analysis, face detection and face recognition using Amazon Rekognition. The node will transmit standard `sensor_msgs::msg::Image` data from ROS topics to Kinesis Video streams, optionally encoding the images as

### README headings

- kinesis_video_streamer
- Overview
- License
- Supported ROS2 Distributions
- Installation
- AWS Credentials
- Building from Source
- Usage
- Run the node
- Configuration File and Parameters
- Node-wide configuration parameters
- Stream-specific configuration parameters
- Node Details
- Subscribed Topics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 77,743 |
| Python | 4,046 |
| CMake | 4,009 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- kinesis_video_msgs/CMakeLists.txt (capture: captured)
- kinesis_video_streamer/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 22
- Forks at capture: 7
- Last updated: 2024-04-14T03:07:02Z
- Last pushed: 2022-02-08T21:51:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/kinesisvideo-ros2)
- [README](https://github.com/aws-robotics/kinesisvideo-ros2/blob/master/README.md)
- [Issues](https://github.com/aws-robotics/kinesisvideo-ros2/issues)
- [Releases](https://github.com/aws-robotics/kinesisvideo-ros2/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
