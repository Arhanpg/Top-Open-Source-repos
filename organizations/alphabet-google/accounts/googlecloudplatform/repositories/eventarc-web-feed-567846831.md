# GoogleCloudPlatform/eventarc-web-feed

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/eventarc-web-feed](https://github.com/GoogleCloudPlatform/eventarc-web-feed)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/eventarc-web-feed/blob/main/README.md)
- README blob SHA: 6f3d7e72ac1bf6a6473853df43b4d9f5389a21a8
- README bytes captured: 4656
- README truncated at capture limit: False
- Repository ID: 567846831
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A serverless and extensible event-driven system for reacting to legacy web feed events

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T21:19:51+00:00

### Short excerpt (up to 300 words)

> No README excerpt captured. Use the upstream README link.

### README headings

- Eventarc Web Feed
- Google Disclaimer
- Services
- Required permissions to deploy
- Dependencies
- If not using devcontainer
- If using devcontainer
- Required GCP APIs
- Organization Policies
- How to deploy
- Clone repo
- If deploying using the devcontainer, run `devcontainer open` to open a new VS Code workspace inside the devcontainer
- Review the default configuration in config.tfvars and modify as needed (please review the README in terraform/ to see input options)
- Additinoal configuration examples can be found in ./examples
- Log in to gcloud cli
- Configure your CLI to point to the GCP project you want to deploy into
- Prepare the GCP project
- Deploy
- Architecture
- Subscribers
- Tech stack

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

No selected README section excerpts were captured.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 24,511 |
| Python | 11,956 |
| Go | 4,568 |
| Shell | 4,252 |
| Makefile | 3,237 |
| Dockerfile | 991 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- .devcontainer/Dockerfile (capture: captured)
- src/feed-reader/go.mod (capture: captured) — dependency clues: cloud.google.com/go/firestore, cloud.google.com/go/pubsub, github.com/GoogleCloudPlatform/functions-framework-go, github.com/cloudevents/sdk-go/v2, github.com/mmcdole/gofeed
- src/subscribers/_example_subscriber/requirements.txt (capture: captured) — dependency clues: functions-framework
- src/subscribers/chat-publisher/requirements.txt (capture: captured) — dependency clues: functions-framework, requests
- src/subscribers/gcp-health-slack-publisher/requirements.txt (capture: captured) — dependency clues: functions-framework, html-slacker, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 3
- Last updated: 2026-05-29T23:26:36Z
- Last pushed: 2026-03-26T04:28:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/eventarc-web-feed)
- [README](https://github.com/GoogleCloudPlatform/eventarc-web-feed/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/eventarc-web-feed/issues)
- [Releases](https://github.com/GoogleCloudPlatform/eventarc-web-feed/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
