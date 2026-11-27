# aws-samples/amazon-opensearch-service-monitor

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-opensearch-service-monitor](https://github.com/aws-samples/amazon-opensearch-service-monitor)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-opensearch-service-monitor/blob/main/README.md)
- README blob SHA: 1e5cb0d20246865bc0afea4b26a5ad3f21916182
- README bytes captured: 9445
- README truncated at capture limit: False
- Repository ID: 346488279
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository contains step by step demonstration to setup monitoring Stack for Amazon OpenSearch Service domains across all specified regions. This example uses AWS CDK and Python.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:47:07+00:00

### Short excerpt (up to 300 words)

> The following tools are See CONTRIBUTING for more

### README headings

- Amazon OpenSearch Service Monitor
- Table of Contents
- Context <a name="context"></a>
- Architecture
- Prerequisites <a name="prerequisites"></a>
- Create and deploy Amazon OpenSearch Service Monitor tool
- clone the repo
- move to directory
- bootstrap the remaining setup (assumes us-west-2)
- Enter the e-mail address for alert, as that will be used for sending the alert
- Alternatively you can change e-mail address manually in opensearch/opensearch_monitor_stack.py
- activate the virtual environment
- Bootstrap the CDK
- bootstrap the cdk
- Deploy <a name="deploy"></a>
- Note: Complete stack gets setup with pre-defined configuration defined in [opensearch_monitor_stack.py](opensearch/opensearch_monitor_stack.py), please review the settings such as e-mail, instance type, username, password before proceeding to deploy. You can also enable UW and dedicated master (if needed)
- Note: After the stack is deployed you will recieve an e-mail to confirm the subscription, please confirm the same to start getting the alerts.
- Post-Deployment: Setup OpenSearch subscription filters for Cloudwatch logs <a name="cw-subscription-filters"></a>
- Pre-built Monitoring Dashboards <a name="dashboards"></a>
- Pre-built Alerts <a name="alerts"></a>
- Cleanup <a name=cleanup></a>
- Total Cost of Ownership <a name=tco></a>
- Reporting Bugs
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Prerequisites <a name="prerequisites"></a>

> The following tools are

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 73,012 |
| Shell | 25,876 |
| JavaScript | 9,464 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, boto3, constructs
- setup.py (capture: captured)
- CWMetricsToOpenSearch/requirements.txt (capture: captured) — dependency clues: certifi, chardet, idna, pytz, requests, requests_aws4auth, six, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 38
- Forks at capture: 13
- Last updated: 2025-12-31T16:07:19Z
- Last pushed: 2023-10-27T02:00:20Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-opensearch-service-monitor)
- [README](https://github.com/aws-samples/amazon-opensearch-service-monitor/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-opensearch-service-monitor/issues)
- [Releases](https://github.com/aws-samples/amazon-opensearch-service-monitor/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
