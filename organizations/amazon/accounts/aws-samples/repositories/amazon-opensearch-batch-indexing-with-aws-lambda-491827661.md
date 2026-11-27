# aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda](https://github.com/aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda/blob/main/README.md)
- README blob SHA: 255c8ff9c56868ffcf12a711ffbc0b67159060da
- README bytes captured: 6941
- README truncated at capture limit: False
- Repository ID: 491827661
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T18:42:19+00:00

### Short excerpt (up to 300 words)

> GET comments_anycompany/_search { "size": 1. **Index Documents**: Indexes

### README headings

- Amazon OpenSearch batch indexing with AWS Lambda
- Architecture Diagram
- Sample Scenario
- Scenario Deployment
- Cloudformation Template
- AWS SAM Application
- Configure your credentials
- Create virtual environment with the needed packages
- Activate the environment
- Package and deploy your application to AWS
- Sample Data
- Running the scenario
- Example of query: How many comments of each Sentiment do we have?
- Example of query: What is the Sentiment of the comments of ratings with less than 3 stars rating?
- Cleanup

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Example of query: What is the Sentiment of the comments of ratings with less than 3 stars rating?

> GET comments_anycompany/_search { "size":

### Architecture and design: Architecture Diagram

> 1. **Index Documents**: Indexes

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 8,700 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- calculate_metrics/requirements.txt (capture: captured) — dependency clues: pandas
- index_documents/requirements.txt (capture: captured) — dependency clues: numpy, opensearch-py, pandas, requests
- update_documents/requirements.txt (capture: captured) — dependency clues: opensearch-py, pandas, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 14
- Forks at capture: 2
- Last updated: 2026-03-06T22:14:23Z
- Last pushed: 2022-10-03T07:07:37Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda)
- [README](https://github.com/aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda/issues)
- [Releases](https://github.com/aws-samples/amazon-opensearch-batch-indexing-with-aws-lambda/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
