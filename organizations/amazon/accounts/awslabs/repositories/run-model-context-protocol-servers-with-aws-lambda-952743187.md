# awslabs/run-model-context-protocol-servers-with-aws-lambda

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/run-model-context-protocol-servers-with-aws-lambda](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda/blob/main/README.md)
- README blob SHA: 4460f3cc2265206921e4f8a87b562f54da0e2b44
- README bytes captured: 28364
- README truncated at capture limit: False
- Repository ID: 952743187
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Run existing Model Context Protocol (MCP) stdio-based servers in AWS Lambda functions

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:43:43+00:00

### Short excerpt (up to 300 words)

> See the development guide See CONTRIBUTING for more

### README headings

- Run Model Context Protocol (MCP) servers with AWS Lambda
- Determine your server parameters
- Passing credentials and other secrets to the MCP server
- Retrieve API key from Secrets Manager
- Get AWS credentials from Lambda execution role to pass to subprocess
- Get AWS credentials from Lambda execution role to pass to subprocess
- Write credentials to disk as default profile
- Use API Gateway
- Create OAuth client provider here
- Use Bedrock AgentCore Gateway
- For example:
- Create OAuth client provider here
- Use a Lambda function URL
- Use the Lambda Invoke API
- Related projects
- Considerations
- Deploy and run the examples
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Deploy and run the examples

> See the development guide

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 150,021 |
| TypeScript | 137,381 |
| Shell | 5,152 |
| JavaScript | 1,698 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pipeline/package.json (capture: captured) — dependency clues: @types/node, aws-cdk, aws-cdk-lib, constructs, typescript
- e2e_tests/python/requirements.txt (capture: captured) — dependency clues: aiohttp, anyio, boto3, certifi, mcp, strands-agents, strands-agents-evals, uvicorn
- e2e_tests/typescript/package.json (capture: captured) — dependency clues: @aws-sdk/client-bedrock-runtime, @aws-sdk/client-cloudformation, @aws-sdk/client-s3, @aws-sdk/client-secrets-manager, @aws-sdk/client-ssm, @cfworker/json-schema, @eslint/js, @modelcontextprotocol/sdk, @strands-agents/sdk, @types/aws-lambda, @types/json-schema, @types/node, eslint, typescript, typescript-eslint, winston
- src/python/pyproject.toml (capture: captured) — dependency clues: aiobotocore, anyio, aws-lambda-powertools, mcp, mcp-proxy-for-aws, types-aiobotocore
- src/typescript/package.json (capture: captured) — dependency clues: @aws-crypto/sha256-js, @aws-sdk/client-lambda, @aws-sdk/credential-provider-node, @aws-sdk/protocol-http, @aws-sdk/types, @cfworker/json-schema, @eslint/js, @modelcontextprotocol/sdk, @smithy/signature-v4, @smithy/util-stream, @tsconfig/recommended, @types/aws-lambda, @types/jest, @types/node, aws-sdk-client-mock, aws-sdk-client-mock-jest, eslint, eslint-plugin-check-file, jest, ts-jest
- examples/chatbots/python/requirements.txt (capture: captured) — dependency clues: anyio, boto3, certifi, mcp, strands-agents, uvicorn

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 385
- Forks at capture: 47
- Last updated: 2026-11-18T15:26:59Z
- Last pushed: 2026-11-19T23:50:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda)
- [README](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda/blob/main/README.md)
- [Issues](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda/issues)
- [Releases](https://github.com/awslabs/run-model-context-protocol-servers-with-aws-lambda/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
