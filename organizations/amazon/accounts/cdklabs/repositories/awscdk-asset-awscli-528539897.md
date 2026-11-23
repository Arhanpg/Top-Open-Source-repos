# cdklabs/awscdk-asset-awscli

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/awscdk-asset-awscli](https://github.com/cdklabs/awscdk-asset-awscli)
- Default branch: awscli-v1/main
- README: [Open upstream README](https://github.com/cdklabs/awscdk-asset-awscli/blob/awscli-v1/main/README.md)
- README blob SHA: 025f3237ec67a44e8e1d7772820a705be9ac24ea
- Repository ID: 528539897
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:07+00:00

### Short excerpt (up to 100 words)

> This module bundles the AWS CLI v1 as a local asset. It exposes constants `ASSET_FILE` and `LAYER_SOURCE_DIR` that can be consumed via the CDK `Asset` construct. Any Lambda Function that uses uses this asset must use a Python 3.x runtime. Usage: // AwsCliLayer bundles the AWS CLI in a lambda layer import { ASSET_FILE, LAYER_SOURCE_DIR } from '@aws-cdk/asset-awscli-v1'; import * as lambda from 'aws-cdk-lib/aws-lambda'; import * as s3_assets from 'aws-cdk-lib/aws-s3-assets'; import { FileSystem } from 'aws-cdk-lib'; declare const fn: lambda.Function; const asset = new s3_assets.Asset(this, 'layer-asset', { path: ASSET_FILE, assetHash: FileSystem.fingerprint(LAYER_SOURCE_DIR), }); fn.addLayers(new lambda.LayerVersion(this, 'AwsCliLayer', { code: lambda.Code.fromBucket(asset.bucket, asset.s3ObjectKey), }));

### README headings

- Asset with AWS CLI v1

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 6,285 |
| Dockerfile | 841 |
| Shell | 620 |
| Python | 115 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen, jsii-pacmak
- layer/Dockerfile (capture: captured)
- layer/requirements.txt (capture: captured) — dependency clues: awscli, pyasn1, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 8
- Forks at capture: 3
- Last updated: 2026-11-02T22:22:48Z
- Last pushed: 2026-11-23T00:22:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/awscdk-asset-awscli)
- [README](https://github.com/cdklabs/awscdk-asset-awscli/blob/awscli-v1/main/README.md)
- [Issues](https://github.com/cdklabs/awscdk-asset-awscli/issues)
- [Releases](https://github.com/cdklabs/awscdk-asset-awscli/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
