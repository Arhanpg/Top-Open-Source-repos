# aws-robotics/kinesisvideo-ros1

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/kinesisvideo-ros1](https://github.com/aws-robotics/kinesisvideo-ros1)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-robotics/kinesisvideo-ros1/blob/master/README.md)
- README blob SHA: 461b6ae1ed6f3456ccabd275cc1774006a6c5b86
- Repository ID: 154743405
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS packages for facilitating the use of AWS cloud services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:16+00:00

### Short excerpt (up to 100 words)

> The Kinesis Video Streams ROS package enables robots to stream video to the cloud for analytics, playback, and archival use. Out of the box, the nodes provided make it possible to encode & stream image data (e.g. video feeds and LIDAR scans) from a ROS “Image” topic to the cloud, enabling you to view the live video feed through the Kinesis Video Console, consume the stream via other applications, or perform intelligent analysis, face detection and face recognition using Amazon Rekognition. The node will transmit standard `sensor_msgs::Image` data from ROS topics to Kinesis Video streams, optionally encoding the images as

### README headings

- kinesis_video_streamer
- Overview
- License
- Supported ROS Distributions
- Installation
- AWS Credentials
- Building from Source
- Launch Files
- Usage
- Run the node
- Configuration File and Parameters
- Node-wide configuration parameters
- Stream-specific configuration parameters
- Performance and Benchmark Results
- Node Details
- Subscribed Topics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 63,896 |
| CMake | 4,136 |

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
- Stars at capture: 21
- Forks at capture: 19
- Last updated: 2026-01-05T16:25:01Z
- Last pushed: 2022-02-08T21:49:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/kinesisvideo-ros1)
- [README](https://github.com/aws-robotics/kinesisvideo-ros1/blob/master/README.md)
- [Issues](https://github.com/aws-robotics/kinesisvideo-ros1/issues)
- [Releases](https://github.com/aws-robotics/kinesisvideo-ros1/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
