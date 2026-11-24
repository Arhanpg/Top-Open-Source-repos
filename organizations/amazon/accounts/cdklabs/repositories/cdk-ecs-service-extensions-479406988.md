# cdklabs/cdk-ecs-service-extensions

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-ecs-service-extensions](https://github.com/cdklabs/cdk-ecs-service-extensions)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-ecs-service-extensions/blob/main/README.md)
- README blob SHA: ac421daadab12c4e7a826f0cceec9d83afd8b589
- Repository ID: 479406988
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:03+00:00

### Short excerpt (up to 100 words)

> This library provides a high level, extensible pattern for constructing services deployed using Amazon ECS. import { AppMeshExtension, CloudwatchAgentExtension, Container, Environment, FireLensExtension, HttpLoadBalancerExtension, Service, ServiceDescription, XRayExtension, } from '@aws-cdk-containers/ecs-service-extensions'; If you are using the `@aws-cdk-containers/ecs-service-extensions` v1 and need to migrate to v2, see the Migration Guide. The `Service` construct provided by this module can be extended with optional `ServiceExtension` classes that add supplemental ECS features including: - AWS X-Ray for tracing your application - Amazon CloudWatch Agent for capturing per task stats - AWS AppMesh for adding your application to a service mesh - Application Load Balancer, for exposing your

### README headings

- CDK Construct library for building ECS services
- `Service` construct
- Example
- Creating an `Environment`
- Defining your `ServiceDescription`
- Logging using `awslogs` log driver
- Launching the `ServiceDescription` as a `Service`
- Creating your own taskRole
- Configure Custom Health Check
- Task Auto-Scaling
- Creating your own custom `ServiceExtension`
- Connecting services
- Importing a pre-existing cluster
- Injecter Extension
- Publishing to SNS Topics
- Queue Extension
- Setting up SNS Topic Subscriptions for SQS Queues
- Configuring auto scaling based on SQS Queues
- Publish/Subscribe Service Pattern
- Community Extensions

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 206,247 |
| Python | 62,887 |
| Shell | 548 |
| Dockerfile | 157 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen
- lambda/assign-public-ip/Pipfile (capture: captured) — dependency clues: boto3, coverage, name, python_version, url, verify_ssl, yapf
- test/queue-handler/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 67
- Forks at capture: 11
- Last updated: 2026-11-02T22:19:35Z
- Last pushed: 2026-11-23T00:05:41Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-ecs-service-extensions)
- [README](https://github.com/cdklabs/cdk-ecs-service-extensions/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-ecs-service-extensions/issues)
- [Releases](https://github.com/cdklabs/cdk-ecs-service-extensions/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
