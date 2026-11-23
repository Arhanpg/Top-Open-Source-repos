# awslabs/amazon-athena-cross-account-catalog

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/amazon-athena-cross-account-catalog](https://github.com/awslabs/amazon-athena-cross-account-catalog)
- Default branch: master
- README: [Open upstream README](https://github.com/awslabs/amazon-athena-cross-account-catalog/blob/master/README.md)
- README blob SHA: 7026fef305c29d6632e32434b8bc4c5ebbae69ef
- Repository ID: 224262047
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

🌉 Reference implementation for granting cross-account AWS Glue Data Catalog access from Amazon Athena

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:27:11+00:00

### Short excerpt (up to 100 words)

> 🌉 ~~Reference implementation for granting cross-account AWS Glue Data Catalog access from Amazon Athena~~ 💁 **NOTICE** Amazon Athena now officialy supports connecting to an AWS Glue Data Catalog in another account. As such, this repository will be archived in the near future. This package uses the Athena External Hive Metastore functionality to allow cross-account data access. It is implemented as an AWS Lambda function that reads the metadata from the Glue Data Catalog and converts it into the format necessary for Athena. Users must have access to the S3 resources that the tables point to and be granted access to

### README headings

- Amazon Athena Cross Account Data Catalog
- Overview
- Deployment
- 1. Zipped Lambda Function
- 2. Dockerized Lambda Function
- Create IAM Role
- Build deployment package
- Zip File
- Docker Image
- Create function
- Register Data Source with Athena
- Grant Cross-account Access to Lambda
- Test it...
- Update it
- Limitations
- Additional Considerations

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 90,367 |
| Makefile | 460 |
| Dockerfile | 194 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Makefile (capture: captured)
- requirements.txt (capture: captured) — dependency clues: six, thrift

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 30
- Forks at capture: 19
- Last updated: 2025-04-08T01:45:30Z
- Last pushed: 2022-07-25T20:35:51Z
- Topics: amazon-athena, aws-glue

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/amazon-athena-cross-account-catalog)
- [README](https://github.com/awslabs/amazon-athena-cross-account-catalog/blob/master/README.md)
- [Issues](https://github.com/awslabs/amazon-athena-cross-account-catalog/issues)
- [Releases](https://github.com/awslabs/amazon-athena-cross-account-catalog/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
