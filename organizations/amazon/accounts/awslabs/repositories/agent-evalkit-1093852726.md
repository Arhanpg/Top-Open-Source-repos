# awslabs/Agent-EvalKit

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/Agent-EvalKit](https://github.com/awslabs/Agent-EvalKit)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/Agent-EvalKit/blob/main/README.md)
- README blob SHA: 539377d27e12ecc7ab65125cf722c105a5efb6d9
- Repository ID: 1093852726
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AI-driven toolkit that automates evaluation processes for AI agents

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:31:35+00:00

### Short excerpt (up to 100 words)

> - Overview - Requirements - Quick Start - What to Expect - Reference - Acknowledgements **Agent-EvalKit** automates the complex evaluation process for your AI agents. **Key Features:** 1. Create evaluation plan by analyzing agent and user requirements 2. Generate test cases for evaluation 3. Add tracing instrumentation to your agent (Optional) 4. Run your agent and collect execution traces 5. Write and run evaluation code to assess performance 6. Generate report with agent improvement recommendations **System:** Linux/macOS • Python 3.11+ • uv • Git **AI Assistant:** Currently supports Kiro CLI, Claude Code, and Kilo Code. uv tool install evalkit --from

### README headings

- Table of Contents
- Overview
- Requirements
- Quick Start
- 1. Install EvalKit
- Install once and use everywhere
- To upgrade later
- 2. Initialize Evaluation Project
- Create dedicated evaluation project
- Copy your agent folder into the evaluation project
- This ensures reliable path resolution and artifact management throughout the evaluation process
- Start your AI assistant (example shown for Claude Code)
- When prompted, agree to use Context7 MCP for documentation access
- Type /evalkit to see available commands
- Note: For Kilo Code and Kiro CLI, detailed setup instructions will be shown
- in the terminal after running 'evalkit init my-agent-evaluation'
- 3. Evaluate Your Agent
- Example: /evalkit.quick Evaluate my search agent at ./search_agent for final response quality
- This command will guide you through the entire evaluation process
- Example: /evalkit.plan Evaluate my search agent at ./search_agent for final response quality
- Example: /evalkit.data Focus on edge cases
- What to Expect from EvalKit
- What You Do Next
- Reference
- CLI Commands
- EvalKit Commands (Available after `evalkit init`)
- Acknowledgements

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 81,478 |
| Shell | 21,099 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: httpx, platformdirs, readchar, rich, truststore, typer
- examples/qa_agent_evaluation/requirements.txt (capture: captured) — dependency clues: deepeval, litellm, opentelemetry-api, opentelemetry-exporter-otlp, opentelemetry-instrumentation, opentelemetry-sdk, strands-agents, tavily-python, traceloop-sdk
- examples/qa_agent_evaluation/qa_agent/requirements.txt (capture: captured) — dependency clues: strands-agents, tavily-python

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 42
- Forks at capture: 7
- Last updated: 2026-10-27T12:24:27Z
- Last pushed: 2026-03-10T19:58:10Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/Agent-EvalKit)
- [README](https://github.com/awslabs/Agent-EvalKit/blob/main/README.md)
- [Issues](https://github.com/awslabs/Agent-EvalKit/issues)
- [Releases](https://github.com/awslabs/Agent-EvalKit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
