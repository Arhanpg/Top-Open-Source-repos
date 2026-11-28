# google/DirectXShaderCompiler

- Company: Alphabet (Google)
- Account: google
- Repository: https://github.com/google/DirectXShaderCompiler
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:55:13+00:00

## Project purpose

The DirectX Shader Compiler project includes a compiler and related tools used to compile High-Level Shader Language (HLSL) programs into DirectX Intermediate Language (DXIL) representation. Applications that make use of DirectX for graphics, games, and computation can use it to generate shader programs.

## Why this project is used

This repo hosts the source for the DirectX Shader Compiler which is based on LLVM/Clang.

## Core features

- dxc.exe, a command-line tool that can compile HLSL programs for shader model 6.0 or higher: dxc.exe, a command-line tool that can compile HLSL programs for shader model 6.0 or higher
  - Evidence: README.md#Features and Goals
- dxcompiler.dll, a DLL providing a componentized compiler, assembler, disassembler, and validator: dxcompiler.dll, a DLL providing a componentized compiler, assembler, disassembler, and validator
  - Evidence: README.md#Features and Goals
- dxilconv.dll, a DLL providing a converter from DXBC (older shader bytecode format): dxilconv.dll, a DLL providing a converter from DXBC (older shader bytecode format)
  - Evidence: README.md#Features and Goals
- various other tools based on the above components: various other tools based on the above components
  - Evidence: README.md#Features and Goals

## Technology stack

- Languages: C++, HLSL, LLVM, C, Python, C#, CMake, Objective-C, HTML, Shell, Batchfile, Assembly, Cuda, JavaScript, Perl, Emacs Lisp, Makefile, Roff, NASL, PowerShell, AppleScript, Pawn
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lib/TableGen/Main.cpp, tools/llvm-c-test/main.c, utils/llvm-build/llvmbuild/main.py, lib/Analysis/AliasAnalysis.cpp

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/google/DirectXShaderCompiler/blob/master/README.md
- README SHA: 506af319ca80c190df7ad7928874598652626705
- Manifests: CMakeLists.txt, docs/CMakeLists.txt, examples/CMakeLists.txt, external/CMakeLists.txt, lib/CMakeLists.txt, projects/CMakeLists.txt
- Sampled source files: lib/TableGen/Main.cpp, tools/llvm-c-test/main.c, utils/llvm-build/llvmbuild/main.py, lib/Analysis/AliasAnalysis.cpp
- Git tree state: captured
- Evidence fingerprint: 21dd99d187e9476d15f461c725237519f56575d7b11c2f73a2a1869f1316755f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
