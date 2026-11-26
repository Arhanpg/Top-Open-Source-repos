# awslabs/aws-virtual-application-management

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-virtual-application-management](https://github.com/awslabs/aws-virtual-application-management)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/aws-virtual-application-management/blob/main/README.md)
- README blob SHA: 6980a6b4f3495829a31fd78e4fb2a8a5146660b6
- README bytes captured: 30415
- README truncated at capture limit: False
- Repository ID: 399564882
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A solution designed to automate the curation of Amazon AppStream 2.0 Images and allows administrators to create an application repository.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T04:08:24+00:00

### Short excerpt (up to 300 words)

> In the optional section VAM creates some artifacts

### README headings

- VAM -- Virtual Application Management
- Using an AWS CloudFormation template
- Step 1: Verify the zip archive
- Step 2: Creating the S3 bucket
- Step 3: Creating a CloudFormation stack
- Step 4: Obtaining website URL
- Step 5: Logging in
- Deploy using a pre-existing VPC and subnets
- Deploy using a pre-existing VPC, subnets and Active Directory
- Create Self-signed certificate for HTTPS Listener
- Enable PSRemoting on Image Builder
- Installation
- Interactive Installation
- Audits
- AWS Web Application Firewall (WAF)
- Allow new IPs to access the website
- Disable WAF (Not recommended)
- Removing the Solution
- Removal Prerequisites
- Remove VAM created AppStream 2.0 Fleets
- Remove any VAM created EC2 instances
- Remove Policies added to VAM deployed Roles
- Deployed Using an AWS CloudFormation template
- "DemoDeployment" Parameter set to "Yes"
- Deleting the Code Pipeline
- Prerequisite
- Removing the Pipeline
- Deployed via Interactive Deployment
- Manually Removing the Solution
- Note on S3 Bucket Namespace

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Installation

> In the optional section

### Technology and requirements: Removal Prerequisites

> VAM creates some artifacts

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| JavaScript | 3,943,323 |
| Shell | 25,138 |
| CSS | 18,481 |
| PowerShell | 2,121 |
| HTML | 502 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @aws-ee/base-serverless-settings-helper, @aws-ee/base-serverless-solution-commands, @aws-ee/main-assembly, @aws-ee/main-commands, @aws-ee/main-registry-docs, fast-check, jest-fast-check, serverless
- main/integration-tests/package.json (capture: captured) — dependency clues: eslint, eslint-config-airbnb, eslint-config-airbnb-base, eslint-config-prettier, eslint-import-resolver-node, eslint-plugin-import, eslint-plugin-jest, eslint-plugin-jsx-a11y, eslint-plugin-prettier, husky, jest, jest-junit, prettier, pretty-quick, request, request-promise-native
- main/packages/assembly/package.json (capture: captured) — dependency clues: @aws-ee/appstream-image-builder-assembly, @aws-ee/base-assembly, @aws-ee/base-assembly-tasks, @aws-ee/base-auth-cognito-assembly, @aws-ee/base-auth-cognito-serverless-commands, @aws-ee/base-cicd-assembly, @aws-ee/base-post-deployment-assembly, @aws-ee/base-rest-api-assembly, @aws-ee/base-script-utils, @aws-ee/base-serverless-settings-helper, @aws-ee/base-ui-assembly, @aws-ee/base-ui-public-hosting-assembly, @aws-ee/base-workflow-assembly, @aws-ee/eventbridge-assembly, @aws-ee/vam-api-assembly, @aws-ee/vam-sample-applications-assembly, @aws-ee/vam-silky-smooth-deployments-assembly, @aws-ee/vam-ui-assembly, @babel/cli, @babel/core
- main/packages/main-commands/package.json (capture: captured) — dependency clues: @aws-ee/base-auth-cognito-serverless-commands, @aws-ee/base-script-utils, @aws-ee/base-serverless-settings-helper, @babel/cli, @babel/core, @babel/preset-env, @types/jest, eslint, eslint-config-airbnb, eslint-config-airbnb-base, eslint-config-prettier, eslint-import-resolver-node, eslint-plugin-import, eslint-plugin-jest, eslint-plugin-prettier, fs-extra, husky, jest, jest-junit, js-yaml
- main/packages/main-controllers/package.json (capture: captured) — dependency clues: @aws-ee/base-controllers, @aws-ee/main-services, @babel/cli, @babel/core, @babel/preset-env, @babel/runtime, @types/jest, eslint, eslint-config-airbnb, eslint-config-airbnb-base, eslint-config-prettier, eslint-import-resolver-node, eslint-plugin-import, eslint-plugin-jest, eslint-plugin-prettier, husky, jest, jest-junit, lodash, prettier
- main/packages/main-services/package.json (capture: captured) — dependency clues: @aws-ee/base-services, @aws-ee/base-services-container, @babel/cli, @babel/core, @babel/preset-env, @babel/runtime, @types/jest, eslint, eslint-config-airbnb, eslint-config-airbnb-base, eslint-config-prettier, eslint-import-resolver-node, eslint-plugin-import, eslint-plugin-jest, eslint-plugin-prettier, husky, jest, jest-junit, lodash, prettier

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 20
- Forks at capture: 9
- Last updated: 2024-11-29T21:53:17Z
- Last pushed: 2023-08-15T22:02:09Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-virtual-application-management)
- [README](https://github.com/awslabs/aws-virtual-application-management/blob/main/README.md)
- [Issues](https://github.com/awslabs/aws-virtual-application-management/issues)
- [Releases](https://github.com/awslabs/aws-virtual-application-management/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
