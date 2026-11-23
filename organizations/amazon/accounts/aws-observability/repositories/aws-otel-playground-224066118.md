# aws-observability/aws-otel-playground

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-playground](https://github.com/aws-observability/aws-otel-playground)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-playground/blob/main/README.md)
- README blob SHA: 6ec2b430b15d7d3b70ef1b7dafab204b57e6e20a
- Repository ID: 224066118
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sample Application for the AWS X-Ray SDK with support for OpenTelemetry

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:14:15+00:00

### Short excerpt (up to 100 words)

> This repository contains a toy application which exhibits a simple yet somewhat representative trace, including AWS SDK calls, a frontend and backend, and HTTP and gRPC. The same application is instrumented in several ways, allowing us to compare the experience when viewing traces for the different types of instrumentation. Current instrumentation includes - OpenTelemetry Auto Instrumentation + OpenTelemetry Collector - X-Ray SDK Instrumentation + X-Ray Daemon - Does not instrument many libraries like gRPC and Lettuce The playground access various endpoints hosted on AWS. Feel free to skip this section to just see traces with local endpoints. To set up

### README headings

- X-Ray Instrumentation Playground
- Setting up AWS resources
- Running
- Cleaning up
- How it works
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 25,667 |
| HCL | 21,780 |
| Kotlin | 11,558 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle.kts (capture: captured)
- api/build.gradle.kts (capture: captured)
- appdb/build.gradle.kts (capture: captured)
- backend-webflux/build.gradle.kts (capture: captured)
- backend/build.gradle.kts (capture: captured)
- dependencyManagement/build.gradle.kts (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 35
- Forks at capture: 14
- Last updated: 2026-08-05T00:00:32Z
- Last pushed: 2023-09-05T22:15:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-playground)
- [README](https://github.com/aws-observability/aws-otel-playground/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-playground/issues)
- [Releases](https://github.com/aws-observability/aws-otel-playground/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
