# amazon-connect/amazon-connect-chat-ios

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/amazon-connect-chat-ios
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T22:51:36+00:00

## Project purpose

The Amazon Connect Chat SDK for iOS is a Swift library that gives you the power to easily integrate Amazon Connect Chat directly into your native iOS applications. The Amazon Connect Chat SDK helps handle client side chat logic and back-end communications similar to the Amazon Connect ChatJS Library. The SDK wraps the Amazon Connect Participant Service APIs and abstracts away the management of the chat session and WebSocket. This allows you to focus on the user interface and experience while relying on the Amazon Connect Chat SDK to interact with all the back-end services. This approach still requires using your own chat back end to call the Amazon Connect StartChatContact API to initiate contact. You can read instructions on how to quickly set up a StartChatContact Lambda from our startChatContactAPI example.

## Why this project is used

Amazon Connect Chat SDK for iOS

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Swift, Objective-C
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: AmazonConnectChatIOSTests/Core/Network/APIClientTests.swift, AmazonConnectChatIOSTests/Core/Network/AWSClientTests.swift, AmazonConnectChatIOSTests/Core/Network/MessageReceiptsManagerTests.swift, AmazonConnectChatIOSTests/Core/Network/Mocks/MockAPIClient.swift

## Setup and usage

- Installation Steps: Swift Package Manager is the supported installation method for Amazon Connect Chat SDK 3.0 and later. The SDK supports Xcode 26 or later and iOS 15 or later.
- Installation Steps: > ⚠️ **CocoaPods is no longer supported as of 3.0.** The SDK now depends on aws-sdk-swift, which does not publish podspecs, so it cannot be distributed through CocoaPods. See the 3.0 migration guide for how to move to Swift Package Manager.
- Getting Started: The first step to leveraging the Amazon Connect Chat SDK after installation is to import the library into your file. Next, let's call the StartChatContact API and pass the response details into the SDK’s ChatSession object. Here is an example of how we would set this up in Swift. For reference, you can visit the iOSChatExample demo within the Amazo
- Getting Started: The majority of the SDKs functionality will be accessed through the ChatSession object. In order to use this object in the file, we have to first import the AmazonConnectChatIOS library via:
- Getting Started: import AmazonConnectChatIOS
- Getting Started: Next, we can create a ChatManager class that helps bridge UI and SDK communication. This class should be responsible for managing interactions with the ChatSession object. We can either add it as a class property or reference it directly using ChatSession.shared.
- Getting Started: class ChatManager: ObservableObject {
- Getting Started: private var chatSession = ChatSession.shared

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/amazon-connect/amazon-connect-chat-ios/blob/main/README.md
- README SHA: 29f61ff77c52cbb0b87e6a5ac5e6f08fb8753cf8
- Manifests: none
- Sampled source files: AmazonConnectChatIOSTests/Core/Network/APIClientTests.swift, AmazonConnectChatIOSTests/Core/Network/AWSClientTests.swift, AmazonConnectChatIOSTests/Core/Network/MessageReceiptsManagerTests.swift, AmazonConnectChatIOSTests/Core/Network/Mocks/MockAPIClient.swift
- Git tree state: captured
- Evidence fingerprint: 73d6038203c473ebc3f227d53540e490fddf0338a9fa6d29214720da51d28852

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
