# GoogleCloudPlatform/gke-rbac-demo

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/gke-rbac-demo](https://github.com/GoogleCloudPlatform/gke-rbac-demo)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/gke-rbac-demo/blob/master/README.md)
- README blob SHA: a07d824c4f21499d7c5d1bdcfac426c5917476ce
- README bytes captured: 30606
- README truncated at capture limit: False
- Repository ID: 142068783
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This project covers two use cases for RBAC within a Kubernetes Engine cluster. First, assigning different permissions to user personas. Second, granting limited API access to an application running within your cluster. Since RBAC's flexibility can occasionally result in complex rules, you will also perform common steps for troubleshooting RBAC as a part of the second scenario.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:40:18+00:00

### Short excerpt (up to 300 words)

> This tutorial covers the The Google Cloud SDK This tutorial focuses on

### README headings

- Using Role-Based Access Control in Kubernetes Engine
- Table of Contents
- Introduction
- Architecture
- Prerequisites
- Run Demo in a Google Cloud Shell
- Tools
- Install Cloud SDK
- Install kubectl CLI
- Install Terraform
- Deployment
- Authenticate gcloud
- Configure gcloud settings
- Where the region is us-east1
- Where the zone inside the region is us-east1-c
- Where the project name is my-project-name
- Setup this project
- Provisioning the Kubernetes Engine Cluster
- From within the project root, use make to apply the terraform
- Validation
- Scenario 1: Assigning permissions by user persona
- IAM - Role
- Simulating users
- Creating the RBAC rules
- SSH to the admin
- Managing resources as the owner
- SSH to the "owner" instance
- On the "owner" instance
- List all hello-server pods in all namespaces
- Viewing resources as the auditor

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> This tutorial covers the

### Getting started and usage: Install Cloud SDK

> The Google Cloud SDK

### Architecture and design: Architecture

> This tutorial focuses on

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 27,092 |
| Shell | 18,942 |
| Python | 13,518 |
| Makefile | 2,482 |
| Dockerfile | 1,102 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- images/pod-labeler/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 165
- Forks at capture: 81
- Last updated: 2026-07-07T16:21:41Z
- Last pushed: 2024-08-19T20:33:58Z
- Topics: gke, gke-helmsman, google-cloud-platform, kubernetes, kubernetes-engine, rbac, security

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/gke-rbac-demo)
- [README](https://github.com/GoogleCloudPlatform/gke-rbac-demo/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/gke-rbac-demo/issues)
- [Releases](https://github.com/GoogleCloudPlatform/gke-rbac-demo/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
