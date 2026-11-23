# AWS Serverless Application Model (SAM) Transform

- **Company grouping:** Amazon / AWS
- **GitHub organization:** [aws](https://github.com/aws)
- **Repository:** [aws/serverless-application-model](https://github.com/aws/serverless-application-model)
- **Default branch:** default branch as shown by upstream GitHub metadata
- **README:** [Open upstream README](https://github.com/aws/serverless-application-model/blob/default/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `0069a1eca03028566d184dc108404d2fabfd199b`

## Project overview

The AWS SAM transform is a CloudFormation macro that converts AWS SAM templates into standard AWS CloudFormation templates. It extends CloudFormation template syntax with serverless resource types and defaults.

## Features and capabilities

- Adds AWS::Serverless-2016-10-31 to the Transform section of a CloudFormation template.
- Expands concise SAM resources such as AWS::Serverless::Function into underlying CloudFormation resources, including Lambda functions and IAM roles.
- The README lists built-in best practices and sensible defaults.
- Supports local testing and debugging through the AWS SAM CLI.
- Provides developer documentation, workshops, tutorials, schema generation and Python development/testing instructions.

## Technology stack

Python package aws-sam-translator; PyPI distribution; AWS CloudFormation macro/transform; AWS SAM template specification; AWS SAM CLI; the example creates AWS Lambda and IAM resources.

## Getting started

Create a template.yaml with the AWS::Serverless-2016-10-31 Transform declaration and a serverless resource, then use the AWS SAM CLI (the README shows sam sync) to deploy. Development instructions require Python 3.8+ and use a virtual environment, make init and make pr.

## Cloud, security and operational considerations

The transform is a template translator, not the SAM CLI itself. Deployment creates AWS resources and requires appropriate IAM permissions and cost review. Lambda runtime names evolve; check the current AWS Lambda runtime support policy rather than copying an old example blindly.

## Evaluation guidance

Review the version-specific AWS documentation, IAM requirements, deployment template and resource-cleanup procedure before running this project in an AWS account. Validate the costs of any cloud resources created by examples or controllers. This dossier summarizes the upstream README and is not a complete source-code, cloud-security or infrastructure review.

## Upstream references

- [Repository](https://github.com/aws/serverless-application-model)
- [README](https://github.com/aws/serverless-application-model/blob/default/README.md)
- [Issues](https://github.com/aws/serverless-application-model/issues)
- [Releases](https://github.com/aws/serverless-application-model/releases)

*Evidence note: README blob SHA above identifies the upstream revision inspected. Technology details are limited to the README's evidence; a full dependency and infrastructure-manifest audit remains outstanding.*
