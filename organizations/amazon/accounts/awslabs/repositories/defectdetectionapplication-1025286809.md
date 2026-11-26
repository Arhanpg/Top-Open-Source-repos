# awslabs/DefectDetectionApplication

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/DefectDetectionApplication](https://github.com/awslabs/DefectDetectionApplication)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/DefectDetectionApplication/blob/main/README.md)
- README blob SHA: 948590122ab6db2baadb6f3a102b1f4a2d5286a8
- README bytes captured: 149348
- README truncated at capture limit: False
- Repository ID: 1025286809
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Defect Detection Application - A Edge Based Industrial Inspection System - AWS Solution Guidance

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T18:57:52+00:00

### Short excerpt (up to 300 words)

> DDA provides real-time defect The DDA video tutorial DDA supports both single-account AWS CLI configured, with Secure Tunneling reaches the

### README headings

- Defect Detection Application (DDA) - Portal Edition
- Table of Contents
- Overview
- Key Benefits
- Portal Features
- Agentic Operations
- Video Tutorials
- User Guide
- Deployment
- Architecture Overview
- Architecture Components
- Prerequisites
- Docker
- Component artifact bucket
- every region except us-east-1 requires the LocationConstraint
- us-east-1 must NOT pass --create-bucket-configuration
- Retrying a failed first deploy
- add --force if it holds images; that deletes those images
- deleting a table deletes its items; after a failed first deploy both are empty
- IAM Permissions for Installation
- Roles involved
- Policy files
- One-time setup (administrator)
- The user or role that assumes the installer role, for example an IAM Identity Center role
- What each step needs
- What the execution policies allow
- Step 1: Deploy Portal Infrastructure (Portal Account)
- 1.1 Configure CloudWatch Logs for API Gateway
- 1. Create IAM role for API Gateway CloudWatch Logs
- 2. Attach the AWS managed policy API Gateway uses to write logs

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> DDA provides real-time defect

### Getting started and usage: Video Tutorials

> The DDA video tutorial

### Architecture and design: Architecture Overview

> DDA supports both single-account

### Technology and requirements: Prerequisites

> AWS CLI configured, with

### Limitations and security: Security model (important)

> Secure Tunneling reaches the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 41,710,725 |
| TypeScript | 10,848,813 |
| Shell | 1,240,573 |
| C++ | 1,131,558 |
| Jupyter Notebook | 96,367 |
| Dockerfile | 51,563 |
| CMake | 38,342 |
| SWIG | 22,439 |
| CSS | 9,547 |
| JavaScript | 8,083 |
| HTML | 7,138 |
| PowerShell | 4,069 |
| C | 2,175 |
| Mako | 1,270 |
| Batchfile | 769 |
| SCSS | 766 |
| Makefile | 638 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- setup.py (capture: captured)
- hmi/package.json (capture: captured) — dependency clues: @playwright/test, fast-check, jsdom, typescript, vite, vitest
- com.dda.InferenceUploader/artifacts/requirements.txt (capture: captured) — dependency clues: boto3
- datasets/detection_training/requirements.txt (capture: captured) — dependency clues: numpy, onnx, onnxruntime, onnxslim, ultralytics
- edge-cv-portal/backend/requirements.txt (capture: captured) — dependency clues: PyYAML, boto3, botocore

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 24
- Forks at capture: 5
- Last updated: 2026-11-18T15:38:09Z
- Last pushed: 2026-11-23T15:55:12Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/DefectDetectionApplication)
- [README](https://github.com/awslabs/DefectDetectionApplication/blob/main/README.md)
- [Issues](https://github.com/awslabs/DefectDetectionApplication/issues)
- [Releases](https://github.com/awslabs/DefectDetectionApplication/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
