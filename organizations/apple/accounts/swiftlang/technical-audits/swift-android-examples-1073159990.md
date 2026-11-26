# swiftlang/swift-android-examples

- Company: Apple
- Account: swiftlang
- Repository: https://github.com/swiftlang/swift-android-examples
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:55:01+00:00

## Project purpose

This repository contains example applications that demonstrate how to use the Swift SDK for Android. Each example showcases different integration patterns for Swift on Android.

## Why this project is used

This repository contains example applications that demonstrate how to use the Swift SDK for Android. Each example showcases different integration patterns for Swift on Android.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C, Kotlin, Swift, Shell, C++, CMake
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle Kotlin build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: hello-cpp-swift/app/src/main/java/com/example/hellocppswift/MainActivity.kt, hello-cpp-swift/cpp-lib/src/calculator.cpp, hello-swift-java/hashing-app/src/androidTest/java/com/example/hashingapp/ExampleInstrumentedTest.kt, hello-swift-java/hashing-app/src/main/java/com/example/hashingapp/MainActivity.kt

## Setup and usage

- Getting Started: The **hello-swift-java** example is the recommended
- Getting Started: approach for integrating Swift into Android applications. This example
- Getting Started: demonstrates how to build a Swift library that can be seamlessly called from
- Getting Started: Kotlin/Java code using swift-java,
- Getting Started: which automatically generates the necessary Java wrappers and JNI bindings for
- Getting Started: The example consists of two components:
- Getting Started: - **hashing-lib**: A Swift package that uses swift-crypto to provide SHA256
- Getting Started: hashing functionality

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/swiftlang/swift-android-examples/blob/main/README.md
- README SHA: 28b81329aa42bbdcf36b274a8cbd6cc221259d6d
- Manifests: build.gradle.kts, hello-swift-raw-jni-callback/build.gradle.kts, hello-swift-raw-jni-library/build.gradle.kts, hello-swift-raw-jni/build.gradle.kts, native-activity/build.gradle.kts, hello-cpp-swift/app/build.gradle.kts
- Sampled source files: hello-cpp-swift/app/src/main/java/com/example/hellocppswift/MainActivity.kt, hello-cpp-swift/cpp-lib/src/calculator.cpp, hello-swift-java/hashing-app/src/androidTest/java/com/example/hashingapp/ExampleInstrumentedTest.kt, hello-swift-java/hashing-app/src/main/java/com/example/hashingapp/MainActivity.kt
- Git tree state: captured
- Evidence fingerprint: 41fd7e3cfa8ab6d59476db76f53a0a8edd16ab56a08b72f4c674a385555d77b8

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
