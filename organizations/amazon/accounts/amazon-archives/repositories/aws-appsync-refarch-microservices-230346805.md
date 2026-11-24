# amazon-archives/aws-appsync-refarch-microservices

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-appsync-refarch-microservices](https://github.com/amazon-archives/aws-appsync-refarch-microservices)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-appsync-refarch-microservices/blob/master/README.md)
- README blob SHA: fe46ce5861d3c0cc783a13f9b50f248bd1f27c85
- Repository ID: 230346805
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS AppSync Microservices Access Layer Reference Architecture

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:57+00:00

### Short excerpt (up to 100 words)

> The AWS AppSync Serverless GraphQL microservice-access-layer reference architecture showcases AWS AppSync as a single interface to access and combine data from multiple microservices running in different environments : - **UserService:** RESTful API built using Amazon API Gateway and AWS Lambda - **OrderService:** GraphQL API on different AWS AppSync endpoint - **PaymentService:** Containerized service running inside an isolated VPC with no internet access The sample app is based on a very simple webstore where users can login, and interact with different services. - One-Click Deploy with the Amplify Console - Setup local environment - Clean Up 1. **Prerequisites** - AWS Account

### README headings

- AWS AppSync Microservices-Access-Layer Reference Architecture
- Quicklinks
- Getting Started
- One-Click Deploy with the Amplify Console
- Setup local environment
- Clean up

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 24,362 |
| Python | 3,111 |
| Shell | 1,902 |
| HTML | 1,708 |
| CSS | 672 |
| Dockerfile | 285 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: apollo-link, apollo-link-http, aws-amplify, aws-amplify-react, aws-appsync, glamor, graphql-tag, react, react-dom, react-router-dom, react-scripts
- paymentapp/Dockerfile (capture: captured)
- paymentapp/requirements.txt (capture: captured) — dependency clues: boto3, flask

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 53
- Forks at capture: 65
- Last updated: 2026-11-07T02:47:10Z
- Last pushed: 2020-01-07T02:40:27Z
- Topics: amplify, aws-appsync, fargate, graphql, microservices

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-appsync-refarch-microservices)
- [README](https://github.com/amazon-archives/aws-appsync-refarch-microservices/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-appsync-refarch-microservices/issues)
- [Releases](https://github.com/amazon-archives/aws-appsync-refarch-microservices/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
