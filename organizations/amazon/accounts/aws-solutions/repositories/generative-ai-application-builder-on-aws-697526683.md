# aws-solutions/generative-ai-application-builder-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/generative-ai-application-builder-on-aws](https://github.com/aws-solutions/generative-ai-application-builder-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/blob/main/README.md)
- README blob SHA: 18cb66d82badbe2ed22338a8b8e51bbdc8bcef26
- Repository ID: 697526683
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Generative AI Application Builder on AWS facilitates the development, rapid experimentation, and deployment of generative artificial intelligence (AI) applications without requiring deep experience in AI. The solution includes integrations with Amazon Bedrock and its included LLMs, such as Amazon Titan, and pre-built connectors for 3rd-party LLMs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:28:44+00:00

### Short excerpt (up to 100 words)

> The Generative AI Application Builder on AWS solution (GAAB) provides a web-based management dashboard to deploy customizable Generative AI (Gen AI) use cases. This Deployment dashboard allows customers to deploy, experiment with, and compare different combinations of Large Language Model (LLM) use cases. Once customers have successfully configured and optimized their use case, they can take their deployment into production and integrate it within their applications. The Generative AI Application Builder is published under an Apache 2.0 license and is targeted for novice to experienced users who want to experiment and productionize different Gen AI use cases. The solution uses

### README headings

- On this page
- Architecture Overview
- Deployment Dashboard
- Use Cases
- Text Use Case
- Agent Use Case
- Deployment
- 1. Using `cdk deploy`
- 2. Using a custom build
- Source code
- Project structure
- SageMaker Model Input Documentation
- Creating a custom build
- 1. Clone the repository
- 2. Build the solution for deployment
- 3. Customize the Web App (UI) Projects
- Prerequisites
- Setting up the Local Development Environment
- Customizing the Web App
- Data collection
- Migrating from v1.X to v2.X

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 6,708,223 |
| Python | 2,288,009 |
| JavaScript | 308,527 |
| Shell | 147,869 |
| SCSS | 11,676 |
| Dockerfile | 4,501 |
| CSS | 1,680 |
| HTML | 1,431 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/cdk-solution-helper/package.json (capture: captured)
- source/infrastructure/package.json (capture: captured) — dependency clues: @aws-solutions-constructs/aws-apigateway-lambda, @aws-solutions-constructs/aws-apigatewayv2websocket-sqs, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-constructs-factories, @aws-solutions-constructs/aws-lambda-dynamodb, @aws-solutions-constructs/aws-sqs-lambda, @aws-solutions-constructs/aws-wafwebacl-apigateway, @aws-solutions-constructs/core, @types/jest, @types/mock-fs, @types/node, @types/npmlog, @types/uuid, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdk, cdk-nag, constructs
- source/ui-chat/package.json (capture: captured) — dependency clues: @aws-amplify/core, @aws-amplify/ui-react, @cloudscape-design/chat-components, @cloudscape-design/code-view, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @cloudscape-design/test-utils-core, @reduxjs/toolkit, @tanstack/react-query, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/node, @types/react, @types/react-dom, @types/sinon, @types/uuid, @typescript-eslint/eslint-plugin, @typescript-eslint/parser
- source/ui-deployment/package.json (capture: captured) — dependency clues: @aws-amplify/ui-react, @aws-sdk/util-arn-parser, @cloudscape-design/code-view, @cloudscape-design/components, @cloudscape-design/global-styles, @tanstack/react-query, @tanstack/react-query-devtools, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/jest, @types/lodash, @types/react-test-renderer, @types/uuid, @vitejs/plugin-react, @vitest/coverage-v8, ace-builds, bootstrap, file-loader, identity-obj-proxy
- deployment/ecr/gaab-strands-agent/Dockerfile (capture: captured)
- deployment/ecr/gaab-strands-agent/pyproject.toml (capture: captured) — dependency clues: aws-opentelemetry-distro, bedrock-agentcore, black, boto3, gaab-strands-common, isort, mcp, moto, mypy, pip, pydantic, pytest, pytest-cov, pytest-mock, setuptools, strands-agents, strands-agents-tools, wheel

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 358
- Forks at capture: 140
- Last updated: 2026-11-18T16:55:42Z
- Last pushed: 2026-11-09T17:16:28Z
- Topics: bedrock, chatbot, generative-ai, llms, retrieval-augmented-generation

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/generative-ai-application-builder-on-aws)
- [README](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/issues)
- [Releases](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
