# aws-actions/aws-cloudformation-github-deploy

- Company: Amazon
- GitHub account: [https://github.com/aws-actions](https://github.com/aws-actions)
- Mapping status: official-directory-listed
- Repository: [aws-actions/aws-cloudformation-github-deploy](https://github.com/aws-actions/aws-cloudformation-github-deploy)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-actions/aws-cloudformation-github-deploy/blob/master/README.md)
- README blob SHA: 87ea800e0ff29eec5f65ec95b80e899eb2e13d04
- Repository ID: 248828679
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Deploys AWS CloudFormation Stacks

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:33:24+00:00

### Short excerpt (up to 100 words)

> Deploys AWS CloudFormation Stacks. - name: Deploy to AWS CloudFormation uses: aws-actions/aws-cloudformation-github-deploy@v2.0.0 with: name: MyStack template: myStack.yaml parameter-overrides: 'MyParam1=myValue,MyParam2=${{ secrets.MY_SECRET_VALUE }}' The action can be passed a CloudFormation Stack `name` and a `template` file. The `template` file can be a local file existing in the working directory, or a URL to template that exists in an Amazon S3 bucket. It will create the Stack if it does not exist, or create a Change Set to update the Stack. An update fails by default when the Change Set is empty. Setting `fail-on-empty-changeset: false` will override this behavior and not throw an

### README headings

- AWS CloudFormation "Deploy CloudFormation Stack" Action for GitHub Actions
- Usage
- Enhanced Change Set Support
- 1. Create & Execute (Default)
- 2. Create Change Set Only (Review Mode)
- Review the outputs
- 3. Execute Existing Change Set
- Drift-Aware Change Sets
- PR Review Workflow
- Inputs
- parameter-overrides (OPTIONAL)
- Credentials and Region
- Permissions
- API Calls Made by This Action
- Example
- Proxy Configuration
- Your environment configuration
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 269,588 |
| JavaScript | 1,678 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: @actions/core, @aws-sdk/client-cloudformation, @aws-sdk/client-s3, @smithy/node-http-handler, @types/jest, @types/js-yaml, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, @vercel/ncc, aws-sdk-client-mock, aws-sdk-client-mock-jest, eslint, eslint-config-prettier, eslint-plugin-github, eslint-plugin-jest, eslint-plugin-prettier, fast-check, https-proxy-agent, husky

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 283
- Forks at capture: 130
- Last updated: 2026-11-10T21:54:39Z
- Last pushed: 2026-11-12T00:24:59Z
- Topics: aws, cloudformation, nodejs

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-actions/aws-cloudformation-github-deploy)
- [README](https://github.com/aws-actions/aws-cloudformation-github-deploy/blob/master/README.md)
- [Issues](https://github.com/aws-actions/aws-cloudformation-github-deploy/issues)
- [Releases](https://github.com/aws-actions/aws-cloudformation-github-deploy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
