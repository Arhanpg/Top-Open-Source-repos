# aws-solutions/cloud-migration-factory-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/cloud-migration-factory-on-aws](https://github.com/aws-solutions/cloud-migration-factory-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/cloud-migration-factory-on-aws/blob/main/README.md)
- README blob SHA: f123632b7527c9f3da85f4559f3a7ece81917de7
- Repository ID: 249775638
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Cloud Migration Factory on AWS solution is designed to coordinate and automate manual processes for large-scale migrations. This solution helps enterprises improve performance and prevents long cutover windows by providing an orchestration platform for migrating workloads to AWS at scale.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:29+00:00

### Short excerpt (up to 100 words)

> Cloud Migration Factory on AWS is an AWS Solutions Implementation that helps migrate a large number of servers with CloudEndure Migration in a simplified and expedited way at scale. The solution automates many of the manual, time-consuming tasks that enterprises commonly face in migrating servers from on-premise to the cloud; for example, checking prerequisites on the source machine, installing/uninstalling software on the source and target machine. Thousands of servers have been migrated to AWS using this solution. When customers deploy the solution, its AWS CloudFormation template automatically provisions and configures the necessary AWS services. The solution also deploys Amazon CloudFront,

### README headings

- Cloud Migration Factory on AWS
- File Structure
- Customization
- Build
- Default encryption:
- Enable public access block:
- Deployment
- Frontend development
- Browser Extensions to Bypass CORS
- For Chrome:
- Important Notes:
- Unit Testing Framework
- Javascript/frontend
- Coverage reporting
- Running the unit tests
- Python/backend
- Run Lambda Unit Tests
- Running a single unit test for development
- Coverage reporting
- SonarQube - Code Quality
- License
- Collection of Anonymous Operational Metrics

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 3,065,074 |
| TypeScript | 2,241,294 |
| Shell | 23,116 |
| PowerShell | 12,969 |
| HTML | 8,950 |
| CSS | 3,954 |
| JavaScript | 3,725 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/frontend/package.json (capture: captured) — dependency clues: @aws-amplify/api, @aws-amplify/auth, @aws-amplify/core, @babel/core, @babel/preset-env, @babel/preset-react, @babel/preset-typescript, @cloudscape-design/code-view, @cloudscape-design/component-toolkit, @cloudscape-design/components, @cloudscape-design/global-styles, @cloudscape-design/jest-preset, @dagrejs/dagre, @eslint/compat, @eslint/eslintrc, @eslint/js, @storybook/addon-designs, @storybook/addon-essentials, @storybook/addon-interactions, @storybook/addon-onboarding
- source/backend/lambda_unit_test/pyproject.toml (capture: captured) — dependency clues: PyJWT, PyYAML, aws-lambda-powertools, boto3, botocore, coverage, cryptography, defusedxml, docker, joserfc, moto, mypy-boto3-dynamodb, pyasn1, pyparsing, python-jose, python-ulid, requests, simplejson, troposphere, urllib3
- source/integrations/integration_unit_tests/pyproject.toml (capture: captured) — dependency clues: boto3, botocore, coverage, cryptography, freezegun, joserfc, moto, paramiko, polling2, urllib3
- source/backend/lambda_functions/lambda_genai_sockets_auth/pyproject.toml (capture: captured) — dependency clues: cryptography, pyasn1, python-jose
- source/backend/lambda_functions/lambda_genai_sockets_handler/pyproject.toml (capture: captured)
- source/backend/lambda_functions/lambda_gfbuild/pyproject.toml (capture: captured) — dependency clues: troposphere

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 89
- Forks at capture: 91
- Last updated: 2026-10-26T15:01:26Z
- Last pushed: 2026-10-26T15:01:13Z
- Topics: automation, aws, mgn, migration

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/cloud-migration-factory-on-aws)
- [README](https://github.com/aws-solutions/cloud-migration-factory-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/cloud-migration-factory-on-aws/issues)
- [Releases](https://github.com/aws-solutions/cloud-migration-factory-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
