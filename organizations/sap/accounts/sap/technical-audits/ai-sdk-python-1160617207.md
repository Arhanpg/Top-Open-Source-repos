# SAP/ai-sdk-python

- Company: SAP
- Account: SAP
- Repository: https://github.com/SAP/ai-sdk-python
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:00:16+00:00

## Project purpose

SAP Cloud SDK for AI is the official Software Development Kit (SDK) for SAP AI Core, SAP Generative AI Hub, and Orchestration Service.

## Why this project is used

SAP Cloud SDK for AI is the official Software Development Kit (SDK) for SAP AI Core, SAP Generative AI Hub, and Orchestration Service.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Jupyter Notebook, Makefile, CSS, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: aenum, click, dacite, fastapi, h11, httpx, langchain, langchain-classic, langchain-openai, langcodes, openai, overloading, packaging, pandas, pydantic, pyhumps, requests, sap-ai-sdk-base, sap-ai-sdk-core, sap-ai-sdk-gen, uvicorn
- Build/package tools: Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: packages/core/ai_core_sdk/cli.py, sample-code/sample_code/server.py, packages/core/ai_core_sdk/__init__.py, packages/core/ai_core_sdk/ai_core_v2_client.py

## Setup and usage

- Installation: Install the SDK with support for all model providers:
- Installation: pip install "sap-ai-sdk-gen[all]"
- Installation: Install the default package (OpenAI support):
- Installation: pip install sap-ai-sdk-gen
- Installation: Install selected extras:
- Installation: pip install "sap-ai-sdk-gen[google,amazon]"

## Limitations and caveats

- Security / Disclosure: If you find a potential security issue, please follow the process in Security Policy.
- Security / Disclosure: Please do not create public GitHub issues for security-related reports.

## Evidence and provenance

- README: https://github.com/SAP/ai-sdk-python/blob/main/README.md
- README SHA: 621e8a82a910f228170d0d60525ee5daea877144
- Manifests: Makefile, pyproject.toml, sample-code/pyproject.toml, packages/base/pyproject.toml, packages/core/pyproject.toml, packages/gen/pyproject.toml
- Sampled source files: packages/core/ai_core_sdk/cli.py, sample-code/sample_code/server.py, packages/core/ai_core_sdk/ai_core_v2_client.py
- Git tree state: captured
- Evidence fingerprint: ed956af3baa61e2210b0cc3cbc8cb041b8b99fe44b9538567d024678d78d7ba1

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
