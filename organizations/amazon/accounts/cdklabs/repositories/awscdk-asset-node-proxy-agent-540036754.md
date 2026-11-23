# cdklabs/awscdk-asset-node-proxy-agent

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/awscdk-asset-node-proxy-agent](https://github.com/cdklabs/awscdk-asset-node-proxy-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/awscdk-asset-node-proxy-agent/blob/main/README.md)
- README blob SHA: 4d6f984a3511b8d29cf371fdedaeec72972b4822
- Repository ID: 540036754
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:23+00:00

### Short excerpt (up to 100 words)

> This module bundles the NPM dependency `proxy-agent` as a local asset. It exposes constants `ASSET_FILE` and `LAYER_SOURCE_DIR` that can be consumed via the CDK `Asset` construct. Usage: import { ASSET_FILE, LAYER_SOURCE_DIR } from '@aws-cdk/asset-node-proxy-agent-v6'; import * as lambda from 'aws-cdk-lib/aws-lambda'; import * as s3_assets from 'aws-cdk-lib/aws-s3-assets'; import { FileSystem } from 'aws-cdk-lib'; declare const fn: lambda.Function; const asset = new s3_assets.Asset(this, 'layer-asset', { path: ASSET_FILE, assetHash: FileSystem.fingerprint(LAYER_SOURCE_DIR), }); fn.addLayers(new lambda.LayerVersion(this, 'ProxyAgentLayer', { code: lambda.Code.fromBucket(asset.bucket, asset.s3ObjectKey), }));

### README headings

- AWS Lambda Layer with the NPM dependency proxy-agent

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 5,434 |
| Dockerfile | 501 |
| Shell | 446 |
| JavaScript | 105 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-pacmak, jsii-rosetta
- layer/Dockerfile (capture: captured)
- layer/package.json (capture: captured) — dependency clues: proxy-agent

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 2
- Last updated: 2026-11-09T23:04:37Z
- Last pushed: 2026-11-23T00:33:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/awscdk-asset-node-proxy-agent)
- [README](https://github.com/cdklabs/awscdk-asset-node-proxy-agent/blob/main/README.md)
- [Issues](https://github.com/cdklabs/awscdk-asset-node-proxy-agent/issues)
- [Releases](https://github.com/cdklabs/awscdk-asset-node-proxy-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
