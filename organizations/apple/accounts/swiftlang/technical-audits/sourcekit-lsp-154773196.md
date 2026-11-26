# swiftlang/sourcekit-lsp

- Company: Apple
- Account: swiftlang
- Repository: https://github.com/swiftlang/sourcekit-lsp
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:34:13+00:00

## Project purpose

SourceKit-LSP is an implementation of the Language Server Protocol (LSP) for Swift and C-based languages. It provides intelligent editor functionality like code-completion and jump-to-definition to editors that support LSP. SourceKit-LSP is built on top of sourcekitd and clangd for high-fidelity language support, and provides a powerful source code index as well as cross-language support. SourceKit-LSP supports projects that use the Swift Package Manager and projects that generate a compile_commands.json file, such as CMake.

## Why this project is used

Language Server Protocol implementation for Swift and C-based languages

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Swift, C, Python, CMake, Dockerfile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: CMake configuration, Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: Package.swift, SourceKitLSPDevUtils/Package.swift, SourceKitLSPDevUtils/Sources/ConfigSchemaGen/ConfigSchemaGen.swift, SourceKitLSPDevUtils/Sources/ConfigSchemaGen/JSONSchema.swift

## Setup and usage

- Getting Started: SourceKit-LSP is included in the Swift toolchains available on swift.org and is bundled with Xcode.
- Getting Started: swift.org/tools has a list of popular editors that support LSP and can thus be hooked up to SourceKit-LSP to provide intelligent editor functionality as well as set-up guides.
- Getting Started: > SourceKit-LSP does not update its global index in the background or build Swift modules in the background. Thus, a lot of cross-module or global functionality is limited if the project hasn't been built recently. To update the index or rebuild the Swift modules, build your project or enable the experimental background indexing as described in Ena
- Getting Started: To learn more about SourceKit-LSP, refer to the Documentation.
- Getting Started: > If you are using SourceKit-LSP with a SwiftPM project in which you need to pass additional arguments to the swift build invocation, as is commonly the case for embedded projects, you need to teach SourceKit-LSP about those arguments as described in Using SourceKit-LSP with Embedded Projects.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/swiftlang/sourcekit-lsp/blob/main/README.md
- README SHA: 0185d7ba399916796618ea92ee7863e331155a74
- Manifests: CMakeLists.txt, Sources/CMakeLists.txt, .devcontainer/default/Dockerfile, Sources/BuildServerIntegration/CMakeLists.txt, Sources/CCompletionScoring/CMakeLists.txt, Sources/ClangLanguageService/CMakeLists.txt
- Sampled source files: Package.swift, SourceKitLSPDevUtils/Package.swift, SourceKitLSPDevUtils/Sources/ConfigSchemaGen/ConfigSchemaGen.swift, SourceKitLSPDevUtils/Sources/ConfigSchemaGen/JSONSchema.swift
- Git tree state: captured
- Evidence fingerprint: 458a09e3017a8b470cef89383eaf14053ac249cf5354bc24f3fa616140c377dc

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
