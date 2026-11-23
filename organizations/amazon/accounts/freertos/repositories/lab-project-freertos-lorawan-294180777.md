# FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN

- Company: Amazon
- GitHub account: [https://github.com/freertos](https://github.com/freertos)
- Mapping status: official-directory-listed
- Repository: [FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN)
- Default branch: main
- README: [Open upstream README](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN/blob/main/README.md)
- README blob SHA: e551e4f5587659a4b3b446da25f7eda23c0d65b1
- Repository ID: 294180777
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Reference implementation of LoRaWAN connectivity on FreeRTOS.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:30:22+00:00

### Short excerpt (up to 100 words)

> Reference implementation of LoRaWAN connectivity on FreeRTOS. The project is a FreeRTOS adaptation of Semtech's LoRaMAC Node implementation. Class-A offers low-powered communincation between the end device and LoRa Network Server. Its the most common use-case and should be implemented by all end-devices supporting LoRaWAN. TheThings Network (TTN) diagrams and summaries shows the communication between end-device and Network Server in Class A. All communications are initiated by an end-device sending uplink message at any time to the server. End-device opens two receiver slot windows after a successful uplink. Server can choose to send any downlink packets during this window. Both end-device

### README headings

- Getting Statted
- Class A demo
- LoRaMAC task
- LoRaWAN Class A task
- Low Power Mode
- Supported Platforms
- Downloading the Code
- Setting up IDE and Project
- Nordic NRF52840
- STMicroElectronics STM32L4 Discovery Kit IoT Node
- Create a TTN account, TTN Appication, and register your device
- Configure device credentials
- Build and Run the Code
- Nordic NRF52840-DK
- STMicroelectronics STM32L4 Discovery Kit IoT Node
- View your device traffic in TTN

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 9,628,054 |
| HTML | 111,751 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- demos/classA/Nordic_NRF52/nRF5_SDK_15.2.0/external/micro-ecc/nrf51_armgcc/armgcc/Makefile (capture: captured)
- demos/classA/Nordic_NRF52/nRF5_SDK_15.2.0/external/micro-ecc/nrf51_iar/armgcc/Makefile (capture: captured)
- demos/classA/Nordic_NRF52/nRF5_SDK_15.2.0/external/micro-ecc/nrf51_keil/armgcc/Makefile (capture: captured)
- demos/classA/Nordic_NRF52/nRF5_SDK_15.2.0/external/micro-ecc/nrf52hf_armgcc/armgcc/Makefile (capture: captured)
- demos/classA/Nordic_NRF52/nRF5_SDK_15.2.0/external/micro-ecc/nrf52hf_iar/armgcc/Makefile (capture: captured)
- demos/classA/Nordic_NRF52/nRF5_SDK_15.2.0/external/micro-ecc/nrf52hf_keil/armgcc/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 57
- Forks at capture: 23
- Last updated: 2026-11-12T00:42:24Z
- Last pushed: 2026-06-26T23:02:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN)
- [README](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN/blob/main/README.md)
- [Issues](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN/issues)
- [Releases](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-LoRaWAN/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
