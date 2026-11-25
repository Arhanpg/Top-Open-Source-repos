# awslabs/aws-media-replay-engine

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-media-replay-engine](https://github.com/awslabs/aws-media-replay-engine)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/aws-media-replay-engine/blob/main/README.md)
- README blob SHA: 016ccf52b8528b417c4be8edfd2d79a921315c6a
- README bytes captured: 30371
- README truncated at capture limit: False
- Repository ID: 429563291
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Media Replay Engine (MRE) is a framework to build automated video clipping and replay (highlight) generation pipelines for live and video-on-demand content.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T21:12:59+00:00

### Short excerpt (up to 300 words)

> Media Replay Engine (MRE) For cost optimization, MRE 1. Execute uninstall.sh python == 3.11 aws-cli MRE uses AWS_IAM to

### README headings

- Install
- Prerequisites
- Deploying MRE using EC2
- Greenfield Deployment
- Upgrading
- MRE Backend
- MRE Frontend
- Run Frontend Locally
- Outputs
- Architecture Overview
- Architecture Components
- Control plane
- Data plane
- Generative AI Search
- Code Layout
- Demo
- Developers
- Security
- Improve HTTPS viewer connection security
- :heavy_exclamation_mark: **Important!**
- Cost
- Approximate cost (excluding free tiers)
- Limitations
- Uninstall
- Option 1: Uninstall using AWS CDK
- Delete the Frontend stack
- Delete the Gateway API stack
- Delete the Generative AI Search
- Delete the Dataplane stack
- Delete the Controlplane stacks

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> Media Replay Engine (MRE)

### Features and capabilities: Enabling Optional Data Export Features

> For cost optimization, MRE

### Getting started and usage: Option 2: Uninstall using script

> 1. Execute uninstall.sh

### Technology and requirements: Prerequisites

> python == 3.11 aws-cli

### Limitations and security: Security

> MRE uses AWS_IAM to

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,710,963 |
| JavaScript | 598,771 |
| Shell | 69,296 |
| CSS | 6,037 |
| HTML | 2,319 |
| Dockerfile | 1,648 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- tests/requirements.txt (capture: captured) — dependency clues: PyYAML, attrs, aws-cdk-lib, aws-cdk.asset-awscli-v1, aws-cdk.asset-kubectl-v20, aws-cdk.asset-node-proxy-agent-v5, blessed, boto3, botocore, cattrs, cdk-nag, certifi, chalice, charset-normalizer, click, constructs, execnet, filelock, idna, importlib-resources
- deployment/lambda_layer_factory/Dockerfile (capture: captured)
- docs/source/requirements.txt (capture: captured) — dependency clues: Babel, Jinja2, MarkupSafe, PyJWT, PyYAML, Pygments, Sphinx, WebOb, WebTest, alabaster, attrs, autodoc, aws-lambda-powertools, beautifulsoup4, blessed, boto3, botocore, certifi, chalice, chalicedoc
- source/frontend/package.json (capture: captured) — dependency clues: @aws-crypto/sha256-js, @aws-sdk/protocol-http, @aws-sdk/signature-v4, @babel/plugin-proposal-private-property-in-object, @emotion/react, @emotion/styled, @material-ui/core, @material-ui/icons, @material-ui/lab, @tanstack/react-query, ajv, aws-amplify, aws-cloudfront-sign, clsx, history, lodash, material-ui, moment, moment-duration-format, protocol-http
- source/gateway/requirements.txt (capture: captured)
- source/shared/requirements.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 115
- Forks at capture: 25
- Last updated: 2026-11-18T03:17:26Z
- Last pushed: 2026-09-13T20:09:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-media-replay-engine)
- [README](https://github.com/awslabs/aws-media-replay-engine/blob/main/README.md)
- [Issues](https://github.com/awslabs/aws-media-replay-engine/issues)
- [Releases](https://github.com/awslabs/aws-media-replay-engine/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
