# FreeRTOS/freertos-gdb

- Company: Amazon
- GitHub account: [https://github.com/freertos](https://github.com/freertos)
- Mapping status: official-directory-listed
- Repository: [FreeRTOS/freertos-gdb](https://github.com/FreeRTOS/freertos-gdb)
- Default branch: main
- README: [Open upstream README](https://github.com/FreeRTOS/freertos-gdb/blob/main/README.md)
- README blob SHA: ad5189f2f5eca865f77b87b9094ac57ad4346f9f
- Repository ID: 543743766
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:06:47+00:00

### Short excerpt (up to 100 words)

> GDB extension to display FreeRTOS tasks and set task-specific breakpoints. GDB must be built with Python 2+. 1. In gdb, use the command ```show data-directory``` to find the path to where GDB searches for auxillary data files. We'll call this ```[data-directory]```. 2. Copy ```freertos.py``` from this repository into the folder ```[data-directory]/python/gdb/command/```. (gdb) freertos "freertos" must be followed by the name of a subcommand. List of freertos subcommands: freertos break -- Create a breakpoint that will only get tripped by the specific task. freertos tasks -- Displays FreeRTOS tasks and information. * ID: The memory address of the task's TCB_t *

### README headings

- freertos-gdb
- Prerequisites
- Setup
- Commands
- Tasks Display
- Breakpoints
- References

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 7,906 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 10
- Forks at capture: 4
- Last updated: 2026-08-31T04:45:31Z
- Last pushed: 2022-11-21T18:55:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/FreeRTOS/freertos-gdb)
- [README](https://github.com/FreeRTOS/freertos-gdb/blob/main/README.md)
- [Issues](https://github.com/FreeRTOS/freertos-gdb/issues)
- [Releases](https://github.com/FreeRTOS/freertos-gdb/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
