# amazon-connect/touchpoint-ios

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/touchpoint-ios
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:07:59+00:00

## Project purpose

**Status: pre-release.** The public API will change without notice until a 1.0 release is tagged.

## Why this project is used

Amazon Connect Customer Touchpoint SDK for iOS: chat, in-app voice and Live Sync for Amazon Connect contact centres, as Swift packages.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Swift, Shell, Python, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: Package.swift, Scripts/check-api-breaks.sh, Scripts/check-build-graph.sh, Scripts/check-competing-pins.sh

## Setup and usage

- Installation: Add the package with Swift Package Manager and depend on the products you use:
- Installation: // Before 1.0.0 a minor release may change the API, so take patches only.
- Installation: .package(url: "https://github.com/amazon-connect/touchpoint-ios", .upToNextMinor(from: "0.1.0")),
- Installation: .target(name: "MyApp", dependencies: [
- Installation: .product(name: "TouchpointChat", package: "touchpoint-ios"),
- Installation: .product(name: "TouchpointVoice", package: "touchpoint-ios"), // only if you call
- Installation: .product(name: "TouchpointLiveSync", package: "touchpoint-ios"), // only if you use Live Sync
- Installation: The package depends on the Connect chat SDK, which is built on the AWS SDK for Swift:

## Limitations and caveats

- Security: To report a potential security issue, use the AWS
- Security: vulnerability reporting page; please do
- Security: **not** create a public GitHub issue. What the SDK protects, and what your app and backend must do, is
- Security: in the security guide.

## Evidence and provenance

- README: https://github.com/amazon-connect/touchpoint-ios/blob/main/README.md
- README SHA: f2b7f9ab66308ca483048cdacc5014eee449a883
- Manifests: Makefile
- Sampled source files: Package.swift, Scripts/check-api-breaks.sh, Scripts/check-build-graph.sh, Scripts/check-competing-pins.sh
- Git tree state: captured
- Evidence fingerprint: fb7f7377a6b1a3b761996942f3f54d063b6c5ad9a2a93a9d88edeb0036d7db79

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
