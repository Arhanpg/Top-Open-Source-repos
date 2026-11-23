# aws-actions/configure-aws-credentials

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/configure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-actions/configure-aws-credentials/blob/main/README.md)
- README blob SHA: 6dfeb15c9c439ddba1aa54362e43005eb4429b3a
- Repository ID: 220391287
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Configure AWS credential environment variables for use in other GitHub Actions.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:46+00:00

### Short excerpt (up to 100 words)

> Authenticate to AWS in GitHub Actions (and others)! Works especially well with 1. Create an IAM Identity Provider in your AWS account for GitHub OIDC. (See 2. Create an IAM Role in your AWS account with a trust policy that allows GitHub Actions to assume it. (Expand the sections below) <details> { "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Federated": "arn:aws:iam::<AWS_ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com" }, "Action": "sts:AssumeRoleWithWebIdentity", "Condition": { "StringEquals": { "token.actions.githubusercontent.com:aud": "sts.amazonaws.com", "token.actions.githubusercontent.com:sub": "repo:<GITHUB_ORG>@<ORG_ID>/<GITHUB_REPOSITORY>@<REPO_ID>:ref:refs/heads/<GITHUB_BRANCH>" } } } ] } Note: The value of the `sub` claim may be different depending on the workflow and the environment in which it's running.

### README headings

- Configure AWS Credentials
- Quick Start (OIDC, recommended)
- Security Recommendations
- Non-OIDC Authentication Options
- Additional Options
- Options
- Adjust the retry mechanism
- Mask account ID
- Unset current credentials
- Inputs as environment variables
- Configure named AWS profiles
- Skip the cleanup
- Use an HTTP proxy
- Your environment configuration
- Special characters in AWS_SECRET_ACCESS_KEY
- Session Naming and Policies
- Custom session tags
- Session policies
- Inline session policies
- Managed session policies
- Custom STS endpoint
- OIDC Configuration Details
- OIDC Audience
- Configuring IAM to trust GitHub
- Claims and scoping permissions
- Immutable subject claims
- Legacy (mutable) sub claim
- Immutable sub claim
- Inspecting the token
- Further information about OIDC

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 199,743 |
| JavaScript | 54 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @aws-sdk/client-sts, @aws-sdk/credential-provider-env, @aws-sdk/credential-provider-node, @biomejs/biome, @smithy/node-http-handler, @smithy/property-provider, @types/node, @vitest/coverage-v8, aws-sdk-client-mock, esbuild, generate-license-file, json-schema, markdownlint-cli, memfs, proxy-agent, standard-version, typescript, vitest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 3031
- Forks at capture: 583
- Last updated: 2026-11-22T17:23:08Z
- Last pushed: 2026-11-17T03:44:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/configure-aws-credentials)
- [README](https://github.com/aws-actions/configure-aws-credentials/blob/main/README.md)
- [Issues](https://github.com/aws-actions/configure-aws-credentials/issues)
- [Releases](https://github.com/aws-actions/configure-aws-credentials/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
