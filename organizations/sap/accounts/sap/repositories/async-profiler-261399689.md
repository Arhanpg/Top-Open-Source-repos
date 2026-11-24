# SAP/async-profiler

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/async-profiler](https://github.com/SAP/async-profiler)
- Default branch: master
- README: [Open upstream README](https://github.com/SAP/async-profiler/blob/master/README.md)
- README blob SHA: 9eae0aec1602061b29c3ed937c9711cbda5adb61
- Repository ID: 261399689
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sampling CPU and HEAP profiler for Java featuring AsyncGetCallTrace + perf_events

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:40+00:00

### Short excerpt (up to 100 words)

> This project is a low overhead sampling profiler for Java that does not suffer from the Safepoint bias problem. It features HotSpot-specific API to collect stack traces and to track memory allocations. The profiler works with OpenJDK and other Java runtimes based on the HotSpot JVM. Unlike traditional Java profilers, async-profiler monitors non-Java threads (e.g., GC and JIT compiler threads) and shows native and kernel frames in stack traces. What can be profiled: - CPU time - Allocations in Java Heap - Native memory allocations and leaks - Contended locks - Hardware and software performance counters like cache misses, page

### README headings

- Async-profiler
- Download
- Stable release: [4.6](https://github.com/async-profiler/async-profiler/releases/tag/v4.6)
- Nightly builds
- Quick start
- Building
- Build status
- Minimum requirements
- How to build
- Supported platforms
- Documentation
- Basic usage
- Profiler output
- Advanced usage
- Troubleshooting

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 889,701 |
| Java | 457,795 |
| HTML | 191,699 |
| C | 56,815 |
| Makefile | 12,539 |
| Shell | 4,424 |
| Dockerfile | 2,722 |
| Assembly | 348 |
| Linker Script | 347 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pom.xml (capture: captured) — dependency clues: async-profiler, central-publishing-maven-plugin, maven-compiler-plugin, maven-gpg-plugin, maven-jar-plugin, maven-javadoc-plugin, maven-source-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3
- Forks at capture: 2
- Last updated: 2026-11-10T00:17:16Z
- Last pushed: 2026-11-20T00:17:07Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/async-profiler)
- [README](https://github.com/SAP/async-profiler/blob/master/README.md)
- [Issues](https://github.com/SAP/async-profiler/issues)
- [Releases](https://github.com/SAP/async-profiler/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
