# aws-solutions/amazon-marketing-cloud-uploader-from-aws

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:55:16+00:00

## Project purpose

This solution enables users to upload first party datasets from Amazon S3 into the Amazon Marketing Cloud (AMC). It includes a web application in which users are guided through the process of defining datasets and their PII attributes. Once this information is submitted, the solution initiates an ETL workflow that performs data normalization, hashing of plain-text PII, time-series partitioning, and upload to AMC.

## Why this project is used

Easily upload first-party signals into Amazon Marketing Cloud (AMC) for evaluating and planning advertising campaigns

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Vue, Shell, JavaScript, CSS, HTML, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: aws-xray-sdk, chalice, requests, urllib3
- Build/package tools: Docker build configuration, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/website/src/store/index.js, source/api/app.py, source/amc_uploader/lib/__init__.py, source/amc_uploader/lib/tasks.py

## Setup and usage

- INSTALLATION: The following Cloudformation templates will deploy the application.
- INSTALLATION: US East (N. Virginia) | [](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=amcufa&templateURL=https://solutions-reference.s3.amazonaws.com/amazon-marketing-cloud-uploader-from-aws/latest/amazon-marketing-cloud-uploader-from-aws.template)
- INSTALLATION: EU West (Ireland) | [](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=amcufa&templateURL=https://solutions-reference.s3.amazonaws.com/amazon-marketing-cloud-uploader-from-aws/latest/amazon-marketing-cloud-uploader-from-aws.template)
- INSTALLATION: Once the Cloud Formation stack has been created, open the URL shown in the UserInterface output of the base stack. You can also get this URL with the following AWS CLI command:
- INSTALLATION: aws cloudformation --region $REGION describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='UserInterface'].OutputValue" --output text
- INSTALLATION: For more installation options, see the Advanced Installation section.

## Limitations and caveats

- Known Issues: Visit the Issue page in this repository for known issues and feature requests.

## Evidence and provenance

- README: https://github.com/aws-solutions/amazon-marketing-cloud-uploader-from-aws/blob/main/README.md
- README SHA: b2be86a832269dd319b98bcb510c255a332ac728
- Manifests: deployment/lambda_layer_factory/Dockerfile, deployment/lambda_layer_factory/requirements.txt, source/amc_uploader/requirements.txt, source/amc_uploader/setup.py, source/anonymous_data_logger/requirements.txt, source/api/requirements.txt
- Sampled source files: source/website/src/store/index.js, source/api/app.py, source/amc_uploader/lib/tasks.py
- Git tree state: captured
- Evidence fingerprint: 846ecf770dc7c695a76dd4509efc18ed7d6c83d670cf8f51a3a0f41e7d8cb880

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
