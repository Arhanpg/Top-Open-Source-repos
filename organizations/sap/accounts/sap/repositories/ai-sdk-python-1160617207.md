# SAP/ai-sdk-python

- Company: SAP
- GitHub account: [https://github.com/SAP](https://github.com/SAP)
- Mapping status: verified
- Repository: [SAP/ai-sdk-python](https://github.com/SAP/ai-sdk-python)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP/ai-sdk-python/blob/main/README.md)
- README blob SHA: 7dbcfcbdbb697d001f703534b6a63c72eeaba487
- Repository ID: 1160617207
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

SAP Cloud SDK for AI is the official Software Development Kit (SDK) for SAP AI Core, SAP Generative AI Hub, and Orchestration Service.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:42:04+00:00

### Short excerpt (up to 100 words)

> SAP Cloud SDK for AI is the official Software Development Kit (SDK) for SAP AI Core, SAP Generative AI Hub, and Orchestration Service. The SDK formerly known as generative AI Hub SDK was rebranded. Install the SDK with support for all model providers: pip install "sap-ai-sdk-gen[all]" Install the default package (OpenAI support): pip install sap-ai-sdk-gen Install selected extras: pip install "sap-ai-sdk-gen[google,amazon]" For detailed configuration and usage examples, see README_sphynx.md. Main SDK modules are under gen_ai_hub. Integration tests are split into two groups: 1. Standard integration tests. 2. Bedrock integration tests marked with the pytest marker bedrock. Run tests with: pytest

### README headings

- SAP Cloud SDK for AI (Python)
- Installation
- Development
- Documentation
- Support, Feedback, Contributing
- Security / Disclosure
- Code of Conduct
- Licensing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,862,001 |
| Jupyter Notebook | 273,264 |
| Makefile | 3,163 |
| CSS | 2,585 |
| Shell | 86 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- pyproject.toml (capture: captured)
- sample-code/pyproject.toml (capture: captured) — dependency clues: fastapi, sap-ai-sdk-gen, uvicorn
- packages/base/pyproject.toml (capture: captured) — dependency clues: aenum, pyhumps, requests
- packages/core/pyproject.toml (capture: captured) — dependency clues: click, sap-ai-sdk-base
- packages/gen/pyproject.toml (capture: captured) — dependency clues: aiobotocore, boto3, click, dacite, google-genai, h11, httpx, langchain, langchain-aws, langchain-classic, langchain-google-genai, langchain-openai, langcodes, openai, overloading, packaging, pandas, pydantic, sap-ai-sdk-core, sap-ai-sdk-gen

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 4
- Last updated: 2026-11-06T23:46:45Z
- Last pushed: 2026-11-23T15:52:09Z
- Topics: ai, gen-ai, llm, orchestration, python

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP/ai-sdk-python)
- [README](https://github.com/SAP/ai-sdk-python/blob/main/README.md)
- [Issues](https://github.com/SAP/ai-sdk-python/issues)
- [Releases](https://github.com/SAP/ai-sdk-python/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
