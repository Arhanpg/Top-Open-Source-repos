# GoogleCloudPlatform/migrate-from-service-account-keys

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/migrate-from-service-account-keys](https://github.com/GoogleCloudPlatform/migrate-from-service-account-keys)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/migrate-from-service-account-keys/blob/main/README.md)
- README blob SHA: 47bf3d67577b34c3ef9c55a2161a49559c151fed
- README bytes captured: 13899
- README truncated at capture limit: False
- Repository ID: 718205354
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repo produces a data pipeline to help you assess service account key usage, as described in the Assess phase of the Google Cloud documentation migrate from service account keys to more secure alternatives.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T22:07:55+00:00

### Short excerpt (up to 300 words)

> The following sections introduce The following diagram shows

### README headings

- Migrate from service account keys to more secure authentication methods
- Architecture
- Tables
- Deploying the infrastructure
- Before you begin
- Loop through all projects in the organization
- Set Terraform variables and deploy
- (optional) Manually trigger the scheduled workflow
- Clean up
- Sample query usage
- How many persistent keys have been created?
- Which projects use service account keys to authenticate?
- Which keys are inactive?
- Are keys associated with service accounts that have overly privileged IAM roles?
- Notes on data freshness

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Sample query usage

> The following sections introduce

### Architecture and design: Architecture

> The following diagram shows

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 25,372 |
| Python | 9,423 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- src/access-analyzer/requirements.txt (capture: captured) — dependency clues: functions-framework, google-cloud-asset, google-cloud-bigquery, google-cloud-resource-manager, google-cloud-storage
- src/cai-export/requirements.txt (capture: captured) — dependency clues: flask, functions-framework, google-cloud-asset, google-cloud-bigquery, google-cloud-resource-manager, google-cloud-storage

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 6
- Last updated: 2026-09-15T06:31:03Z
- Last pushed: 2026-09-15T00:14:14Z
- Topics: gcp

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/migrate-from-service-account-keys)
- [README](https://github.com/GoogleCloudPlatform/migrate-from-service-account-keys/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/migrate-from-service-account-keys/issues)
- [Releases](https://github.com/GoogleCloudPlatform/migrate-from-service-account-keys/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
