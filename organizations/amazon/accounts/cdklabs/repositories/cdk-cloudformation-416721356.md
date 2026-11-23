# cdklabs/cdk-cloudformation

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-cloudformation/blob/main/README.md)
- README blob SHA: 72e0a72617dea1715f7dfd878f5ff3313c8721a3
- Repository ID: 416721356
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:31:14+00:00

### Short excerpt (up to 100 words)

> This project includes an AWS CDK construct library for every public extension in the [AWS CloudFormation Registry]. Every public extension (module/resource) in the AWS CloudFormation Registry is available in a separate code library in all AWS CDK supported languages. Each library includes generated constructs and data types based on the extension's schema. For example, to use the `TF::Random::String` type in TypeScript: Install the module: npm install @cdk-cloudformation/tf-random-string Import the construct to your code and add it to your app like any other construct: import { CfnString } from '@cdk-cloudformation/tf-random-string'; new CfnString(this, 'MyString', { length: 100, lower: true, upper: true, });

### README headings

- Construct Libraries for Public CloudFormation Extensions
- Usage
- Versioning
- Release Status
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 1,357,995 |
| JavaScript | 2,302 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-github-oidc, aws-cdk-lib, aws-sdk, case, cdk-import, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-pacmak
- packages/@cdk-cloudformation/alexa-ask-skill/package.json (capture: captured) — dependency clues: aws-cdk-lib, constructs
- packages/@cdk-cloudformation/aqua-enterprise-enforcer/package.json (capture: captured) — dependency clues: aws-cdk-lib, constructs
- packages/@cdk-cloudformation/aqua-enterprise-kubeenforcer/package.json (capture: captured) — dependency clues: aws-cdk-lib, constructs
- packages/@cdk-cloudformation/aqua-enterprise-scanner/package.json (capture: captured) — dependency clues: aws-cdk-lib, constructs
- packages/@cdk-cloudformation/aqua-enterprise-server/package.json (capture: captured) — dependency clues: aws-cdk-lib, constructs

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 66
- Forks at capture: 5
- Last updated: 2026-11-10T10:39:44Z
- Last pushed: 2026-11-23T00:53:05Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-cloudformation)
- [README](https://github.com/cdklabs/cdk-cloudformation/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-cloudformation/issues)
- [Releases](https://github.com/cdklabs/cdk-cloudformation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
