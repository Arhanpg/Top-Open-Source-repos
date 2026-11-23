# WeKnora — LLM Knowledge and Agent Platform

- Company association: Tencent
- Upstream GitHub account: [Tencent](https://github.com/Tencent)
- Repository: [Tencent/WeKnora](https://github.com/Tencent/WeKnora)
- Default branch: main
- README: [Open upstream README](https://github.com/Tencent/WeKnora/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: dd5634e3d9b26576b8fc210820ad94178a4e4398
- Account relationship: The repository is hosted under Tencent's verified primary public GitHub organization.

## Project overview

An open-source knowledge and agent platform that combines document parsing, hybrid retrieval, RAG question-answering, agent reasoning and an automatically generated wiki. Its architecture is modular: document parsing, vectorization and retrieval feed LLM inference, while clients and channels integrate with the application.

## Features and capabilities documented by the README

- Offers quick knowledge-base Q&A with citations and a smart-reasoning ReAct agent that can use web search, MCP tools, skills and a local browser.
- Supports automatically generated and interlinked wiki pages with a knowledge graph, citations, editing, revision history and rollback.
- Provides keyword/vector hybrid search, reranking, parent-child chunking and GraphRAG/knowledge-graph capabilities.
- Supports FAQ, document and wiki knowledge bases; document formats include PDF, Word, PowerPoint, Excel, CSV, TXT, Markdown, HTML, EPUB, MHTML, JSON, XMind and images.
- Integrates multiple LLM vendors, embedding services, vector databases, object stores, data sources and IM channels.
- Includes workspace RBAC, scoped API keys, OIDC, encrypted credentials, observability with Langfuse and task-queue dashboards.
- Provides a built-in MCP server, agent-first CLI, Go SDK, browser extension/local browser integration, and sandbox backends such as Docker, E2B and Cube.

## Technology stack

Go backend (the README's development and validation commands use gofmt, golangci-lint and go test); Vue/TypeScript frontend references in the development guide; PostgreSQL with pgvector/ParadeDB, Redis, optional vector stores such as Elasticsearch, OpenSearch, Milvus, Weaviate and Qdrant; Docker Compose/Kubernetes Helm; LLM and embedding provider integrations; MCP; Langfuse; sandbox runtimes. The README describes a modular component architecture rather than one fixed model/backend stack.

## Getting started

Use the official installation guide to choose Docker Compose, Kubernetes/Helm, Lite single-binary or desktop deployment. For development, the README documents make dev-start, make dev-app and make dev-frontend, with Go/backend and frontend hot-reload workflows. Configure the LLM, embedding, vector-store and object-storage backends for the intended deployment.

## Lifecycle, compatibility and operational considerations

Security warning from the README: WeKnora has login authentication, but production deployments should remain on an internal/private network rather than be exposed directly to the public internet; configure firewalls/access controls and keep the release current. The README's latest release notes list breaking configuration and migration changes; review the version-specific upgrade notes before updating. The Python MCP server is marked deprecated in favour of the built-in MCP server.

## Evaluation guidance

Check the exact upstream release, source manifests, platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a complete source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/Tencent/WeKnora)
- [README](https://github.com/Tencent/WeKnora/blob/main/README.md)
- [Issues](https://github.com/Tencent/WeKnora/issues)
- [Releases](https://github.com/Tencent/WeKnora/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Technical claims are limited to README-supported material; details not established by the README are left unspecified.
