# amazon-connect/ai-agents-lab-amazon-connect

- Company: Amazon
- Account: amazon-connect
- Repository: https://github.com/amazon-connect/ai-agents-lab-amazon-connect
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:03:24+00:00

## Project purpose

A browser-based tool for inspecting Amazon Connect AI agent execution traces, testing agents at scale, and evaluating response quality. No backend — the React SPA calls AWS APIs directly using temporary credentials obtained via IAM Identity Center OIDC.

## Why this project is used

A browser-based tool for inspecting Amazon Connect AI agent execution traces, testing agents at scale, and evaluating response quality. No backend — the React SPA calls AWS APIs directly using temporary credentials obtained via IAM Identity Center OIDC.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Shell, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-sdk/client-bedrock-runtime, @aws-sdk/client-connect, @aws-sdk/client-connectparticipant, @aws-sdk/client-iam, @aws-sdk/client-lex-models-v2, @aws-sdk/client-polly, @aws-sdk/client-qconnect, @aws-sdk/client-s3, @aws-sdk/client-sso, @aws-sdk/client-sso-oidc, @aws-sdk/client-sts, @aws-sdk/credential-providers, @cloudscape-design/code-view, @cloudscape-design/components, @cloudscape-design/design-tokens, @cloudscape-design/global-styles, @playwright/test, @testing-library/jest-dom, @testing-library/react, @types/jest, @types/node, @types/react, @types/react-dom, @vitejs/plugin-react-swc, amazon-chime-sdk-js, aws-cdk-lib, constructs, fast-check, jest, jsdom, react, react-dom, react-router-dom, ts-jest, ts-node, typescript, vite, vitest, yaml
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/contextual-help/index.ts, src/waterfall/index.ts, infra/bin/app.ts, infra/lib/infra-stack.ts

## Setup and usage

- Quick Start (full deploy): ./scripts/deploy.sh all -c identityCenterStartUrl=https://d-XXXXXXXXXX.awsapps.com/start
- Quick Start (full deploy): 1. Installs all dependencies (app + CDK infra)
- Quick Start (full deploy): 2. Bootstraps CDK if needed
- Quick Start (full deploy): 3. Deploys infrastructure (OIDC client registration via Lambda)
- Quick Start (full deploy): 4. Populates .env with stack outputs
- Quick Start (full deploy): After deployment, run npm run dev to start the app locally at http://127.0.0.1:5173.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/amazon-connect/ai-agents-lab-amazon-connect/blob/main/README.md
- README SHA: c54b9843c778b2e787d95d62870ac89109bc6d8b
- Manifests: package.json, infra/package.json
- Sampled source files: src/contextual-help/index.ts, src/waterfall/index.ts, infra/bin/app.ts, infra/lib/infra-stack.ts
- Git tree state: captured
- Evidence fingerprint: 5e9b86e1421624bf95f981d9b47c02f5a9e6c6e5fee78587f5a5dafd4160659f

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
