# aws-solutions/dynamic-object-and-rule-extensions-for-anfw

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/dynamic-object-and-rule-extensions-for-anfw](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/blob/main/README.md)
- README blob SHA: e2ba02b3a5648ce90ec9bbdbf1133a95c60c4f18
- Repository ID: 457540158
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Solution to specify elastic and dynamic cloud resources as objects that can be easily referenced within AWS Network Firewall rules

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:28:33+00:00

### Short excerpt (up to 100 words)

> **You can find other AWS Solutions in the AWS Solutions Library.** Dynamic Object and Rule Extensions for AWS Network Firewall enables customers to define objects that reference cloud native elastic resources, and to create AWS Network Firewall rules based on these custom objects. The solution continually synchronises the customers AWS Network Firewall (ANFW) instance with the state of the referenced elastic resources, to keep it up to date in near real-time. The solution provides a RESTful interface with CRUD APIs for managing rule bundles, rules and objects. _Request Orchestration_ 1. The API gateway provides the primary interface for the customer

### README headings

- Important: This AWS Solution is no longer available.
- dynamic-object-and-rule-extensions-for-anfw
- Architecture Overview
- File Structure
- Prerequisite
- Configuration
- Running Unit Tests
- API schema and examples
- API schema document
- API usage example
- Building and Deploy the solution
- Uninstall the solution
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 887,395 |
| JavaScript | 26,680 |
| Open Policy Agent | 19,400 |
| Dockerfile | 1,239 |
| Shell | 919 |
| Makefile | 817 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-servicecatalogappregistry-alpha, @aws-cdk/aws-synthetics-alpha, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk-lib, constructs, eslint, eslint-config-prettier, eslint-plugin-header, eslint-plugin-prettier, jest, prettier, source-map-support, ts-jest, ts-node, typescript, uuid
- source/ecs_sidecar/Dockerfile (capture: captured)
- source/integration-tests/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-sdk/client-auto-scaling, @aws-sdk/client-cloudformation, @aws-sdk/client-dynamodb, @aws-sdk/client-lambda, @aws-sdk/client-network-firewall, @aws-sdk/client-sts, @aws-sdk/credential-providers, @aws-sdk/util-dynamodb, @types/jest, @types/node, @types/uuid, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, aws-sdk, clean-webpack-plugin, constructs, eslint
- source/opa/Dockerfile (capture: captured)
- source/opa/Makefile (capture: captured)
- source/lambda/app-registry-cr/package.json (capture: captured) — dependency clues: @aws-sdk/client-service-catalog-appregistry, @types/aws-lambda, aws-crt, aws-lambda, babel-loader, ts-loader, ts-mockito, typescript, webpack, webpack-cli, webpack-node-externals

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 18
- Forks at capture: 1
- Last updated: 2026-01-05T20:42:53Z
- Last pushed: 2025-02-19T22:37:30Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw)
- [README](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/issues)
- [Releases](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
