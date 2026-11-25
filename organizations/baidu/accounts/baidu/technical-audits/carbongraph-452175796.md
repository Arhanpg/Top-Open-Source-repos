# baidu/CarbonGraph

- Company: Baidu
- Account: baidu
- Repository: https://github.com/baidu/CarbonGraph
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:55:21+00:00

## Project purpose

CarbonGraph is a Swift dependency injection / lookup framework for iOS. You can use it to build loose coupling between modules.

## Why this project is used

A Swift dependency injection / lookup framework for iOS

## Core features

- [x] Complete dependency injection capabilities: [x] Complete dependency injection capabilities
  - Evidence: README.md#Features
- [x] Complete Objective-C support: [x] Complete Objective-C support
  - Evidence: README.md#Features
- [x] Convenient object definition DSL: [x] Convenient object definition DSL
  - Evidence: README.md#Features
- [x] High-performance thread-safe solution: [x] High-performance thread-safe solution
  - Evidence: README.md#Features
- [x] Support resolving native Swift types: [x] Support resolving native Swift types
  - Evidence: README.md#Features
- [x] Support resolving with external parameters: [x] Support resolving with external parameters
  - Evidence: README.md#Features
- [x] Support resolving with circular dependencies: [x] Support resolving with circular dependencies
  - Evidence: README.md#Features
- [x] Automatic scanning of configuration: [x] Automatic scanning of configuration
  - Evidence: README.md#Features
- [x] Additional module life cycle management capabilities: [x] Additional module life cycle management capabilities
  - Evidence: README.md#Features

## Technology stack

- Languages: Swift, Objective-C, Ruby, C
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Bundler manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: CarbonCore/CarbonCore/ApplicationContext/Application.swift, CarbonCore/CarbonCore/ApplicationContext/ApplicationContext.swift, CarbonCore/CarbonCore/ApplicationContext/Module.swift, CarbonCore/CarbonCore/ApplicationContext/ModuleDelegate.swift

## Setup and usage

- Installation: CocoaPods is a dependency manager for Cocoa projects. For usage and installation instructions, visit their website. To integrate CarbonGraph into your Xcode project using CocoaPods, specify it in your Podfile:
- Installation: > pod 'CarbonCore', '~> 1.3.3'
- Quick Start: * Basic object registration and resolving
- Quick Start: let context = ObjectContext()
- Quick Start: let definitionBuilder = Definition("filevc")
- Quick Start: .protocol(UIViewController.self)
- Quick Start: .object(FileViewController())
- Quick Start: context.register(builder: definitionBuilder)

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/baidu/CarbonGraph/blob/main/README.md
- README SHA: a0075acef7dc4f5905dea2a5a07b1583e0966ba0
- Manifests: Example/Netdisk/Gemfile
- Sampled source files: CarbonCore/CarbonCore/ApplicationContext/Application.swift, CarbonCore/CarbonCore/ApplicationContext/ApplicationContext.swift, CarbonCore/CarbonCore/ApplicationContext/Module.swift, CarbonCore/CarbonCore/ApplicationContext/ModuleDelegate.swift
- Git tree state: captured
- Evidence fingerprint: d334233c8e7b09d47bf3e02eb513dc9a5e2cb838a493af6091752e9bf73edeba

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
