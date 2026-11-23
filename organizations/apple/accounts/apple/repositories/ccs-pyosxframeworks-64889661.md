# apple/ccs-pyosxframeworks

- Company: Apple
- GitHub account: [https://github.com/apple](https://github.com/apple)
- Mapping status: verified
- Repository: [apple/ccs-pyosxframeworks](https://github.com/apple/ccs-pyosxframeworks)
- Default branch: master
- README: [Open upstream README](https://github.com/apple/ccs-pyosxframeworks/blob/master/README)
- README blob SHA: 9fb05dea65450152cccba102e691dd2536d06510
- Repository ID: 64889661
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Python Framework for macOS APIs used by CalendarServer

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:10:01+00:00

### Short excerpt (up to 100 words)

> Getting Started =============== This is a python library that wraps a number of useful OS X frameworks. Develop ======= cffi wrappers for various frameworks live in the osx.frameworks modules. Run the osx._corefoundation_cffi_build module to create the osx._corefoundation.so module. That contains the cffi extension module for the wrappers. Each time changes are made to the wrapper modules, re-run the cffi build. The other modules in osx are Python objects that wrap various CoreFoundation objects to provide implicit CFRetain/CFRelease behavior and also simple data conversion APIs between the CF types and Python types. For example to turn a Python string "s" into

### README headings

- No headings captured

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 96,824 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 27
- Forks at capture: 20
- Last updated: 2026-07-28T22:10:37Z
- Last pushed: 2017-02-27T21:32:24Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/apple/ccs-pyosxframeworks)
- [README](https://github.com/apple/ccs-pyosxframeworks/blob/master/README)
- [Issues](https://github.com/apple/ccs-pyosxframeworks/issues)
- [Releases](https://github.com/apple/ccs-pyosxframeworks/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
