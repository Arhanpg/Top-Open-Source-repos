# aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit](https://github.com/aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit/blob/main/README.md)
- README blob SHA: 872a664514f7b3cb7550ad07ac7575769b7f8ace
- README bytes captured: 13482
- README truncated at capture limit: False
- Repository ID: 748821740
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T06:25:54+00:00

### Short excerpt (up to 300 words)

> Using Command Line : The Architecture of this AWS S3 Bucket to See CONTRIBUTING for more

### README headings

- Amazon Managed Service for Apache Flink - PyFlink Starter Kit
- Architecture
- Pre-requisites
- 
- AWS Account Requirements
- 
- Applicaiton Repository Information
- Applicaiton Setup Instructions
- Building Apache Flink Uber Jar
- setting up python environment - assuming conda is already installed
- setting up pyflink application dependencies
- Deployment Instructions
- Infrastructure Deployment Instructions
- KDA PyFlink Starter Application Execution
- Starting the Application - AWS Console
- Navigate to Managed Apache Flink Service &rarr; Apache Flink applications &rarr; select "kda-pyflink-starterkit" &rarr; click on Run button (select Run without snapshot) &rarr; Run
- Select "kda-pyflink-starterkit"
- Click on Run button
- Application Start in-progress
- Application Started
- Application Dashboard - view Flink dashboard (Click on Open Apache Flink dashboard button)
- Flink dashboard
- Flink dashboard - process view
- KDA PyFlink Starter Application Data Generator
- Using Command Line : Navigate to root folder "kda-pyflink-starterkit" &rarr; lambda_code &rarr;kda-pyflink-starter-sql-function &rarr; run the command
- Flink dashboard - will show the Byte received and Record Received/Sent
- Verify data recevied in Aurora DB using Lambda
- Navigate to AWS Lambda &rarr; Functions &rarr; select "kda-pyflink-starter-sql-function" &rarr; click on Test button (configure an event) &rarr; Execution result &rarr;
- Appendix
- KDA Application exeception

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: setting up python environment - assuming conda is already installed

> Using Command Line :

### Architecture and design: Architecture

> The Architecture of this

### Technology and requirements: AWS Account Requirements

> AWS S3 Bucket to

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 25,796 |
| Python | 18,200 |
| Shell | 1,065 |
| Java | 161 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: apache-flink, boto3, botocore, jmespath, s3transfer, urllib3
- flink-java-dependency/pom.xml (capture: captured) — dependency clues: flink-connector-elasticsearch7, flink-connector-jdbc, flink-connector-kinesis, flink-s3-fs-hadoop, flink-uber, maven-shade-plugin, postgresql
- tf/requirements.txt (capture: captured) — dependency clues: apache-flink, boto3, botocore, jmespath, s3transfer, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 0
- Forks at capture: 1
- Last updated: 2024-03-22T21:42:58Z
- Last pushed: 2024-01-26T23:06:22Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit)
- [README](https://github.com/aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit/issues)
- [Releases](https://github.com/aws-samples/amazon-managed-apache-flink-service-pyflink-starter-kit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
