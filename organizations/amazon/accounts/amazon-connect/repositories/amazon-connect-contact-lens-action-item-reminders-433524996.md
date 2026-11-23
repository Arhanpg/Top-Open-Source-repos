# amazon-connect/amazon-connect-contact-lens-action-item-reminders

- Company: Amazon
- GitHub account: [https://github.com/amazon-connect](https://github.com/amazon-connect)
- Mapping status: official-directory-listed
- Repository: [amazon-connect/amazon-connect-contact-lens-action-item-reminders](https://github.com/amazon-connect/amazon-connect-contact-lens-action-item-reminders)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-connect/amazon-connect-contact-lens-action-item-reminders/blob/main/README.md)
- README blob SHA: 2c6f04dc3fe96e17d5bd5a2f13c0c87295f875cd
- Repository ID: 433524996
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:07:53+00:00

### Short excerpt (up to 100 words)

> This repo is attached to the blog "Create action item reminders with Amazon Connect Tasks and Contact Lens for Amazon Connect". Head there to get the full set of steps for using this code. 1. Install CDK and run the CDK bootstrap command if this is the first time running CDK in an AWS Account. npm -g install typescript npm -g install aws-cdk cdk bootstrap aws://ACCOUNT_ID/AWS_REGION 2. Install dependencies npm install 3. Deploy the project cdk deploy --context amazonConnectUrl=<YOUR INSTANCE URL> --context amazonConnectArn=<YOUR INSTANCE ARN> --context contactFlowId=<CONTACT FLOW ID> --context amazonConnectId=<INSTANCE ID> --context taskQueueArn=<TASK QUEUE ARN> --context contactLensS3BucketName=<YOUR BUCKET NAME>

### README headings

- Amazon Connect Contact lens action item reminders
- Deployment Steps
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 4,184 |
| JavaScript | 3,631 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-sns, @aws-cdk/aws-sns-subscriptions, @aws-cdk/core, @types/jest, @types/node, aws-cdk, jest, source-map-support, ts-jest, ts-node, typescript

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 1
- Forks at capture: 2
- Last updated: 2026-07-01T14:27:33Z
- Last pushed: 2023-10-18T16:15:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-connect/amazon-connect-contact-lens-action-item-reminders)
- [README](https://github.com/amazon-connect/amazon-connect-contact-lens-action-item-reminders/blob/main/README.md)
- [Issues](https://github.com/amazon-connect/amazon-connect-contact-lens-action-item-reminders/issues)
- [Releases](https://github.com/amazon-connect/amazon-connect-contact-lens-action-item-reminders/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
