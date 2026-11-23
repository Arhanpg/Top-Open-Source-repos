# awslabs/agent-behavior-validator

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/agent-behavior-validator](https://github.com/awslabs/agent-behavior-validator)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/agent-behavior-validator/blob/main/README.md)
- README blob SHA: bd0f0409dc392f17793b4d42c465c4f738c6684c
- Repository ID: 1352784824
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:31:29+00:00

### Short excerpt (up to 100 words)

> Validate what your AI agents actually **did**, not just what they said. Output-quality evaluation scores the answer. This validates the *process*: which data sources the agent consulted, which steps it executed and in what order, whether it escalated when required, and whether its output carries required evidence. It reads the OpenTelemetry traces your agents already emit — no changes to agent code — and produces audit-ready evidence records for every validated execution. The failure it exists to catch: an agent that answers a question correctly and fluently, with a plausible-looking citation, **without ever consulting the required data source**. That execution

### README headings

- Agent Behavior Validator
- Packages
- Quick look
- claims_contract.yaml
- Framework support
- Support and stability
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 223,266 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- packages/agentic-behavioral-contracts/pyproject.toml (capture: captured) — dependency clues: agentic-otel, boto3, opentelemetry-api, opentelemetry-sdk, pytest, pytest-asyncio, pyyaml, ruff
- packages/agentic-otel/pyproject.toml (capture: captured) — dependency clues: pytest

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-08-31T20:57:45Z
- Last pushed: 2026-08-31T21:52:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/agent-behavior-validator)
- [README](https://github.com/awslabs/agent-behavior-validator/blob/main/README.md)
- [Issues](https://github.com/awslabs/agent-behavior-validator/issues)
- [Releases](https://github.com/awslabs/agent-behavior-validator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
