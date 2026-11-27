# aws/agentcore-cli

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/agentcore-cli
- Default branch: v1.x
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T06:58:25+00:00

## Project purpose

agentcore is a command-line tool and interactive terminal UI (TUI) for **Amazon Bedrock AgentCore**, the platform for building and running production AI agents (documentation).

## Why this project is used

The terminal experience for AgentCore!

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, Python, JavaScript, Dockerfile, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: @aws-cdk/cloudformation-diff, @aws-cdk/toolkit-lib, @aws-sdk/client-application-signals, @aws-sdk/client-bedrock-agent, @aws-sdk/client-bedrock-agentcore, @aws-sdk/client-bedrock-agentcore-control, @aws-sdk/client-cloudformation, @aws-sdk/client-cloudwatch-logs, @aws-sdk/client-iam, @aws-sdk/client-s3, @aws-sdk/client-sts, @aws-sdk/client-xray, @aws-sdk/util-endpoints, @aws/agent-inspector, @aws/agentcore-cdk, @napi-rs/keyring, @opentelemetry/api, @opentelemetry/exporter-metrics-otlp-http, @opentelemetry/otlp-transformer, @opentelemetry/resources, @opentelemetry/sdk-metrics, @secretlint/secretlint-rule-preset-recommend, @smithy/core, @tanstack/react-query, @types/bun, @types/cross-spawn, @types/node, @types/react, @types/semver, @types/ws, aws-cdk, aws-cdk-lib, bedrock-agentcore, cli-truncate, commander, constructs, cross-spawn, handlebars, husky, ink, ink-scroll-view, ink-testing-library, lint-staged, lodash, oxlint, prettier, react, react-devtools-core, react-router, secretlint, semver, smol-toml, string-width, terminal-size, typescript, vitest, winston, winston-daily-rotate-file, ws, yaml, zod
- Build/package tools: Docker build configuration, npm-compatible manifest, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/assets/templates/a2a-python-strands/main.py, src/assets/templates/agent-python-langchain/main.py, src/assets/templates/agent-python-minimal/main.py, src/assets/templates/agent-python-strands/main.py

## Setup and usage

- Installation: You need Node.js 20.12 or later and AWS credentials configured as for the AWS CLI. Python templates
- Installation: npm install -g @aws/agentcore
- Installation: If the Python-based Bedrock AgentCore Starter Toolkit is installed, uninstall it: both provide an
- Quick Start: A project holds either kind of agent, or both:
- Quick Start: - A **Harness** is a managed agent you configure in YAML — model, system prompt, tools, skills — and
- Quick Start: AgentCore runs for you.
- Quick Start: - A **Runtime** is agent code you own, scaffolded from a template and deployed for you.
- Quick Start: Create a project, add a Harness to it, deploy it, and send a prompt:

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws/agentcore-cli/blob/v1.x/README.md
- README SHA: 59aaa8eb450144fadec78c4092f464c976ee2304
- Manifests: Makefile, package.json, .github/harness/Dockerfile, src/assets/cdk/package.json, src/assets/evaluators/python-lambda/pyproject.toml, src/assets/templates/a2a-python-strands/pyproject.toml
- Sampled source files: src/assets/templates/a2a-python-strands/main.py, src/assets/templates/agent-python-langchain/main.py, src/assets/templates/agent-python-minimal/main.py, src/assets/templates/agent-python-strands/main.py
- Git tree state: captured
- Evidence fingerprint: 2700d352b67acb5c8027ead675628e774c5b019bce0ed59b764a4d1e7d98466e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
