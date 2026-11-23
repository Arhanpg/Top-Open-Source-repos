# amazon-archives/aws-amplify-serverless-plugin

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-amplify-serverless-plugin](https://github.com/amazon-archives/aws-amplify-serverless-plugin)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-amplify-serverless-plugin/blob/master/README.md)
- README blob SHA: 443a1afc731f89359834afd2700f03556dcec476
- Repository ID: 149808447
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Plugin for the Serverless Framework to output AWS Amplify configuration files.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:29:13+00:00

### Short excerpt (up to 100 words)

> This is a plugin for the Serverless Framework that generates appropriate configuration files for using AWS Amplify with the Serverless Framework. Install the plugin via Yarn (recommended) yarn add aws-amplify-serverless-plugin or via NPM npm install --save aws-amplify-serverless-plugin Edit your `serverless.yml` file to include something like the following: plugins: - aws-amplify-serverless-plugin custom: amplify: - filename: examples/awsconfiguration.json type: native appClient: AndroidUserPoolClient s3bucket: UserFiles - filename: examples/schema.json type: schema.json - filename: examples/aws-exports.js type: javascript appClient: WebUserPoolClient s3bucket: disabled Each entry in the `amplify` section must consist of two parts, with two optional parts: * `filename` is where you want the file to be

### README headings

- AWS Amplify Plugin for Serverless Framework
- Installation
- Configuration
- Another Example
- Support for GraphQL Code Generation (Android)
- Support for GraphQL Code Generation (iOS)
- Supported Resources
- Questions, Issues, Feature Requests

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 28,050 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: amplify-graphql-docs-generator, aws-appsync-codegen, chalk, json-stable-stringify-pretty, serverless
- example/package.json (capture: captured) — dependency clues: aws-amplify-serverless-plugin, chalk, serverless, serverless-appsync-plugin

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 123
- Forks at capture: 30
- Last updated: 2025-10-26T19:19:39Z
- Last pushed: 2020-03-23T23:32:22Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-amplify-serverless-plugin)
- [README](https://github.com/amazon-archives/aws-amplify-serverless-plugin/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-amplify-serverless-plugin/issues)
- [Releases](https://github.com/amazon-archives/aws-amplify-serverless-plugin/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
