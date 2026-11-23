# aws-solutions/distributed-load-testing-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/distributed-load-testing-on-aws](https://github.com/aws-solutions/distributed-load-testing-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/README.md)
- README blob SHA: 482c97bb37bf016094d6dbd1eb8d275546f83d6f
- Repository ID: 220571062
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Distributed Load Testing on AWS automates performance testing at scale, demonstrating how systems behave under different load conditions and helping identify potential performance issues throughout their lifecycle.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:28:25+00:00

### Short excerpt (up to 100 words)

> Distributed Load Testing on AWS helps you automate performance testing of your software applications at scale to identify bottlenecks before you release your application. This solution simulates thousands of connected users generating HTTP requests at a sustained rate without the need to provision servers. - Deploy Amazon ECS on AWS Fargate containers that run independently to test the load capacity of your application. - Simulate tens of thousands of concurrent users across multiple AWS Regions generating requests at a continuous pace. - Customize your application tests using JMeter, K6, Locust test scripts, or simple HTTP endpoint configuration. - Schedule load

### README headings

- Distributed Load Testing on AWS
- On this Page
- Public Roadmap
- Architecture Overview
- MCP Server Integration (Optional)
- Traffic shape: Standard and Native
- Deployment
- Source Code
- Local Development
- Prerequisites
- Environment Setup
- Deploying from Source
- Regional Stack Management
- Regional Stack Version Compatibility
- Available Make Targets
- Notes
- Testing
- Creating a custom build
- Prerequisites
- Running unit tests for customization
- Building distributable for customization
- Creating a custom container build
- Third-party testing frameworks
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 3,749,601 |
| JavaScript | 3,055,617 |
| Shell | 99,500 |
| Python | 12,145 |
| Makefile | 11,485 |
| Dockerfile | 8,143 |
| CSS | 1,431 |
| HTML | 552 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- package.json (capture: captured) — dependency clues: @eslint/js, @rollup/rollup-linux-x64-gnu, @types/node, @vitest/coverage-v8, aws-sdk-client-mock, esbuild, eslint, globals, jiti, prettier, syncpack, ts-node, typescript, typescript-eslint, vitest
- source/package.json (capture: captured) — dependency clues: @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-config-prettier, eslint-config-standard, eslint-plugin-cypress, eslint-plugin-header, eslint-plugin-import, eslint-plugin-jsdoc, eslint-plugin-node, eslint-plugin-prettier, eslint-plugin-react, prettier, typescript
- source/api-services/package.json (capture: captured) — dependency clues: @amzn/dlt-common, @aws-sdk/client-cloudformation, @aws-sdk/client-cloudwatch, @aws-sdk/client-cloudwatch-events, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-devops-agent, @aws-sdk/client-dynamodb, @aws-sdk/client-ecs, @aws-sdk/client-lambda, @aws-sdk/client-s3, @aws-sdk/client-scheduler, @aws-sdk/client-service-quotas, @aws-sdk/client-sfn, @aws-sdk/lib-dynamodb, @babel/preset-env, @babel/preset-typescript, @types/aws-lambda, @types/jest, axios, axios-mock-adapter
- source/cli/package.json (capture: captured) — dependency clues: @amzn/dlt-common, @aws-sdk/client-cognito-identity, @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-s3, @aws-sdk/credential-providers, @types/archiver, @types/aws4, @types/node, archiver, aws4, chalk, cognito-srp-helper, commander, memfs, open
- source/common/package.json (capture: captured) — dependency clues: @aws-lambda-powertools/logger, @aws-sdk/client-dynamodb, @aws-sdk/lib-dynamodb, @types/luxon, cron-parser, luxon, nanoid, zod

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 424
- Forks at capture: 155
- Last updated: 2026-11-19T21:35:46Z
- Last pushed: 2026-11-16T15:25:46Z
- Topics: api, aws, jmeter, k6, load-testing, locust, mcp, scale

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/distributed-load-testing-on-aws)
- [README](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/distributed-load-testing-on-aws/issues)
- [Releases](https://github.com/aws-solutions/distributed-load-testing-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
