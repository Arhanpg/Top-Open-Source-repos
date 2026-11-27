# aws-samples/amazon-omics-webapp-integrations

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-omics-webapp-integrations](https://github.com/aws-samples/amazon-omics-webapp-integrations)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-omics-webapp-integrations/blob/main/README.md)
- README blob SHA: f067626a15bb410f8d612cd7c06540bfec9ccc1c
- README bytes captured: 9446
- README truncated at capture limit: False
- Repository ID: 623553817
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This project contains the webapp sample integrated with AWS HealthOmics, which allows users such as admin and bioinformaticians to operate Amazon Omics workflow easily and check the run command status with charts and tables.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:41:07+00:00

### Short excerpt (up to 300 words)

> You can create new You can create new An AWS accoount Create See CONTRIBUTING for more

### README headings

- AWS HealthOmics Webapp
- Architecture overview
- Dashboard
- Repository
- Workflow
- Private workflow
- Ready2Run workflow
- Job
- Users (Only Admin)
- Prerequisites
- Webapp configuration
- Add your aws profile in `cdk.json`
- Create a config file as `config.ts`
- Deployment
- Deploy the infrastructure and frontend stacks with AWS CDK
- Cleanup
- Destroy all stacks(the infrastructure and frontend stack) with AWS CDK
- Multi-tenancy mode
- Prerequisites
- Commands
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Architecture overview

> You can create new

### Architecture and design: Architecture overview

> You can create new

### Technology and requirements: Prerequisites

> An AWS accoount Create

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Vue | 83,591 |
| TypeScript | 83,415 |
| JavaScript | 18,743 |
| Velocity Template Language | 2,344 |
| HTML | 1,411 |
| SCSS | 777 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-ssm, @aws-sdk/credential-providers, @types/aws-lambda, @types/jest, @types/lodash, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdk-nag, constructs, esbuild, eslint, eslint-config-prettier, eslint-plugin-prettier, fs, husky, jest, lint-staged
- webapp/package.json (capture: captured) — dependency clues: @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-omics, @quasar/app-vite, @quasar/cli, @quasar/extras, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @urql/devtools, @urql/exchange-auth, @urql/vue, apexcharts, autoprefixer, aws-amplify, eslint, eslint-config-prettier, eslint-plugin-vue, graphql, lodash, path
- api/lambda/listOmicsJob/package.json (capture: captured) — dependency clues: @aws-sdk/client-omics, lodash
- api/lambda/manipulationEcr/package.json (capture: captured) — dependency clues: @aws-sdk/client-ecr, lodash
- api/lambda/mutationOmics/package.json (capture: captured) — dependency clues: @aws-sdk/client-ecr, @aws-sdk/client-iam, @aws-sdk/client-omics, lodash

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 19
- Forks at capture: 1
- Last updated: 2025-04-14T23:25:29Z
- Last pushed: 2024-11-20T23:36:28Z
- Topics: appsync, aws, cdk, graphql, lambda, omics, serverless, ui, vue3

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-omics-webapp-integrations)
- [README](https://github.com/aws-samples/amazon-omics-webapp-integrations/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-omics-webapp-integrations/issues)
- [Releases](https://github.com/aws-samples/amazon-omics-webapp-integrations/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
