# aws-actions/amazon-ecs-deploy-express-service

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/amazon-ecs-deploy-express-service
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:03:56+00:00

## Project purpose

Deploys an Amazon ECS Express Mode service. ECS Express Mode is a simplified deployment model that automatically provisions and manages the underlying infrastructure (Application Load Balancer, target groups, security groups, etc.) for your containerized applications.

## Why this project is used

Deploys an ECS Express Mode Service

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @aws-sdk/client-ecs, @eslint/js, @vercel/ncc, eslint, jest
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: index.js, index.test.js

## Setup and usage

- Basic Tag Usage: - When used, tags are added onto the ECS Service and all resources created during the CreateExpressGatewayService operation.
- Basic Tag Usage: - Any new resources created upon update inherit these tags from the ECS Service.
- Basic Tag Usage: - name: Deploy with tags (JSON format)
- Basic Tag Usage: uses: aws-actions/amazon-ecs-deploy-express-service@v1
- Basic Tag Usage: image: 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
- Basic Tag Usage: execution-role-arn: arn:aws:iam::123456789012:role/ecsTaskExecutionRole
- Basic Tag Usage: infrastructure-role-arn: arn:aws:iam::123456789012:role/ecsInfrastructureRole
- Basic Tag Usage: {"key": "Environment", "value": "Production"},

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-actions/amazon-ecs-deploy-express-service/blob/main/README.md
- README SHA: 01f2609df77f3446b7d07eeee794bf5aa9c6ea3b
- Manifests: package.json
- Sampled source files: index.js, index.test.js
- Git tree state: captured
- Evidence fingerprint: 7051bf3e13f921fb960f63bf39fd92731a55235c539c506c1394143ee7c44ce0

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
