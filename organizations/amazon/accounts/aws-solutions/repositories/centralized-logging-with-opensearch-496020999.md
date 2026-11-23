# aws-solutions/centralized-logging-with-opensearch

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/centralized-logging-with-opensearch](https://github.com/aws-solutions/centralized-logging-with-opensearch)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/centralized-logging-with-opensearch/blob/main/README.md)
- README blob SHA: 0d26e92b838e4667e5c83e5ab763fb1ce1592983
- Repository ID: 496020999
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Build your own log analytics platform on OpenSearch in 20 minutes

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:04:06+00:00

### Short excerpt (up to 100 words)

> **Important: This AWS Solution will retire in December 2026. We encourage customers to explore using [Amazon CloudWatch's new unified data management and analytics capabilities](https://aws.amazon.com/blogs/aws/amazon-cloudwatch-introduces-unified-data-management-and-analytics-for-operations-security-and-compliance/). Learn more about AWS CloudWatch unified data and telemetry and give it a try in the AWS CloudWatch console.** **For customers in the Amazon Web Services China (Ningxia) Region: Support for Amazon CloudFront in the Amazon Web Services China (Ningxia) Region will end on May 31, 2027, with no new customers accepted after September 30, 2026 (see the End of support notice for details). Because Centralized Logging with OpenSearch depends on Amazon CloudFront, it will follow

### README headings

- Centralized Logging with OpenSearch
- Table of content
- Solution Overview
- Architecture
- Deployment
- Customization
- Data Collection

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 6,255,054 |
| TypeScript | 3,831,345 |
| SCSS | 66,635 |
| Shell | 62,608 |
| Velocity Template Language | 44,225 |
| JavaScript | 6,061 |
| Dockerfile | 2,216 |
| HTML | 1,624 |
| Lua | 359 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/cdk-solution-helper/package.json (capture: captured)
- source/constructs/package.json (capture: captured) — dependency clues: @aws-cdk/aws-appsync-alpha, @aws-cdk/aws-glue-alpha, @aws-solutions-constructs/aws-cloudfront-oai-s3, @aws-solutions-constructs/aws-cloudfront-s3, @types/jest, @types/node, @types/prettier, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cdk-nag, constructs, eslint, eslint-config-prettier, eslint-import-resolver-node, eslint-import-resolver-typescript, eslint-plugin-import, eslint-plugin-prettier, jest
- source/portal/package.json (capture: captured) — dependency clues: @apollo/client, @aws-amplify/auth, @aws-amplify/core, @aws-amplify/ui-react, @material-ui/core, @material-ui/icons, @material-ui/lab, @reduxjs/toolkit, @testing-library/jest-dom, @testing-library/react, @testing-library/react-hooks, @types/jest, @types/lodash.clonedeep, @types/node, @types/react, @types/react-copy-to-clipboard, @types/react-dom, @types/react-router-dom, @types/react-syntax-highlighter, @types/redux-mock-store
- deployment/ecr/clo-logging-syslog/Dockerfile (capture: captured)
- deployment/ecr/clo-s3-list-objects/Dockerfile (capture: captured)
- deployment/ecr/clo-s3-list-objects/pyproject.toml (capture: captured) — dependency clues: boto3, cryptography, moto, pygments, pytest, pytest-cov, pytest-mock, requests, requests-aws4auth, requests-mock, setuptools, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 132
- Forks at capture: 44
- Last updated: 2026-11-10T17:08:41Z
- Last pushed: 2026-11-10T17:14:00Z
- Topics: centralized-logging, log-analysis, log-analytics, opensearch

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/centralized-logging-with-opensearch)
- [README](https://github.com/aws-solutions/centralized-logging-with-opensearch/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/centralized-logging-with-opensearch/issues)
- [Releases](https://github.com/aws-solutions/centralized-logging-with-opensearch/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
