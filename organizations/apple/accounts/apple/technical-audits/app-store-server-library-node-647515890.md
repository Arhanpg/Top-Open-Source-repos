# apple/app-store-server-library-node

- Company: Apple
- Account: apple
- Repository: https://github.com/apple/app-store-server-library-node
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:14:55+00:00

## Project purpose

The Node.js server library for the App Store Server API, App Store Server Notifications, Retention Messaging API, and Advanced Commerce API. Also available in Swift, Python, and Java.

## Why this project is used

The Node.js server library for the App Store Server API and App Store Server Notifications.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Lua, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @types/jest, @types/jsonwebtoken, @types/jsrsasign, @types/node, @types/node-fetch, base64url, jest, jsonwebtoken, jsrsasign, node-fetch, ts-jest, typedoc, typescript
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: helper_validation_utils.ts, jws_signature_creator.ts, jws_verification.ts, models/AbstractAdvancedCommerceBaseItem.ts

## Setup and usage

- API Usage: import { AppStoreServerAPIClient, Environment, SendTestNotificationResponse } from "@apple/app-store-server-library"
- API Usage: const issuerId = "99b16628-15e4-4668-972b-eeff55eeff55"
- API Usage: const keyId = "ABCDEFGHIJ"
- API Usage: const bundleId = "com.example"
- API Usage: const filePath = "/path/to/key/SubscriptionKey_ABCDEFGHIJ.p8"
- API Usage: const encodedKey = readFile(filePath) // Specific implementation may vary
- API Usage: const environment = Environment.SANDBOX
- API Usage: const client = new AppStoreServerAPIClient(encodedKey, keyId, issuerId, bundleId, environment)

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/apple/app-store-server-library-node/blob/main/README.md
- README SHA: 6f662520d7c99529ae7e169c55b2cdfa0fae54b1
- Manifests: package.json
- Sampled source files: helper_validation_utils.ts, jws_signature_creator.ts, jws_verification.ts, models/AbstractAdvancedCommerceBaseItem.ts
- Git tree state: captured
- Evidence fingerprint: 9ea893b3843d5ce0aeb7304e2fc03c2e6ca9ef88f882a79d4c7defe541b78658

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
