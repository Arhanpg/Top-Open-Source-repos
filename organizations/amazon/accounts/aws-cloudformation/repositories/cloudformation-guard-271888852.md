# aws-cloudformation/cloudformation-guard

- Company: Amazon
- GitHub account: [https://github.com/aws-cloudformation](https://github.com/aws-cloudformation)
- Mapping status: official-directory-listed
- Repository: [aws-cloudformation/cloudformation-guard](https://github.com/aws-cloudformation/cloudformation-guard)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-cloudformation/cloudformation-guard/blob/main/README.md)
- README blob SHA: aa93e08bc8b3f0797d5a3173bcc0d6d7ecf40096
- README bytes captured: 38616
- README truncated at capture limit: False
- Repository ID: 271888852
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Guard offers a policy-as-code domain-specific language (DSL) to write rules and validate JSON- and YAML-formatted data such as CloudFormation Templates, K8s configurations, and Terraform JSON plans/configurations against those rules.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T20:19:05+00:00

### Short excerpt (up to 300 words)

> Resources: mySecurityGroup: Type: "AWS::EC2::SecurityGroup" **Clauses:** Provides the foundational $ curl --proto '=https' 1. Install docker. Follow Resources: mySecurityGroup: Type: "AWS::EC2::SecurityGroup"

### README headings

- AWS CloudFormation Guard
- Table of Contents
- FAQs
- Skip the checks if there are no S3 buckets present
- Guard DSL
- Tenets
- Features of Guard DSL
- Guard CLI
- Installation
- Installation from Pre-Built Release Binaries
- MacOS
- Ubuntu
- Windows
- Installation of Rust and Cargo
- Ubuntu/MacOS: Install Rust and Cargo
- Windows 10: Install Rust and Cargo
- Cargo-based Installation
- How does Guard CLI work?
- Validate
- Kubernetes container based limit checks
- These set of rules primarily apply to the version 1 of the API spec (including v1Beta) and
- the kind of document is a 'Pod'
- For the 'Pod' document ensure that containers have resource limits set
- for memory
- For the 'Pod' document ensure that containers have resource limits set
- for cpu
- Using Input Parameters
- How to use
- Example Usage
- ---

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Description: CloudFormation - EC2 Security Group

> Resources: mySecurityGroup: Type: "AWS::EC2::SecurityGroup"

### Features and capabilities: Features of Guard DSL

> **Clauses:** Provides the foundational

### Getting started and usage: Ubuntu/MacOS: Install Rust and Cargo

> $ curl --proto '=https'

### Technology and requirements: Prerequisites

> 1. Install docker. Follow

### Limitations and security: Description: CloudFormation - EC2 Security Group

> Resources: mySecurityGroup: Type: "AWS::EC2::SecurityGroup"

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Rust | 1,709,971 |
| TypeScript | 53,861 |
| JavaScript | 22,938 |
| Shell | 11,782 |
| Python | 7,896 |
| PowerShell | 4,127 |
| Dockerfile | 1,221 |
| C | 966 |
| Makefile | 810 |
| Handlebars | 225 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Cargo.toml (capture: captured)
- Dockerfile (capture: captured)
- Makefile (capture: captured)
- pyproject.toml (capture: captured)
- .devcontainer/Dockerfile (capture: captured)
- action/package.json (capture: captured) — dependency clues: @actions/core, @actions/exec, @actions/github, @eslint/eslintrc, @eslint/js, @jest/globals, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vercel/ncc, cfn-guard, eslint, eslint-plugin-github, eslint-plugin-jest, eslint-plugin-jsonc, eslint-plugin-prettier, globals, jest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1396
- Forks at capture: 201
- Last updated: 2026-11-23T16:49:44Z
- Last pushed: 2026-11-23T17:25:07Z
- Topics: cfn-guard, cloudformation, compliance, governance, k8s, policy-as-code, policy-rule-evaluation, security, terraform

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-cloudformation/cloudformation-guard)
- [README](https://github.com/aws-cloudformation/cloudformation-guard/blob/main/README.md)
- [Issues](https://github.com/aws-cloudformation/cloudformation-guard/issues)
- [Releases](https://github.com/aws-cloudformation/cloudformation-guard/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
