# aws-robotics/kinesisvideo-ros1

- Company: Amazon
- Account: aws-robotics
- Repository: https://github.com/aws-robotics/kinesisvideo-ros1
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:50:48+00:00

## Project purpose

The Kinesis Video Streams ROS package enables robots to stream video to the cloud for analytics, playback, and archival use. Out of the box, the nodes provided make it possible to encode & stream image data (e.g. video feeds and LIDAR scans) from a ROS “Image” topic to the cloud, enabling you to view the live video feed through the Kinesis Video Console, consume the stream via other applications, or perform intelligent analysis, face detection and face recognition using Amazon Rekognition.

## Why this project is used

ROS packages for facilitating the use of AWS cloud services.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, CMake
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: kinesis_video_streamer/src/main.cpp, kinesis_video_streamer/src/ros_stream_subscription_installer.cpp, kinesis_video_streamer/src/streamer.cpp, kinesis_video_streamer/src/subscriber_callbacks.cpp

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-robotics/kinesisvideo-ros1/blob/master/README.md
- README SHA: 461b6ae1ed6f3456ccabd275cc1774006a6c5b86
- Manifests: kinesis_video_msgs/CMakeLists.txt, kinesis_video_streamer/CMakeLists.txt
- Sampled source files: kinesis_video_streamer/src/main.cpp, kinesis_video_streamer/src/ros_stream_subscription_installer.cpp, kinesis_video_streamer/src/streamer.cpp, kinesis_video_streamer/src/subscriber_callbacks.cpp
- Git tree state: captured
- Evidence fingerprint: 2697c532a49394633a4375b30bdde0ed248de6e41b5f7cb3d347cf9d240eeb59

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
