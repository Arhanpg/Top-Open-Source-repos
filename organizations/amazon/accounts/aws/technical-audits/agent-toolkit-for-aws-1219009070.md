# aws/agent-toolkit-for-aws

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/agent-toolkit-for-aws
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:52:37+00:00

## Project purpose

Help AI coding agents build, deploy, and manage applications on AWS.

## Why this project is used

Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, TypeScript, Shell, HCL, HTML, JavaScript, Go Template, Java, PowerShell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: annotated-types, anyio, bedrock-agentcore, boto3, botocore, certifi, click, h11, httpcore, httpx, idna, jmespath, langchain-anthropic, langchain-google-genai, langchain-openai, langgraph, marked, pydantic, pydantic-core, python-dateutil, requests, s3transfer, six, starlette, typing-inspection, urllib3, uvicorn, websockets
- Build/package tools: Docker build configuration, npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: plugins/aws-agents/skills/agents-pay/packages/openclaw/src/index.ts, plugins/aws-startup-advisor/fixtures/bma-scan-workloads-mixed/repo/app/main.py, plugins/aws-startup-advisor/skills/render-to-aws/fixtures/render-application/src/app.py, plugins/aws-startup-advisor/fixtures/bma-scan-agents-openai/repo/support/app.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws/agent-toolkit-for-aws/blob/main/README.md
- README SHA: ccd48d4cf8f9a397039a464b728b4045f45f453c
- Manifests: .github/scripts/package.json, plugins/aws-agents/skills/agents-pay/requirements.txt, plugins/aws-startup-advisor/fixtures/bma-scan-agents-independent/repo/requirements.txt, plugins/aws-startup-advisor/fixtures/bma-scan-agents-langgraph/repo/Dockerfile, plugins/aws-startup-advisor/fixtures/bma-scan-agents-langgraph/repo/requirements.txt, plugins/aws-startup-advisor/fixtures/bma-scan-agents-openai/repo/Dockerfile
- Sampled source files: plugins/aws-agents/skills/agents-pay/packages/openclaw/src/index.ts, plugins/aws-startup-advisor/fixtures/bma-scan-workloads-mixed/repo/app/main.py, plugins/aws-startup-advisor/skills/render-to-aws/fixtures/render-application/src/app.py, plugins/aws-startup-advisor/fixtures/bma-scan-agents-openai/repo/support/app.py
- Git tree state: captured
- Evidence fingerprint: 4fbaba0e5edd497c7e7e476d9e29cca3da49cee3d01d4494b2843f7769d39efb

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
