# aws-deepracer/ros-kvs-streamer

- Company: Amazon
- GitHub account: [https://github.com/aws-deepracer](https://github.com/aws-deepracer)
- Mapping status: official-directory-listed
- Repository: [aws-deepracer/ros-kvs-streamer](https://github.com/aws-deepracer/ros-kvs-streamer)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-deepracer/ros-kvs-streamer/blob/main/README.md)
- README blob SHA: f45372f91b113dcd3e3eca581e3dd90b282d1939
- Repository ID: 501444019
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ROS1 kinesis video streamer

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:15:33+00:00

### Short excerpt (up to 100 words)

> Generic ROS1 kinesis video streamer The source code is released under Apache 2.0. * ROS KVS streamer Under the condition that RoboMaker team does not bloom release these packages for Ubuntu20:04 and ROS Noetic, they have to be built from source. .git and .github are removed to track these code in code.amazon.com. Otherwise, these packages will be track as sudmodules. https://github.com/aws-robotics/utils-common at commit b70e9416968ca5a56fd263ff9c96c80793a7230f ROS AWS Utils Common Library https://github.com/aws-robotics/utils-ros1 at commit d4d64f73727149fd8885f13581a74d5ca6dcfb6c AWS Utils Library for ROS1 with patch https://github.com/aws-robotics/utils-ros1/pull/36 to support ROS Noetic with Ubuntu20:04 SDK https://github.com/aws-robotics/kinesisvideo-encoder-common at commit b798a06cca43891170d33da3aa329648c864a418 ROS H264 Video Encoding Library for Amazon Kinesis

### README headings

- We have made a difficult decision of ceasing active development on this repo as of Jul 2022.
- 1. ROS KVS Stramer
- 1.1 License
- 1.2 Resources
- 2. Open source packages from github
- 2.1 utils-common
- 2.2 utils-ros1
- 2.3 kinesisvideo-encoder-common
- 2.4 kinesisvideo-encoder-ros1
- 2.5 kinesisvideo-common
- 2.6 kinesisvideo-ros1
- 3. Setup
- 3.1 setup
- 3.2 aws configure
- 4. Launch and run
- 4.1 using launch file
- 4.2 using python script
- start using static method #
- stop using static method #
- using class instantiation #
- start
- stop
- 5. checkout kvs stream

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 33,095 |
| Shell | 1,871 |
| CMake | 466 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- ros_kvs_streamer/CMakeLists.txt (capture: captured)
- ros_kvs_streamer/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2023-01-27T22:52:34Z
- Last pushed: 2022-07-22T19:25:56Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-deepracer/ros-kvs-streamer)
- [README](https://github.com/aws-deepracer/ros-kvs-streamer/blob/main/README.md)
- [Issues](https://github.com/aws-deepracer/ros-kvs-streamer/issues)
- [Releases](https://github.com/aws-deepracer/ros-kvs-streamer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
