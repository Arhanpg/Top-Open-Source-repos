# AutoGen — archived multi-agent framework

- **Company:** Microsoft
- **GitHub owner:** [microsoft](https://github.com/microsoft)
- **Repository:** [microsoft/autogen](https://github.com/microsoft/autogen)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/microsoft/autogen/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `042b9df197a220ec7072a116d694cd497ec332ad`

## Project overview

AutoGen was a framework for creating multi-agent AI applications that could act autonomously or work alongside humans. The current README labels the project archived and no longer maintained, and directs new users to Microsoft Agent Framework.

## Features and capabilities documented by the README

- README examples demonstrate assistant agents and OpenAI model-client integration.
- Supports tool use, including a documented MCP workbench example using Playwright MCP.
- Demonstrates multi-agent orchestration by wrapping specialist agents as tools for a coordinating agent.
- The README links AutoGen Studio as a no-code GUI for experimenting with agent workflows.
- Provides a Python AgentChat package and extension packages for model and tool integrations.
- Includes migration material for users upgrading from AutoGen v0.2 and a migration path toward Microsoft Agent Framework.

## Technology stack

Python 3.10+; autogen-agentchat; autogen-ext provider/tool extensions; examples use OpenAI-compatible model clients and MCP workbench integration. The README also documents AutoGen Studio.

## Getting started

The README's historical installation example installs autogen-agentchat and autogen-ext[openai]. It states that OpenAI API credentials are required for the illustrated OpenAI quickstart. For new development, follow the linked Microsoft Agent Framework migration guidance instead of beginning a new AutoGen deployment.

## Lifecycle, compatibility and operational notes

The README explicitly says AutoGen is archived and no longer actively maintained; it will receive no bug fixes, security fixes, new features or support. It advises against production use and recommends Microsoft Agent Framework as the enterprise-ready successor. Retain this page for historical/reference purposes and migration planning only.

## Evaluation guidance

Check the current release, upstream documentation, dependency manifests, supported platforms, licence and maintenance policy before adoption. This README-based dossier is not a complete source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/microsoft/autogen)
- [README](https://github.com/microsoft/autogen/blob/main/README.md)
- [Issues](https://github.com/microsoft/autogen/issues)
- [Releases](https://github.com/microsoft/autogen/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology and lifecycle claims are limited to the README evidence; additional manifest and source verification remains separate.*
