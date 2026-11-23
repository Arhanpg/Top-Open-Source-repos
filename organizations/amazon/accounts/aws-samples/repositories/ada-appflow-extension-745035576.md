# aws-samples/ada-appflow-extension

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/ada-appflow-extension](https://github.com/aws-samples/ada-appflow-extension)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/ada-appflow-extension/blob/main/README.md)
- README blob SHA: d044cfcd66762125d463ab01676515481cf12176
- Repository ID: 745035576
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon AppFlow extension for Automated Data Analytics (ADA) on AWS

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:27:03+00:00

### Short excerpt (up to 100 words)

> The ADA Extension streamlines the integration process, making it easy to connect ADA with a multitude of external SaaS data sources through Amazon AppFlow. This connection allows for the automatic retrieval and integration of data, eliminating the need for users to manually configure data flows within ADA. This extension leverages Amazon EventBridge, AWS Lambda and AWS Step Functions to orchestrate ADA data-product creation for a source AppFlow flow by consuming flow execution events. When an AppFlow flow execution with destination S3 ends succesfully, the event will trigger step function state machine. The state machine will create the respective ADA data-product.

### README headings

- Automated Data Analytics(ADA) Amazon AppFlow Extension
- Solution Architecture
- Pre-requisites
- Deployment
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 53,132 |
| Batchfile | 437 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, cdk-nag, constructs
- lambdas/create_ada_dataproduct/requirements.txt (capture: captured) — dependency clues: boto3, requests
- lambdas/existing_flow_handler_cr/requirements.txt (capture: captured) — dependency clues: boto3, requests
- lambdas/notify_user/requirements.txt (capture: captured) — dependency clues: boto3
- lambdas/trigger_ada_data_update/requirements.txt (capture: captured) — dependency clues: boto3, requests
- lambdas/update_flow_metadata/requirements.txt (capture: captured) — dependency clues: boto3, moto

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 3
- Forks at capture: 0
- Last updated: 2025-02-09T08:53:59Z
- Last pushed: 2024-05-21T07:23:16Z
- Topics: ada, analytics, appflow

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/ada-appflow-extension)
- [README](https://github.com/aws-samples/ada-appflow-extension/blob/main/README.md)
- [Issues](https://github.com/aws-samples/ada-appflow-extension/issues)
- [Releases](https://github.com/aws-samples/ada-appflow-extension/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
