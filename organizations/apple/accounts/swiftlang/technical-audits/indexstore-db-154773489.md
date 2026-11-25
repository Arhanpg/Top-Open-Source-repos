# swiftlang/indexstore-db

- Company: Apple
- Account: swiftlang
- Repository: https://github.com/swiftlang/indexstore-db
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:03:06+00:00

## Project purpose

IndexStoreDB is a source code indexing library. It provides a composable and efficient query API for looking up source code symbols, symbol occurrences, and relations. IndexStoreDB uses the libIndexStore library, which lives in swiftlang/llvm-project, for reading raw index data. Raw index data can be produced by compilers such as Apple Clang and Swift using the -index-store-path option. IndexStoreDB enables efficiently querying this data by maintaining acceleration tables in a key-value database built with LMDB.

## Why this project is used

Index database library for use with sourcekit-lsp

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C++, Swift, C, Python, CMake, Objective-C++, Objective-C
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: Sources/ISDBTestSupport/INPUTS/RelativeWorkingDir/main.c, Sources/ISDBTestSupport/INPUTS/SingleUnit/main.c, Package.swift, Sources/index-dump/index-dump.swift

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/swiftlang/indexstore-db/blob/main/README.md
- README SHA: 896700a7af9c51ad59cad53bedc7f8ef543b470a
- Manifests: CMakeLists.txt, Sources/CMakeLists.txt, cmake/modules/CMakeLists.txt, Sources/IndexStoreDB/CMakeLists.txt, Sources/IndexStoreDB_CIndexStoreDB/CMakeLists.txt, Sources/IndexStoreDB_Core/CMakeLists.txt
- Sampled source files: Sources/ISDBTestSupport/INPUTS/RelativeWorkingDir/main.c, Sources/ISDBTestSupport/INPUTS/SingleUnit/main.c, Package.swift, Sources/index-dump/index-dump.swift
- Git tree state: captured
- Evidence fingerprint: 6243c59e0f1ac0a30981223bd028178d6884dc5ebaadf8f85b9a406231a1fa79

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
