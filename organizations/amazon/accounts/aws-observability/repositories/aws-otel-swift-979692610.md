# aws-observability/aws-otel-swift

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-swift](https://github.com/aws-observability/aws-otel-swift)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-swift/blob/main/README.md)
- README blob SHA: eb0ebebc1d1603bfbeda5e7d530ea6ede6e54814
- Repository ID: 979692610
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:14:23+00:00

### Short excerpt (up to 100 words)

> AWS Distro for OpenTelemetry (ADOT) Swift is a redistribution of the OpenTelemetry Swift, configured with in-house instrumentations to use with AWS CloudWatch Real User Monitoring. At this time, we only officially support iOS 16+. However, we also have continuation integration in place for latest versions of macOS, tvOS, watchOS, and visionOS. Add the following to your `Package.swift` file: dependencies: [ .package(url: "https://github.com/aws-observability/aws-otel-swift.git", .upToNextMajor(from: "1.0.0")) ] At this time, Cocoapods distribution is not supported. Please open an issue to get this work prioritized. Add `AwsOpenTelemetryAgent` to target dependencies. This will automatically setup the AWS OTel agent using `AwsOpenTelemetryCore` as a transitive

### README headings

- AWS Distro for OpenTelemetry for Swift
- Feature Support
- Available Platforms
- Available Instrumentations
- Available Metadata
- Getting Started
- Installation
- Swift Package Manager (SPM)
- Cocoapods
- Zero-Code Initialization
- Manual Initialization
- Configuration
- Root Configuration
- AwsConfig
- AwsExportOverride
- AwsTelemetryConfig
- Export Strategy
- Default Export Behavior
- SigV4 Authentication
- Crash Report Symbolication
- Custom Events
- Custom Span Example
- Custom Log Example
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Swift | 637,932 |
| Shell | 110,072 |
| Python | 23,466 |
| Makefile | 7,283 |
| Objective-C | 5,359 |
| JavaScript | 3,230 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- Examples/AwsOtelUI/package.json (capture: captured) — dependency clues: @opentelemetry/otlp-transformer, compression, express, open, protobufjs
- Examples/SimpleAwsDemo/Makefile (capture: captured)
- Examples/SimpleAwsDemo/SimpleAwsDemo/cdk/package.json (capture: captured) — dependency clues: @types/jest, @types/node, aws-cdk, aws-cdk-lib, constructs, jest, source-map-support, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 8
- Forks at capture: 10
- Last updated: 2026-09-15T23:00:25Z
- Last pushed: 2026-08-24T17:39:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-swift)
- [README](https://github.com/aws-observability/aws-otel-swift/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-swift/issues)
- [Releases](https://github.com/aws-observability/aws-otel-swift/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
