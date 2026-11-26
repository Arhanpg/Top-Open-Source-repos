# apple/app-store-server-library-java

- Company: Apple
- Account: apple
- Repository: https://github.com/apple/app-store-server-library-java
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:07:09+00:00

## Project purpose

The Java server library for the App Store Server API, App Store Server Notifications, Retention Messaging API, and Advanced Commerce API. Also available in Swift, Python, and Node.js.

## Why this project is used

The Java server library for the App Store Server API and App Store Server Notifications.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Java, Lua
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Gradle build file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/main/java/com/apple/itunes/storekit/advancedcommerce/AdvancedCommerceInAppSignatureCreator.java, src/main/java/com/apple/itunes/storekit/client/APIError.java, src/main/java/com/apple/itunes/storekit/client/APIException.java, src/main/java/com/apple/itunes/storekit/client/AppStoreServerAPIClient.java

## Setup and usage

- API Usage: import com.apple.itunes.storekit.client.APIException;
- API Usage: import com.apple.itunes.storekit.client.AppStoreServerAPIClient;
- API Usage: import com.apple.itunes.storekit.model.Environment;
- API Usage: import com.apple.itunes.storekit.model.SendTestNotificationResponse;
- API Usage: import java.io.IOException;
- API Usage: import java.nio.file.Files;
- API Usage: import java.nio.file.Path;
- API Usage: public class APIExample {

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/apple/app-store-server-library-java/blob/main/README.md
- README SHA: 640dc46e75d60c02dba76320e21f837800d686d9
- Manifests: build.gradle
- Sampled source files: src/main/java/com/apple/itunes/storekit/advancedcommerce/AdvancedCommerceInAppSignatureCreator.java, src/main/java/com/apple/itunes/storekit/client/APIError.java, src/main/java/com/apple/itunes/storekit/client/APIException.java, src/main/java/com/apple/itunes/storekit/client/AppStoreServerAPIClient.java
- Git tree state: captured
- Evidence fingerprint: d878a0e433a2479966e61786e993db6a15e9367c9116c688c6aa440bfd4686b6

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
