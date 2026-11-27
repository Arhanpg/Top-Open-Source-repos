# GoogleCloudPlatform/inspec-gke-cis-benchmark

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/inspec-gke-cis-benchmark](https://github.com/GoogleCloudPlatform/inspec-gke-cis-benchmark)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/inspec-gke-cis-benchmark/blob/master/README.md)
- README blob SHA: f718f5903e688b72b5e21007c9e284c7679acbc6
- README bytes captured: 6078
- README truncated at capture limit: False
- Repository ID: 288587145
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

GKE CIS 1.1.0 Benchmark InSpec Profile

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T19:26:31+00:00

### Short excerpt (up to 300 words)

> $ gem install inspec-bin Configure access via the

### README headings

- GKE CIS 1.1.0 Benchmark Inspec Profile
- Required Disclaimer
- Coverage
- Prerequisites
- CLI Example (Cloud Shell)
- install inspec (later version might work but not tested)
- clone the Git Repo
- Write an inputs file, see basic example below
- Connect to GKE Cluster (getting credentials in ~/.kubeconfig, validate using kubectl)
- install inspec-k8s and relevant gems (needs to run in directory of Gemfile)
- (refer to the inspec-k8s docs for details and troubleshooting)
- install InSpec plugin train-kubernetes
- Add the host you are running from to the master-authorized-networks to allow access to Private K8S Clusters
- make sure you're authenticated to GCP
- acquire credentials to use with Application Default Credentials
- Create a file inputs.yml which contains the required and optional inputs to the profiles in the subdirectories
- Profile Inputs (combined across all profiles)
- Cloud Shell Walkthrough
- Required Permissions

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: install inspec (later version might work but not tested)

> $ gem install inspec-bin

### Technology and requirements: Prerequisites

> Configure access via the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Ruby | 111,517 |
| Shell | 4,079 |
| Dockerfile | 701 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Gemfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 25
- Forks at capture: 21
- Last updated: 2026-02-05T17:28:20Z
- Last pushed: 2021-09-07T19:22:04Z
- Topics: auditing, benchmark, cis, compliance, gcp, gke, inspec, security

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/inspec-gke-cis-benchmark)
- [README](https://github.com/GoogleCloudPlatform/inspec-gke-cis-benchmark/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/inspec-gke-cis-benchmark/issues)
- [Releases](https://github.com/GoogleCloudPlatform/inspec-gke-cis-benchmark/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
