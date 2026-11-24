# aws-samples/amazon-aurora-s3-redshift-serverless-dwh

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-aurora-s3-redshift-serverless-dwh](https://github.com/aws-samples/amazon-aurora-s3-redshift-serverless-dwh)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-aurora-s3-redshift-serverless-dwh/blob/main/README.md)
- README blob SHA: 834b7be36a4a28430b0a5db74dfa25cbab512433
- README bytes captured: 5901
- README truncated at capture limit: False
- Repository ID: 800261843
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T22:11:14+00:00

### Short excerpt (up to 300 words)

> このサンプルでは、Amazon EventBridge をシステム実行のスケジューラーとしています。データ集約は AWS

### README headings

- Aurora to S3 & Redshift Serverless System
- Use Case
- Use Case1
- Use Case2
- Use Case3
- Architecture
- 各ステップの概要
- Deploy
- 1. パッケージインストール
- 2. CDK のセットアップ
- (Option1)新規の Aurora MySQL を利用する場合
- (Option2) 既存の Aurora MySQL を利用する場合
- 3. Stack をデプロイ
- FAQ
- Amazon RDS zero-ETL integrations with Amazon Redshift との違いはなんですか？
- Documentation
- Contributing
- Licence

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: Architecture

> このサンプルでは、Amazon EventBridge をシステム実行のスケジューラーとしています。データ集約は AWS

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 18,754 |
| Python | 13,673 |
| JavaScript | 1,210 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/aws-lambda-python-alpha, @aws-prototyping-sdk/pdk-nag, @types/jest, @types/node, aws-cdk, aws-cdk-lib, constructs, jest, n, ts-jest, ts-node, typescript
- lambda/auroraloadkicker/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, boto3, pymysql, pytz
- lambda/checks3object/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, boto3, pytz
- lambda/redshiftanalysistable/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, boto3
- lambda/redshiftinit/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, boto3
- lambda/redshiftloadkicker/requirements.txt (capture: captured) — dependency clues: aws-lambda-powertools, boto3, pandas

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 4
- Forks at capture: 0
- Last updated: 2025-12-22T04:41:48Z
- Last pushed: 2025-04-10T02:09:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-aurora-s3-redshift-serverless-dwh)
- [README](https://github.com/aws-samples/amazon-aurora-s3-redshift-serverless-dwh/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-aurora-s3-redshift-serverless-dwh/issues)
- [Releases](https://github.com/aws-samples/amazon-aurora-s3-redshift-serverless-dwh/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
