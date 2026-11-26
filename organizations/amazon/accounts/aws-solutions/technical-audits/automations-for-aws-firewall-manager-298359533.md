# aws-solutions/automations-for-aws-firewall-manager

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/automations-for-aws-firewall-manager
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:05:49+00:00

## Project purpose

⚠️🚨⚠️ The Automations for AWS Firewall Manager solution has been deprecated and will not be receiving any additional features or updates. We encourage customers to explore using the latest deployment, multi-account management, and compliance features in AWS Firewall Manager for management and enforcement of firewall rules. ⚠️🚨⚠️

## Why this project is used

The Automations For AWS Firewall Manager solution is intended for customers looking to easily manage consistent security posture across their entire AWS Organization. The solution uses AWS Firewall Manager Service.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-cdk/assert, @aws-lambda-powertools/commons, @aws-lambda-powertools/logger, @aws-lambda-powertools/parameters, @aws-lambda-powertools/tracer, @aws-sdk/client-dynamodb, @aws-sdk/client-ec2, @aws-sdk/client-fms, @aws-sdk/client-organizations, @aws-sdk/client-ram, @aws-sdk/client-route53resolver, @aws-sdk/client-s3, @aws-sdk/client-shield, @aws-sdk/client-sns, @aws-sdk/client-sqs, @aws-sdk/client-ssm, @aws-sdk/client-support, @aws-sdk/types, @aws-solutions-constructs/aws-cloudfront-s3, @aws-solutions-constructs/aws-eventbridge-lambda, @types/aws-lambda, @types/jest, @types/node, @types/uuid, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, aws-sdk-client-mock, aws-sdk-client-mock-jest, constructs, csv-writer, eslint, eslint-config-prettier, eslint-plugin-prettier, got, jest, jest-sonar-reporter, prettier, ts-jest, ts-node, typedoc, typedoc-plugin-no-inherit, typescript, uuid
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/services/policyManager/lib/clientHelpers/index.ts, source/services/utilsLayer/lib/index.ts, deployment/cdk-solution-helper/index.ts, source/resources/bin/app.ts

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/automations-for-aws-firewall-manager/blob/main/README.md
- README SHA: c82b9bd5d96dd52132251ad8ff40e4cd2bc4831c
- Manifests: package.json, deployment/cdk-solution-helper/package.json, source/resources/package.json, source/services/complianceGenerator/package.json, source/services/helper/package.json, source/services/policyManager/package.json
- Sampled source files: source/services/policyManager/lib/clientHelpers/index.ts, source/services/utilsLayer/lib/index.ts, deployment/cdk-solution-helper/index.ts, source/resources/bin/app.ts
- Git tree state: captured
- Evidence fingerprint: 5f9f6d35dab8fcaf2436d88cfae0fabdb0cf52def0c2c238bb8f9829301647de

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
