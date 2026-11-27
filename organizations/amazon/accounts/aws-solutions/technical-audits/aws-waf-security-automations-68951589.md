# aws-solutions/aws-waf-security-automations

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/aws-waf-security-automations
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:06:41+00:00

## Project purpose

**Important: Security Automations for AWS WAF will retire in December 2026. Deployments (via CloudFormation or GitHub) will remain operational, but customers will assume responsibility for maintenance and API-related updates post-retirement. Customers can explore using native AWS WAF capabilities including AWS Managed Rules, native rate-based rules, and the AWS WAF Console for intuitive configuration and management. These native capabilities provide superior functionality, better performance, real-time updates, and enhanced security features compared to the solution.**

## Why this project is used

This solution automatically deploys a single web access control list (web ACL) with a set of AWS WAF rules designed to filter common web-based attacks.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, TypeScript, Shell, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @eslint/js, @types/jest, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, aws-cdk-lib, aws-lambda-powertools, aws-xray-sdk, backoff, constructs, cryptography, eslint, globals, jest, jest-sonar-reporter, jinja2, prettier, pyparsing, ts-jest, ts-node, typescript, urllib3
- Build/package tools: npm-compatible manifest, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: source/infrastructure/lib/aws-waf-security-automations-stack.ts, source/infrastructure/lib/components/athenaPartition/athena-partitions-role.ts, source/infrastructure/lib/components/athenaPartition/athena-partitions.ts, source/infrastructure/lib/components/badBot/bad-bot.ts

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/aws-waf-security-automations/blob/main/README.md
- README SHA: 13db3167ac7980f189b702e8cc59bb5542d01f7c
- Manifests: source/custom_resource/pyproject.toml, source/helper/pyproject.toml, source/infrastructure/package.json, source/ip_retention_handler/pyproject.toml, source/log_parser/pyproject.toml, source/metrics/pyproject.toml
- Sampled source files: source/infrastructure/lib/aws-waf-security-automations-stack.ts, source/infrastructure/lib/components/athenaPartition/athena-partitions-role.ts, source/infrastructure/lib/components/athenaPartition/athena-partitions.ts, source/infrastructure/lib/components/badBot/bad-bot.ts
- Git tree state: captured
- Evidence fingerprint: a2a6623ae01149b8402736558b954c1076d05847e6ffd919a975ce475d575eb9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
