# amazon-archives/amazon-quicksight-embedding-sample

- Company: Amazon
- Account: amazon-archives
- Repository: https://github.com/amazon-archives/amazon-quicksight-embedding-sample
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:43:37+00:00

## Project purpose

Thank you for using Amazon QuickSight. We have put together a sample for embedding dashboards in your apps running on a web browser. As the embedding API currently does not support CORS, we have provided an example of a lambda based setup, which enables you to invoke the embedding API from your web app.

## Why this project is used

A QuickSight dashboard embedding sample for web apps.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: HTML, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: amazon-cognito-identity-js, aws-sdk, node-fetch
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: OpenIdAuthentication/lambda/index.js, QuickSightAuthentication/lambda/index.js, OpenIdAuthentication/web/amazon-cognito-identity.min.js

## Setup and usage

- Usage: Before you can embed an Amazon QuickSight dashboard, you need to publish it and ensure that users are granted necessary permissions. For more information, see Embedding Amazon QuickSight Dashboards in the Amazon QuickSight User Guide.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-archives/amazon-quicksight-embedding-sample/blob/master/README.md
- README SHA: 889a783029d6038fa6db21d4bd23c8137044527e
- Manifests: OpenIdAuthentication/lambda/package.json, QuickSightAuthentication/lambda/package.json
- Sampled source files: OpenIdAuthentication/lambda/index.js, QuickSightAuthentication/lambda/index.js, OpenIdAuthentication/web/amazon-cognito-identity.min.js
- Git tree state: captured
- Evidence fingerprint: b06a3588247ae6b4c576933ee296be37dea2af54f6fc5a42536dd663389ba40d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
