# FreeRTOS/iot-reference-arm-corstone3xx

- Company: Amazon
- GitHub account: [https://github.com/freertos](https://github.com/freertos)
- Mapping status: official-directory-listed
- Repository: [FreeRTOS/iot-reference-arm-corstone3xx](https://github.com/FreeRTOS/iot-reference-arm-corstone3xx)
- Default branch: main
- README: [Open upstream README](https://github.com/FreeRTOS/iot-reference-arm-corstone3xx/blob/main/README.md)
- README blob SHA: cf50bd83b1202c193d78a36dcb0f4bd04b9d5855
- Repository ID: 670246463
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Featured FreeRTOS IoT Integration targeting an Arm Corstone-3xx platform based on Arm Cortex-M MCU.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:30:01+00:00

### Short excerpt (up to 100 words)

> This reference integration demonstrates how to develop cloud connected applications and update them securely by integrating modular and utilizing hardware enforced security based on Arm TrustZone (Armv8-M). To utilize the hardware enforced security, this integration uses PSA Certified reference implementation Trusted Firmware-M. Trusted Firmware-M provides various Secure services such as Secure boot, Crypto, Secure Storage, Attestation and Update services meeting PSA Certified requirements. Developers and partners can use this integration as a starting point to build FreeRTOS kernel and libraries based software stack on top of Arm Cortex-M based platforms. All the components are put together in a modular manner

### README headings

- IoT Reference Integration for Arm Corstone-3xx
- Introduction
- ML model update
- Supported Targets
- Supported Toolchains
- Project organisation
- Examples
- Secure TLS Connection
- Secure OTA Updates
- Software Components
- Fetching
- Trusted Firmware M
- Mbed TLS
- PKCS11 PSA Shim
- AWS OTA PAL PSA implementation
- Mali-C55 Versatile Image Signal Processor for Computer Vision and Smart Display Systems
- Tools
- Python script for automating AWS interactions
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 2,060,615 |
| Python | 212,830 |
| C++ | 171,552 |
| CMake | 170,583 |
| Linker Script | 53,596 |
| Shell | 19,255 |
| Dockerfile | 8,262 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- .devcontainer/Dockerfile (capture: captured)
- bsp/CMakeLists.txt (capture: captured)
- components/CMakeLists.txt (capture: captured)
- applications/blinky/CMakeLists.txt (capture: captured)
- applications/freertos_iot_libraries_tests/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 27
- Forks at capture: 25
- Last updated: 2026-10-21T02:27:12Z
- Last pushed: 2026-04-23T19:08:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/FreeRTOS/iot-reference-arm-corstone3xx)
- [README](https://github.com/FreeRTOS/iot-reference-arm-corstone3xx/blob/main/README.md)
- [Issues](https://github.com/FreeRTOS/iot-reference-arm-corstone3xx/issues)
- [Releases](https://github.com/FreeRTOS/iot-reference-arm-corstone3xx/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
