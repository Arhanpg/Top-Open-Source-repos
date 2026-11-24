# cdklabs/cdk-ecs-codedeploy

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-ecs-codedeploy](https://github.com/cdklabs/cdk-ecs-codedeploy)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-ecs-codedeploy/blob/main/README.md)
- README blob SHA: 0ece52f4ffaff08f143e0c322e22b896e479f122
- Repository ID: 569454594
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:00+00:00

### Short excerpt (up to 100 words)

> This project contains CDK constructs to create CodeDeploy ECS deployments. yarn add @cdklabs/cdk-ecs-codedeploy See https://mvnrepository.com/artifact/io.github.cdklabs/cdk-ecs-codedeploy See https://pypi.org/project/cdklabs.ecs-codedeploy/ See https://www.nuget.org/packages/Cdklabs.CdkEcsCodeDeploy/ CodeDeploy for ECS can manage the deployment of new task definitions to ECS services. Only 1 deployment construct can be defined for a given EcsDeploymentGroup. declare const deploymentGroup: codeDeploy.IEcsDeploymentGroup; declare const taskDefinition: ecs.ITaskDefinition; new EcsDeployment({ deploymentGroup, targetService: { taskDefinition, containerName: 'mycontainer', containerPort: 80, }, }); The deployment will use the AutoRollbackConfig for the EcsDeploymentGroup unless it is overridden in the deployment: declare const deploymentGroup: codeDeploy.IEcsDeploymentGroup; declare const taskDefinition: ecs.ITaskDefinition; new EcsDeployment({ deploymentGroup, targetService: { taskDefinition, containerName: 'mycontainer', containerPort: 80, }, autoRollback:

### README headings

- CDK ECS CodeDeploy
- Installation
- Deployments
- API Canaries
- Application Load Balanced CodeDeployed Fargate Service
- Local Development
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 107,609 |
| JavaScript | 2,200 |
| Dockerfile | 99 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @aws-sdk/client-codedeploy, @stylistic/eslint-plugin, @types/aws-lambda, @types/jest, @types/lambda-tester, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, aws-sdk-client-mock, aws-sdk-client-mock-jest, cdk-nag, cdklabs-projen-project-types, commit-and-tag-version, constructs, esbuild, eslint
- canary-src/package.json (capture: captured) — dependency clues: jmespath
- test/nginx/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 40
- Forks at capture: 10
- Last updated: 2026-10-26T19:09:33Z
- Last pushed: 2026-11-23T18:05:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-ecs-codedeploy)
- [README](https://github.com/cdklabs/cdk-ecs-codedeploy/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-ecs-codedeploy/issues)
- [Releases](https://github.com/cdklabs/cdk-ecs-codedeploy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
