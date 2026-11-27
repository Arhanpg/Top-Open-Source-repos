# awslabs/visual-asset-management-system

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/visual-asset-management-system](https://github.com/awslabs/visual-asset-management-system)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/visual-asset-management-system/blob/main/README.md)
- README blob SHA: 9034c30dceac9b8fdaf8ce49c880523a4d48bdc6
- README bytes captured: 15907
- README truncated at capture limit: False
- Repository ID: 539642587
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Visual Asset Management System (VAMS) is a purpose-built, AWS native accelerator solution for the management and distribution of traditional to specialized visual assets used in physical AI and spatial computing. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T21:18:32+00:00

### Short excerpt (up to 300 words)

> **Visual Asset Management System cd ../infra && npm VAMS deploys as a Python 3.12+, Docker (or VAMS follows the AWS

### README headings

- Visual Asset Management System (VAMS)
- _Notice_
- Introduction
- Overview
- Key capabilities
- Screenshots
- Architecture
- Quick start
- Prerequisites
- Deploy
- 1. Build the web application
- Viewer plugins are baked in at build time from
- web/src/visualizerPlugin/config/viewerConfig.json; the shipped defaults work unedited.
- To change which viewers ship, edit it before building.
- See documentation/docusaurus-site/docs/additional/viewer-plugins.md
- 2. Install CDK dependencies
- 3. Bootstrap CDK (first time only)
- This Quick start deploys to us-east-1. The Region is env.region in config.json, or
- your AWS CLI default Region when env.region is empty (as shipped).
- For any other Region, including AWS GovCloud (US) and the AWS European Sovereign
- Cloud, and for importing an existing VPC, follow the Bootstrap step in
- documentation/docusaurus-site/docs/deployment/deploy-the-solution.md
- 4. Configure deployment (edit infra/config/config.json)
- See documentation/docusaurus-site/docs/deployment/configuration-reference.md
- 5. Deploy
- Documentation
- Documentation sections
- Access methods
- Partner integrations
- Configuration

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> **Visual Asset Management System

### Getting started and usage: 2. Install CDK dependencies

> cd ../infra && npm

### Architecture and design: Architecture

> VAMS deploys as a

### Technology and requirements: Prerequisites

> Python 3.12+, Docker (or

### Limitations and security: Security

> VAMS follows the AWS

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 20,334,590 |
| TypeScript | 11,852,388 |
| C# | 197,479 |
| JavaScript | 126,518 |
| CSS | 98,078 |
| Dockerfile | 34,857 |
| Shell | 28,357 |
| SCSS | 17,417 |
| PowerShell | 15,161 |
| HTML | 7,876 |
| Makefile | 241 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @types/sanitize-html, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-plugin-react, minimist, prettier, standard-version
- backend/makefile (capture: captured)
- backend/pyproject.toml (capture: captured) — dependency clues: aws-lambda-powertools, boto3, casbin, coverage, flake8, geojson, joserfc, locked-dict, moto, mypy, opensearch-py, pydantic, pyjwt, pytest, pytest-mock, pytest-watch, pytest-xdist, urllib3
- backend/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, boto3, botocore, casbin, certifi, charset-normalizer, events, idna, jmespath, locked-dict, opensearch-py, pydantic, python-dateutil, requests, s3transfer, simpleeval, six, typing-extensions, urllib3
- infra/package.json (capture: captured) — dependency clues: @aws-cdk/aws-lambda-python-alpha, @aws-sdk/client-iam, @aws-sdk/client-ssm, @esbuild/darwin-arm64, @esbuild/darwin-x64, @esbuild/linux-x64, @opensearch-project/opensearch, @types/aws-lambda, @types/aws4, @types/jest, @types/node, aws-cdk, aws-cdk-lib, aws4, cdk-nag, constructs, dotenv, esbuild, jest, source-map-support
- web/package.json (capture: captured) — dependency clues: @aws-amplify/ui-react, @aws-sdk/client-s3, @aws-sdk/lib-storage, @aws-sdk/s3-request-presigner, @babel/plugin-proposal-private-property-in-object, @babel/preset-env, @babel/preset-react, @babel/preset-typescript, @badgateway/oauth2-client, @cloudscape-design/collection-hooks, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @cloudscape-design/jest-preset, @dnd-kit/core, @dnd-kit/sortable, @dnd-kit/utilities, @esbuild/darwin-arm64, @esbuild/darwin-x64, @esbuild/linux-x64

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 153
- Forks at capture: 63
- Last updated: 2026-11-18T02:04:27Z
- Last pushed: 2026-11-23T19:26:30Z
- Topics: 2d, 3d, datalake, digital-asset-management, extended-reality, metadata, physical-ai, pipelines, spatial-computing, spatial-data

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/visual-asset-management-system)
- [README](https://github.com/awslabs/visual-asset-management-system/blob/main/README.md)
- [Issues](https://github.com/awslabs/visual-asset-management-system/issues)
- [Releases](https://github.com/awslabs/visual-asset-management-system/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
