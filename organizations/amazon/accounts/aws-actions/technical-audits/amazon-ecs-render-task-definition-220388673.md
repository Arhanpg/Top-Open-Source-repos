# aws-actions/amazon-ecs-render-task-definition

- Company: Amazon
- Account: aws-actions
- Repository: https://github.com/aws-actions/amazon-ecs-render-task-definition
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:20:41+00:00

## Project purpose

Inserts a container image URI into an Amazon ECS task definition JSON file, creating a new task definition file.

## Why this project is used

Inserts a container image URI into an Amazon ECS task definition JSON file.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @actions/core, @aws-sdk/client-ecs, @vercel/ncc, eslint, jest, tmp
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: index.js, index.test.js

## Setup and usage

- Usage: If task definition file is provided that has precedence over any other option to fetch task definition.
- Usage: If both task definition file and task definition arn are provided, a warning that both have been provided will be returned and the task definition file will be used.
- Usage: If neither of task definition file, task definition arn, and task definition family are provided, an error will be thrown. (At least one option needs to be provided)
- Usage: To insert the image URI amazon/amazon-ecs-sample:latest as the image for the web container in the task definition file, and then deploy the edited task definition file to ECS:
- Usage: - name: Render Amazon ECS task definition
- Usage: id: render-web-container
- Usage: uses: aws-actions/amazon-ecs-render-task-definition@v1
- Usage: task-definition: task-definition.json

## Limitations and caveats

- Security Disclosures: If you would like to report a potential security issue in this project, please do not create a GitHub issue. Instead, please follow the instructions here or email AWS security directly.

## Evidence and provenance

- README: https://github.com/aws-actions/amazon-ecs-render-task-definition/blob/master/README.md
- README SHA: f3642287c39fdfd1db16e5ffa4f9ff902364a11c
- Manifests: package.json
- Sampled source files: index.js, index.test.js
- Git tree state: captured
- Evidence fingerprint: 750a9f3ad785a79bdc8cee2d075d0b0e470efe7ab174fc6caed7a36b7e2552de

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
