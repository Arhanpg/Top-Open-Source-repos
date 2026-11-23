# aws-solutions/digital-evidence-archive-on-aws

- Company: Amazon
- GitHub account: [https://github.com/aws-solutions](https://github.com/aws-solutions)
- Mapping status: official-directory-listed
- Repository: [aws-solutions/digital-evidence-archive-on-aws](https://github.com/aws-solutions/digital-evidence-archive-on-aws)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-solutions/digital-evidence-archive-on-aws/blob/main/README.md)
- README blob SHA: 08af0d7cf7872729d53dcb75ebdda0fa638ede7b
- Repository ID: 547390948
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:12:43+00:00

### Short excerpt (up to 100 words)

> Digital Evidence Archive on AWS enables Law Enforcement organizations to ingest evidence data to aid digital data management Follow these steps to deploy your production environment. If developing/testing, follow the Simple Deployment Section. You can deploy using your local computer via the terminal (for Mac/Linux users) or Command Prompt for Windows Users. The commands in the following steps may use different commands depending on which OS your computer is running, so make sure to follow the directions carefully. We recommend using a custom domain, since the default URL for this solution is not human readable and is limited to older

### README headings

- Deprecation Warning
- This solution will be deprecated as of 06/30/2024. Please view our alternative partner solutions [here](https://aws.amazon.com/solutions/justice-public-safety/digital-forensics-evidence-management-systems/)
- Digital Evidence Archive
- Code Coverage
- Getting Started
- Production Deployment
- Step 0: Setup a Custom Domain (Recommended)
- Option 1: Using a Route53 Domain
- Option 2: Using a non-Route53 Domain
- Pre-requisites
- Step 1: Clone the repository
- Step 2: Customize your configuration
- Generate the Config File
- Customize your System Use Notification
- Step 3: Launch the Stack
- FIPS
- Step 4: Integrate your CJIS Compliant Identity Provider
- 4.1: IdP Side Integration
- Integrating with Okta
- Create Attribute in Okta
- Create SAML 2.0 Application in Okta
- Configuring DEA to connect with IdP
- Integrating with Identity Center
- Enable IAM Identity Center
- Sync Active Directory or external Identity Provider to Identity Center
- Create SAML 2.0 Application in Identity Center
- Sync Users & Groups (Active Directory only)
- Configuring DEA to connect with IdP
- 4.2: Relaunch Stack to Update with Authentication Information
- Step 5: Save your Configuration File

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| TypeScript | 2,184,168 |
| Shell | 47,409 |
| JavaScript | 25,062 |
| SCSS | 2,361 |
| Python | 2,103 |
| HTML | 576 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- deployment/cdk-solution-helper/package.json (capture: captured) — dependency clues: fs
- source/dea-app/package.json (capture: captured) — dependency clues: @aws-sdk/client-athena, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-cognito-identity, @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-datasync, @aws-sdk/client-dynamodb, @aws-sdk/client-firehose, @aws-sdk/client-iam, @aws-sdk/client-identitystore, @aws-sdk/client-s3, @aws-sdk/client-s3-control, @aws-sdk/client-secrets-manager, @aws-sdk/client-sqs, @aws-sdk/client-ssm, @aws-sdk/client-sts, @aws-sdk/s3-request-presigner, @aws-sdk/types, @aws-sdk/util-stream-node, @aws/workbench-core-audit, @casl/ability
- source/dea-backend/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-cognito-identitypool-alpha, @aws-cdk/aws-glue-alpha, @aws-cdk/aws-kinesisfirehose-alpha, @aws-cdk/aws-kinesisfirehose-destinations-alpha, @aws-cdk/aws-servicecatalogappregistry-alpha, @aws-sdk/client-cloudformation, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-kinesis, @aws-sdk/client-s3, @aws/dea-app, @rushstack/eslint-config, @rushstack/heft, @rushstack/heft-jest-plugin, @rushstack/heft-node-rig, @types/aws-lambda, @types/convict, @types/heft-jest, @types/inquirer, @types/js-yaml
- source/dea-main/package.json (capture: captured) — dependency clues: @aws-cdk/aws-glue-alpha, @aws/dea-backend, @aws/dea-ui, @aws/dea-ui-infrastructure, @rushstack/eslint-config, @rushstack/heft, @rushstack/heft-jest-plugin, @rushstack/heft-node-rig, @types/heft-jest, @types/js-yaml, @types/lodash, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, aws-lambda, axios, constructs, dynamodb-onetable
- source/dea-ui/infrastructure/package.json (capture: captured) — dependency clues: @aws/dea-backend, @aws/dea-ui, @rushstack/eslint-config, @rushstack/heft, @rushstack/heft-jest-plugin, @rushstack/heft-node-rig, @types/heft-jest, @types/jest, @types/js-yaml, @types/node, @types/prettier, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, cheerio, constructs, eslint, eslint-plugin-import, eslint-plugin-security
- source/dea-ui/ui/package.json (capture: captured) — dependency clues: @aws-sdk/client-athena, @aws-sdk/client-cognito-identity, @aws-sdk/client-cognito-identity-provider, @aws-sdk/client-s3, @aws/dea-app, @babel/core, @babel/preset-env, @babel/preset-react, @babel/preset-typescript, @cloudscape-design/collection-hooks, @cloudscape-design/component-toolkit, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @cloudscape-design/jest-preset, @rushstack/eslint-config, @rushstack/heft, @rushstack/heft-jest-plugin, @rushstack/heft-node-rig, @testing-library/dom

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 18
- Forks at capture: 5
- Last updated: 2025-11-30T18:21:11Z
- Last pushed: 2024-07-02T21:33:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-solutions/digital-evidence-archive-on-aws)
- [README](https://github.com/aws-solutions/digital-evidence-archive-on-aws/blob/main/README.md)
- [Issues](https://github.com/aws-solutions/digital-evidence-archive-on-aws/issues)
- [Releases](https://github.com/aws-solutions/digital-evidence-archive-on-aws/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
