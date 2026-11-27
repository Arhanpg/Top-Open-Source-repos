# google/gazoo-device

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/gazoo-device](https://github.com/google/gazoo-device)
- Default branch: master
- README: [Open upstream README](https://github.com/google/gazoo-device/blob/master/README.md)
- README blob SHA: e52ac05e63112fc3bf5bf4458c283a8015bdb105
- README bytes captured: 18012
- README truncated at capture limit: False
- Repository ID: 310440527
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Gazoo Device Manager is a framework for testing smart devices. It is used for device management and handles device communication, logging, log event filtering, and device health checks. Device controllers implement a common interface which allows GDM tests to be device-agnostic. GDM has a CLI to make common device interactions easy.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T20:31:08+00:00

### Short excerpt (up to 300 words)

> 1 new devices detected: Supported host operating systems:

### README headings

- Gazoo Device Manager (GDM)
- Table of contents
- Install
- Uninstall
- Quick start
- Device controllers in GDM
- Config files
- Logs
- The `gdm.txt` log
- Device log files, such as `linuxexample-1eb2-20201113-123538.txt`
- Device log event files, such as `linuxexample-1eb2-20201113-123548-events.txt`
- Detecting devices
- Step 1/3: Detecting potential new communication addresses. #####
- Step 2/3 Identify Device Type of Connections. #####
- Step 3/3: Extract Persistent Info from Detected Devices. #####
- Detection Summary #####
- Using the CLI
- Exploring device capabilities without a physical device
- Exploring device capabilities with a physical device
- Basic CLI usage
- Using the gazoo_device python package
- How to use GDM with test frameworks
- Contributor documentation
- License
- Dependency license compliance
- Disclaimer

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Detection Summary

> 1 new devices detected:

### Getting started and usage: Install

> Supported host operating systems:

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,764,699 |
| Shell | 19,036 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: fire, immutabledict, intelhex, pigweed, prompt-toolkit, protobuf, psutil, pylibftdi, pylink-square, pyserial, pyudev, pyusb, pyvisa, pyvisa-py, requests, urllib3, websocket-client, xmodem
- setup.py (capture: captured)
- examples/example_extension_package/setup.py (capture: captured)
- examples/example_matter_extension_package/setup.py (capture: captured)
- gazoo_device/tests/setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 28
- Forks at capture: 10
- Last updated: 2026-07-21T09:12:52Z
- Last pushed: 2026-04-23T05:37:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/gazoo-device)
- [README](https://github.com/google/gazoo-device/blob/master/README.md)
- [Issues](https://github.com/google/gazoo-device/issues)
- [Releases](https://github.com/google/gazoo-device/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
