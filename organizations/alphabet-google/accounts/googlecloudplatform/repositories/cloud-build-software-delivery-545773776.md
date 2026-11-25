# GoogleCloudPlatform/cloud-build-software-delivery

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-build-software-delivery](https://github.com/GoogleCloudPlatform/cloud-build-software-delivery)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-build-software-delivery/blob/main/README.md)
- README blob SHA: 9850fa08c3d4d1e131beab1bee74eed13362ca8a
- README bytes captured: 16696
- README truncated at capture limit: False
- Repository ID: 545773776
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A walkthrough of setting up a secure CI/CD pipeline for a containerized workloads using Google Cloud Build

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T06:48:57+00:00

### Short excerpt (up to 300 words)

> The purpose of this 1. A Google Cloud

### README headings

- Securing software supply chain
- Introduction
- System Overview
- Standard CI/CD Pipeline
- Secured CI/CD Pipeline
- Demo scope & output
- Demo setup
- Prerequisites
- Set environment variables on Mac/Linux
- Set your project as the current project
- Or if you want a new project, Create a project and set as default
- Enable the Required API’s
- Create a cluster for this demo, these commands do not provision a production ready cluster
- Create an Artifact Repository
- Allow the Cloud Build Service Account to run scans
- Allow the Cloud Build Service Account to deploy to GKE
- Allow Cloud Build Service Account the permission to attest
- Setup Cloud Source Repository
- Create a repo called sec-soft-chain
- Configure credentials
- Add your new repo as a remote repo called google
- Push code to the new repo called google
- Create the Cloud Build trigger
- Modify cloudbuild.yaml
- Setup Sonarqube
- Binary Authorization
- Build and register the custom build step with Cloud Build
- Create Cloud KMS [asymmetric key](https://cloud.google.com/kms/docs/create-validate-signatures) for signing attestations
- Create a Container Analysis note named vulnz-note
- Give CloudBuild Service account name permission on note

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> The purpose of this

### Technology and requirements: Prerequisites

> 1. A Google Cloud

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 1,448 |
| Smarty | 1,104 |
| Dockerfile | 1,038 |
| Go | 948 |
| Open Policy Agent | 216 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle (capture: captured)
- Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 24
- Forks at capture: 13
- Last updated: 2026-07-10T19:29:30Z
- Last pushed: 2024-05-01T17:56:21Z
- Topics: cicd, cloud-build, google, google-cloud

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-build-software-delivery)
- [README](https://github.com/GoogleCloudPlatform/cloud-build-software-delivery/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-build-software-delivery/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-build-software-delivery/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
