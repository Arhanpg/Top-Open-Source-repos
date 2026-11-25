# GoogleCloudPlatform/cloud-run-anthos-reference-web-app

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-run-anthos-reference-web-app](https://github.com/GoogleCloudPlatform/cloud-run-anthos-reference-web-app)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-run-anthos-reference-web-app/blob/main/README.md)
- README blob SHA: 3f9a504918ba30447b083069af397dafcf83d92b
- README bytes captured: 9750
- README truncated at capture limit: False
- Repository ID: 255677237
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

 An opinionated set of best practices aimed at demonstrating a reference architecture for building a web application on Google Cloud using Cloud Run for Anthos.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T19:33:21+00:00

### Short excerpt (up to 300 words)

> **English** | Español

### README headings

- Cloud Run for Anthos Reference Web App
- 🛑 This project is archived and is not being actively maintained 🛑
- Prerequisites
- Development Environment
- Cloud Shell
- Local Setup
- Custom Domain
- Identity Platform for Auth and Firestore Setup
- Deploying the Application for the First Time
- 1. Configure GCP Project
- 2. Fill out TODO sections in `env.mk`
- 3. Create a GKE Cluster
- 4. Add a verified owner for the domain
- 5. Build and deploy
- Try Out the Application
- Setup first admin user
- Update the Application
- builds and deploys backend, frontend, and KCC infrastructure
- builds and deploys only the backend Go service
- builds and deploys only the frontend angular webapp
- Cleanup

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> **English** | Español

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 118,792 |
| Go | 85,435 |
| HTML | 20,421 |
| Shell | 10,657 |
| JavaScript | 9,743 |
| Makefile | 7,988 |
| SCSS | 7,529 |
| Mustache | 6,435 |
| Gherkin | 5,432 |
| CSS | 2,005 |
| Dockerfile | 1,803 |
| JSONiq | 1,121 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- makefile (capture: captured)
- backend/go.mod (capture: captured) — dependency clues: cloud.google.com/go/firestore, github.com/google/go-cmp, github.com/google/uuid, github.com/gorilla/mux, google.golang.org/api, google.golang.org/grpc
- istio-auth/go.mod (capture: captured) — dependency clues: cloud.google.com/go/firestore, cloud.google.com/go/storage, firebase.google.com/go
- webui/package.json (capture: captured) — dependency clues: @angular-devkit/build-angular, @angular-material-extensions/password-strength, @angular/animations, @angular/cdk, @angular/cli, @angular/common, @angular/compiler, @angular/compiler-cli, @angular/core, @angular/fire, @angular/flex-layout, @angular/forms, @angular/material, @angular/platform-browser, @angular/platform-browser-dynamic, @angular/router, @cypress/webpack-preprocessor, @types/cypress-cucumber-preprocessor, @types/jasmine, @types/node
- backend/api-service/Dockerfile (capture: captured)
- backend/user-service/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 38
- Forks at capture: 19
- Last updated: 2025-11-26T01:44:52Z
- Last pushed: 2021-04-22T15:11:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-run-anthos-reference-web-app)
- [README](https://github.com/GoogleCloudPlatform/cloud-run-anthos-reference-web-app/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-run-anthos-reference-web-app/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-run-anthos-reference-web-app/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
