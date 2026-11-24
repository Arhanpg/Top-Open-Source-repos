# cdklabs/cdk-ethereum-node

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-ethereum-node](https://github.com/cdklabs/cdk-ethereum-node)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-ethereum-node/blob/main/README.md)
- README blob SHA: a1a635a10ce6a76d41495199a5190126d9c194c1
- Repository ID: 523776470
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

CDK construct to deploy an Ethereum node running on Amazon Managed Blockchain

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:39:07+00:00

### Short excerpt (up to 100 words)

> This repository contains a CDK construct to deploy an Ethereum node running on Amazon Managed Blockchain. The following networks are supported: * Mainnet (default) * Testnet: Goerli * Testnet: Rinkeby * Testnet: Ropsten Note that this construct requires AWS CDK v2. npm install --save @cdklabs/cdk-ethereum-node pip3 install cdklabs.cdk-ethereum-node Add the following to `pom.xml`: dotnet add package Cdklabs.CdkEthereumNode A minimally complete deployment is shown below. By default, a `bc.t3.large` node will be created on the Ethereum Mainnet. import { Stack, StackProps } from 'aws-cdk-lib'; import { Construct } from 'constructs'; import { EthereumNode, Network, InstanceType } from '@cdklabs/cdk-ethereum-node'; export class MyStack

### README headings

- Ethereum on Amazon Managed Blockchain
- Installation
- JavaScript
- Python
- Java
- .NET
- Usage
- References
- Contributing
- Security
- Authors
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 10,783 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdk-nag, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen, jsii-pacmak, jsii-rosetta, projen

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 15
- Forks at capture: 5
- Last updated: 2026-05-31T02:18:22Z
- Last pushed: 2026-07-01T14:21:57Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-ethereum-node)
- [README](https://github.com/cdklabs/cdk-ethereum-node/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-ethereum-node/issues)
- [Releases](https://github.com/cdklabs/cdk-ethereum-node/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
