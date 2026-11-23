# aws-observability/aws-otel-test-framework

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-test-framework](https://github.com/aws-observability/aws-otel-test-framework)
- Default branch: terraform
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-test-framework/blob/terraform/README.md)
- README blob SHA: 49bbe8d0c98119f449485615bebab09709e31970
- Repository ID: 295885704
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Distro for OpenTelemetry Test Framework

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:14:24+00:00

### Short excerpt (up to 100 words)

> Before adding a new component into ADOT Collector, we require contributors to add related end-to-end test cases, this project is a testing framework which helps contributors to easily add testing into AWS Otel Collector. * Contributors won't need to run the test locally to provide the testing result, instead, just define it. The test case will be automatically picked by the github workflow in AWS Otel Collector repo to run integration test and soaking test on different platforms. We will notify contributors if a certain test case is failed. * Contributors won't need to build the validation logic for their

### README headings

- ADOT Testing Framework
- 1. Two PRs to contribute your component to [ADOT Collector](https://github.com/aws-observability/aws-otel-collector)
- 1.1 Create a PR to Define test case in testing framework Repo
- 1.1.1 create test case folder
- 1.1.2 place `otconfig.tpl` under test case folder
- 1.1.3 place `parameters.tfvars` under test case folder
- 1.2 Create a PR to Link test case to ADOT Collector Repo
- 1.2.1 case_name
- 1.2.2 platforms
- 2. Run testing framework
- 3. Contributing
- 4. Security issue notifications
- 5. License
- Support

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 298,531 |
| HCL | 243,230 |
| Smarty | 98,526 |
| Go | 63,818 |
| Mustache | 55,438 |
| TypeScript | 34,267 |
| Shell | 15,978 |
| Dockerfile | 4,232 |
| Makefile | 3,029 |
| Python | 1,780 |
| JavaScript | 187 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build.gradle (capture: captured)
- Makefile (capture: captured)
- cdk_infra/Makefile (capture: captured)
- cdk_infra/package.json (capture: captured) — dependency clues: @aws-cdk/aws-ec2, @aws-cdk/aws-eks, @aws-cdk/aws-iam, @aws-cdk/core, @aws-cdk/lambda-layer-kubectl, @aws-cdk/lambda-layer-kubectl-v29, @aws-cdk/lambda-layer-kubectl-v30, @aws-cdk/lambda-layer-kubectl-v31, @aws-cdk/lambda-layer-kubectl-v32, @aws-cdk/lambda-layer-kubectl-v33, @aws-cdk/lambda-layer-kubectl-v34, @types/jest, @types/js-yaml, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, ajv, ajv-errors, aws-cdk, aws-cdk-lib
- load-generator/build.gradle (capture: captured)
- terraform/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 35
- Forks at capture: 66
- Last updated: 2026-11-03T12:08:29Z
- Last pushed: 2026-11-03T12:08:33Z
- Topics: observability, open-source, open-telemetry, testing-tools

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-test-framework)
- [README](https://github.com/aws-observability/aws-otel-test-framework/blob/terraform/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-test-framework/issues)
- [Releases](https://github.com/aws-observability/aws-otel-test-framework/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
