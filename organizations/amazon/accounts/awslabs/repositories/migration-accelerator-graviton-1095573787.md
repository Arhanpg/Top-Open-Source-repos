# awslabs/migration-accelerator-graviton

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/migration-accelerator-graviton](https://github.com/awslabs/migration-accelerator-graviton)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/migration-accelerator-graviton/blob/main/README.md)
- README blob SHA: e4b5af829e898ea2a0f0b1628abac7a47518e7fa
- README bytes captured: 16612
- README truncated at capture limit: False
- Repository ID: 1095573787
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:40:30+00:00

### Short excerpt (up to 300 words)

> Migrating from x86 to python graviton_validator.py app-sbom.json --yes pip install -r requirements.txt AWS account with administrative python graviton_validator.py app-sbom.json --yes

### README headings

- Migration Accelerator for Graviton
- Overview
- Why Migrate to AWS Graviton?
- Target Audience
- What Can It Analyze?
- 📋 Application Inventories (SBOM Files)
- 📦 Dependency Files
- How Does It Work?
- 🔍 **Analysis Process**
- 📊 **Compatibility Results**
- Architecture
- Solution Overview
- AWS Services Used
- Getting Started
- Prerequisites
- Option 0: Generate SBOM Files (If Needed)
- Option 1: Use app_identifier for running instances/VMs
- Fleet-wide discovery using AWS SSM
- Or use Ansible for multiple servers
- Option 1: AWS Hosted Solution (Recommended)
- Step 1: Deploy Infrastructure
- Deploy everything with one command (recommended)
- The deploy script automatically:
- - Creates/manages Terraform state bucket
- - Deploys Terraform infrastructure
- - Enables S3 EventBridge notifications
- - Verifies deployment
- - Shows usage instructions
- Use existing state bucket
- Or manual deployment (requires state bucket)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> Migrating from x86 to

### Features and capabilities: Comprehensive analysis with all features

> python graviton_validator.py app-sbom.json --yes

### Getting started and usage: Install Python dependencies

> pip install -r requirements.txt

### Technology and requirements: Prerequisites

> AWS account with administrative

### Limitations and security: Quick compatibility check in pipeline

> python graviton_validator.py app-sbom.json --yes

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,059,446 |
| Shell | 94,647 |
| HCL | 36,286 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: PyYAML, beautifulsoup4, defusedxml, openpyxl, packaging, pytest, pytest-cov, python-Levenshtein, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 6
- Last updated: 2026-11-12T19:18:34Z
- Last pushed: 2026-05-11T05:37:33Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/migration-accelerator-graviton)
- [README](https://github.com/awslabs/migration-accelerator-graviton/blob/main/README.md)
- [Issues](https://github.com/awslabs/migration-accelerator-graviton/issues)
- [Releases](https://github.com/awslabs/migration-accelerator-graviton/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
