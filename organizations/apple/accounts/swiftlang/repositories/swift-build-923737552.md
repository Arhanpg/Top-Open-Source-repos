# swiftlang/swift-build

- Company: Apple
- GitHub account: [https://github.com/swiftlang](https://github.com/swiftlang)
- Mapping status: official-project-linked
- Repository: [swiftlang/swift-build](https://github.com/swiftlang/swift-build)
- Default branch: main
- README: [Open upstream README](https://github.com/swiftlang/swift-build/blob/main/README.md)
- README blob SHA: 67fbbe578e00422f1c13944245544cf3d8579f42
- Repository ID: 923737552
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A high-level build system based on llbuild, used by Xcode, Swift Playground, and the Swift Package Manager

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:48:05+00:00

### Short excerpt (up to 100 words)

> Swift Build ======= Swift Build is a high-level build system based on llbuild with great support for building Swift. It is used by SwiftPM, Xcode, and Swift Playground. Usage Swift Build is the default SwiftPM build system in nightly snapshots of Swift's `main` branches. In Swift 6.2 and 6.3, it can be enabled by passing `--build-system swiftbuild`. When building SwiftPM from source it will be built as a package dependency. When checking out the full set of Swift repositories, `SWIFTCI_USE_LOCAL_DEPS=1 swift build --package-path /path/to/swiftpm` can be used to test local changes to Swift Build and SwiftPM together. The `Utilities` directory

### README headings

- With SwiftPM
- With Xcode
- With xcodebuild
- Debugging

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Swift | 20,918,091 |
| C++ | 110,298 |
| CMake | 57,781 |
| C | 50,998 |
| Shell | 1,656 |
| Emacs Lisp | 719 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- Sources/CMakeLists.txt (capture: captured)
- cmake/modules/CMakeLists.txt (capture: captured)
- Sources/SWBAndroidPlatform/CMakeLists.txt (capture: captured)
- Sources/SWBApplePlatform/CMakeLists.txt (capture: captured)
- Sources/SWBBuildService/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2253
- Forks at capture: 251
- Last updated: 2026-11-23T15:55:00Z
- Last pushed: 2026-11-23T09:03:32Z
- Topics: build, build-system, build-tool, build-tools, swift, swift-package-manager

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/swiftlang/swift-build)
- [README](https://github.com/swiftlang/swift-build/blob/main/README.md)
- [Issues](https://github.com/swiftlang/swift-build/issues)
- [Releases](https://github.com/swiftlang/swift-build/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
