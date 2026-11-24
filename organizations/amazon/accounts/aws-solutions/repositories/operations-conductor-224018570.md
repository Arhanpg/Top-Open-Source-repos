# aws-solutions/operations-conductor

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/operations-conductor](https://github.com/aws-solutions/operations-conductor)
- Default branch: develop
- README: [Open upstream README](https://github.com/aws-solutions/operations-conductor/blob/develop/README.md)
- README blob SHA: 75b92ba3f3f0dbe689b97b30383553781c3557a3
- Repository ID: 224018570
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

[Deprecated] This solution helps customers reduce operational complexity and enables administrators to quickly create manual, event-based or time-based triggers for managing resources.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:37:41+00:00

### Short excerpt (up to 100 words)

> As of 03/03/2023, Operations Conductor on AWS has been deprecated and will not be receiving any additional features or updates. We encourage customers to explore using to create, run, and manage tasks from one central, managed service. Operations Conductor on AWS is a framework that provides an easy-to-use interface for automating and orchestrating operational tasks to manage AWS resources at scale. * Clone the repository, then make the desired code changes. git clone https://github.com/aws-solutions/operations-conductor.git cd operations-conductor export OPS_CO_PATH=`pwd` * Next, run unit tests to make sure added customization passees the tests. cd $OPS_CO_PATH/deployment chmod +x ./run-unit-tests.sh ./run-unit-tests.sh * Configure the

### README headings

- Deprecation Notice
- Operations Conductor on AWS
- Description
- Running unit tests for customization
- Building the customized solution
- Deploying the customized solution
- Collection of operational metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 565,027 |
| Shell | 5,664 |
| JavaScript | 1,269 |
| SCSS | 821 |
| HTML | 721 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/console/package.json (capture: captured) — dependency clues: @aws-amplify/api, @aws-amplify/auth, @aws-amplify/core, @aws-amplify/ui-react, @testing-library/jest-dom, @testing-library/react, @testing-library/user-event, @types/react, @types/react-bootstrap, @types/react-dom, @types/react-router-bootstrap, @types/react-router-dom, bootstrap, eslint-plugin-jest-dom, msw, react, react-bootstrap, react-dom, react-router-bootstrap, react-router-dom
- source/services/package.json (capture: captured) — dependency clues: @types/aws-lambda, @types/aws-serverless-express, @types/cors, @types/express, @types/jest, @types/jwt-decode, @types/node, @types/request-promise, @types/uuid, aws-lambda, aws-sdk, aws-serverless-express, body-parser, cors, express, jest, jwt-decode, moment, request, request-promise

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 14
- Forks at capture: 6
- Last updated: 2023-05-26T17:03:57Z
- Last pushed: 2023-03-08T19:45:55Z
- Topics: aws, aws-solutions, aws-ssm, aws-ssm-document

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/operations-conductor)
- [README](https://github.com/aws-solutions/operations-conductor/blob/develop/README.md)
- [Issues](https://github.com/aws-solutions/operations-conductor/issues)
- [Releases](https://github.com/aws-solutions/operations-conductor/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
