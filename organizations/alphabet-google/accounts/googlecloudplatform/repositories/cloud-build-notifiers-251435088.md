# GoogleCloudPlatform/cloud-build-notifiers

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-build-notifiers](https://github.com/GoogleCloudPlatform/cloud-build-notifiers)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/README.md)
- README blob SHA: 5f39d05c7602271563fb968a93cd00921db3c27f
- README bytes captured: 3893
- README truncated at capture limit: False
- Repository ID: 251435088
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Notifier images for Cloud Build, complete with build status filtering and Google Secret Manager integration

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T06:43:21+00:00

### Short excerpt (up to 300 words)

> This repo provides deployable notifier images and sources, as well as libraries for creating new notifiers. containers that connect to the that adapt Pub/Sub messages

### README headings

- Cloud Build Notifiers
- Setup Script
- Common Flags
- `--smoketest`
- `--setup_check`
- First build the notifier locally.
- Then run the `setup_check` with your YAML.
- --interactive to allow reading from STDIN.
- --rm to clean/remove the image once it exits.
- License
- Contributing
- Support

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: Cloud Build Notifiers

> This repo provides deployable notifier images and sources, as well as libraries for creating new notifiers. containers that connect to the that adapt Pub/Sub messages

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 134,171 |
| Dockerfile | 11,982 |
| Shell | 7,830 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/bigquery, cloud.google.com/go/cloudbuild, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/longrunning, cloud.google.com/go/secretmanager, cloud.google.com/go/storage, github.com/antlr4-go/antlr/v4, github.com/apache/arrow/go/v14, github.com/containerd/stargz-snapshotter/estargz, github.com/docker/cli, github.com/docker/distribution, github.com/docker/docker, github.com/docker/docker-credential-helpers, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr
- bigquery/Dockerfile (capture: captured)
- githubissues/Dockerfile (capture: captured)
- googlechat/Dockerfile (capture: captured)
- http/Dockerfile (capture: captured)
- slack/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 160
- Forks at capture: 143
- Last updated: 2026-11-08T13:49:25Z
- Last pushed: 2026-09-01T23:08:36Z
- Topics: gcp, gcp-cloud-build, notifications

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-build-notifiers)
- [README](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-build-notifiers/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
