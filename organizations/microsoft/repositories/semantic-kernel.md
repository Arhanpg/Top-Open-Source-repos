# Semantic Kernel

<sub>Company: Microsoft · Repository: [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

Semantic Kernel is a model-agnostic SDK for building, orchestrating and deploying AI agents and multi-agent systems. Its README presents it as a framework for connecting model services to application code, tools, plugins, memory and workflow logic.

**Important lifecycle context:** the README prominently states that Semantic Kernel is now succeeded by [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). The successor is described as the enterprise-ready direction, with version 1.0, stable APIs and long-term-support commitments. Teams beginning a new implementation should evaluate the successor and the official migration guide before selecting this repository.

## Core abstractions and features

### Model-provider flexibility

The README lists built-in connections to services and model ecosystems including OpenAI, Azure OpenAI, Hugging Face and NVIDIA offerings. It also documents local model paths through Ollama, LM Studio and ONNX.

### Modular agents

Developers can define agents with instructions and access to tools or plugins. The README's Python example creates a chat-completion agent, provides instructions and invokes it with a user message.

### Plugin and tool integration

The plugin system can expose native code functions, prompt templates, OpenAPI specifications and Model Context Protocol (MCP) capabilities. This allows application logic to be represented as callable tools that an agent can use.

### Multi-agent orchestration

The README includes examples of multiple specialist agents, such as billing and refund agents, coordinated by a triage agent. The pattern separates domain responsibilities and gives a coordinating agent the ability to route a request to the appropriate specialist.

### Structured outputs and vector search

The README demonstrates structured output using a typed model and lists integrations with vector databases and search systems, including Azure AI Search, Elasticsearch and Chroma.

### Multimodal and process workflows

Text, vision and audio input are mentioned, along with a process framework for modelling complex business workflows. The README also emphasizes enterprise-oriented concerns such as observability, security and stable APIs.

## Technology profile

| Area | README-supported details |
|---|---|
| SDK / framework | Semantic Kernel |
| Python | Python 3.11–3.14 listed in the README |
| .NET | .NET 10.0+ listed in the README |
| Java | JDK 17+ listed in the README |
| Operating systems | Windows, macOS and Linux |
| AI services | OpenAI, Azure OpenAI, Hugging Face, NVIDIA and more |
| Local inference integrations | Ollama, LM Studio and ONNX |
| Extension points | Native functions, prompt templates, OpenAPI and MCP |
| Retrieval / vector integrations | Azure AI Search, Elasticsearch, Chroma and more |

The README lists these system requirements and integrations; verify current version-specific support in the official docs before starting a new implementation.

## Installation examples

The README provides separate package installation paths.

Python:

```bash
pip install semantic-kernel
```

.NET:

```bash
dotnet add package Microsoft.SemanticKernel
dotnet add package Microsoft.SemanticKernel.Agents.Core
```

The README links a separate Java build guide. Model-service credentials are configured through environment variables in its examples.

## Typical application patterns

- A single assistant that calls a configured model service.
- A tool-using agent that invokes application functions.
- Multi-agent routing where a triage agent delegates to specialist agents.
- Retrieval-assisted assistants connected to vector stores or search services.
- Structured business workflows whose steps are represented as a process.

These are patterns demonstrated or explicitly listed by the README, not a guarantee of autonomous correctness. Tool permissions, model behaviour and business rules must be controlled by the integrating application.

## Migration and lifecycle guidance

The repository README identifies Microsoft Agent Framework as the successor and links a [Semantic Kernel migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel). Before adopting Semantic Kernel in a new product, compare the successor's APIs and migration path. Existing systems should inventory their language binding, connectors, plugins, prompts and agent orchestration before migrating.

## Upstream references

- [Repository](https://github.com/microsoft/semantic-kernel)
- [Primary README](https://github.com/microsoft/semantic-kernel/blob/main/README.md)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [Migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel)
- [Java build guide](https://github.com/microsoft/semantic-kernel-java/blob/main/BUILD.md)

**Evidence note:** README blob inspected: `03d3bd61c758c5d3fbdc83dd36bc317bb7c63d9f`.
