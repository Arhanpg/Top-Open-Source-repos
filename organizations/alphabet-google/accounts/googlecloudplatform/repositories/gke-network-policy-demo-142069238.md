# GoogleCloudPlatform/gke-network-policy-demo

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/gke-network-policy-demo](https://github.com/GoogleCloudPlatform/gke-network-policy-demo)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/gke-network-policy-demo/blob/master/README.md)
- README blob SHA: 3de2447a125faccf819df96cb9b1a3e0c98ccf57
- README bytes captured: 16409
- README truncated at capture limit: False
- Repository ID: 142069238
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This guide demonstrates how to improve the security of your Kubernetes Engine by applying fine-grained restrictions to network communication. You will provision a simple HTTP server and two client pods in a Kubernetes Engine cluster, then use a Network Policy restrict connections from client pods.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T05:20:42+00:00

### Short excerpt (up to 300 words)

> This guide demonstrates how The Google Cloud SDK For demonstration purposes, you

### README headings

- How to use a Network Policy in Kubernetes Engine
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
- Installing the hello server
- Confirming default access to the hello server
- Restricting access with a Network Policy
- Restricting namespaces with Network Policies
- Validation
- Tear Down
- Troubleshooting
- The install script fails with a `Permission denied` when running Terraform
- Invalid fingerprint error during Terraform operations
- Relevant Material

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> This guide demonstrates how

### Getting started and usage: Install Cloud SDK

> The Google Cloud SDK

### Architecture and design: Architecture

> For demonstration purposes, you

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 17,421 |
| HCL | 14,386 |
| Python | 11,481 |
| Makefile | 2,618 |

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
- Stars at capture: 102
- Forks at capture: 85
- Last updated: 2026-10-29T13:51:52Z
- Last pushed: 2023-12-14T21:50:19Z
- Topics: gke, gke-helmsman, kubernetes, kubernetes-engine, networking, security

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/gke-network-policy-demo)
- [README](https://github.com/GoogleCloudPlatform/gke-network-policy-demo/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/gke-network-policy-demo/issues)
- [Releases](https://github.com/GoogleCloudPlatform/gke-network-policy-demo/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
