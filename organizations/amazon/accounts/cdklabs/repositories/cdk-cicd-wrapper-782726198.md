# cdklabs/cdk-cicd-wrapper

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-cicd-wrapper](https://github.com/cdklabs/cdk-cicd-wrapper)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-cicd-wrapper/blob/main/README.md)
- README blob SHA: 5b7991c05f513e754fd22ebae60ecdcd4a2193c7
- Repository ID: 782726198
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository contains the infrastructure as code to wrap your AWS CDK project with CI/CD around it.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:31:10+00:00

### Short excerpt (up to 100 words)

> The CDK CI/CD Wrapper turns an ordinary AWS CDK app into a multi-account delivery pipeline. You describe the source repository and the stages (each with its account and Regions) in one `cicd.config.ts`. The `cdk-cicd` CLI provisions the pipeline in your pipeline account, and from then on every push builds, checks and deploys the app stage by stage. Your `bin/` stays an ordinary CDK app: the one wrapper import the basic flow needs is the `stageStackName` helper, which names a stack per stage. 1. **`npx cdk-cicd init`** writes `cicd.config.ts` and points `cdk.json` at `cdk-cicd exec`, which runs your app with the

### README headings

- CDK CI/CD Wrapper
- How it works
- Quick start
- What the pipeline runs
- Choosing an engine
- AI agents: before a deploy, and after a failure
- CLI commands
- Deployment contracts
- Features
- Repository layout
- Security
- License
- Community
- Contributors

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 1,594,139 |
| Shell | 231,250 |
| JavaScript | 22,322 |
| Python | 3,392 |
| Dockerfile | 37 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @commitlint/cli, @commitlint/config-conventional, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @typescript-eslint/typescript-estree, aislop, all-contributors-cli, cdklabs-projen-project-types, constructs, eslint, eslint-config-prettier, eslint-plugin-prettier, husky, node-fetch, prettier, projen, shx, ts-node, typescript
- samples/cdk-cicd-wrapper-example/package.json (capture: captured) — dependency clues: @cdklabs/cdk-cicd-wrapper, @cdklabs/cdk-cicd-wrapper-cli, aws-cdk, aws-cdk-lib, cdk-nag, constructs, ts-node, typescript
- samples/cdk-python-example/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, constructs
- samples/security-plugins-proof/package.json (capture: captured) — dependency clues: @cdklabs/cdk-cicd-wrapper, aws-cdk, aws-cdk-lib, cdk-nag, constructs, ts-node, typescript
- packages/@cdklabs/cdk-cicd-wrapper-cli/package.json (capture: captured) — dependency clues: @aws-cdk/cloud-assembly-schema, @aws-sdk/client-s3, @aws-sdk/credential-providers, @cdklabs/cdk-cicd-wrapper, @types/fs-extra, @types/jest, @types/node, @types/semver, @types/yargs, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @typescript-eslint/typescript-estree, commit-and-tag-version, constructs, csv, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier
- packages/@cdklabs/cdk-cicd-wrapper/package.json (capture: captured) — dependency clues: @aws-cdk/app-staging-synthesizer-alpha, @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @cloudcomponents/cdk-pull-request-approval-rule, @cloudcomponents/cdk-pull-request-check, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @typescript-eslint/typescript-estree, aws-cdk-lib, cdk-nag, cdk-pipelines-github, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 33
- Forks at capture: 9
- Last updated: 2026-11-09T07:58:59Z
- Last pushed: 2026-11-23T11:52:15Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-cicd-wrapper)
- [README](https://github.com/cdklabs/cdk-cicd-wrapper/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-cicd-wrapper/issues)
- [Releases](https://github.com/cdklabs/cdk-cicd-wrapper/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
