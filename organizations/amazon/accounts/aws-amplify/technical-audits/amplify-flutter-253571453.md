# aws-amplify/amplify-flutter

- Company: Amazon
- Account: aws-amplify
- Repository: https://github.com/aws-amplify/amplify-flutter
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T06:56:36+00:00

## Project purpose

AWS Amplify provides a declarative and easy-to-use interface across different categories of cloud operations. Our default implementation works with Amazon Web Services (AWS), but AWS Amplify is designed to be open and pluggable for any custom backend or service. See AWS Amplify for further details about the Amplify Framework.

## Why this project is used

A declarative library with an easy-to-use interface for building Flutter applications on AWS.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Dart, Swift, Kotlin, TypeScript, Shell, JavaScript, C++, CMake, HTML, Java, Python, Objective-C, Smithy, Ruby, PowerShell, C, Makefile, CSS, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @actions/exec, @actions/github, @actions/http-client, @actions/tool-cache, @aws-amplify/backend, @aws-amplify/backend-cli, @aws-crypto/client-node, @aws-sdk/client-amplify, @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-s3, @types/aws-lambda, @types/babel__traverse, @types/jest, @types/node, @vercel/ncc, aws-amplify, aws-cdk, aws-cdk-lib, constructs, esbuild, infra-common, jest, node-fetch, source-map-support, ts-jest, ts-node, tsx, typescript
- Build/package tools: Gradle build file, Docker build configuration, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: canaries/amplify/backend/function/canaries741cf74ePreSignup/src/index.js, infra-gen2/infra-common/src/index.ts, packages/amplify/amplify_flutter/example/windows/runner/main.cpp, packages/analytics/amplify_analytics_pinpoint/example/windows/runner/main.cpp

## Setup and usage

- Getting Started With Amplify Flutter: 1. Open your Flutter project. If you do not have an active Flutter project, you can create one after installing the Flutter development tooling and running flutter create in your terminal.
- Getting Started With Amplify Flutter: 2. Run the following to create an amplify project:
- Getting Started With Amplify Flutter: npm create amplify@latest -y
- Getting Started With Amplify Flutter: 4. To use the Authenticator, you need to add the following dependencies to your project:
- Getting Started With Amplify Flutter: amplify_auth_cognito: ^2.0.0
- Getting Started With Amplify Flutter: amplify_authenticator: ^2.0.0
- Getting Started With Amplify Flutter: amplify_flutter: ^2.0.0
- Getting Started With Amplify Flutter: 5. run flutter pub get

## Limitations and caveats

- Category / Platform Support: | Category | Android | iOS | Web | Windows | MacOS | Linux |
- Category / Platform Support: | -------------- | :-----: | :-: | :-: | :-----: | :---: | :---: |
- Category / Platform Support: | Analytics | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
- Category / Platform Support: | API (REST) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
- Category / Platform Support: | API (GraphQL) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
- Category / Platform Support: | Authentication | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
- Category / Platform Support: | DataStore | ✅ | ✅ | 🔴 | 🔴 | 🔴 | 🔴 |
- Category / Platform Support: | Storage | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Evidence and provenance

- README: https://github.com/aws-amplify/amplify-flutter/blob/main/README.md
- README SHA: d5230187e0cd58c00816e5ae6f28fc26d9fee03f
- Manifests: .devcontainer/Dockerfile, actions/package.json, infra-gen2/package.json, infra/package.json, canaries/android/build.gradle, infra-gen2/infra-common/package.json
- Sampled source files: canaries/amplify/backend/function/canaries741cf74ePreSignup/src/index.js, infra-gen2/infra-common/src/index.ts, packages/amplify/amplify_flutter/example/windows/runner/main.cpp, packages/analytics/amplify_analytics_pinpoint/example/windows/runner/main.cpp
- Git tree state: captured
- Evidence fingerprint: ea03683fb2ec3b4a38e9d2c3362883968d8feaf0db1d3dc6e235aac217df7d1e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
