# swiftlang/llvm-project

- Company: Apple
- Account: swiftlang
- Repository: https://github.com/swiftlang/llvm-project
- Default branch: next
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T06:59:26+00:00

## Project purpose

This is Swift's fork of llvm-project. For more information on Swift's branching scheme, please see apple-docs/AppleBranchingScheme.md.

## Why this project is used

The LLVM Project is a collection of modular and reusable compiler and toolchain technologies.  This fork is used to manage Swift’s stable releases of Clang as well as support the Swift project.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: LLVM, C++, C, Assembly, MLIR, Python, Fortran, FIRRTL, CMake, Objective-C, HLSL, HTML, Starlark, HIP, Cuda, Objective-C++, SWIG, Swift, OCaml, JavaScript, Makefile, Shell, Perl, Awk, TypeScript, Pawn, Jupyter Notebook, Emacs Lisp, CSS, Roff, Batchfile, Mustache, Groovy, NASL, Vim Script, Dockerfile, Tree-sitter Query, Lua, M, GDB, Nix, Cool, Rust, MATLAB, Linker Script, TeX, AMPL, Go Template, Wolfram Language, AppleScript, POV-Ray SDL, DTrace, Limbo, PHP, RPC, Mercury
- Frameworks/libraries: Unknown / not established
- Dependency names: PyGithub, google-cloud-storage, junitparser
- Build/package tools: CMake configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: flang-rt/lib/runtime/main.cpp, flang/lib/Optimizer/Builder/Runtime/Main.cpp, bolt/utils/dot2html/__main__.py, clang-tools-extra/clang-doc/assets/index.js

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/swiftlang/llvm-project/blob/next/README.md
- README SHA: 5811635868237d7d59cf488c381718e5e29fb78a
- Manifests: .ci/requirements.txt, bolt/CMakeLists.txt, clang-tools-extra/CMakeLists.txt, clang/CMakeLists.txt, compiler-rt/CMakeLists.txt, cross-project-tests/CMakeLists.txt
- Sampled source files: flang-rt/lib/runtime/main.cpp, flang/lib/Optimizer/Builder/Runtime/Main.cpp, bolt/utils/dot2html/__main__.py, clang-tools-extra/clang-doc/assets/index.js
- Git tree state: captured
- Evidence fingerprint: 046fe2915a13b183a3eb7a148891d0b5adbad2c715e918a9897185cc01c8d32b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
