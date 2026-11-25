# aws-solutions/amazon-s3-glacier-refreezer

- Company: Amazon
- Account: aws-solutions
- Repository: https://github.com/aws-solutions/amazon-s3-glacier-refreezer
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:05:17+00:00

## Project purpose

> [!WARNING] > In December 2023, the Data Transfer from Amazon S3 Glacier Vaults to Amazon S3 solution replaced this solution. All existing deployments of the Amazon S3 Glacier Re:Freezer solution will continue to work, but we no longer support or maintain this solution. > > The benefits of using the Data Transfer from Amazon S3 Glacier Vaults to Amazon S3 solution include improved performance and enhanced integration with AWS services, especially Amazon S3. We encourage customers to use this solution for future transfers

## Why this project is used

The Amazon S3 Glacier Re:Freezer is a serverless solution that automatically copies entire Amazon S3 Glacier vault archives to a defined destination Amazon Simple Storage Service (Amazon S3 bucket) and S3 storage class.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: JavaScript, TypeScript, Shell, Python
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-cdk/aws-glue-alpha, @types/jest, @types/node, @types/prettier, aws-cdk, aws-cdk-lib, aws-sdk, chai, chai-as-promised, constructs, crypto-js, fs, glob-parent, jest, mocha, moment, prettier, proxyquire, sinon, source-map-support, ts-jest, ts-node, typescript
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: deployment/cdk-solution-helper/index.js, source/lambda/calculateMetrics/index.js, source/lambda/calculateTreehash/index.js, source/lambda/copyChunk/index.js

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-solutions/amazon-s3-glacier-refreezer/blob/main/README.md
- README SHA: 7eb615f8e15ed1a9535217badd37ec863d196248
- Manifests: source/package.json, deployment/cdk-solution-helper/package.json, source/lambda/calculateMetrics/package.json, source/lambda/calculateTreehash/package.json, source/lambda/copyChunk/package.json, source/lambda/copyToDestinationBucket/package.json
- Sampled source files: deployment/cdk-solution-helper/index.js, source/lambda/calculateMetrics/index.js, source/lambda/calculateTreehash/index.js, source/lambda/copyChunk/index.js
- Git tree state: captured
- Evidence fingerprint: 58bea4fc899fe7285bdede99e6bd7b2e4a358abdd603b72377b167e1982b7d3b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
