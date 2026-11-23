# awslabs/agent-evaluation

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/agent-evaluation](https://github.com/awslabs/agent-evaluation)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/agent-evaluation/blob/main/README.md)
- README blob SHA: 48683938cddf6dad762059691cb1c6db3c6a5326
- Repository ID: 774582281
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A generative AI-powered framework for testing virtual agents.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:31:38+00:00

### Short excerpt (up to 100 words)

> Agent Evaluation is a generative AI-powered framework for testing virtual agents. Internally, Agent Evaluation implements an LLM agent (evaluator) that will orchestrate conversations with your own agent (target) and evaluate the responses during the conversation. - Built-in support for popular AWS services including Amazon Bedrock, Amazon Q Business, and Amazon SageMaker. You can also bring your own agent to test using Agent Evaluation. - Orchestrate concurrent, multi-turn conversations with your agent while evaluating its responses. - Define hooks to perform additional tasks such as integration testing. - Can be incorporated into CI/CD pipelines to expedite the time to delivery while

### README headings

- Agent Evaluation
- ✨ Key features
- 📚 Documentation
- 👏 Contributors

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 113,635 |
| Jinja | 4,438 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- requirements.txt (capture: captured) — dependency clues: boto3, click, jinja2, jsonpath-ng, pydantic, pyyaml, rich
- setup.py (capture: captured)
- samples/aws_step_functions_deployment/requirements.txt (capture: captured) — dependency clues: aws-cdk-lib, constructs, pathlib
- samples/streamlit_app/requirements.txt (capture: captured) — dependency clues: Faker, GitPython, Jinja2, Markdown, MarkupSafe, PyYAML, Pygments, SQLAlchemy, agent-evaluation, altair, annotated-types, attrs, beautifulsoup4, blinker, boto3, botocore, cachetools, certifi, charset-normalizer, click
- samples/aws_step_functions_deployment/layers/agent-evaluation/requirements.txt (capture: captured) — dependency clues: agent-evaluation

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 377
- Forks at capture: 51
- Last updated: 2026-11-18T09:49:19Z
- Last pushed: 2025-12-15T18:10:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/agent-evaluation)
- [README](https://github.com/awslabs/agent-evaluation/blob/main/README.md)
- [Issues](https://github.com/awslabs/agent-evaluation/issues)
- [Releases](https://github.com/awslabs/agent-evaluation/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
