# amazon-archives/appsync-lambda-ai

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/appsync-lambda-ai](https://github.com/amazon-archives/appsync-lambda-ai)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/appsync-lambda-ai/blob/master/README.md)
- README blob SHA: dd804ddd34a76773c71ea9f36b5b228291e1f542
- Repository ID: 139794147
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Demo of using a GraphQL resolver to hit a lambda function, interact with Amazon Translate & Amazon Polly, return the response & play it back in the app. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:28:59+00:00

### Short excerpt (up to 100 words)

> This app demonstrates how you can use a Lambda function as an AWS AppSync datasource to perform really cool operations and return the result in a GraphQL query. In this example, we build an app that allows someone to put the text they would like to translate into the app, the app then returns the translation into voice for the user to play back. 1. clone the project git clone https://github.com/dabit3/appsync-lambda-ai.git 2. change directories into the project & install depencies cd appsync-lambda-ai yarn || npm install 1. Visit https://s3.console.aws.amazon.com/ and click __Create bucket__ 2. Give the bucket a name and

### README headings

- AI Enabled GraphQL with AWS AppSync
- Getting Started
- React Native setup
- Creating an S3 bucket
- Setting up the Lambda function
- AWS AppSync Setup

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 5,676 |
| Objective-C | 3,912 |
| Starlark | 1,732 |
| Java | 1,658 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: aws-amplify, babel-preset-react-native, buffer, jest, react, react-native, react-native-elements, react-native-sound, react-native-vector-icons, react-test-renderer, util
- android/build.gradle (capture: captured)
- lambda/package.json (capture: captured) — dependency clues: aws-sdk, uuid
- android/app/build.gradle (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 16
- Forks at capture: 7
- Last updated: 2023-07-27T12:04:05Z
- Last pushed: 2020-04-03T19:32:48Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/appsync-lambda-ai)
- [README](https://github.com/amazon-archives/appsync-lambda-ai/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/appsync-lambda-ai/issues)
- [Releases](https://github.com/amazon-archives/appsync-lambda-ai/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
