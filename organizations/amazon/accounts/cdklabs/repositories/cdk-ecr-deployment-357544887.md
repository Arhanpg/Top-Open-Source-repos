# cdklabs/cdk-ecr-deployment

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-ecr-deployment](https://github.com/cdklabs/cdk-ecr-deployment)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-ecr-deployment/blob/main/README.md)
- README blob SHA: 76c2902348c83ec683ca55db00e7a95a57f89b0b
- Repository ID: 357544887
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CDK construct to deploy docker image to Amazon ECR

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:43+00:00

### Short excerpt (up to 100 words)

> CDK construct to synchronize single docker image between docker registries. - Copy image or multi-architecture image index from ECR/external registry to (another) ECR/external registry - Copy an archive tarball image from s3 to ECR/external registry import { DockerImageAsset } from 'aws-cdk-lib/aws-ecr-assets'; const image = new DockerImageAsset(this, 'CDKDockerImage', { directory: path.join(__dirname, 'docker'), }); // Copy from cdk docker image asset to another ECR. new ecrdeploy.ECRDeployment(this, 'DeployDockerImage1', { src: new ecrdeploy.DockerImageName(image.imageUri), dest: new ecrdeploy.DockerImageName(`${cdk.Aws.ACCOUNT_ID}.dkr.ecr.us-west-2.amazonaws.com/my-nginx:latest`), }); // Copy from docker registry to ECR. new ecrdeploy.ECRDeployment(this, 'DeployDockerImage2', { src: new ecrdeploy.DockerImageName('nginx:latest'), dest: new ecrdeploy.DockerImageName(`${cdk.Aws.ACCOUNT_ID}.dkr.ecr.us-west-2.amazonaws.com/my-nginx2:latest`), }); // Copy from private docker registry to ECR. //

### README headings

- cdk-ecr-deployment
- Features
- Usage
- Examples: [examples/](./examples)
- [API](./API.md)
- Tech Details & Contributions

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 84,653 |
| TypeScript | 25,630 |
| Makefile | 1,046 |
| Shell | 1,041 |
| Dockerfile | 416 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen, jsii-pacmak
- examples/Dockerfile (capture: captured)
- lambda-src/Dockerfile (capture: captured)
- lambda-src/go.mod (capture: captured) — dependency clues: cyphar.com/go-pathrs, dario.cat/mergo, github.com/BurntSushi/toml, github.com/Microsoft/go-winio, github.com/ProtonMail/go-crypto, github.com/VividCortex/ewma, github.com/acarl005/stripansi, github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/ecr, github.com/aws/aws-sdk-go-v2/service/ecrpublic, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum
- lambda-src/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 189
- Forks at capture: 38
- Last updated: 2026-11-11T11:50:01Z
- Last pushed: 2026-11-23T00:37:49Z
- Topics: aws, cdk, deployment, docker, ecr, transport

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-ecr-deployment)
- [README](https://github.com/cdklabs/cdk-ecr-deployment/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-ecr-deployment/issues)
- [Releases](https://github.com/cdklabs/cdk-ecr-deployment/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
