# awslabs/aws-jwt-verify

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-jwt-verify](https://github.com/awslabs/aws-jwt-verify)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/aws-jwt-verify/blob/main/README.md)
- README blob SHA: 02f42d833ee9aa900dab40f0b64f3a393baa184a
- README bytes captured: 54689
- README truncated at capture limit: False
- Repository ID: 407226090
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

JS library for verifying JWTs signed by Amazon Cognito, and any OIDC-compatible IDP that signs JWTs with RS256, RS384, RS512, ES256, ES384, ES512, Ed25519 and Ed448

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:26:46+00:00

### Short excerpt (up to 300 words)

> npm install aws-jwt-verify This See CONTRIBUTING for more

### README headings

- AWS JWT Verify
- Installation
- Basic usage
- Amazon Cognito
- Other IDPs
- Non-standard IDPs
- Application Load Balancer
- Philosophy of this library
- Intended Usage
- Usage in the Web browser
- Table of Contents
- Verifying JWTs from Amazon Cognito
- `CognitoJwtVerifier` `verify` parameters
- Checking scope
- Custom JWT and JWK checks
- Trusting multiple User Pools
- Using the generic JWT verifier for Cognito JWTs
- Verifying JWTs from a Cognito identity pool
- Verifying JWTs from any OIDC-compatible IDP
- `JwtVerifier` `verify` parameters
- Verifying user claims JWTs from Application Load Balancers
- `AlbJwtVerifier` `verify` parameters
- Trusting multiple Application Load Balancers
- How the algorithm (`alg`) is selected to verify the JWT signature with
- Advanced: enforcing the algorithm (`alg`)
- Peeking inside unverified JWTs
- Verification errors
- Peek inside invalid JWTs
- The JWKS cache
- Loading the JWKS from file

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> npm install aws-jwt-verify This

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 330,490 |
| JavaScript | 8,373 |
| Shell | 2,177 |
| HTML | 1,250 |
| CSS | 474 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @eslint/compat, @eslint/eslintrc, @eslint/js, @tsconfig/node16, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-plugin-security, globals, jest, jest-junit, nock, prettier, ts-jest, ts-node, typescript
- tests/cognito/package.json (capture: captured) — dependency clues: @aws-sdk/client-cognito-identity-provider, @types/jest, @types/jsdom, @types/node, aws-cdk, aws-cdk-lib, cdk-nag, constructs, dotenv, jest, jsdom, source-map-support, ts-jest, ts-node, typescript
- tests/import-tests/package.json (capture: captured)
- tests/installation-and-basic-usage/package.json (capture: captured) — dependency clues: @types/node, typescript
- tests/vite-app/package.json (capture: captured) — dependency clues: @cypress/webpack-preprocessor, @rollup/plugin-node-resolve, @types/node, cypress, ts-loader, ts-node, typescript, vite
- tests/vite-app/util/package.json (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 750
- Forks at capture: 55
- Last updated: 2026-11-19T22:20:20Z
- Last pushed: 2026-11-17T20:38:44Z
- Topics: amazon-cognito, amplify, jwt, nodejs, typescript

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-jwt-verify)
- [README](https://github.com/awslabs/aws-jwt-verify/blob/main/README.md)
- [Issues](https://github.com/awslabs/aws-jwt-verify/issues)
- [Releases](https://github.com/awslabs/aws-jwt-verify/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
