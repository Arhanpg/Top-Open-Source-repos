# amazon-connect/voicemail-for-amazon-connect

- Company: Amazon
- GitHub account: [https://github.com/amazon-connect](https://github.com/amazon-connect)
- Mapping status: official-directory-listed
- Repository: [amazon-connect/voicemail-for-amazon-connect](https://github.com/amazon-connect/voicemail-for-amazon-connect)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-connect/voicemail-for-amazon-connect/blob/master/README.md)
- README blob SHA: f07e8a878ec108956f3298e2400c498e121ee3c9
- Repository ID: 237274873
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Voicemail for Amazon Connect solution helps call center administrators and managers automate a voicemail solution using Amazon Connect. A customer can call in, enter the extension number of the agent they want to speak with, and leave a voicemail for that specific agent. The solution generates voicemail recordings and transcripts that are delivered to agents using their preferred communication setting: SMS and/or email.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:30:47+00:00

### Short excerpt (up to 100 words)

> This solutions deploys the resources necessary to configure a voicemail system to use with Amazon Connect. See Solution Architecture. The master and development branches have been updated to account for the recent S3 changes. Updated CloudFormation Templates and deployment instructions can be found here We have added a new branch to this solution: the "development" branch. The "development" branch contains the same solution, but has a simplified build system that removes complexities introduced by the AWS Solution. If you would like to pull down this code to modify it for your own testing, you should use the "development" branch. The

### README headings

- Voicemail for Amazon Connect
- Development Branch
- Running unit tests for customization
- Building distributable for customization
- File Structure

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 271,191 |
| TypeScript | 71,375 |
| Java | 52,948 |
| Python | 15,832 |
| Shell | 9,945 |
| HTML | 1,996 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- source/Pipfile (capture: captured) — dependency clues: boto3, host_files, name, python_version, url, verify_ssl
- source/aws-connect-vm-portal/package.json (capture: captured) — dependency clues: @colors/colors, @material-ui/core, @material-ui/icons, @types/jest, @types/material-ui, @types/node, @types/react, @types/react-dom, @types/react-redux, @types/react-router, @types/react-router-dom, @types/redux-thunk, @types/request-promise, awesome-phonenumber, aws-amplify, aws-amplify-react, aws-sdk, classnames, command-line-args, command-line-usage
- source/aws-connect-vm-portal/Pipfile (capture: captured) — dependency clues: deploy_dev, deploy_prod, name, python_version, stacker, url, verify_ssl
- source/aws-connect-vm-serverless/package.json (capture: captured) — dependency clues: @babel/core, @babel/preset-env, amazon-cognito-identity-js, awesome-phonenumber, aws-sdk, babel-cli, babel-core, babel-jest, babel-loader, babel-plugin-transform-runtime, babel-plugin-webpack-aliases, babel-preset-env, babel-preset-es2015, babel-preset-stage-2, babel-runtime, eslint, glob, is-nan, jest, jmespath
- source/aws-connect-vm-serverless/pom.xml (capture: captured) — dependency clues: amazon-kinesis-video-streams-parser-library, apache-client, aws-connect-vm, aws-java-sdk-cloudwatch, aws-java-sdk-dynamodb, aws-java-sdk-kinesisvideo, aws-java-sdk-s3, aws-java-sdk-transcribe, aws-lambda-java-core, aws-lambda-java-events, aws-lambda-java-log4j2, commons-lang3, json, junit, log4j-api, log4j-core, log4j-slf4j18-impl, maven-shade-plugin, maven-shade-plugin.log4j2-cachefile-transformer, netty-nio-client

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 71
- Forks at capture: 79
- Last updated: 2026-09-05T15:58:05Z
- Last pushed: 2024-05-07T17:28:03Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-connect/voicemail-for-amazon-connect)
- [README](https://github.com/amazon-connect/voicemail-for-amazon-connect/blob/master/README.md)
- [Issues](https://github.com/amazon-connect/voicemail-for-amazon-connect/issues)
- [Releases](https://github.com/amazon-connect/voicemail-for-amazon-connect/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
