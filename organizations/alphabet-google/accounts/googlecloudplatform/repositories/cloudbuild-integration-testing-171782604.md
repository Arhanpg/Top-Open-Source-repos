# GoogleCloudPlatform/cloudbuild-integration-testing

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloudbuild-integration-testing](https://github.com/GoogleCloudPlatform/cloudbuild-integration-testing)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloudbuild-integration-testing/blob/master/README.md)
- README blob SHA: 7c15dea2951dc59bea895b237341d9542a37003e
- README bytes captured: 4070
- README truncated at capture limit: False
- Repository ID: 171782604
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Example of techniques for using Google Cloud Build to do integration tests of a microservices application

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:16:34+00:00

### Short excerpt (up to 300 words)

> 2a: Deploying to an Build the docker-compose community

### README headings

- Integration Testing on GCB
- Method 1: docker-compose
- Prerequisites
- Running Build
- Method 2: Google Kubernetes Engine
- Overview
- Prerequisites
- Running Build
- When you're done
- Method 3: Deploy to self-destructing VM
- to do things locally:
- run terraform to create a self-destructing VM w/ microk8s
- get the IP from terraform
- patch the IP into the kubectl config
- (backup flag is passed for macOS compatibility)
- TODO: use a better regex so this can work repeatedly instead of just once
- kubectl can now deploy to microk8s
- see services
- to do things in Cloud Build:

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> 2a: Deploying to an

### Technology and requirements: Prerequisites

> Build the docker-compose community

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 9,206 |
| Shell | 3,574 |
| HCL | 2,513 |
| TSQL | 1,201 |
| CSS | 707 |
| HTML | 363 |
| Dockerfile | 322 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- mysql/Dockerfile (capture: captured)
- web/Dockerfile (capture: captured)
- web/package.json (capture: captured) — dependency clues: chai, chai-http, cookie-parser, debug, eslint, express, http-errors, mocha, morgan, mysql, pug, sinon

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 88
- Forks at capture: 20
- Last updated: 2026-11-16T18:49:40Z
- Last pushed: 2025-04-29T02:02:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloudbuild-integration-testing)
- [README](https://github.com/GoogleCloudPlatform/cloudbuild-integration-testing/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloudbuild-integration-testing/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloudbuild-integration-testing/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
