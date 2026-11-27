# GoogleCloudPlatform/gke-vault-demo

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/gke-vault-demo](https://github.com/GoogleCloudPlatform/gke-vault-demo)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/gke-vault-demo/blob/master/README.md)
- README blob SHA: cc267b8bb7f713df8ba411e24ca9a150d87711a9
- README bytes captured: 23087
- README truncated at capture limit: False
- Repository ID: 172743546
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This demo builds two GKE Clusters and guides you through using secrets in Vault, using Kubernetes authentication from within a pod to login to Vault, and fetching short-lived Google Service Account credentials on-demand from Vault within a pod.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:57:06+00:00

### Short excerpt (up to 300 words)

> Many new users to If you are not The demonstration code will The steps described in

### README headings

- Vault on GKE
- Table of Contents
- Introduction
- Architecture
- Prerequisites
- Cloud Project
- Install Cloud SDK
- Install Kubectl
- Install Terraform
- Install Vault CLI
- Configure Authentication
- Deployment
- Create the clusters
- Configure Static Key-Value Secrets in Vault
- Configure Kubernetes Pod Authentication to Vault
- Manually Retrieve Secrets from a Pod
- Install curl and jq
- Fetch the pod's service account token
- Use curl to login to vault and obtain a client access token
- View the login response which includes the vault client access token
- Extract just the client access token
- Use the client access token to retrieve the contents of the secret
- Configure an Auto-Init Example Application
- Configure Dynamic GCP Service Account Credentials
- Fetch the pod's service account token
- Use curl to login to vault and obtain a client access token
- Extract just the client access token
- Use the client access token to retrieve the contents of the service account credential
- Validation
- Teardown

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> Many new users to

### Getting started and usage: Install Cloud SDK

> If you are not

### Architecture and design: Architecture

> The demonstration code will

### Technology and requirements: Prerequisites

> The steps described in

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 23,178 |
| HCL | 17,480 |
| Python | 9,735 |
| Makefile | 2,825 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 72
- Forks at capture: 20
- Last updated: 2025-10-16T20:10:08Z
- Last pushed: 2024-08-14T14:22:10Z
- Topics: containers, gcp, gke, gke-helmsman, hashicorp-vault, kubernetes, kubernetes-engine, security, vault

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/gke-vault-demo)
- [README](https://github.com/GoogleCloudPlatform/gke-vault-demo/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/gke-vault-demo/issues)
- [Releases](https://github.com/GoogleCloudPlatform/gke-vault-demo/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
