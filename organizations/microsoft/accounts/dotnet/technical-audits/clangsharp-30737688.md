# dotnet/ClangSharp

- Company: Microsoft
- Account: dotnet
- Repository: https://github.com/dotnet/ClangSharp
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:00:12+00:00

## Project purpose

ClangSharp provides Clang bindings written in C#. It is self-hosted and auto-generates itself by parsing the Clang C header files using ClangSharpPInvokeGenerator.

## Why this project is used

Clang bindings for .NET written in C#

## Core features

- Auto-generated using Clang C headers files, and supports all functionality exposed by them ~ which means you can build tooling around C/C++: Auto-generated using Clang C headers files, and supports all functionality exposed by them ~ which means you can build tooling around C/C++
  - Evidence: README.md#Features
- Exposes the raw unsafe API for performance: Exposes the raw unsafe API for performance
  - Evidence: README.md#Features
- Exposes a slightly higher abstraction that is type safe (CXIndex and CXTranslationUnit are different types, despite being pointers internally): Exposes a slightly higher abstraction that is type safe (CXIndex and CXTranslationUnit are different types, despite being pointers internally)
  - Evidence: README.md#Features
- Exposes an again slightly higher abstraction that tries to mirror the Clang C++ Type Hierarchy where possible: Exposes an again slightly higher abstraction that tries to mirror the Clang C++ Type Hierarchy where possible
  - Evidence: README.md#Features
- Nearly identical to the Clang C APIs, e.g. clang_getDiagnosticSpelling in C, vs. clang.getDiagnosticSpelling (notice the . in the C# API): Nearly identical to the Clang C APIs, e.g. clang_getDiagnosticSpelling in C, vs. clang.getDiagnosticSpelling (notice the . in the C# API)
  - Evidence: README.md#Features

## Technology stack

- Languages: C#, C++, C, PowerShell, Shell, CMake, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: build.sh, pack.sh, restore.sh, scripts/build.sh

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/dotnet/ClangSharp/blob/main/README.md
- README SHA: 898fdf5ca5e3114a20ee8b62d52e150b19a8f90f
- Manifests: CMakeLists.txt, sources/CMakeLists.txt, sources/libClangSharp/CMakeLists.txt
- Sampled source files: build.sh, pack.sh, restore.sh, scripts/build.sh
- Git tree state: captured
- Evidence fingerprint: 2f25d2b87f4b16cd25405e0e713e573d25d71790971765e9b76d3fa5e71827c5

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
