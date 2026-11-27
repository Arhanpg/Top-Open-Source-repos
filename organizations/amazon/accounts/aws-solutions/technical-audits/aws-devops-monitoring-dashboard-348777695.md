# aws-solutions/aws-devops-monitoring-dashboard

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/aws-devops-monitoring-dashboard
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T06:59:53+00:00

## Project purpose

⚠️ __Important: DevOps Monitoring Dashboard on AWS will no longer be supported starting December 3, 2024. You can find other AWS Solutions in the AWS Solutions Library__ ⚠️

## Why this project is used

The DevOps Monitoring Dashboard on AWS solution is a reference implementation that automates the process for monitoring and visualizing performance and operational metrics in continuous integration/continuous delivery (CI/CD) pipeline following AWS best practices.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, TypeScript, Python, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-cdk/assert, @aws-cdk/aws-glue-alpha, @aws-cdk/aws-servicecatalogappregistry-alpha, @aws-sdk/client-athena, @aws-sdk/client-cloudwatch, @aws-sdk/client-eventbridge, @aws-sdk/client-glue, @aws-sdk/client-s3, @aws-sdk/client-secrets-manager, @aws-solutions-constructs/aws-eventbridge-kinesisfirehose-s3, @aws-solutions-constructs/aws-eventbridge-lambda, @aws-solutions-constructs/aws-kinesisfirehose-s3, @aws-solutions-constructs/core, @types/jest, @types/node, PyYAML, async, aws-cdk, aws-cdk-lib, aws-sdk-mock, axios, axios-mock-adapter, boto3, botocore, cdk-nag, chai, constructs, crhelper, eslint, eslint-config-prettier, eslint-config-react-app, eslint-plugin-header, eslint-plugin-import, eslint-plugin-node, eslint-plugin-prettier, jest, mocha, mock, moto, npm-run-all, nyc, prettier, pytest, pytest-cov, pytest-env, requests, sinon, sinon-chai, source-map-support, tenacity, ts-jest, ts-node, typescript, urllib3, uuid
- Build/package tools: npm-compatible manifest, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: deployment/cdk-solution-helper/index.js, source/lambda/event_parser/index.js, source/lambda/query_runner/index.js, source/lambda/tag_query/index.js

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/aws-devops-monitoring-dashboard/blob/main/README.md
- README SHA: 77384560857596063c0456d14412019e1565a15a
- Manifests: source/package.json, deployment/cdk-solution-helper/package.json, source/lambda/event_parser/package.json, source/lambda/multi_account_custom_resources/package.json, source/lambda/query_runner/package.json, source/lambda/quicksight-custom-resources/pyproject.toml
- Sampled source files: deployment/cdk-solution-helper/index.js, source/lambda/event_parser/index.js, source/lambda/query_runner/index.js, source/lambda/tag_query/index.js
- Git tree state: captured
- Evidence fingerprint: a8ad5f29edc1a1215ef9a47394ceff2a862007fbebd63dfb1ffa3e9ed6495642

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
