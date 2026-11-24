# cdklabs/deploy-time-build

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/deploy-time-build](https://github.com/cdklabs/deploy-time-build)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/deploy-time-build/blob/main/README.md)
- README blob SHA: 52948eb4ac8f8da45e1990338e2bdb335af909b5
- README bytes captured: 10341
- README truncated at capture limit: False
- Repository ID: 1101389191
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Run build on CDK deployment time

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T07:38:27+00:00

### Short excerpt (up to 300 words)

> I talked about why Install from npm: npm

### README headings

- Deploy-time Build
- Usage
- Build Node.js apps
- Allowing access from the build environment to other AWS resources
- Motivation - why do we need the `NodejsBuild` construct?
- Caching
- Compute Type
- Considerations
- Build a container image
- Build SOCI index for a container image
- Motivation - why do we need the `SociIndexBuild` construct?
- Development
- run test locally

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Motivation - why do we need the `NodejsBuild` construct?

> I talked about why

### Getting started and usage: Usage

> Install from npm: npm

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 86,810 |
| JavaScript | 37,392 |
| CSS | 1,950 |
| Dockerfile | 1,715 |
| Shell | 1,002 |
| HTML | 590 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/integ-runner, @aws-cdk/integ-tests-alpha, @stylistic/eslint-plugin, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdklabs-projen-project-types, commit-and-tag-version, constructs, eslint, eslint-import-resolver-typescript, eslint-plugin-import, jest, jest-junit, jsii, jsii-diff, jsii-docgen
- example/example-app/package.json (capture: captured) — dependency clues: @types/react, @types/react-dom, @vitejs/plugin-react, react, react-dom, typescript, vite
- example/example-image/Dockerfile (capture: captured)
- lambda/trigger-codebuild/package.json (capture: captured) — dependency clues: @aws-sdk/client-codebuild, @types/aws-lambda, @types/node, esbuild
- test/integ.container-image-build.ts.snapshot/asset.27d689e5b89504940c061916e0e9be8cc0a0f37417918f37e94199237655d0bb/Dockerfile (capture: captured)
- test/integ.nodejs-build.ts.snapshot/asset.657a7f55c12b1b65fa1771aa6a43166cc7568399770ab8ff597aa97e52656994/package.json (capture: captured) — dependency clues: @types/react, @types/react-dom, @vitejs/plugin-react, react, react-dom, typescript, vite

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 1
- Last updated: 2026-11-04T08:14:38Z
- Last pushed: 2026-11-20T08:40:05Z
- Topics: aws, cdk

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/deploy-time-build)
- [README](https://github.com/cdklabs/deploy-time-build/blob/main/README.md)
- [Issues](https://github.com/cdklabs/deploy-time-build/issues)
- [Releases](https://github.com/cdklabs/deploy-time-build/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
