# model-checking/kani-vscode-extension

- Company: Amazon
- Account: model-checking
- Repository: https://github.com/model-checking/kani-vscode-extension
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T23:02:42+00:00

## Project purpose

A Visual Studio Code extension that allows users to run and debug their Kani Rust Verifier harnesses in VS Code.

## Why this project is used

Kani VSCode Extension

## Core features

- Automatically indexes and shows Kani harnesses in a tree view.: Automatically indexes and shows Kani harnesses in a tree view.
  - Evidence: README.md#Features
- One-click button for verifying Kani harnesses.: One-click button for verifying Kani harnesses.
  - Evidence: README.md#Features
- Generate counterexamples as Rust unit tests.: Generate counterexamples as Rust unit tests.
  - Evidence: README.md#Features
- Debug counterexamples using a standard debugger.: Debug counterexamples using a standard debugger.
  - Evidence: README.md#Features
- View coverage information inline using VS Code source highlighting.: View coverage information inline using VS Code source highlighting.
  - Evidence: README.md#Features

## Technology stack

- Languages: TypeScript, JavaScript, Python, Rust, Shell, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: @types/emscripten, @types/mocha, @types/node, @types/vscode, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vscode/test-electron, esbuild, eslint, eslint-config-love, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-header, eslint-plugin-import, eslint-plugin-n, eslint-plugin-no-null, eslint-plugin-prettier, eslint-plugin-promise, glob, mocha, prettier, readline, toml, typescript, web-tree-sitter
- Build/package tools: Cargo manifest, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: resources/test-crates/simple-test/src/lib.rs, resources/test-crates/simple-test/src/funs.rs, src/constants.ts, src/debugger/debugger.ts

## Setup and usage

- Usage: 1. Open a Rust package in Visual Studio Code.
- Usage: 2. Navigate to the testing panel and expand on the Kani harness tree view where the harnesses are shown.
- Usage: 3. Click on the play button beside the harness or the filename or the crate to run Kani on the respective test case.
- Usage: Check user guide for more detailed information.
- Installation: The Kani VSCode Extension is available as a VSCode plugin. You can install the Kani VSCode Extension from the Visual Studio Marketplace.
- Installation: If you want to build and package from source directly, see dev-documentation for more information.

## Limitations and caveats

- Security: See SECURITY for more information.

## Evidence and provenance

- README: https://github.com/model-checking/kani-vscode-extension/blob/main/README.md
- README SHA: 3f742d204aa377e6ade831a0fd17a93b6881b1c1
- Manifests: makefile, package.json, resources/test-crates/simple-test/Cargo.toml
- Sampled source files: resources/test-crates/simple-test/src/lib.rs, resources/test-crates/simple-test/src/funs.rs, src/constants.ts, src/debugger/debugger.ts
- Git tree state: captured
- Evidence fingerprint: 34446b6d58ce57a79a57c7a0d305219d579324b2d01c616f1b6c952736265a41

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
