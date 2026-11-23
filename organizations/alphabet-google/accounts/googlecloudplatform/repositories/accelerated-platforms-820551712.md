# GoogleCloudPlatform/accelerated-platforms

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/accelerated-platforms](https://github.com/GoogleCloudPlatform/accelerated-platforms)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/accelerated-platforms/blob/main/README.md)
- README blob SHA: ee8d53f43f26d58ca41a54cb0d4f81f26a863935
- Repository ID: 820551712
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository is a collection of accelerated platform best practices, reference architectures, example use cases, reference implementations, and various other assets on Google Cloud.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T21:21:26+00:00

### Short excerpt (up to 100 words)

> This repository is a collection of accelerated platform best practices, reference architectures, example use cases, reference implementations, and various other assets on Google Cloud. An accelerated platform utilizes specialized hardware components, or accelerators, such as increase the speed of computationally intensive tasks. These tasks may include data analysis, machine learning, artificial intelligence, and graphics rendering. By offloading demanding workloads from traditional CPUs to dedicated hardware accelerators, which are capable of much faster parallel calculations, the platform optimizes high-performance computing. The GKE Base Platform (reference implementation) is an opinionated, foundational platform built on GKE using modular Terraform (Terraservices) that incorporates security,

### README headings

- Google Cloud Accelerated Platforms
- Google Kubernetes Engine (GKE)
- GKE Base Platform
- Inference Reference Architecture
- Secure Runtimes for AI Agents Reference Architecture (GKE Agent Sandbox & Agent Substrate)
- Training Reference Architecture
- Reinforcement Learning
- ComfyUI Reference Implementation
- Federated Learning
- Guides
- Cloud Workstations (CWS)
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 1,428,009 |
| Shell | 942,552 |
| Python | 897,023 |
| Go | 56,146 |
| Dockerfile | 53,863 |
| JavaScript | 33,457 |
| Go Template | 30,649 |
| HTML | 20,586 |
| CSS | 13,332 |
| Smarty | 2,386 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: fsspec, gcsfs, google-cloud-storage, jsonpickle, pandas, preshed, pyyaml, ray, spacy, thejsonlogger
- .devcontainer/Dockerfile (capture: captured)
- .devcontainer/dependencies/package.json (capture: captured) — dependency clues: prettier
- .devcontainer/dependencies/requirements.txt (capture: captured) — dependency clues: black, isort
- projects/workflow-api/Dockerfile (capture: captured)
- projects/workflow-api/go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, github.com/KyleBanks/depth, github.com/bytedance/sonic, github.com/bytedance/sonic/loader, github.com/cloudwego/base64x, github.com/davecgh/go-spew, github.com/felixge/httpsnoop, github.com/gabriel-vasile/mimetype, github.com/gin-contrib/sse, github.com/gin-gonic/gin, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/spec, github.com/go-openapi/swag, github.com/go-playground/locales, github.com/go-playground/universal-translator

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 110
- Forks at capture: 39
- Last updated: 2026-11-12T04:33:35Z
- Last pushed: 2026-11-23T17:06:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/accelerated-platforms)
- [README](https://github.com/GoogleCloudPlatform/accelerated-platforms/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/accelerated-platforms/issues)
- [Releases](https://github.com/GoogleCloudPlatform/accelerated-platforms/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
