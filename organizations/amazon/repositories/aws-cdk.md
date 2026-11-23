# AWS Cloud Development Kit (AWS CDK)

<sub>Company: Amazon / AWS · Repository: [aws/aws-cdk](https://github.com/aws/aws-cdk) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

The AWS Cloud Development Kit (AWS CDK) is an open-source framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. It offers high-level, object-oriented abstractions for describing AWS resources using familiar programming languages.

**Problem it addresses:** infrastructure defined directly as large collections of low-level configuration can be repetitive and difficult to reuse. CDK lets developers express infrastructure with reusable constructs and compose those constructs into stacks that can be synthesized and deployed through CloudFormation.

## Core building blocks

### Constructs

A construct is a reusable cloud component. The README describes the AWS Construct Library as containing modules for AWS services, with APIs that encapsulate service-specific configuration and reduce glue code.

### Stacks

Constructs are composed into stacks. A stack is part of the infrastructure definition that can be synthesized and deployed through AWS CloudFormation.

### CDK applications and CLI

Developers create a CDK app using one of the supported languages, then use the CDK CLI to interact with that app. The README identifies CLI workflows for:

- Synthesizing CloudFormation templates.
- Deploying stacks to development AWS accounts.
- Diffing local infrastructure definitions against deployed stacks to understand changes.

This creates a source-code-oriented workflow for infrastructure definition, review and deployment.

## Supported programming languages

The README lists the following language support and minimum versions:

| Language | Requirement shown in README |
|---|---|
| JavaScript | Node.js 20.x or newer |
| TypeScript | Node.js 20.x or newer |
| Python | Python 3.8 or newer |
| Java | Java 8 or newer; Maven 3.5.4 or newer |
| .NET | .NET 8.0 or newer |
| Go | Go 1.16.4 or newer |

These requirements are taken from the README inspected for this catalogue. Check current project documentation and language end-of-life policies before choosing a runtime version.

## Technology profile

| Area | README-supported details |
|---|---|
| Product category | Infrastructure as Code framework |
| Provisioning engine | AWS CloudFormation |
| Programming interfaces | JavaScript, TypeScript, Python, Java, .NET and Go |
| Reusable abstraction | Constructs |
| Deployment unit | Stacks |
| Command-line interface | AWS CDK CLI |
| Construct ecosystem | AWS Construct Library |
| Package distribution | npm, PyPI, NuGet, Maven Central and Go reference links |

## Typical development workflow

1. Create a CDK app using a supported language.
2. Define reusable constructs for the required cloud resources.
3. Compose the constructs into one or more stacks.
4. Use the CDK CLI to synthesize the CloudFormation representation.
5. Review the generated infrastructure and the diff against the deployed environment.
6. Deploy the stack through the documented AWS workflow.

The README positions constructs as a way to encapsulate infrastructure best practices and share reusable components. Teams should still review the generated template and permissions before deploying.

## Where it is useful

- Managing cloud infrastructure through version-controlled application code.
- Reusing infrastructure patterns across services and environments.
- Defining AWS resources with normal programming-language abstractions.
- Reviewing infrastructure changes before deployment.
- Creating higher-level internal construct libraries for platform engineering teams.

## Operational considerations

Infrastructure-as-Code can create or modify real cloud resources. Treat deployment credentials, IAM permissions, environment separation, approval gates and change review as part of the delivery pipeline. A successful synthesis is not proof that a deployment is safe or cost-effective.

The README also notes that language versions are subject to vendor/community end-of-life and that supported versions can change with notice. Check current requirements before bootstrapping a new project.

## Upstream references

- [Repository](https://github.com/aws/aws-cdk)
- [Primary README](https://github.com/aws/aws-cdk/blob/main/README.md)
- [Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide)
- [API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html)
- [Getting started](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
- [Construct Hub](https://constructs.dev/)

**Evidence note:** README blob inspected: `11341e56689e146b0d4aaed18f58e2abe9017b3c`.
