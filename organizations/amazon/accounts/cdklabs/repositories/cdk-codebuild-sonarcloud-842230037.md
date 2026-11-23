# cdklabs/cdk-codebuild-sonarcloud

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-codebuild-sonarcloud](https://github.com/cdklabs/cdk-codebuild-sonarcloud)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-codebuild-sonarcloud/blob/main/README.md)
- README blob SHA: 5d60f40b9c76720050c6d37b55a2f1e38c7453e2
- Repository ID: 842230037
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:31:15+00:00

### Short excerpt (up to 100 words)

> This CDK construct creates an AWS Codebuild action to perform static code analysis using Sonarcloud. Here is how to include the construct in your CDK code : const sonarcloudScan = new CDKCodeBuildSonarcloud(this, 'SonarcloudBuildAction', { sourceOutput: sourceOutput, sonarOrganizationName: 'my-sonarcloud-organization-name', sonarProjectName: 'my-sonarcloud-project-name', }); Check Here for an example on how to use the construct. A Sonarcloud account is required to use this construct. Create a Sonarcloud token to connect securely to Sonarcloud from AWS CodeBuild. Store this token in your AWS account in AWS Secret Manager, name the secret "sonar-token" and use "SONAR_TOKEN" as the secret key. Please review the AWS Secret

### README headings

- Getting started
- Security

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 4,695 |
| Dockerfile | 1,332 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen, jsii-pacmak

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 2
- Forks at capture: 0
- Last updated: 2026-11-02T22:17:50Z
- Last pushed: 2026-11-20T08:32:32Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-codebuild-sonarcloud)
- [README](https://github.com/cdklabs/cdk-codebuild-sonarcloud/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-codebuild-sonarcloud/issues)
- [Releases](https://github.com/cdklabs/cdk-codebuild-sonarcloud/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
