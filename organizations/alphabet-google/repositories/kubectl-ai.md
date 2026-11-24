# kubectl-ai — LLM-Powered Kubernetes Assistant

- Company association: Alphabet / Google
- Upstream GitHub account: [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Repository: [GoogleCloudPlatform/kubectl-ai](https://github.com/GoogleCloudPlatform/kubectl-ai)
- Default branch: `main`
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/kubectl-ai/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: `fd46f3ce534b8bcd49b08e36b50f390113c69629`
- Account relationship: The repository is hosted under the separately inventoried GoogleCloudPlatform account, which Google Cloud documentation links for its cloud samples.

## Project overview

A command-line assistant that translates natural-language intent into Kubernetes operations. It can inspect and act on clusters through Kubernetes tooling, while allowing different hosted and local LLM providers.

## Features and capabilities documented by the README

- Supports interactive chat, one-shot prompts, standard input, and optional saved sessions that can be resumed or deleted.
- Documents provider support for Gemini, Vertex AI, Azure OpenAI, OpenAI, Grok, AWS Bedrock and local Ollama/llama.cpp endpoints.
- Includes built-in kubectl and bash tools and supports custom tool definitions.
- Provides MCP client mode for connecting external MCP servers and MCP server mode for exposing Kubernetes tools to other MCP clients.
- Supports terminal and web UI modes, Docker execution and kubectl plugin invocation as kubectl ai.
- Offers configurable model/provider settings, iteration limits, Kubernetes kubeconfig location, tool configuration, prompt templates and tracing.
- Documents a permission setting that defaults to requiring confirmation for resource-modifying commands.

## Technology stack

Go CLI (the repository README includes a Go Report Card); Kubernetes kubectl; configurable LLM providers; local model support via Ollama and llama.cpp; MCP client/server; Docker; YAML configuration and custom tool definitions.

## Getting started

Install kubectl and configure the intended kubeconfig first. The README documents Linux/macOS installation, manual release installation on Windows, Krew and NixOS options. Then configure the LLM provider and run an interactive prompt or a one-shot command. Review the model, tools and permissions configuration before using it with a cluster.

## Lifecycle, compatibility and operational considerations

**Operational caution:** kubectl-ai can invoke kubectl and bash, so prompts may lead to cluster-changing operations. Keep its permission confirmation enabled (the README shows skipPermissions=false by default), use a least-privilege kubeconfig, and test with a non-production namespace before allowing resource modifications. MCP/custom tools extend the available action surface. README model identifiers are examples and should be checked against each provider's current model catalogue.

## Evaluation guidance

Check the exact upstream release/branch, environment prerequisites, licence and security guidance before adopting the project. For archived or superseded repositories, follow the stated successor path. This dossier summarizes the inspected README and repository metadata; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/GoogleCloudPlatform/kubectl-ai)
- [README](https://github.com/GoogleCloudPlatform/kubectl-ai/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/kubectl-ai/issues)
- [Releases](https://github.com/GoogleCloudPlatform/kubectl-ai/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Lifecycle statements are cross-checked against the current repository metadata where noted.
