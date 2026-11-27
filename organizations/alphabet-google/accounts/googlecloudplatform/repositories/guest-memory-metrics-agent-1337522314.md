# GoogleCloudPlatform/guest-memory-metrics-agent

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/guest-memory-metrics-agent](https://github.com/GoogleCloudPlatform/guest-memory-metrics-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/guest-memory-metrics-agent/blob/main/README.md)
- README blob SHA: 64dcab6e8641d75521d4ff850a8dc94f1f697502
- README bytes captured: 17699
- README truncated at capture limit: False
- Repository ID: 1337522314
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A lightweight, low-overhead Linux guest daemon and CLI to record, analyze, and explain granular kernel memory, cgroup, and NUMA metrics with built-in PII scrubbing.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:31:18+00:00

### Short excerpt (up to 300 words)

> The **Guest Memory Metrics The agent operates via Pre-compiled, fully statically linked ARCH=$(uname -m | sed

### README headings

- Guest Memory Metrics Agent
- Overview
- Project Goals
- What It Does
- How the PII Scrubber Works
- Concrete Transformation Examples
- Implementation Flowchart
- 1. Machine-Salted FNV-1a Hash
- 2. Restricting Digit Suffixes to Physical Metrics
- Intended Users
- Installation and Usage Instructions
- 1. Fast Binary Installation (Recommended)
- 1. Detect architecture (x86_64 -> amd64, aarch64 -> arm64)
- 2. Construct download URL based on version
- 3. Download pre-compiled static binary
- 4. Download systemd service file
- 5. Reload systemd daemon
- 2. Building from Source (Optional)
- 1. Clone repository
- 2. Build static binary
- 3. Install binary and service
- 3. Automated Startup and Background Execution (Recommended)
- 4. Generating Reports from the Daemon
- A. Comprehensive Time-Series Report (`--comprehensive`)
- Output comprehensive CSV to a file:
- Or stream comprehensive CSV to STDOUT:
- B. Delta Comparative Report (`--delta` or default)
- Display delta summary table in STDOUT (default):
- Export delta summary to CSV file:
- Stream delta summary as CSV to STDOUT:

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> The **Guest Memory Metrics

### Features and capabilities: What It Does

> The agent operates via

### Getting started and usage: 1. Fast Binary Installation (Recommended)

> Pre-compiled, fully statically linked

### Architecture and design: 1. Detect architecture (x86_64 -> amd64, aarch64 -> arm64)

> ARCH=$(uname -m | sed

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 144,548 |
| Starlark | 7,190 |
| Shell | 2,424 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 1
- Last updated: 2026-08-18T23:04:45Z
- Last pushed: 2026-08-18T23:09:52Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/guest-memory-metrics-agent)
- [README](https://github.com/GoogleCloudPlatform/guest-memory-metrics-agent/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/guest-memory-metrics-agent/issues)
- [Releases](https://github.com/GoogleCloudPlatform/guest-memory-metrics-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
