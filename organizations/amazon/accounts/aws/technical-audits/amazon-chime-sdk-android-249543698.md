# aws/amazon-chime-sdk-android

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/amazon-chime-sdk-android
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:12:01+00:00

## Project purpose

Amazon Chime SDK Project Board

## Why this project is used

An Android client library for integrating multi-party communications powered by the Amazon Chime service.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Kotlin, Java, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: amazon-chime-sdk/src/androidTest/java/com/amazonaws/services/chime/sdk/meetings/audiovideo/video/backgroundfilter/BackgroundFilterVideoFrameProcessorTest.kt, amazon-chime-sdk/src/androidTest/java/com/amazonaws/services/chime/sdk/meetings/internal/utils/SQLiteDatabaseManagerIntegrationTests.kt, amazon-chime-sdk/src/main/java/com/amazonaws/services/chime/sdk/meetings/analytics/DefaultEventAnalyticsController.kt, amazon-chime-sdk/src/main/java/com/amazonaws/services/chime/sdk/meetings/analytics/DefaultMeetingStatsCollector.kt

## Setup and usage

- Usage examples: > Replace with the latest version from the latest release.
- Usage: - Screen and content share
- Usage: - Custom Video Source
- Usage: - Background Blur and Replacement

## Limitations and caveats

- Java Compatibility: For Java 17 compatibility, add this inside your app/build.gradle:
- Java Compatibility: sourceCompatibility JavaVersion.VERSION_17
- Java Compatibility: targetCompatibility JavaVersion.VERSION_17

## Evidence and provenance

- README: https://github.com/aws/amazon-chime-sdk-android/blob/master/README.md
- README SHA: 3f2c9ff1037b0be6581c2924b2f150a1b6df0856
- Manifests: build.gradle, amazon-chime-sdk/build.gradle, app/build.gradle
- Sampled source files: amazon-chime-sdk/src/androidTest/java/com/amazonaws/services/chime/sdk/meetings/audiovideo/video/backgroundfilter/BackgroundFilterVideoFrameProcessorTest.kt, amazon-chime-sdk/src/androidTest/java/com/amazonaws/services/chime/sdk/meetings/internal/utils/SQLiteDatabaseManagerIntegrationTests.kt, amazon-chime-sdk/src/main/java/com/amazonaws/services/chime/sdk/meetings/analytics/DefaultEventAnalyticsController.kt, amazon-chime-sdk/src/main/java/com/amazonaws/services/chime/sdk/meetings/analytics/DefaultMeetingStatsCollector.kt
- Git tree state: captured
- Evidence fingerprint: 3bed74a9f8784d317ebda90f2a0945c1dd3b77e7c32dd7ca5cbc0b9c918256fc

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
