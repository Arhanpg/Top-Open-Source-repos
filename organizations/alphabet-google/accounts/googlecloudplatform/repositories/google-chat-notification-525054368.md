# GoogleCloudPlatform/google-chat-notification

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/google-chat-notification](https://github.com/GoogleCloudPlatform/google-chat-notification)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/google-chat-notification/blob/main/README.md)
- README blob SHA: 80aad2a1c85a437857acb5912c829558d961f1eb
- README bytes captured: 3898
- README truncated at capture limit: False
- Repository ID: 525054368
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T06:15:18+00:00

### Short excerpt (up to 300 words)

> This project provide tools that helps to send message to Google Chat from any pub/sub message. The tools support templating messages base on Handlebars

### README headings

- Google-chat-notification
- Create a Google chat webhook
- Step 1: Register the incoming webhook
- Deploy a handlebar (HBS) template and upload to a GCS bucket
- if my mybucket-hbs does not exist
- gsutil mb gs://mybucket-hbs/
- Copy template to the target bucket
- Deploy the Cloud Function
- Clone the github repo
- Service account
- Disclaimer

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Google-chat-notification

> This project provide tools that helps to send message to Google Chat from any pub/sub message. The tools support templating messages base on Handlebars

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 7,823 |
| Handlebars | 2,016 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: cloudevents-api, functions-framework-api, google-chat-notification, google-cloud-storage, google-cloudevent-types, handlebars, handlebars-jackson2, jackson-core, junit-jupiter-engine, logback-classic, logstash-logback-encoder, lombok, maven-compiler-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 8
- Forks at capture: 2
- Last updated: 2023-10-20T12:04:00Z
- Last pushed: 2022-08-17T18:48:45Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/google-chat-notification)
- [README](https://github.com/GoogleCloudPlatform/google-chat-notification/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/google-chat-notification/issues)
- [Releases](https://github.com/GoogleCloudPlatform/google-chat-notification/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
