# FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core

- Company: Amazon
- GitHub account: [https://github.com/freertos](https://github.com/freertos)
- Mapping status: official-directory-listed
- Repository: [FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core](https://github.com/FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core)
- Default branch: main
- README: [Open upstream README](https://github.com/FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core/blob/main/README.md)
- README blob SHA: f11c2f5b8f84fcf4ee590b213a0871af9391a828
- Repository ID: 659950619
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An example of an AWS IoT Core OTA orchestrator, running on the FreeRTOS POSIX port

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:16+00:00

### Short excerpt (up to 100 words)

> AWS IoT CoreOTA enables simple Over-The-Air (OTA) updates through an extensible and modular set of interfaces. When properly setup, the CoreOTA 'Orchestrator' (see CoreOTA concepts & architecture) will handle the standard OTA behaviors like downloading the OTA file, parsing update metadata, and updating OTA status remotely. These functions are performed through the different interfaces which allow for customization for new fields and extensibility to new services. Using this library will allow you to easily configure OTA updates from a variety of sources and keep OTA functionality separated from any on-device application. This repository contains the following two example OTA orchestrators.

### README headings

- FreeRTOS Labs - OTA Example for AWS IoT Core
- 0. Concepts and Architecture
- 1. Demo Prerequisites
- 2. Demo Setup
- 2.1 Setup AWS IoT Core
- 2.2 Perform one-time setup of OTA cloud resources
- 2.3 Build the coreOTA_Demo Binary
- optional command - skip if you do not have Nix installed
- 3. Run the OTA Demo
- 3.1 Create an OTA Update in AWS IoT Core
- 3.2 Run the simulator
- 3.3 Verify successful OTA in the AWS IoT Core Console
- 4. Run the Unit Tests
- 4.1 Running the OTA Parser Unit tests
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 11,246 |
| CMake | 6,630 |
| Nix | 3,679 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 10
- Forks at capture: 10
- Last updated: 2026-06-26T23:02:55Z
- Last pushed: 2026-06-26T23:02:51Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core)
- [README](https://github.com/FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core/blob/main/README.md)
- [Issues](https://github.com/FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core/issues)
- [Releases](https://github.com/FreeRTOS/Lab-Project-ota-example-for-AWS-IoT-Core/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
