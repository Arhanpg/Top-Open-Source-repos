# apple/FHIRModels

- Company: Apple
- Account: apple
- Repository: https://github.com/apple/FHIRModels
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:06:53+00:00

## Project purpose

FHIRModels ==========

## Why this project is used

Swift library for FHIR® resource data models

## Core features

- Native Swift representation of FHIR resources, elements and data types: Native Swift representation of FHIR resources, elements and data types
  - Evidence: README.md#Features
- Separate targets for DSTU2, STU3, R4, R4B, R5 and latest build versions: Separate targets for DSTU2, STU3, R4, R4B, R5 and latest build versions
  - Evidence: README.md#Features
- Enforced non-nullability of mandatory parameters: Enforced non-nullability of mandatory parameters
  - Evidence: README.md#Features
- Enums for most closed code systems: Enums for most closed code systems
  - Evidence: README.md#Features
- Enums to support value[x] types: Enums to support value[x] types
  - Evidence: README.md#Features
- Date/Time parsing, validation and conversion to and from NSDate: Date/Time parsing, validation and conversion to and from NSDate
  - Evidence: README.md#Features
- Swift Codable and Sendable: Swift Codable and Sendable
  - Evidence: README.md#Features

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

Architecture is not interpreted in evidence-only mode. Sampled source files: Package.swift, Sources/FMCore/ConstructibleFromNSDate.swift, Sources/FMCore/DecodingError+Utilities.swift, Sources/FMCore/ExpressibleAsNSDate.swift

## Setup and usage

- Installation: [Swift Package Manager][spm] is the recommended way to add FHIRModels to your project:
- Installation: 1. In Xcode 11 and newer, go to “File” » “Add Package Dependencies...”
- Installation: 2. Search for “FHIRModels” in the panel that comes up or paste the full URL to the GitHub repository, then select the package
- Installation: 3. Pick the versioning that best works for you (usually the current version and “up to next major”)
- Installation: 4. In order to update the dependency, periodically select “Update to Latest Package Versions” from Xcode's “File” » ”Packages” menu
- Installation: Alternatively, you can add FHIRModels to your Package.swift file as a dependency:
- Installation: .package(url: "https://github.com/apple/FHIRModels.git",
- Installation: .upToNextMajor(from: "0.9.4"))

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/apple/FHIRModels/blob/main/README.md
- README SHA: 4ac2766113f2eb93099c621f1704a6d8ec2bc8cb
- Manifests: none
- Sampled source files: Package.swift, Sources/FMCore/ConstructibleFromNSDate.swift, Sources/FMCore/DecodingError+Utilities.swift, Sources/FMCore/ExpressibleAsNSDate.swift
- Git tree state: captured
- Evidence fingerprint: 28c5a25eb8126e8c32bc9fd9dde5ac30c65730fb29ea4ae46183a15ecd2601ed

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
