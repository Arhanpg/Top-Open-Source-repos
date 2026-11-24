# GoogleCloudPlatform/activeassist-anthos-toolchain

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/activeassist-anthos-toolchain](https://github.com/GoogleCloudPlatform/activeassist-anthos-toolchain)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/activeassist-anthos-toolchain/blob/main/README.md)
- README blob SHA: 99ae183ec9d8ec50e159a93e1ee5baee0f4593f9
- Repository ID: 417442279
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:44:09+00:00

### Short excerpt (up to 100 words)

> This repository contains code that shows you how you can use the Anthos toolchain to retrieve and parse Active Assist recommendations using Kpt. It demonstrates a workflow where you use a Cloud Build trigger to hydrate Config Connector KRM templates in a DRY repository using Kpt setters, this trigger pushes hydrated resources to one or more hydrated repositories.This workflow assumes your Anthos environment is managed using Anthos Config Management. A second scheduled Cloud Build trigger runs a Kpt function to invoke the Active Assist APIs, review active recommendations, compare the recommendation to the as-is state of Config Connector managed resources

### README headings

- Using the Anthos toolchain with Active Assist
- How to use this example
- Quickstart
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 572,658 |
| Dockerfile | 2,263 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- recommender-kpt-function/Dockerfile (capture: captured)
- recommender-kpt-function/package.json (capture: captured) — dependency clues: @types/jasmine, @types/node, @types/request-promise, create-kpt-functions, googleapis, jasmine, kpt-functions, npm, pkg, request, request-promise, tslint, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 0
- Last updated: 2023-01-10T22:16:44Z
- Last pushed: 2021-10-15T09:31:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/activeassist-anthos-toolchain)
- [README](https://github.com/GoogleCloudPlatform/activeassist-anthos-toolchain/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/activeassist-anthos-toolchain/issues)
- [Releases](https://github.com/GoogleCloudPlatform/activeassist-anthos-toolchain/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
