# amazon-connect/amazon-connect-in-app-calling-examples

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/amazon-connect-in-app-calling-examples
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:38:21+00:00

## Project purpose

Amazon Connect's out of the box communication widget and agent workspace allow you to add in-app, web, and video calling capabilities to your website or mobile application with a few lines of code. This repository contains examples of: 1) how to create multi-user web and video calling experiences, 2) how to integrate in-app calling into iOS and Android applications, 3) an example backend that works with these iOS and Android mobile samples, and 4) while web calling works out of the box with custom CCPs for voice call, we show to integrate video calling into an custom CCP.

## Why this project is used

Amazon Connect's out of the box communication widget and agent workspace allow you to add in-app, web, and video calling capabilities to your website or mobile application with a few lines of code. This repository contains examples of: 1) how to create multi-user web and video calling experiences, 2) how to integrate in-app calling into iOS and Android applications, 3) an example backend that works with these iOS and Android mobile samples, and 4) while web calling works out of the box with custom CCPs for voice call, we show to integrate video calling into an custom CCP.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Swift, JavaScript, Kotlin, TypeScript, Shell, CSS, HTML, Ruby
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-sdk/client-connect, @aws-sdk/client-connectparticipant, @aws-sdk/client-dynamodb, @aws-sdk/lib-dynamodb, @types/aws-lambda, @types/node, amazon-chime-sdk-js, amazon-connect-streams, aws-cdk, aws-cdk-lib, concurrently, constructs, cors, dotenv, esbuild, esbuild-plugins-node-modules-polyfill, express, nodemon, source-map-support, ts-node, typescript, uuid
- Build/package tools: Gradle build file, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: Web/amazon-connect-multi-user-web-calling-sample/server/index.js, Web/amazon-connect-multi-user-web-calling-sample/client/index.js, Android/AmazonConnectInAppCallingAndroidSample/app/src/main/java/com/amazonaws/services/connect/inappcalling/sample/CallConfiguration.kt, Android/AmazonConnectInAppCallingAndroidSample/app/src/main/java/com/amazonaws/services/connect/inappcalling/sample/common/Extensions.kt

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-connect/amazon-connect-in-app-calling-examples/blob/main/README.md
- README SHA: 9770d2abfaa3185bc86892a6796824a94791af2a
- Manifests: Android/AmazonConnectInAppCallingAndroidSample/build.gradle, Backend/AmazonConnectNetraApiSample/package.json, Web/amazon-connect-ccp-web-calling-example/package.json, Web/amazon-connect-multi-user-web-calling-sample/package.json, Android/AmazonConnectInAppCallingAndroidSample/app/build.gradle, Backend/AmazonConnectNetraApiSample/lambda/package.json
- Sampled source files: Web/amazon-connect-multi-user-web-calling-sample/server/index.js, Web/amazon-connect-multi-user-web-calling-sample/client/index.js, Android/AmazonConnectInAppCallingAndroidSample/app/src/main/java/com/amazonaws/services/connect/inappcalling/sample/CallConfiguration.kt, Android/AmazonConnectInAppCallingAndroidSample/app/src/main/java/com/amazonaws/services/connect/inappcalling/sample/common/Extensions.kt
- Git tree state: captured
- Evidence fingerprint: aa589390c9f431004b434c839f72e19b09f7e00643f4c1556f370e50f55be645

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
