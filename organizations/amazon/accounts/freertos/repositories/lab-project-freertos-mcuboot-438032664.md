# FreeRTOS/Lab-Project-FreeRTOS-MCUBoot

- Company: Amazon
- GitHub account: [https://github.com/freertos](https://github.com/freertos)
- Mapping status: official-directory-listed
- Repository: [FreeRTOS/Lab-Project-FreeRTOS-MCUBoot](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-MCUBoot)
- Default branch: main
- README: [Open upstream README](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-MCUBoot/blob/main/README.md)
- README blob SHA: 9037a7f8068d2899d73d939fbe83d1b2922641be
- Repository ID: 438032664
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:12+00:00

### Short excerpt (up to 100 words)

> Reference example for FreeRTOS with MCUBoot support. MCUBoot is a configurable secure bootloader maintained by several industry leaders. It can operate as the first or second stage bootloader, with support for cryptographic verification of software images via one of the following: * ECDSA-P256 * RSA-2048 * RSA-3072 By default, it supports image reversion whereby uploaded image upgrades are tentatively booted once. Upon and image's initial boot, if the upgrade image marks itself as confirmed it is retained as the primary image. If the upgrade image is not confirmed, the subsequent boot will rollback to the prior confirmed image. If no

### README headings

- Labs-FreeRTOS-Plus-MCUBoot
- Demo Description
- Patch Description
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 136,234 |
| Linker Script | 82,039 |
| CMake | 17,379 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- proj/espressif/esp32/app/CMakeLists.txt (capture: captured)
- proj/espressif/esp32/bootloader/CMakeLists.txt (capture: captured)
- proj/espressif/esp32/app/main/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 40
- Forks at capture: 8
- Last updated: 2026-09-14T22:09:14Z
- Last pushed: 2026-06-26T23:02:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-MCUBoot)
- [README](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-MCUBoot/blob/main/README.md)
- [Issues](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-MCUBoot/issues)
- [Releases](https://github.com/FreeRTOS/Lab-Project-FreeRTOS-MCUBoot/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
