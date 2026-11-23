# amazon-connect/touchpoint-android

- Company: Amazon
- GitHub account: [https://github.com/amazon-connect](https://github.com/amazon-connect)
- Mapping status: official-directory-listed
- Repository: [amazon-connect/touchpoint-android](https://github.com/amazon-connect/touchpoint-android)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-connect/touchpoint-android/blob/main/README.md)
- README blob SHA: bb235cf48384d1a71fce03e9b631b5e57778cde4
- Repository ID: 1412090582
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An open-source Kotlin SDK that brings Amazon Connect chat, in-app voice calls and Live Sync to native Android apps. Enables companies running contact centers on Amazon Connect to let customers chat, call and get help from assistants inside their own Android apps.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:30:39+00:00

### Short excerpt (up to 100 words)

> **Status: developer preview.** The public API may change before 1.0; each release's changes are in Native Android SDK for Amazon Connect Customer Touchpoint: chat, outbound voice, and Live Sync, as separately linkable Gradle modules so an app pays only for the modalities it uses. It is the counterpart of the Touchpoint iOS SDK and follows the same design, and it matches Touchpoint for the web's behaviour and options. A chat-only consumer never links the WebRTC media stack, and a Live-Sync-only consumer links neither external SDK. `Scripts/check-build-graph.sh` enforces that on every `make check` by reading each module's resolved release classpath, which

### README headings

- Amazon Connect Customer Touchpoint SDK for Android
- Requirements
- Installing
- From a release bundle
- Developer guide
- How the pieces fit
- 1. Your backend
- Using Touchpoint web's endpoints
- 2. Chat
- 3. The assistant: choices, cards and custom modalities
- 4. Sign-in (Authenticate Customer)
- 5. Guides (Connect Views)
- 6. Attachments
- 7. New-message notifications
- 8. Voice
- 9. Screen share
- 10. Live Sync
- Setup checklist
- Developing
- Security
- Licence

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Kotlin | 1,735,625 |
| Shell | 85,116 |
| Python | 7,246 |
| Makefile | 4,304 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle.kts (capture: captured)
- Makefile (capture: captured)
- touchpoint-chat/build.gradle.kts (capture: captured)
- touchpoint-core-android/build.gradle.kts (capture: captured)
- touchpoint-core/build.gradle.kts (capture: captured)
- touchpoint-development/build.gradle.kts (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 2
- Forks at capture: 1
- Last updated: 2026-11-11T22:07:53Z
- Last pushed: 2026-11-17T18:25:35Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-connect/touchpoint-android)
- [README](https://github.com/amazon-connect/touchpoint-android/blob/main/README.md)
- [Issues](https://github.com/amazon-connect/touchpoint-android/issues)
- [Releases](https://github.com/amazon-connect/touchpoint-android/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
