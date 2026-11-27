# dotnet/LLVMSharp

- Company: Microsoft
- Account: dotnet
- Repository: https://github.com/dotnet/LLVMSharp
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:34:18+00:00

## Project purpose

LLVMSharp is a multi-platform .NET Standard library for accessing the LLVM infrastructure. The bindings are auto-generated using ClangSharp parsing LLVM-C header files.

## Why this project is used

LLVM bindings for .NET Standard written in C# using ClangSharp

## Core features

- Auto-generated using LLVM C headers files, and supports all functionality exposed by them (more than enough to build a full compiler): Auto-generated using LLVM C headers files, and supports all functionality exposed by them (more than enough to build a full compiler)
  - Evidence: README.md#Features
- Type safe (LLVMValueRef and LLVMTypeRef are different types, despite being pointers internally): Type safe (LLVMValueRef and LLVMTypeRef are different types, despite being pointers internally)
  - Evidence: README.md#Features
- Nearly identical to LLVM C APIs, e.g. LLVMModuleCreateWithName in C, vs. LLVM.ModuleCreateWithName (notice the . in the C# API): Nearly identical to LLVM C APIs, e.g. LLVMModuleCreateWithName in C, vs. LLVM.ModuleCreateWithName (notice the . in the C# API)
  - Evidence: README.md#Features

## Technology stack

- Languages: C#, C++, Shell, C, PowerShell, CMake, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: build.sh, pack.sh, restore.sh, samples/KaleidoscopeTutorial/Chapter3/CodeGenVisitor.cs

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/dotnet/LLVMSharp/blob/main/README.md
- README SHA: 889339572a92b0a8930575743ed6f9b7f608b174
- Manifests: CMakeLists.txt, sources/CMakeLists.txt, sources/libLLVMSharp/CMakeLists.txt
- Sampled source files: build.sh, pack.sh, restore.sh, samples/KaleidoscopeTutorial/Chapter3/CodeGenVisitor.cs
- Git tree state: captured
- Evidence fingerprint: 61efea6a7a7bb4d033b7473a245b62143169b775b7fcc0e92f1b5c20f52270d9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
