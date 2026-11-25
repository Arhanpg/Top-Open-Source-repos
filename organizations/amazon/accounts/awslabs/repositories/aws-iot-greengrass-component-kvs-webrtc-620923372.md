# awslabs/aws-iot-greengrass-component-kvs-webrtc

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-iot-greengrass-component-kvs-webrtc](https://github.com/awslabs/aws-iot-greengrass-component-kvs-webrtc)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/aws-iot-greengrass-component-kvs-webrtc/blob/main/README.md)
- README blob SHA: 80580c9fe2f342861a7400c905672184e49c4b1d
- README bytes captured: 26851
- README truncated at capture limit: False
- Repository ID: 620923372
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:15:46+00:00

### Short excerpt (up to 300 words)

> sudo v4l2loopback-ctl set-fps /dev/video0 sudo usermod -aG docker A working installation of

### README headings

- AWS IoT Greengrass V2 Component to send video over Kinesis Video Streams with WebRTC
- Prerequisites
- Part 1 - Validate Setup, connections, drivers, etc.
- ioctl: VIDIOC_ENUM_FMT
- Type: Video Capture
- [0]: 'MJPG' (Motion-JPEG, compressed)
- Size: Discrete 1920x1080
- Interval: Discrete 0.017s (60.000 fps)
- [1]: 'YUYV' (YUYV 4:2:2)
- Size: Discrete 1920x1080
- Interval: Discrete 0.017s (60.000 fps)
- change this command if necessary for different group or GGv2 user
- verify the phrase "Hello from Docker!" in the output
- modify the user if your GGv2 installation has a different user account
- Part 2 - Build the Docker Container and test locally
- ENV TZ=America/Los_Angeles
- example
- EXAMPLE - OPTIONAL - transfer image to target
- transfer the image to the target...
- for example, using scp
- ON THE TARGET
- use values from downloaded credentials
- if using cloud9 or a role, you may also have a session token
- Part 3 - Package and Publish as GGv2 Component
- keeping a local copy of artifacts is generally helpful
- example
- export component_name=com.example.kvs_master
- export component_version=1.0.0
- use the name of your docker container created in Part 1
- example

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: ignore ERROR about pipeline not wanting to run

> sudo v4l2loopback-ctl set-fps /dev/video0

### Getting started and usage: modify the user if your GGv2 installation has a different user account

> sudo usermod -aG docker

### Technology and requirements: Prerequisites

> A working installation of

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Dockerfile | 1,895 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 7
- Forks at capture: 2
- Last updated: 2026-03-24T16:22:53Z
- Last pushed: 2023-03-29T16:45:11Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-iot-greengrass-component-kvs-webrtc)
- [README](https://github.com/awslabs/aws-iot-greengrass-component-kvs-webrtc/blob/main/README.md)
- [Issues](https://github.com/awslabs/aws-iot-greengrass-component-kvs-webrtc/issues)
- [Releases](https://github.com/awslabs/aws-iot-greengrass-component-kvs-webrtc/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
