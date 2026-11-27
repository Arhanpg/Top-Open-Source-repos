# GoogleCloudPlatform/gke-security-scenarios-demo

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/gke-security-scenarios-demo](https://github.com/GoogleCloudPlatform/gke-security-scenarios-demo)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/gke-security-scenarios-demo/blob/master/README.md)
- README blob SHA: d23147bca8f7a30aa8991828a59c1a4acd43f8e7
- README bytes captured: 18062
- README truncated at capture limit: False
- Repository ID: 142068424
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This project demonstrates a series of best practices for improving the security of containerized applications deployed to Kubernetes Engine. You will deploy multiple instances of the same container image with a variety of security settings to illustrate the use of RBAC, security contexts, and AppArmor policies.  

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:45:54+00:00

### Short excerpt (up to 300 words)

> This tutorial demonstrates how The Google Cloud SDK The tutorial uses three

### README headings

- Three examples of securing applications in Kubernetes Engine
- Table of Contents
- Introduction
- Architecture
- Hardened Web Server (nginx)
- System Daemonset (AppArmor Loader)
- Simplified Kubernetes Controller (Pod Labeler)
- Prerequisites
- Run Demo in a Google Cloud Shell
- Tools
- Install Cloud SDK
- Install kubectl CLI
- Install Terraform
- Deployment
- Authenticate gcloud
- Setup this project
- Provisioning the Kubernetes Engine Cluster
- From within the project root, use make to apply the terraform
- Validation
- Set up Nginx
- Set up AppArmor-loader
- On the bastion host
- On the bastion host
- Set up Pod-labeler
- Tear down
- Troubleshooting
- The install script fails with a `Permission denied` when running Terraform
- Error during scp
- Invalid fingerprint error during Terraform operations
- Relevant Material

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> This tutorial demonstrates how

### Getting started and usage: Install Cloud SDK

> The Google Cloud SDK

### Architecture and design: Architecture

> The tutorial uses three

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 23,354 |
| Shell | 16,397 |
| Python | 11,481 |
| Makefile | 2,187 |
| Dockerfile | 1,081 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- images/custom-nginx/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 93
- Forks at capture: 55
- Last updated: 2026-02-12T13:52:33Z
- Last pushed: 2024-08-15T20:10:40Z
- Topics: containers, gke, gke-helmsman, google-cloud-platform, kubernetes, kubernetes-engine, security

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/gke-security-scenarios-demo)
- [README](https://github.com/GoogleCloudPlatform/gke-security-scenarios-demo/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/gke-security-scenarios-demo/issues)
- [Releases](https://github.com/GoogleCloudPlatform/gke-security-scenarios-demo/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
