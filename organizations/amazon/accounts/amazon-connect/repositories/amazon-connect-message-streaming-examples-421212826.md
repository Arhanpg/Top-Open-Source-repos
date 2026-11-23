# amazon-connect/amazon-connect-message-streaming-examples

- Company: Amazon
- GitHub account: [https://github.com/amazon-connect](https://github.com/amazon-connect)
- Mapping status: official-directory-listed
- Repository: [amazon-connect/amazon-connect-message-streaming-examples](https://github.com/amazon-connect/amazon-connect-message-streaming-examples)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-connect/amazon-connect-message-streaming-examples/blob/main/README.md)
- README blob SHA: 1141d1237ed11cb66c5e5ba8373257be3ce7781b
- Repository ID: 421212826
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

This repository contains an example project on how to get started with Amazon Connect Chat Message Streaming APIs to enable SMS and Facebook messenger channels for customer service. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:08:02+00:00

### Short excerpt (up to 100 words)

> - Create a simple contact flow which routes the contact to the appropriate queue. - (You can use the sample contact flow for this example.) - An Amazon Connect Instance - An Amazon Connect Contact Flow setup for Amazon Connect (including Disconnect flow) - AWS CLI setup in your local environment For detailed steps please visit the blog Please refer to this blog on the steps to create a Facebook messenger channel. `npm -g install typescript` `npm install -g aws-cdk` `cdk bootstrap aws://ACCOUNT_ID/AWS_REGION` - `npm install` - `cd src/lambda/inboundMessageHandler` - `npm install` - `cd ../../..` - `cd src/lambda/outboundMessageHandler` - `npm

### README headings

- Message streaming API starter projects
- Prerequisite
- General
- SMS
- FB
- Install AWS CDK
- Deployment commands
- Deploy SMS channel only
- Deploy FB Channel only
- Deploy WhatsApp Channel only
- Deploy BOTH SMS and FB channel
- Deploy FB channel only with PII redaction
- Architecture
- Customer chat path
- Agent chat path
- Repository structure
- CDK
- Lambda
- Video walkthrough
- Troubleshooting
- SDK errors
- Message not getting published to SNS
- Contact flow execution not starting
- Throttling Exception (HTTP Error Code : 429/TooManyRequests)
- CreateParticipantConnection API throwing exception when “ConnectParticipant” Boolean is passed as true
- StartContact Streaming API throwing exception when providing correct SNS ARN
- FAQ
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 41,019 |
| TypeScript | 15,668 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-apigateway, @aws-cdk/aws-apigatewayv2, @aws-cdk/aws-apigatewayv2-integrations, @aws-cdk/aws-dynamodb, @aws-cdk/aws-iam, @aws-cdk/aws-lambda, @aws-cdk/aws-pinpoint, @aws-cdk/aws-s3, @aws-cdk/aws-s3-notifications, @aws-cdk/aws-secretsmanager, @aws-cdk/aws-sns, @aws-cdk/aws-sns-subscriptions, @aws-cdk/core, @types/jest, @types/node, aws-cdk, jest, source-map-support, ts-jest
- src/common-util/package.json (capture: captured)
- src/lambda/digitalChannelHealthCheck/package.json (capture: captured) — dependency clues: aws-sdk, common-util
- src/lambda/inboundMessageHandler/package.json (capture: captured) — dependency clues: aws-sdk, common-util
- src/lambda/outboundMessageHandler/package.json (capture: captured) — dependency clues: aws-sdk, common-util

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 26
- Forks at capture: 42
- Last updated: 2026-10-29T14:25:48Z
- Last pushed: 2023-07-20T06:16:04Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-connect/amazon-connect-message-streaming-examples)
- [README](https://github.com/amazon-connect/amazon-connect-message-streaming-examples/blob/main/README.md)
- [Issues](https://github.com/amazon-connect/amazon-connect-message-streaming-examples/issues)
- [Releases](https://github.com/amazon-connect/amazon-connect-message-streaming-examples/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
