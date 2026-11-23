# model-checking/cbmc-viewer

- Company: Amazon
- GitHub account: [https://github.com/model-checking](https://github.com/model-checking)
- Mapping status: official-directory-listed
- Repository: [model-checking/cbmc-viewer](https://github.com/model-checking/cbmc-viewer)
- Default branch: master
- README: [Open upstream README](https://github.com/model-checking/cbmc-viewer/blob/master/README.md)
- README blob SHA: 4071f9ebfec4a9c9fb542de9c2ce67308e7e2a2e
- Repository ID: 272090494
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CBMC Viewer scans the output of CBMC and produces a browsable summary of its findings, making it easy to root cause the issues it finds.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:37:35+00:00

### Short excerpt (up to 100 words)

> It can prove that (for computations of bounded depth) a C program exhibits no memory safe errors (no buffer overflows, no invalid pointers, etc), no undefined behaviors, and no failures of assertions in the code. that scans the output of CBMC and produces a browsable summary of its findings. Here is a simple example of using cbmc-viewer. Running this example requires installing CBMC. Installation on MacOS is just `brew install cbmc`. Installation on other operation systems is described on the [CBMC release page](https://github.com/diffblue/cbmc/releases/latest). Create a source file `main.c` containing static int global; int main() { int *ptr = malloc(sizeof(int)); assert(global

### README headings

- CBMC Viewer
- Example
- Documentation
- Installation
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 278,829 |
| Makefile | 11,990 |
| HTML | 8,841 |
| Shell | 4,213 |
| JavaScript | 2,507 |
| CSS | 1,557 |
| C | 124 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured)
- docs/Makefile (capture: captured)
- summary/Makefile (capture: captured)
- tests/bin/Makefile (capture: captured)
- tests/coreHTTP/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 41
- Forks at capture: 12
- Last updated: 2026-10-21T17:32:37Z
- Last pushed: 2026-09-01T21:26:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/model-checking/cbmc-viewer)
- [README](https://github.com/model-checking/cbmc-viewer/blob/master/README.md)
- [Issues](https://github.com/model-checking/cbmc-viewer/issues)
- [Releases](https://github.com/model-checking/cbmc-viewer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
