# Agents CLI — Skills and CLI for Building Google Cloud Agents

- Company association: Alphabet / Google
- Upstream GitHub account: [google](https://github.com/google)
- Repository: [google/agents-cli](https://github.com/google/agents-cli)
- Default branch: `main`
- README: [Open upstream README](https://github.com/google/agents-cli/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: `2d287f6cc57d33fdbe3fece33e4181b4182418da`
- Account relationship: The repository is hosted under Google's primary public GitHub organization.

## Project overview

A command-line tool and skill suite that equips coding assistants with workflows for building, evaluating, deploying, publishing and observing agents on Google's Gemini platform and Google Cloud. The README emphasizes that Agents CLI is a tool for coding agents, not a coding agent itself.

## Features and capabilities documented by the README

- Installs CLI commands and skills that can be used with Antigravity CLI, Claude Code, Codex and other coding assistants.
- Scaffolds new agent projects and enhances existing ones with deployment or CI/CD capabilities.
- Provides workflows for ADK agent development, tool integration, orchestration and callbacks.
- Runs agent evaluations using datasets, metrics, LLM-as-judge, adaptive rubrics, comparisons and failure-mode analysis.
- Supports deployment to Agent Runtime, Cloud Run and GKE; includes infrastructure and CI/CD setup workflows.
- Provides Gemini publishing/registration and observability skills for Cloud Trace, logging and third-party integrations.
- Can be run standalone from the terminal or invoked by a coding assistant.

## Technology stack

Python 3.11+; uv; Node.js; Google Agent Development Kit (ADK); Gemini platform; Google Cloud Agent Runtime, Cloud Run and GKE; evaluation datasets and metrics; Ruff linting; CLI/skills distribution via PyPI and npx skills.

## Getting started

The README prerequisites are Python 3.11+, uv and Node.js. It documents installation via uvx google-agents-cli setup, after which users can launch a supported coding assistant or run commands such as agents-cli create, eval run, deploy and publish gemini. Local create/run/eval can use an AI Studio API key; cloud deployment requires Google Cloud.

## Lifecycle, compatibility and operational considerations

**Telemetry disclosure:** the README says the CLI emits one usage signal per command by default into the user's own Google Cloud project and sends usage metadata in request headers to Google for analytics. It says logs exclude file contents and command arguments, and documents opt-out through AGENTS_CLI_TELEMETRY=0 or DO_NOT_TRACK=1. Deployment creates resources in the user's own Google Cloud project and the user is responsible for those resources and associated service terms.

## Evaluation guidance

Check the exact upstream release/branch, environment prerequisites, licence and security guidance before adopting the project. For archived or superseded repositories, follow the stated successor path. This dossier summarizes the inspected README and repository metadata; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/google/agents-cli)
- [README](https://github.com/google/agents-cli/blob/main/README.md)
- [Issues](https://github.com/google/agents-cli/issues)
- [Releases](https://github.com/google/agents-cli/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Lifecycle statements are cross-checked against the current repository metadata where noted.
