# GoogleCloudPlatform/cloudnetworking-config-solutions

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloudnetworking-config-solutions](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/blob/main/README.md)
- README blob SHA: 2acd1a756122c2f8088776968564a99ecf3c284c
- README bytes captured: 18120
- README truncated at capture limit: False
- Repository ID: 810218096
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Cloud Networking config solution makes it easy for you to connect your on-premises network or VPC to Google-managed services.The solution simplifies complex network configurations and takes care of that for you, so you can focus on your business. Plus, it's designed to be scalable and reliable, so you can count on it to handle your growing needs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:36:59+00:00

### Short excerpt (up to 300 words)

> This repository leverages pre-built **Click-to-Deploy Functionality:** Increased coverage 1. **Clone the Repository** **Terraform:** Ensure you have **Security Profiles and Security

### README headings

- CloudNet Config Solutions: Simplified Google Cloud Networking with Terraform 🌐
- Introduction
- Key Features and Enhancements
- Network Services
- Security Services
- Producers
- Producer Connectivity
- Consumers
- Load Balancers
- Network Security Integration
- Deployment Features
- Project Structure
- Prerequisites
- [configuration](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/tree/main/configuration)
- [execution](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/tree/main/execution)
- Prerequisites
- 🚀 Getting Started
- Important Notes

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> This repository leverages pre-built

### Features and capabilities: Deployment Features

> **Click-to-Deploy Functionality:** Increased coverage

### Getting started and usage: 🚀 Getting Started

> 1. **Clone the Repository**

### Technology and requirements: Prerequisites

> **Terraform:** Ensure you have

### Limitations and security: Security Services

> **Security Profiles and Security

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 667,873 |
| Go | 632,220 |
| Python | 183,064 |
| Shell | 23,490 |
| Jinja | 14,306 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- config-generator-beta/requirements.txt (capture: captured) — dependency clues: Jinja2, PyYAML, absl-py, pyfakefs, requests
- execution/test/integration/common_utils/go.mod (capture: captured) — dependency clues: github.com/davecgh/go-spew, github.com/gruntwork-io/terratest, github.com/pmezard/go-difflib, github.com/stretchr/testify, gopkg.in/yaml.v3
- execution/test/integration/networking/go.mod (capture: captured) — dependency clues: github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/common_utils, github.com/agext/levenshtein, github.com/apparentlymart/go-textseg/v15, github.com/bgentry/go-netrc, github.com/davecgh/go-spew, github.com/google/go-cmp, github.com/gruntwork-io/terratest, github.com/hashicorp/errwrap, github.com/hashicorp/go-cleanhttp, github.com/hashicorp/go-getter/v2, github.com/hashicorp/go-multierror, github.com/hashicorp/go-safetemp, github.com/hashicorp/go-version, github.com/hashicorp/hcl/v2, github.com/hashicorp/terraform-json, github.com/jinzhu/copier, github.com/klauspost/compress, github.com/mattn/go-zglob, github.com/mitchellh/go-homedir, github.com/mitchellh/go-testing-interface
- execution/test/integration/network-security-integration/PacketMirroringRule/go.mod (capture: captured) — dependency clues: github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/test/integration/common_utils, github.com/agext/levenshtein, github.com/apparentlymart/go-textseg/v15, github.com/bgentry/go-netrc, github.com/davecgh/go-spew, github.com/gruntwork-io/terratest, github.com/hashicorp/errwrap, github.com/hashicorp/go-cleanhttp, github.com/hashicorp/go-getter/v2, github.com/hashicorp/go-multierror, github.com/hashicorp/go-safetemp, github.com/hashicorp/go-version, github.com/hashicorp/hcl/v2, github.com/hashicorp/terraform-json, github.com/jinzhu/copier, github.com/klauspost/compress, github.com/mattn/go-zglob, github.com/mitchellh/go-homedir, github.com/mitchellh/go-testing-interface, github.com/mitchellh/go-wordwrap
- execution/test/integration/networking/FirewallEndpoint/go.mod (capture: captured) — dependency clues: github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/test/integration/common_utils, github.com/agext/levenshtein, github.com/apparentlymart/go-textseg/v15, github.com/bgentry/go-netrc, github.com/davecgh/go-spew, github.com/gruntwork-io/terratest, github.com/hashicorp/errwrap, github.com/hashicorp/go-cleanhttp, github.com/hashicorp/go-getter/v2, github.com/hashicorp/go-multierror, github.com/hashicorp/go-safetemp, github.com/hashicorp/go-version, github.com/hashicorp/hcl/v2, github.com/hashicorp/terraform-json, github.com/jinzhu/copier, github.com/klauspost/compress, github.com/mattn/go-zglob, github.com/mitchellh/go-homedir, github.com/mitchellh/go-testing-interface, github.com/mitchellh/go-wordwrap
- execution/test/integration/producer/AlloyDB/go.mod (capture: captured) — dependency clues: github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/common_utils, github.com/agext/levenshtein, github.com/apparentlymart/go-textseg/v15, github.com/bgentry/go-netrc, github.com/davecgh/go-spew, github.com/gruntwork-io/terratest, github.com/hashicorp/errwrap, github.com/hashicorp/go-cleanhttp, github.com/hashicorp/go-getter/v2, github.com/hashicorp/go-multierror, github.com/hashicorp/go-safetemp, github.com/hashicorp/go-version, github.com/hashicorp/hcl/v2, github.com/hashicorp/terraform-json, github.com/jinzhu/copier, github.com/klauspost/compress, github.com/mattn/go-zglob, github.com/mitchellh/go-homedir, github.com/mitchellh/go-testing-interface, github.com/mitchellh/go-wordwrap

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 26
- Forks at capture: 15
- Last updated: 2026-07-17T05:11:29Z
- Last pushed: 2026-07-10T15:16:13Z
- Topics: alloydb, app-engine, automation, cloudnetworking, cloudsql, gce, gcp, gcp-automation, google, google-cloud-automation, google-cloud-networking, memory-redis-cluster, network-connectivity-center-automation, terraform

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions)
- [README](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
