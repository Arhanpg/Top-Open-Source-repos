# cdklabs/awscdk-asset-kubectl

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/awscdk-asset-kubectl](https://github.com/cdklabs/awscdk-asset-kubectl)
- Default branch: kubectl-v37/main
- README: [Open upstream README](https://github.com/cdklabs/awscdk-asset-kubectl/blob/kubectl-v37/main/README.md)
- README blob SHA: 19aef6e15c66755699d735bb22ac67a46e82721b
- Repository ID: 536358159
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:39:10+00:00

### Short excerpt (up to 100 words)

> This module exports a single class called `KubectlV37Layer` which is a `lambda.LayerVersion` that bundles the `kubectl` and the Usage: // KubectlLayer bundles the 'kubectl' and 'helm' command lines import { KubectlV37Layer } from '@aws-cdk/lambda-layer-kubectl-v37'; import * as lambda from 'aws-cdk-lib/aws-lambda'; declare const fn: lambda.Function; const kubectl = new KubectlV37Layer(this, 'KubectlLayer'); fn.addLayers(kubectl); `kubectl` will be installed under `/opt/kubectl/kubectl`, and `helm` will be installed under `/opt/helm/helm`.

### README headings

- Lambda Layer with KubeCtl v1.37

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 7,998 |
| Shell | 4,792 |
| Dockerfile | 876 |
| Python | 180 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen
- layer/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 27
- Forks at capture: 22
- Last updated: 2026-11-02T22:20:36Z
- Last pushed: 2026-11-20T08:32:06Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/awscdk-asset-kubectl)
- [README](https://github.com/cdklabs/awscdk-asset-kubectl/blob/kubectl-v37/main/README.md)
- [Issues](https://github.com/cdklabs/awscdk-asset-kubectl/issues)
- [Releases](https://github.com/cdklabs/awscdk-asset-kubectl/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
