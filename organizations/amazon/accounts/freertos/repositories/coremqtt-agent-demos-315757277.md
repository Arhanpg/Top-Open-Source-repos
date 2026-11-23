# FreeRTOS/coreMQTT-Agent-Demos

- Company: Amazon
- GitHub account: [https://github.com/freertos](https://github.com/freertos)
- Mapping status: official-directory-listed
- Repository: [FreeRTOS/coreMQTT-Agent-Demos](https://github.com/FreeRTOS/coreMQTT-Agent-Demos)
- Default branch: main
- README: [Open upstream README](https://github.com/FreeRTOS/coreMQTT-Agent-Demos/blob/main/README.md)
- README blob SHA: aa33ac127d15f75cce6c84077e4fdf36f13b0527
- Repository ID: 315757277
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Demonstrates use of coreMQTT-Agent for simple MQTT connection sharing among different threads of execution. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:52+00:00

### Short excerpt (up to 100 words)

> This repository demonstrates examples of using AWS IoT Device Shadow, Device Defender, and OTA from multiple threads. It uses FreeRTOS and the coreMQTT Agent library, an extension on top of coreMQTT that provides MQTT APIs with thread safety. The examples here share a single MQTT connection amongst multiple concurrent tasks, without requiring the management of any synchronization primitives from the application. This repo uses Git Submodules to bring in dependent components. **Note:** If you download the ZIP file provided by the GitHub UI, you will not get the contents of the submodules. (The ZIP file is also not a valid

### README headings

- coreMQTT Agent and Demo Tasks (including OTA)
- Cloning this repository
- Getting started
- Building Demos
- Visual Studio
- QEMU Cortex-M3
- Getting help
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 953,143 |
| Python | 21,326 |
| templ | 21,253 |
| Makefile | 14,150 |
| Batchfile | 616 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build/Cortex-M3_MPS2_QEMU_GCC/Makefile (capture: captured)
- build/VisualStudio/mqtt_multitask_demo.sln (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 36
- Forks at capture: 30
- Last updated: 2025-11-20T18:34:26Z
- Last pushed: 2025-03-07T10:01:03Z
- Topics: freertos, iot, mqtt

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/FreeRTOS/coreMQTT-Agent-Demos)
- [README](https://github.com/FreeRTOS/coreMQTT-Agent-Demos/blob/main/README.md)
- [Issues](https://github.com/FreeRTOS/coreMQTT-Agent-Demos/issues)
- [Releases](https://github.com/FreeRTOS/coreMQTT-Agent-Demos/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
