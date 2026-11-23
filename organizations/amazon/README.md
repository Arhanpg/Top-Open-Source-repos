# Amazon / AWS — open-source organization profile

- **GitHub account used in this catalogue:** [aws](https://github.com/aws)
- **Company mapping:** AWS engineering account candidate; this does not represent every Amazon business or engineering organization.
- **Source group:** United States & Global
- **Directory status:** initialized; public repository inventory not exhaustive
- **Detailed README records:** 5

## Reviewed project

| Project | Focus | What the README documents |
|---|---|---|
| [AWS Cloud Development Kit](repositories/aws-cdk.md) | Infrastructure as Code | Defines cloud infrastructure using constructs and stacks, then synthesizes and deploys through AWS CloudFormation |

## Project overview

AWS CDK is a framework for describing infrastructure using familiar programming languages rather than writing every low-level resource definition manually. Its construct library packages reusable resource abstractions, while stacks group resources for synthesis and deployment. The CLI supports template synthesis, deployment and infrastructure diffs.

## Technology snapshot

The README lists JavaScript, TypeScript, Python, Java, .NET and Go as supported language interfaces, with language-specific runtime requirements. CloudFormation is the provisioning layer, and the AWS CDK CLI is the main command-line workflow.

## Inventory status and cautions

The `aws` organization is focused on AWS public engineering repositories and should not be assumed to represent all Amazon-owned GitHub repositories. The repository list in this directory is currently a single README-reviewed example, not an exhaustive AWS inventory. Deployment examples must be reviewed for account permissions, cloud cost, environment isolation and change controls before use.

## Upstream

- [AWS GitHub account](https://github.com/aws)
- [AWS CDK repository](https://github.com/aws/aws-cdk)
- [AWS CDK Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide)
- [AWS repository index in this catalogue](repositories/README.md)


## Additional README-reviewed projects — 23 November 2026

Three additional AWS repository briefs have been added: Amazon SageMaker Examples, AWS SAM Transform and Karpenter AWS Provider. These pages cover ML workflow examples, serverless template translation and Kubernetes node provisioning. They preserve cloud-cost, IAM and operational cautions from the project documentation. See the [repository index](repositories/README.md).


## Discovery sample — 23 November 2026

[Open the saved first-page search snapshot](discovery/search-page-1-2026-11-23.json). It contains up to 100 ranked GitHub search results for this account and is not a complete public repository inventory. Full API pagination and wider official-account discovery remain necessary.


## Continued README review — 23 November 2026

1 additional README-reviewed project brief has been added to this account folder. See [the repository index](repositories/README.md). The account's complete public repository inventory and related company organizations still require full discovery and pagination.


## Official AWS GitHub organization directory

The official [Open Source at AWS](https://aws.github.io/) website lists 30 distinct GitHub organization links in its “AWS GitHub Organizations” section, including the primary `aws` account. The catalogue maps the other 29 accounts with the separate `official-directory-listed` status. See [Amazon/AWS Account Discovery](ACCOUNT-DISCOVERY.md) for the account list, sample repository checks and attribution rules.
