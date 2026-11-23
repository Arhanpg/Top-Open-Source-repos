# aws-robotics/rosbag-uploader-ros1

- Company: Amazon
- GitHub account: [https://github.com/aws-robotics](https://github.com/aws-robotics)
- Mapping status: official-directory-listed
- Repository: [aws-robotics/rosbag-uploader-ros1](https://github.com/aws-robotics/rosbag-uploader-ros1)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-robotics/rosbag-uploader-ros1/blob/master/README.md)
- README blob SHA: 72f78a67f6afe7e09c7c8eb5091988240756930b
- Repository ID: 221550863
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS packages for uploading rosbags to AWS cloud services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:31:30+00:00

### Short excerpt (up to 100 words)

> This repository contains ROS nodes for recording rosbags and uploading them to Amazon S3. There are three nodes under this repository: the `duration_recorder`, the `rolling_recorder`, and the `s3_file_uploader`. See the READMEs under the `rosbag_cloud_recorders` and `s3_uploader` directories for more details. - `duration_recorder` - This node provides an action interface to record rosbags for a specified duration. Once that duration is complete the rosbag files are uploaded to S3. - `rolling_recorder` - This node provides an action interface for uploading the past *x* minutes of rosbag files. - `s3_file_uploader` - This node is in the `s3_file_uploader` package and provides an action

### README headings

- Rosbag Cloud Recorders
- Build status
- License
- Installation
- Building from Source
- Running Tests
- Running
- Bugs & Feature Requests

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 197,012 |
| Python | 48,620 |
| CMake | 17,116 |
| TypeScript | 925 |
| Shell | 239 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- file_uploader_msgs/CMakeLists.txt (capture: captured)
- integ_tests/CMakeLists.txt (capture: captured)
- recorder_msgs/CMakeLists.txt (capture: captured)
- rosbag_cloud_recorders/CMakeLists.txt (capture: captured)
- s3_common/CMakeLists.txt (capture: captured)
- s3_file_uploader/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 31
- Forks at capture: 10
- Last updated: 2025-09-29T10:00:42Z
- Last pushed: 2022-02-08T16:17:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-robotics/rosbag-uploader-ros1)
- [README](https://github.com/aws-robotics/rosbag-uploader-ros1/blob/master/README.md)
- [Issues](https://github.com/aws-robotics/rosbag-uploader-ros1/issues)
- [Releases](https://github.com/aws-robotics/rosbag-uploader-ros1/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
