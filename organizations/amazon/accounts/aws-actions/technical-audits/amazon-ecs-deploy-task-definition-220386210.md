# aws-actions/amazon-ecs-deploy-task-definition

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/amazon-ecs-deploy-task-definition
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:12:20+00:00

## Project purpose

Registers an Amazon ECS task definition and deploys it to an ECS service.

## Why this project is used

Registers an Amazon ECS task definition and deploys it to an ECS service.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @aws-sdk/client-codedeploy, @aws-sdk/client-ecs, @eslint/js, @vercel/ncc, eslint, globals, jest, yaml
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: index.js, index.test.js

## Setup and usage

- Usage: - name: Deploy to Amazon ECS
- Usage: uses: aws-actions/amazon-ecs-deploy-task-definition@v2
- Usage: task-definition: task-definition.json
- Usage: wait-for-service-stability: true
- Usage: See action.yml for the full documentation for this action's inputs and outputs.
- Usage: In most cases when running a one-off task, subnet ID's, subnet groups, and assign public IP will be required.
- Usage: Assign public IP will only be applied when a subnet or security group is defined.

## Limitations and caveats

- Security Disclosures: If you would like to report a potential security issue in this project, please do not create a GitHub issue. Instead, please follow the instructions here or email AWS security directly.

## Evidence and provenance

- README: https://github.com/aws-actions/amazon-ecs-deploy-task-definition/blob/master/README.md
- README SHA: 5b45ca995f891b03bd72944ff4d607e13d9247a5
- Manifests: package.json
- Sampled source files: index.js, index.test.js
- Git tree state: captured
- Evidence fingerprint: ba5ea6b0ac9a89283c1460574ae0b081a06fbe2b69eb4c96bf73e96fea514913

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
