# aws/sagemaker-hyperpod-cli

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/sagemaker-hyperpod-cli](https://github.com/aws/sagemaker-hyperpod-cli)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/sagemaker-hyperpod-cli/blob/main/README.md)
- README blob SHA: b3519cabc840dabc8778494b227bde8ede902a16
- README bytes captured: 55689
- README truncated at capture limit: False
- Repository ID: 842208567
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

 A CLI tool that helps manage training jobs on the SageMaker HyperPod clusters orchestrated by Amazon EKS

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:16:00+00:00

### Short excerpt (up to 300 words)

> The SageMaker HyperPod CLI 1. Make sure that create_vpc_stack=True, create_eks_cluster_stack=True, create_hyperpod_cluster_stack=True, HyperPod CLI currently supports

### README headings

- SageMaker HyperPod command-line interface
- Table of Contents
- Overview
- Prerequisites
- Region Configuration
- Prerequisites for Training
- Prerequisites for Inference
- Platform Support
- ML Framework Support
- Installation
- Usage
- Getting Started
- Getting Cluster information
- Connecting to a Cluster
- Getting Cluster Context
- CLI
- Cluster Management
- Initialize Cluster Configuration
- Configure Cluster Parameters
- Validate Configuration
- Create Cluster Stack
- List CloudFormation Stacks
- Describe Cluster Stack
- Delete Cluster Stack
- Update Existing Cluster
- Reset Configuration
- Training
- **Option 1**: Create Pytorch job through init experience
- Initialize Pytorch Job Configuration
- Configure Pytorch Job Parameters

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> The SageMaker HyperPod CLI

### Getting started and usage: Installation

> 1. Make sure that

### Architecture and design: Infrastructure components

> create_vpc_stack=True, create_eks_cluster_stack=True, create_hyperpod_cluster_stack=True,

### Technology and requirements: Prerequisites for Training

> HyperPod CLI currently supports

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,502,146 |
| Shell | 97,158 |
| Go Template | 45,148 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- setup.py (capture: captured)
- doc/Makefile (capture: captured)
- doc/requirements.txt (capture: captured) — dependency clues: autodoc-pydantic, ipykernel, jupyter, linkify-it-py, myst-nb, nbsphinx, sphinx, sphinx-book-theme, sphinx-click, sphinx-copybutton, sphinx-design, sphinx-tabs
- hyperpod-cluster-stack-template/pyproject.toml (capture: captured) — dependency clues: pydantic
- hyperpod-custom-inference-template/pyproject.toml (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 43
- Forks at capture: 98
- Last updated: 2026-11-12T20:33:56Z
- Last pushed: 2026-11-22T03:35:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/sagemaker-hyperpod-cli)
- [README](https://github.com/aws/sagemaker-hyperpod-cli/blob/main/README.md)
- [Issues](https://github.com/aws/sagemaker-hyperpod-cli/issues)
- [Releases](https://github.com/aws/sagemaker-hyperpod-cli/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
