# cdklabs/awscdk-service-spec

- Company: Amazon
- GitHub account: [https://github.com/cdklabs](https://github.com/cdklabs)
- Mapping status: official-directory-listed
- Repository: [cdklabs/awscdk-service-spec](https://github.com/cdklabs/awscdk-service-spec)
- Default branch: main
- README: [Open upstream README](https://github.com/cdklabs/awscdk-service-spec/blob/main/README.md)
- README blob SHA: 6ef7e1a62c52d54397a020a8cf19d3bcf9579dd2
- Repository ID: 593127616
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:38+00:00

### Short excerpt (up to 100 words)

> Source of truth for CDK code generation. - `@cdklabs/tskb` - a typed database; contains build tools, query tools, validation mechanism - `@cdklabs/typewriter` - a code generator with support for types - `@aws-cdk/service-spec-importers` - import spec from data sources, transform into the db format - `@aws-cdk/service-spec-types` - loading, saving, querying and diffing a db - `@aws-cdk/aws-service-spec` - the actual db file The data is read iteratively from various sources. Information from later sources adds on to, or replaces, information from older sources. * **Properties are added**: new properties are added into existing resources and type definitions. Existing properties (and attributes) will

### README headings

- AWS CDK Service Specification
- Packages
- Data Sources
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 711,832 |
| JavaScript | 2,353 |
| Shell | 486 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-schemas, @stylistic/eslint-plugin, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @yarnpkg/types, cdklabs-projen-project-types, constructs, eslint, eslint-config-prettier, eslint-plugin-import, eslint-plugin-prettier, node-fetch, nx, prettier, projen, ts-node, typescript
- packages/@aws-cdk/aws-service-spec/package.json (capture: captured) — dependency clues: @aws-cdk/service-spec-importers, @aws-cdk/service-spec-types, @cdklabs/tskb, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, jest, jest-junit, nx, prettier, source-map-support, ts-jest
- packages/@aws-cdk/service-spec-importers/package.json (capture: captured) — dependency clues: @aws-cdk/service-spec-types, @cdklabs/tskb, @types/fs-extra, @types/glob, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, ajv, ajv-cli, canonicalize, chalk, commander, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier
- packages/@aws-cdk/service-spec-types/package.json (capture: captured) — dependency clues: @cdklabs/tskb, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, jest, jest-junit, nx, prettier, ts-jest, typescript
- packages/@cdklabs/tskb/package.json (capture: captured) — dependency clues: @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, jest, jest-junit, nx, prettier, ts-jest, typescript
- packages/@cdklabs/typewriter/package.json (capture: captured) — dependency clues: @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, commit-and-tag-version, constructs, eslint, eslint-config-prettier, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, jest, jest-junit, nx, prettier, ts-jest, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 43
- Forks at capture: 20
- Last updated: 2026-11-12T04:40:41Z
- Last pushed: 2026-11-23T16:21:54Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/cdklabs/awscdk-service-spec)
- [README](https://github.com/cdklabs/awscdk-service-spec/blob/main/README.md)
- [Issues](https://github.com/cdklabs/awscdk-service-spec/issues)
- [Releases](https://github.com/cdklabs/awscdk-service-spec/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
