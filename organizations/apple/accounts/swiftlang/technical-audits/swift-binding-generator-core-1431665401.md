# swiftlang/swift-binding-generator-core

- Company: Apple
- Account: swiftlang
- Repository: https://github.com/swiftlang/swift-binding-generator-core
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:07:36+00:00

## Project purpose

Shared, reusable, target-language agnostic core libraries useful for building Swift language interop binding generators, such as swift-java and JavaScriptKit and more.

## Why this project is used

Shared, reusable, target-language agnostic core libraries useful for building Swift language interop binding generators, such as swift-java and JavaScriptKit and more.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Swift
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: .github/scripts/install_swiftly.sh, .github/scripts/test_swift_java.sh, Package.swift, Plugins/_StaticBuildConfigPlugin/_StaticBuildConfigPlugin.swift

## Setup and usage

No setup information established.

## Limitations and caveats

- Source Compatibility: This package does not offer strict source stable API, however we make effort to either not break, or update consumers of the library when changes are made here.
- Source Compatibility: This is verified with CI checking downstream consumers: swift-java, JavaScriptKit etc. This approach is beneficial to quick iteration and supporting a limited
- Source Compatibility: set of official language interop libraries and tools, without locking down the API.
- Source Compatibility: If you are maintaining another language target, please reach out and we'll work out a way to collaborate.
- Source Compatibility: In the future we may consider a stricter source compatibility guarantee.

## Evidence and provenance

- README: https://github.com/swiftlang/swift-binding-generator-core/blob/main/README.md
- README SHA: 5d5daf930e1b86cca9ade5b5656a915b3ef6b2a4
- Manifests: none
- Sampled source files: .github/scripts/install_swiftly.sh, .github/scripts/test_swift_java.sh, Package.swift, Plugins/_StaticBuildConfigPlugin/_StaticBuildConfigPlugin.swift
- Git tree state: captured
- Evidence fingerprint: 0a5be1c832e8c63dca3e1a79e8aa0d64bb93b7a764235bed3394f8455bfd22cc

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
