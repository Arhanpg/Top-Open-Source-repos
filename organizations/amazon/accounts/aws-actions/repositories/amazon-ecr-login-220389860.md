# aws-actions/amazon-ecr-login

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/amazon-ecr-login](https://github.com/aws-actions/amazon-ecr-login)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-actions/amazon-ecr-login/blob/main/README.md)
- README blob SHA: 8b5737e3bc742da6c0dae046941b8c748ab1d96a
- Repository ID: 220389860
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Logs into Amazon ECR with the local Docker client.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:33:15+00:00

### Short excerpt (up to 100 words)

> Logs in the local Docker client to one or more Amazon ECR Private registries or an Amazon ECR Public registry. **Table of Contents** - New v2 Release - Example of Usage - Building and pushing an image - Using an image as a service - Credentials - AWS credentials - ECR Private token type - Docker credentials - Self-Hosted Runners - Proxy configuration - Permissions - ECR Private - ECR Public - Troubleshooting - License Summary - Security Disclosures In the new major version for this action, the default value of the `mask-password` input has changed from `false` to `true`.

### README headings

- Amazon ECR "Login" Action for GitHub Actions
- New v2 Release
- Examples of Usage
- Building and pushing an image
- Before each of the following examples, make sure to include the following:
- Login to Amazon ECR Private, then build and push a Docker image:
- Login to Amazon ECR Public, then build and push a Docker image:
- Login to Amazon ECR Private, then package and push a Helm chart:
- Login to Amazon ECR Public, then package and push a Helm chart:
- Other use-cases
- Login to ECR on multiple AWS accounts
- Run an image as a service
- Credentials
- AWS Credentials
- ECR Private token type
- Docker Credentials
- Self-Hosted Runners
- Proxy Configuration
- Your environment configuration
- Permissions
- ECR Private
- ECR Public
- Troubleshooting
- Inputs
- License Summary
- Security Disclosures

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 72,113 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @actions/exec, @aws-sdk/client-ecr, @aws-sdk/client-ecr-public, @aws-sdk/client-signin, @aws-sdk/credential-providers, @aws-sdk/node-http-handler, @eslint/js, @vercel/ncc, aws-sdk-client-mock, eslint, globals, https-proxy-agent, jest
- dist/package.json (capture: captured)
- dist/cleanup/package.json (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1063
- Forks at capture: 211
- Last updated: 2026-11-19T21:35:43Z
- Last pushed: 2026-11-18T00:11:18Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/amazon-ecr-login)
- [README](https://github.com/aws-actions/amazon-ecr-login/blob/main/README.md)
- [Issues](https://github.com/aws-actions/amazon-ecr-login/issues)
- [Releases](https://github.com/aws-actions/amazon-ecr-login/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
