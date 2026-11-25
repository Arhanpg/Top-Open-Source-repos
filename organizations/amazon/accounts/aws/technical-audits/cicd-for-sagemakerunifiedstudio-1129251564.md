# aws/CICD-for-SageMakerUnifiedStudio

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/CICD-for-SageMakerUnifiedStudio
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:45:08+00:00

## Project purpose

> **[IAM + IdC Domains]** This CLI supports both IAM-based and IAM Identity Center (IdC)-based SMUS domains. For IdC domains, additional setup (VPC networking, Lake Formation permissions, inline IAM policies) may be required — see the setup scripts in each example directory.

## Why this project is used

> **[IAM + IdC Domains]** This CLI supports both IAM-based and IAM Identity Center (IdC)-based SMUS domains. For IdC domains, additional setup (VPC networking, Lake Formation permissions, inline IAM policies) may be required — see the setup scripts in each example directory.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: PyYAML, absl-py, aiobotocore, aiohappyeyeballs, aiohttp, aioitertools, aiosignal, aiosqlite, alembic, altair, annotated-doc, annotated-types, antlr4-python3-runtime, anyio, asn1crypto, asttokens, astunparse, attrs, autopep8, aws-embedded-metrics, aws-requests-auth, awswrangler, banks, beautifulsoup4, bedrock-agentcore, bedrock-agentcore-starter-toolkit, black, blinker, bokeh, boto3, botocore, cachetools, certifi, cffi, chardet, charset-normalizer, click, cloudpickle, colorama, comm, contourpy, cryptography, cycler, databricks-sdk, dataclasses-json, datasets, debugpy, decorator, deprecated, dill, dirtyjson, distro, docker, docstring-parser, docstring-to-markdown, duckdb, executing, fastapi, filelock, filetype, flask, flask-cors, flatbuffers, fonttools, frozenlist, fsspec, gast, gitdb, gitpython, google-api-core, google-auth, google-cloud-bigquery, google-cloud-core, google-crc32c, google-pasta, google-resumable-media, googleapis-common-protos, graphene, graphql-core, graphql-relay, greenlet, griffe, grpcio, grpcio-status, gunicorn, h11, h5py, hf-xet, httpcore, httpx, httpx-sse, huggingface-hub, ibis, idna, importlib-metadata, ipykernel, ipython, ipython-pygments-lexers, itsdangerous, jedi, jinja2, jsonschema, moto, opensearch-py, pydantic, pytest, pytest-cov, pytest-mock, pyyaml, requests, retrying, rich, termcolor, typer
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/smus_cicd/cli.py, src/smus_cicd/mcp/__main__.py, src/smus_cicd/mcp/server.py, src/smus_cicd/__init__.py

## Setup and usage

- Quick Start: pip install aws-smus-cicd-cli
- Quick Start: **Deploy your first application:**
- Getting Started: - **Quick Start Guide** - Deploy your first application (10 min)
- Getting Started: - **Admin Guide** - Set up infrastructure (15 min)
- Getting Started: - **Generate a Manifest with AI** - Agent skill that scans your project and generates a manifest

## Limitations and caveats

- Security Notice: Always install from the official AWS PyPI package or source code.

## Evidence and provenance

- README: https://github.com/aws/CICD-for-SageMakerUnifiedStudio/blob/main/README.md
- README SHA: cc8792ff7ddfa725bd94d83e098e18de12a82515
- Manifests: pyproject.toml, requirements.txt, setup.py, tests/requirements.txt, examples/analytic-workflow/data-notebooks/notebooks/requirements.txt, examples/analytic-workflow/genai/job-code/requirements.txt
- Sampled source files: src/smus_cicd/cli.py, src/smus_cicd/mcp/__main__.py, src/smus_cicd/mcp/server.py, src/smus_cicd/__init__.py
- Git tree state: captured
- Evidence fingerprint: f751b9b368383fa62b574cf4cb3a818c5e1f41be9a8ddcc97f30eb5f3c730046

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
