# GoogleCloudPlatform/bq-backup-manager

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/bq-backup-manager](https://github.com/GoogleCloudPlatform/bq-backup-manager)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/bq-backup-manager/blob/main/README.md)
- README blob SHA: b610490c624c9d1ee6ef22146363ebb8fd7c336f
- README bytes captured: 39882
- README truncated at capture limit: False
- Repository ID: 650289190
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T04:09:31+00:00

### Short excerpt (up to 300 words)

> BigQuery Backup Manager is Download Maven Add Maven The solution uses multiple

### README headings

- BigQuery Backup Manager
- Table Of Contents
- Overview
- Architecture
- Backup Policies
- Components
- Scheduler
- Dispatcher
- Configurator
- BigQuery Snapshoter
- GCS Snapshoter
- Tagger
- Design Notes
- Assumptions
- Deployment
- Install Maven
- Setup Environment Variables
- One-time Environment Setup
- Enable GCP APIs
- Prepare Terraform State Bucket
- Prepare Terraform Service Account
- Prepare a Docker Repo
- Solution Deployment
- gcloud
- Build Cloud Run Services Images
- Terraform Variables Configuration
- Create a Terraform .tfvars file
- Configure Project Variables
- Configure Terraform Service Account
- Configure Cloud Run Service Images

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> BigQuery Backup Manager is

### Getting started and usage: Install Maven

> Download Maven Add Maven

### Architecture and design: Design Notes

> The solution uses multiple

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 383,573 |
| HCL | 129,241 |
| Shell | 17,403 |
| Smarty | 16,559 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- services/pom.xml (capture: captured) — dependency clues: bq-snapshoter-manager, libraries-bom, spring-boot-dependencies, spring-boot-starter-parent, spring-cloud-dependencies
- services/configurator-app/pom.xml (capture: captured) — dependency clues: bq-snapshot-manager-configurator-app, bq-snapshot-manager-lib, bq-snapshoter-manager, jib-maven-plugin, junit, snakeyaml, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-test, spring-boot-starter-web
- services/dispatcher-app/pom.xml (capture: captured) — dependency clues: bq-snapshot-manager-dispatcher-app, bq-snapshot-manager-lib, bq-snapshoter-manager, gson, jib-maven-plugin, junit, snakeyaml, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-test, spring-boot-starter-web
- services/library/pom.xml (capture: captured) — dependency clues: bq-snapshot-manager-lib, bq-snapshoter-manager, commons-lang3, functions-framework-api, google-api-services-cloudresourcemanager, google-api-services-iam, google-cloud-bigquery, google-cloud-datastore, google-cloud-pubsub, google-cloud-storage, junit, logback-classic, logstash-logback-encoder, mockito-core, protobuf-java, slf4j-api, spring-boot-starter, spring-boot-starter-test, spring-boot-starter-web
- services/snapshoter-bq-app/pom.xml (capture: captured) — dependency clues: bq-snapshot-manager-lib, bq-snapshot-manager-snapshoter-bq-app, bq-snapshoter-manager, jib-maven-plugin, junit, snakeyaml, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-test, spring-boot-starter-web
- services/snapshoter-gcs-app/pom.xml (capture: captured) — dependency clues: bq-snapshot-manager-lib, bq-snapshot-manager-snapshoter-gcs-app, bq-snapshoter-manager, jib-maven-plugin, junit, snakeyaml, spring-boot-maven-plugin, spring-boot-starter-actuator, spring-boot-starter-test, spring-boot-starter-web

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 24
- Forks at capture: 6
- Last updated: 2026-08-14T15:14:28Z
- Last pushed: 2026-06-18T18:42:39Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/bq-backup-manager)
- [README](https://github.com/GoogleCloudPlatform/bq-backup-manager/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/bq-backup-manager/issues)
- [Releases](https://github.com/GoogleCloudPlatform/bq-backup-manager/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
