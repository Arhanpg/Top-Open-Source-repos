# awslabs/generative-ai-toolkit

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/generative-ai-toolkit](https://github.com/awslabs/generative-ai-toolkit)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/generative-ai-toolkit/blob/main/README.md)
- README blob SHA: 0813807b06d9c7e8dcca0fd2ce66f340858ce997
- README bytes captured: 151851
- README truncated at capture limit: False
- Repository ID: 878156661
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Generative AI Toolkit is a lightweight library for building, testing and evaluating AI agents in Python, using any of the LLMs supported by the Amazon Bedrock Converse API.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T21:44:15+00:00

### Short excerpt (up to 300 words)

> Install generative_ai_toolkit with support The following is a You must make sure

### README headings

- Generative AI Toolkit
- Send a message to the agent and have it stream its response back:
- Assert that the weather_report tool was used (raises an error if not):
- Similar, but using test case with 2 turns:
- Start a new conversation, with empty history:
- Stream traces instead of text chunks:
- (Note: this also yields relevant snapshots of traces that are still underway)
- Trace attributes are OpenTelemetry compatible but preserve fidelity:
- You can also collect metrics, run tests in parallel, compare different model ids
- and other agent parameters against each other, view metrics and traces in a UI,
- add your own tracers, use an LLM mock, expose the agent over HTTP, and much more.
- Screenshots
- Reference Architecture
- Key Terms
- Table of Contents
- 2.1 Installation
- 2.2 Agent implementation
- 2.2.1 Chat with agent
- Response streaming
- 2.2.2 Conversation history
- Persisting conversation history
- Viewing the conversation history
- [{'role': 'user', 'content': [{'text': "What's the capital of France?"}]}, {'role': 'assistant', 'content': [{'text': 'The capital of France is Paris.'}]}, {'role': 'user', 'content': [{'text': 'What are some touristic ...
- Starting a fresh conversation
- Subcontexts
- No subcontext yet
- Set both conversation ID and subcontext ID
- Access the current subcontext ID
- Have a conversation in this subcontext
- Switch to a different subcontext within the same conversation

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: 2.1 Installation

> Install generative_ai_toolkit with support

### Architecture and design: Reference Architecture

> The following is a

### Limitations and security: Security: ensure users access their own conversation history only

> You must make sure

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 704,127 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: boto3, boto3-stubs, flask, generative-ai-toolkit, gradio, gunicorn, ipython, mcp, nltk, opentelemetry-proto, pandas, playwright, pydantic, pytest, pytest-cov, pytest-playwright, ruff, scikit-learn, tabulate
- examples/pydantic_tools/requirements.txt (capture: captured) — dependency clues: generative-ai-toolkit, pydantic, requests
- examples/sample_agent/requirements.txt (capture: captured) — dependency clues: faiss-cpu, pytest, sentence-transformers

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 49
- Forks at capture: 14
- Last updated: 2026-11-01T09:47:55Z
- Last pushed: 2026-04-14T00:44:21Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/generative-ai-toolkit)
- [README](https://github.com/awslabs/generative-ai-toolkit/blob/main/README.md)
- [Issues](https://github.com/awslabs/generative-ai-toolkit/issues)
- [Releases](https://github.com/awslabs/generative-ai-toolkit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
