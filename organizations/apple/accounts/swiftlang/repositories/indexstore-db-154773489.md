# swiftlang/indexstore-db

- Company: Apple
- GitHub account: [https://github.com/swiftlang](https://github.com/swiftlang)
- Mapping status: official-project-linked
- Repository: [swiftlang/indexstore-db](https://github.com/swiftlang/indexstore-db)
- Default branch: main
- README: [Open upstream README](https://github.com/swiftlang/indexstore-db/blob/main/README.md)
- README blob SHA: 896700a7af9c51ad59cad53bedc7f8ef543b470a
- Repository ID: 154773489
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Index database library for use with sourcekit-lsp

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:35:15+00:00

### Short excerpt (up to 100 words)

> IndexStoreDB is a source code indexing library. It provides a composable and efficient query API for looking up source code symbols, symbol occurrences, and relations. IndexStoreDB uses the libIndexStore library, which lives in swiftlang/llvm-project, for reading raw index data. Raw index data can be produced by compilers such as Apple Clang and Swift using the `-index-store-path` option. IndexStoreDB enables efficiently querying this data by maintaining acceleration tables in a key-value database built with LMDB. IndexStoreDB's data model is derived from libIndexStore. For more information about libIndexStore, and producing raw indexing data, see the Indexing While Building whitepaper. For a general

### README headings

- IndexStoreDB
- Building IndexStoreDB
- Building on Linux
- Some Example Users
- Contributing to Swift
- Development

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 3,154,642 |
| Swift | 333,289 |
| C | 79,272 |
| Python | 10,030 |
| CMake | 7,383 |
| Objective-C++ | 1,196 |
| Objective-C | 548 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- Sources/CMakeLists.txt (capture: captured)
- cmake/modules/CMakeLists.txt (capture: captured)
- Sources/IndexStoreDB/CMakeLists.txt (capture: captured)
- Sources/IndexStoreDB_CIndexStoreDB/CMakeLists.txt (capture: captured)
- Sources/IndexStoreDB_Core/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 422
- Forks at capture: 100
- Last updated: 2026-11-17T06:34:01Z
- Last pushed: 2026-11-21T09:57:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/swiftlang/indexstore-db)
- [README](https://github.com/swiftlang/indexstore-db/blob/main/README.md)
- [Issues](https://github.com/swiftlang/indexstore-db/issues)
- [Releases](https://github.com/swiftlang/indexstore-db/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
