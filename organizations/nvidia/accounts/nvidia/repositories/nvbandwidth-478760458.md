# NVIDIA/nvbandwidth

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/nvbandwidth](https://github.com/NVIDIA/nvbandwidth)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/nvbandwidth/blob/main/README.md)
- README blob SHA: b075bba28e5a08252767684b643855c0472b8f19
- README bytes captured: 17247
- README truncated at capture limit: False
- Repository ID: 478760458
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A tool for bandwidth measurements on NVIDIA GPUs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:11:11+00:00

### Short excerpt (up to 300 words)

> ./nvbandwidth -h Usage: nvbandwidth Linux is the primary

### README headings

- nvbandwidth
- Requirements
- Build
- Usage:
- Pairwise GPU Testing
- Finding GPU UUIDs
- One process per GPU — shows all GPUs on every node (e.g. 4 GPUs/node, 2 nodes = -n 8)
- Buffer size
- Single-node pairwise test
- Multinode pairwise test
- Multinode benchmarks
- Pair Sampling for Multinode Tests
- Sampling Options
- Sampling Algorithm
- Examples
- Test all pairs (default/full coverage) on a 4-node, 8-GPU/node system (32 ranks)
- Test 20 carefully selected pairs
- For a 4-node, 8-GPU/node system: 992 total pairs available (32×31)
- Using --targetNumPairs 100 will test ~10% of pairs while covering all GPUs
- Local testing
- Running it on a cluster
- Test Details
- Latency Measurements
- How Pointer Chasing Works
- Important Notes
- Measurement Details
- Unidirectional Bandwidth Tests
- Bidirectional Host <-> Device Bandwidth Tests
- Bidirectional Device <-> Device Bandwidth Tests
- Known Issues

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage:

> ./nvbandwidth -h Usage: nvbandwidth

### Technology and requirements: Requirements

> Linux is the primary

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 756,253 |
| Cuda | 121,063 |
| CMake | 13,650 |
| C | 1,080 |
| Shell | 354 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 807
- Forks at capture: 104
- Last updated: 2026-11-23T06:20:59Z
- Last pushed: 2026-11-12T04:33:14Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/nvbandwidth)
- [README](https://github.com/NVIDIA/nvbandwidth/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/nvbandwidth/issues)
- [Releases](https://github.com/NVIDIA/nvbandwidth/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
