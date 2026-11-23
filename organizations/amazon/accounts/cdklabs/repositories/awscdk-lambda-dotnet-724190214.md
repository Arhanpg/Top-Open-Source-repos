# cdklabs/awscdk-lambda-dotnet

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/awscdk-lambda-dotnet](https://github.com/cdklabs/awscdk-lambda-dotnet)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/awscdk-lambda-dotnet/blob/main/README.md)
- README blob SHA: acdc4677b5d42032fe2eca45c4f8302873ad6777
- Repository ID: 724190214
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:35+00:00

### Short excerpt (up to 100 words)

> This library provides constructs for .NET Lambda functions. To use this module you will either need to have `.NET SDK` installed (`.NET 6.0` or later) with the AWS Lambda Tools for .NET or `Docker` installed. Define a `DotNetFunction`: new dotnet.DotNetFunction(this, 'MyFunction', { projectDir: 'src/MyFunction' }); All other properties of `lambda.Function` are supported, see also the AWS Lambda construct library. With this construct it is possible to use a custom runtime by setting the runtime to `PROVIDED_AL2`. This allows you to run unsupported .NET runtime versions like .NET 7.0 or Native AOT. Setting the runtime to `PROVIDED_AL2` will instruct CDK and

### README headings

- AWS Lambda .NET Library
- .NET Function
- Custom Runtime and Native AOT
- Community Extensions

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 25,731 |
| C# | 3,140 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, jest, jest-junit, jsii, jsii-diff, jsii-docgen
- test/lambda-handler-aot/LambdaHandler.csproj (capture: captured)
- test/lambda-handler-docker/LambdaHandler.csproj (capture: captured)
- test/lambda-handler-dotnet6/LambdaHandler.csproj (capture: captured)
- test/lambda-handler-tools/LambdaHandler.csproj (capture: captured)
- test/lambda-handler/LambdaHandler.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 7
- Forks at capture: 4
- Last updated: 2026-11-09T23:20:22Z
- Last pushed: 2026-11-23T00:38:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/awscdk-lambda-dotnet)
- [README](https://github.com/cdklabs/awscdk-lambda-dotnet/blob/main/README.md)
- [Issues](https://github.com/cdklabs/awscdk-lambda-dotnet/issues)
- [Releases](https://github.com/cdklabs/awscdk-lambda-dotnet/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
