# amazon-archives/aws-appsync-relay

- Company: Amazon
- GitHub account: [https://github.com/amazon-archives](https://github.com/amazon-archives)
- Mapping status: official-directory-listed
- Repository: [amazon-archives/aws-appsync-relay](https://github.com/amazon-archives/aws-appsync-relay)
- Default branch: master
- README: [Open upstream README](https://github.com/amazon-archives/aws-appsync-relay/blob/master/README.md)
- README blob SHA: a3de2ee944bb92446adb3ebb757343a530eda1dd
- Repository ID: 151639295
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A sample Relay app using AWS AppSync

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:38:00+00:00

### Short excerpt (up to 100 words)

> AWS AppSync Relay ================= This sample project shows how to use the Relay library together with an AWS AppSync backend. See the blog post for more in-depth discussion. Here are links to some of the key technologies used in the project: - AWS AppSync - The AWS Amplify Library - AWS CloudFormation - React - Relay To run locally, you'll first need to deploy the backend in AWS, like this: aws cloudformation package --template-file backend/template.yml --s3-bucket my-package-bucket > packaged_template.yml aws cloudformation deploy --template-file packaged_template.yml --stack-name AppSyncRelay --capabilities CAPABILITY_NAMED_IAM Replace "my-package-bucket" with any S3 bucket you want to use to store

### README headings

- Launching the AppSync backend
- Running the app locally
- Deploying the frontend as a static site
- License Summary

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 18,547 |
| Shell | 1,444 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @babel/core, @babel/preset-env, @babel/preset-react, @material-ui/core, @material-ui/icons, aws-amplify, aws-amplify-react, babel-loader, babel-plugin-relay, css-loader, graphql, html-webpack-plugin, react, react-dom, react-relay, relay-compiler, style-loader, webpack, webpack-cli, webpack-dev-server

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 59
- Forks at capture: 12
- Last updated: 2023-07-25T15:41:51Z
- Last pushed: 2021-03-12T06:01:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-archives/aws-appsync-relay)
- [README](https://github.com/amazon-archives/aws-appsync-relay/blob/master/README.md)
- [Issues](https://github.com/amazon-archives/aws-appsync-relay/issues)
- [Releases](https://github.com/amazon-archives/aws-appsync-relay/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
