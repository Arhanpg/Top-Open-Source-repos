# FreeRTOS/coreMQTT-Agent

- Company: Amazon
- GitHub account: [https://github.com/freertos](https://github.com/freertos)
- Mapping status: official-directory-listed
- Repository: [FreeRTOS/coreMQTT-Agent](https://github.com/FreeRTOS/coreMQTT-Agent)
- Default branch: main
- README: [Open upstream README](https://github.com/FreeRTOS/coreMQTT-Agent/blob/main/README.md)
- README blob SHA: 4701ae463e96de55ab9ead28d57da1ba99784907
- Repository ID: 344300940
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Implements an MQTT agent (or daemon) task for simple MQTT connection sharing among different threads of execution.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:50+00:00

### Short excerpt (up to 100 words)

> The coreMQTT Agent library is a high level API that adds thread safety to the coreMQTT library. The library provides thread safe equivalents to the coreMQTT's APIs, greatly simplifying its use in multi-threaded environments. The coreMQTT Agent library manages the MQTT connection by serializing the access to the coreMQTT library and reducing implementation overhead (e.g., removing the need for the application to repeatedly call to `MQTT_ProcessLoop`). This allows your multi-threaded applications to share the same MQTT connection, and enables you to design an embedded application without having to worry about coreMQTT thread safety. This library has gone through code quality

### README headings

- coreMQTT Agent Library
- Cloning this repository
- coreMQTT Agent Library Configurations
- Configuration values to modify timing performance
- Agent queue block time:
- Socket read/recv timeout:
- Agent task priority:
- Porting the coreMQTT Agent Library
- Messaging Interface
- Additional Considerations
- Static Memory
- Subscription Management
- Building the Library
- Building Unit Tests
- Checkout CMock Submodule
- Unit Test Platform Prerequisites
- Steps to build **Unit Tests**
- CBMC
- Reference examples
- Documentation
- Generating documentation
- Getting help
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 341,382 |
| Makefile | 60,279 |
| CMake | 20,849 |
| Python | 19,901 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- test/CMakeLists.txt (capture: captured)
- test/unit-test/CMakeLists.txt (capture: captured)
- test/cbmc/proofs/MQTTAgent_CancelAll/Makefile (capture: captured)
- test/cbmc/proofs/MQTTAgent_CommandLoop/Makefile (capture: captured)
- test/cbmc/proofs/MQTTAgent_Connect/Makefile (capture: captured)
- test/cbmc/proofs/MQTTAgent_Disconnect/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 46
- Forks at capture: 47
- Last updated: 2026-10-01T05:25:49Z
- Last pushed: 2026-06-12T18:12:21Z
- Topics: freertos, iot, mqtt

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/FreeRTOS/coreMQTT-Agent)
- [README](https://github.com/FreeRTOS/coreMQTT-Agent/blob/main/README.md)
- [Issues](https://github.com/FreeRTOS/coreMQTT-Agent/issues)
- [Releases](https://github.com/FreeRTOS/coreMQTT-Agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
