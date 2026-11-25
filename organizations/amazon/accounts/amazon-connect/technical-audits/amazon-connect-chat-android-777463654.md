# amazon-connect/amazon-connect-chat-android

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/amazon-connect-chat-android
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:28:27+00:00

## Project purpose

The Amazon Connect Chat SDK for Android is a Kotlin library that gives you the power to easily integrate Amazon Connect Chat directly into your native Android applications. The Amazon Connect Chat SDK helps handle client side chat logic and back-end communications similar to the Amazon Connect ChatJS Library. The SDK wraps the Amazon Connect Participant Service APIs and abstracts away the management of the chat session and WebSocket. This allows you to focus on the user interface and experience while relying on the Amazon Connect Chat SDK to interact with all the back-end services. This approach still requires using your own chat back end to call the Amazon Connect StartChatContact API to initiate contact. You can read instructions on how to quickly set up a StartChatContact Lambda from our startChatContactAPI example.

## Why this project is used

Amazon Connect Chat SDK for Android

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Kotlin
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle Kotlin build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: app/src/androidTest/java/com/amazon/connect/chat/androidchatexample/ExampleInstrumentedTest.kt, app/src/main/java/com/amazon/connect/chat/androidchatexample/ChatApplication.kt, app/src/main/java/com/amazon/connect/chat/androidchatexample/Config.kt, app/src/main/java/com/amazon/connect/chat/androidchatexample/di/AppModule.kt

## Setup and usage

- Installation Steps: There are two options to install the Amazon Connect Chat SDK for Android to your project:
- Getting Started: The first step to leveraging the Amazon Connect Chat SDK after installation is to import the library into your file. Next, let's call the StartChatContact API and pass the response details into the SDK’s ChatSession object. For reference, you can visit the AndroidChatExample demo within the Amazon Connect Chat UI Examples GitHub repository.
- Getting Started: The majority of the SDKs functionality will be accessed through the ChatSession object. In order to use this object in the file, you can inject it using @HiltViewModel:
- Getting Started: class ChatViewModel @Inject constructor(
- Getting Started: private val chatSession: ChatSession, // Injected ChatSession
- Getting Started: private val chatRepository: ChatRepository,
- Getting Started: private val sharedPreferences: SharedPreferences,
- Getting Started: If you are not using Hilt, then you can initialise ChatSession like this:

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/amazon-connect/amazon-connect-chat-android/blob/main/README.md
- README SHA: 72db513f6cc2a3ea564c5a678c0e3ce151f72cb4
- Manifests: build.gradle.kts, app/build.gradle.kts, chat-sdk/build.gradle.kts
- Sampled source files: app/src/androidTest/java/com/amazon/connect/chat/androidchatexample/ExampleInstrumentedTest.kt, app/src/main/java/com/amazon/connect/chat/androidchatexample/ChatApplication.kt, app/src/main/java/com/amazon/connect/chat/androidchatexample/Config.kt, app/src/main/java/com/amazon/connect/chat/androidchatexample/di/AppModule.kt
- Git tree state: captured
- Evidence fingerprint: bcd817b3f3d06c7ecee280d59df34b8d0046c2cea1e02516880968589218203c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
