# cdklabs/cdk-dynamo-table-viewer

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/cdk-dynamo-table-viewer](https://github.com/cdklabs/cdk-dynamo-table-viewer)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/cdk-dynamo-table-viewer/blob/main/README.md)
- README blob SHA: 2e7dda2cd015a79e8f0ac888415dab5b3f04daf3
- Repository ID: 153631465
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A CDK construct which exposes an endpoint with the contents of a DynamoDB table

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:45:40+00:00

### Short excerpt (up to 100 words)

> An AWS CDK construct which exposes a public HTTP endpoint which displays an HTML page with the contents of a DynamoDB table in your stack. __SECURITY NOTE__: this construct was built for demonstration purposes and using it in production is probably a really bad idea. It exposes the entire contents of a DynamoDB table in your account to the general public. The library is published under the following names: Install via npm: $ npm i cdk-dynamo-table-viewer Add to your CDK stack: declare const cookiesTable: dynamodb.Table; const viewer = new TableViewer(this, 'CookiesViewer', { table: cookiesTable, title: 'Cookie Sales', // optional sortBy:

### README headings

- cdk-dynamo-table-viewer
- Usage (TypeScript/JavaScript)
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 6,531 |
| JavaScript | 5,843 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @aws-sdk/client-dynamodb, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 125
- Forks at capture: 28
- Last updated: 2026-11-09T23:22:50Z
- Last pushed: 2026-11-23T00:38:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/cdk-dynamo-table-viewer)
- [README](https://github.com/cdklabs/cdk-dynamo-table-viewer/blob/main/README.md)
- [Issues](https://github.com/cdklabs/cdk-dynamo-table-viewer/issues)
- [Releases](https://github.com/cdklabs/cdk-dynamo-table-viewer/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
