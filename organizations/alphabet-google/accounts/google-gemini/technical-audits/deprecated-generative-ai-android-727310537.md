# google-gemini/deprecated-generative-ai-android

- Company: Alphabet (Google)
- Account: google-gemini
- Repository: https://github.com/google-gemini/deprecated-generative-ai-android
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:37:57+00:00

## Project purpose

With Gemini 2.0, we took the chance to create a unified SDK for mobile developers who want to use Google's GenAI models (Gemini, Veo, Imagen, etc). As part of that process, we took all of the feedback from this SDK and what developers like about other SDKs in the ecosystem to directly work with the Firebase SDK. We don't plan to add anything to this SDK or making any further changes. We know how disruptive an SDK change can be and don't take this change lightly, but our goal is to create an extremely simple and clear path for developers to build with our models so it felt necessary to make this change.

## Why this project is used

This SDK is now deprecated, use the unified Firebase SDK.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Kotlin, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle Kotlin build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: common/src/main/kotlin/com/google/ai/client/generativeai/common/APIController.kt, common/src/main/kotlin/com/google/ai/client/generativeai/common/client/Types.kt, common/src/main/kotlin/com/google/ai/client/generativeai/common/Exceptions.kt, common/src/main/kotlin/com/google/ai/client/generativeai/common/Request.kt

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/google-gemini/deprecated-generative-ai-android/blob/main/README.md
- README SHA: 4464de79fe781aa198d0adeb9839a0e937be1549
- Manifests: build.gradle.kts, common/build.gradle.kts, generativeai-android-sample/build.gradle.kts, generativeai/build.gradle.kts, plugins/build.gradle.kts, generativeai-android-sample/app/build.gradle.kts
- Sampled source files: common/src/main/kotlin/com/google/ai/client/generativeai/common/APIController.kt, common/src/main/kotlin/com/google/ai/client/generativeai/common/client/Types.kt, common/src/main/kotlin/com/google/ai/client/generativeai/common/Exceptions.kt, common/src/main/kotlin/com/google/ai/client/generativeai/common/Request.kt
- Git tree state: captured
- Evidence fingerprint: 3a843ce1e13de5597e495a8a8986c94c27a4f9ce9ba155a0c1c140263815bc72

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
