# cdklabs/aws-delivlib

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/aws-delivlib](https://github.com/cdklabs/aws-delivlib)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/aws-delivlib/blob/main/README.md)
- README blob SHA: 4b3c3e5f8a7c8e1de25cb0cedccbec91b908e227
- Repository ID: 153164192
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

setup and manage continuous delivery pipelines for code libraries in multiple languages

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:00+00:00

### Short excerpt (up to 100 words)

> **aws-delivlib** is a fabulous library for defining continuous pipelines for building, testing and publishing code libraries through AWS CodeBuild and AWS CodePipeline. **aws-delivlib** is used by the AWS Cloud Development Kit and was designed to support simultaneous delivery of the AWS CDK in multiple programming languages packaged via jsii. A delivlib pipeline consists of the following sequential stages. Each stage will execute all tasks concurrently: +-----------+ +-----------+ +-----------+ +----------------+ +-----------+ +-----------+ +-----+-----+ +-------+--------+ v v +-----+-----+ +-------+-------+ +-----------+ +---------------+ +-----------+ +---------------+ +-----------+ +---------------+ +-----------+ +---------------+ +---------------+ +---------------+ The following sections describe each stage and the configuration options available: - aws-delivlib

### README headings

- aws-delivlib
- Pipeline Structure
- Installation
- Source
- `repo`: Source Repository (required)
- CodeCommit
- GitHub
- `branch`: Source Control Branch (optional)
- Pull Request Builds
- Build
- `buildSpec`: Build Script (optional)
- `buildImage`: Build container image (optional)
- `env`: Build environment variables (optional)
- Other Build Options
- Tests
- Publish
- npm.js (JavaScript)
- NuGet (.NET)
- Assembly Signature
- Obtaining a new Code Signing Certificate
- Maven Central (Java)
- GPG Signing Key
- Sonatype Credentials
- Staging Profile ID
- PyPI (Python)
- GitHub Releases
- GitHub Pages
- Metrics
- Automatic Bumps and Pull Request Builds
- GitHub Access

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 445,396 |
| Shell | 36,804 |
| JavaScript | 2,727 |
| PowerShell | 671 |
| Dockerfile | 531 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-cloudwatch, @aws-sdk/client-codepipeline, @aws-sdk/client-s3, @aws-sdk/client-secrets-manager, @aws-sdk/client-ssm, @babel/plugin-transform-modules-commonjs, @stylistic/eslint-plugin, @types/adm-zip, @types/aws-lambda, @types/follow-redirects, @types/fs-extra, @types/jest, @types/node, @types/tar, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, JSONStream, adm-zip, aws-cdk, aws-cdk-lib
- lib/custom-resource-handlers/Dockerfile (capture: captured)
- lib/publishing/github/package.json (capture: captured) — dependency clues: @types/changelog-parser, @types/node, changelog-parser, octokit, typescript
- lib/__tests__/registry-sync/docker-asset/Dockerfile (capture: captured)
- lib/__tests__/package-integrity/handler/__fixtures__/non-projen-project/package.json (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 377
- Forks at capture: 37
- Last updated: 2026-11-19T21:08:06Z
- Last pushed: 2026-11-23T00:16:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/aws-delivlib)
- [README](https://github.com/cdklabs/aws-delivlib/blob/main/README.md)
- [Issues](https://github.com/cdklabs/aws-delivlib/issues)
- [Releases](https://github.com/cdklabs/aws-delivlib/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
