# aws/aws-iot-device-sdk-arduino-yun

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-iot-device-sdk-arduino-yun](https://github.com/aws/aws-iot-device-sdk-arduino-yun)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/aws-iot-device-sdk-arduino-yun/blob/master/README.md)
- README blob SHA: 84abbdcf7985399504b0b2e607571a92a17a2cd0
- README bytes captured: 78337
- README truncated at capture limit: False
- Repository ID: 43451986
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SDK for connecting to AWS IoT from an Arduino Yún. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T00:55:17+00:00

### Short excerpt (up to 300 words)

> The AWS-IoT-Arduino-Yún-SDK allows developers Before proceeding to the

### README headings

- [ARCHIVED] AWS IoT Arduino Yún SDK
- What is AWS IoT Arduino Yún SDK
- Overview
- MQTT connection
- Thing shadow
- Credentials
- X.509 certificate
- IAM credentials
- Installation
- Download AWS-IoT-Arduino-Yún-SDK
- Set up your Arduino Yún Board
- Installation on Mac OS/Linux
- Installation on Windows
- API documentation
- IoT\_Error\_t setup(const char\* client\_id, bool clean\_session, MQTTv\_t MQTT\_version, bool useWebsocket)
- IoT\_Error\_t config(const char\* host, unsigned int port, const char\* cafile\_path, const char\* keyfile\_path, const char\* certfile_path)
- IoT\_Error\_t configWss(const char\* host, unsigned int port, const char\* cafile\_path)
- IoT\_Error\_t configBackoffTiming(unsigned int baseReconnectQuietTimeSecond, unsigned int maxReconnectQuietTimeSecond, unsigned int stableConnectionTimeSecond)
- IoT\_Error\_t configOfflinePublishQueue(unsigned int queueSize, DropBehavior\_t behavior)
- IoT\_Error\_t configDrainingInterval(float numberOfSeconds)
- IoT\_Error\_t connect(unsigned int keepalive\_interval)
- IoT\_Error\_t publish(const char\* topic, const char\* payload, unsigned int payload\_len, unsigned int qos, bool retain)
- IoT\_Error\_t subscribe(const char\* topic, unsigned int qos, message\_callback cb)
- IoT\_Error\_t unsubscribe(const char\* topic)
- IoT\_Error\_t yield()
- IoT\_Error\_t disconnect()
- IoT\_Error\_t shadow\_init(const char\* thingName)
- IoT\_Error\_t shadow\_update(const char\* thingName, const char* payload, unsigned int payload_len, message\_callback cb, unsigned int timeout)
- IoT\_Error\_t shadow\_get(const char\* thingName, message\_callback cb, unsigned int timeout)
- IoT\_Error\_t shadow\_delete(const char\* thingName, message\_callback cb, unsigned int timeout)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: What is AWS IoT Arduino Yún SDK

> The AWS-IoT-Arduino-Yún-SDK allows developers

### Getting started and usage: Installation on Mac OS/Linux

> Before proceeding to the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 92,756 |
| C++ | 45,664 |
| C | 8,920 |
| Shell | 6,287 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 163
- Forks at capture: 75
- Last updated: 2026-07-11T22:32:33Z
- Last pushed: 2026-06-22T19:38:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-iot-device-sdk-arduino-yun)
- [README](https://github.com/aws/aws-iot-device-sdk-arduino-yun/blob/master/README.md)
- [Issues](https://github.com/aws/aws-iot-device-sdk-arduino-yun/issues)
- [Releases](https://github.com/aws/aws-iot-device-sdk-arduino-yun/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
