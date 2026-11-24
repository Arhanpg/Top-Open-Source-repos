# aws/amazon-neptune-for-graphql

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-neptune-for-graphql](https://github.com/aws/amazon-neptune-for-graphql)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-neptune-for-graphql/blob/main/README.md)
- README blob SHA: 137742e6a6e30e78272ddf150e084ffd89f1bf9a
- Repository ID: 687774198
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon Neptune utility for GraphQL™ schemas and resolvers

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:35:02+00:00

### Short excerpt (up to 100 words)

> The Amazon Neptune utility for GraphQL&trade; is a Node.js command-line utility to help with the creation and maintenance of a GraphQL API for the Amazon Neptune Database or Neptune Analytics graph. It is a no-code solution for a GraphQL resolver when GraphQL queries have a variable number of input parameters and return a variable number of nested fields. If you **start from a Neptune database with data**, the utility discovers the graph database schema including nodes, edges, properties and edges cardinality. This database schema is then used to generate the GraphQL schema with the directives required to map the GraphQL

### README headings

- **Amazon Neptune utility for GraphQL&trade; schemas and resolvers - v2.2.0**
- Install and Setup
- Node.js is required in any scenario
- Install the Amazon Neptune utility for GraphQL
- Reach to a Neptune database endpoint
- Next Step
- Starting from a Neptune database with data
- References:
- Starting from a GraphQL schema and an empty Neptune database
- References:
- Starting from a GraphQL schema with directives
- Customize the GraphQL schema with directives
- Please no mutations in my schema
- @alias
- @relationship
- @graphQuery, @cypher
- @id
- Reserved types, queries and mutations names
- Re-apply your changes with --input-schema-changes-file
- AWS resources for the GraphQL API
- Let the utility create the resources
- I prefer a CDK file
- Let me setup the resources manually or with my favorite DevOps toolchain
- Generate Apollo Server Artifacts
- Using Custom Scalars with Apollo Server
- AWS AppSync Scalars
- Known limitations
- Roadmap
- License
- Contributing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 460,077 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-sdk/client-appsync, @aws-sdk/client-iam, @aws-sdk/client-lambda, @aws-sdk/client-neptune, @aws-sdk/client-neptune-graph, @aws-sdk/client-neptunedata, @aws-sdk/credential-providers, @eslint/js, @jest/test-sequencer, archiver, aws4-axios, axios, eslint, globals, graphql, graphql-tag, jest, ora, pino, pino-pretty
- test/package.json (capture: captured) — dependency clues: @aws-sdk/client-appsync, adm-zip, axios, graphql-tag
- templates/ApolloServer/package.json (capture: captured) — dependency clues: @apollo/server, @apollo/subgraph, @aws-sdk/credential-providers, aws4-axios, axios, dotenv, graphql, retry-axios
- templates/Lambda4AppSyncGraphSDK/package.json (capture: captured) — dependency clues: @aws-sdk/client-neptune-graph, graphql
- templates/Lambda4AppSyncHTTP/package.json (capture: captured) — dependency clues: aws4-axios, axios, graphql, retry-axios
- templates/Lambda4AppSyncSDK/package.json (capture: captured) — dependency clues: @aws-sdk/client-neptunedata, graphql

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 29
- Forks at capture: 10
- Last updated: 2026-11-10T01:14:57Z
- Last pushed: 2026-09-21T21:14:41Z
- Topics: aws, aws-neptune, graphql

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-neptune-for-graphql)
- [README](https://github.com/aws/amazon-neptune-for-graphql/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-neptune-for-graphql/issues)
- [Releases](https://github.com/aws/amazon-neptune-for-graphql/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
