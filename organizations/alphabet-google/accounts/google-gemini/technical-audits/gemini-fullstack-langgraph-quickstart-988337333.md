# google-gemini/gemini-fullstack-langgraph-quickstart

- Company: Alphabet (Google)
- Account: google-gemini
- Repository: https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:01:36+00:00

## Project purpose

This project demonstrates a fullstack application using a React frontend and a LangGraph-powered backend agent. The agent is designed to perform comprehensive research on a user's query by dynamically generating search terms, querying the web using Google Search, reflecting on the results to identify knowledge gaps, and iteratively refining its search until it can provide a well-supported answer with citations. This application serves as an example of building research-augmented conversational AI using LangGraph and Google's Gemini models.

## Why this project is used

Get started with building Fullstack Agents using Gemini 2.5 and LangGraph

## Core features

- 💬 Fullstack application with a React frontend and LangGraph backend.: 💬 Fullstack application with a React frontend and LangGraph backend.
  - Evidence: README.md#Features
- 🧠 Powered by a LangGraph agent for advanced research and conversational AI.: 🧠 Powered by a LangGraph agent for advanced research and conversational AI.
  - Evidence: README.md#Features
- 🔍 Dynamic search query generation using Google Gemini models.: 🔍 Dynamic search query generation using Google Gemini models.
  - Evidence: README.md#Features
- 🌐 Integrated web research via Google Search API.: 🌐 Integrated web research via Google Search API.
  - Evidence: README.md#Features
- 🤔 Reflective reasoning to identify knowledge gaps and refine searches.: 🤔 Reflective reasoning to identify knowledge gaps and refine searches.
  - Evidence: README.md#Features
- 📄 Generates answers with citations from gathered sources.: 📄 Generates answers with citations from gathered sources.
  - Evidence: README.md#Features
- 🔄 Hot-reloading for both frontend and backend during development.: 🔄 Hot-reloading for both frontend and backend during development.
  - Evidence: README.md#Features

## Technology stack

- Languages: Jupyter Notebook, TypeScript, Python, CSS, Dockerfile, Makefile, JavaScript, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @eslint/js, @langchain/core, @langchain/langgraph-sdk, @radix-ui/react-scroll-area, @radix-ui/react-select, @radix-ui/react-slot, @radix-ui/react-tabs, @radix-ui/react-tooltip, @tailwindcss/vite, @types/node, @types/react, @types/react-dom, @vitejs/plugin-react-swc, class-variance-authority, clsx, eslint, eslint-plugin-react-hooks, eslint-plugin-react-refresh, fastapi, globals, google-genai, langchain, langchain-google-genai, langgraph, langgraph-api, langgraph-cli, langgraph-sdk, lucide-react, python-dotenv, react, react-dom, react-markdown, react-router-dom, tailwind-merge, tailwindcss, tw-animate-css, typescript, typescript-eslint, vite
- Build/package tools: Docker build configuration, npm-compatible manifest, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: backend/src/agent/app.py, backend/src/agent/__init__.py, backend/src/agent/configuration.py, backend/src/agent/graph.py

## Setup and usage

- Gemini Fullstack LangGraph Quickstart: This project demonstrates a fullstack application using a React frontend and a LangGraph-powered backend agent. The agent is designed to perform comprehensive research on a user's query by dynamically generating search terms, querying the web using Google Search, reflecting on the results to identify knowledge gaps, and iteratively refining its sea
- Getting Started: Development and Local Testing: Follow these steps to get the application running locally for development and testing.
- Getting Started: Development and Local Testing: **1. Prerequisites:**
- Getting Started: Development and Local Testing: - Node.js and npm (or yarn/pnpm)
- Getting Started: Development and Local Testing: - **GEMINI_API_KEY**: The backend agent requires a Google Gemini API key.
- Getting Started: Development and Local Testing: 1. Navigate to the backend/ directory.
- Getting Started: Development and Local Testing: 2. Create a file named .env by copying the backend/.env.example file.
- Getting Started: Development and Local Testing: 3. Open the .env file and add your Gemini API key: GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/blob/main/README.md
- README SHA: eef0356b27bb3cf8e9b13e53dff70af587945402
- Manifests: Dockerfile, Makefile, backend/Makefile, backend/pyproject.toml, frontend/package.json
- Sampled source files: backend/src/agent/app.py, backend/src/agent/__init__.py, backend/src/agent/configuration.py, backend/src/agent/graph.py
- Git tree state: captured
- Evidence fingerprint: 49f9fdb8d3f8cbbde72bd87861fe68b86ff4f66f9c351ce7a02f9d5dc49f080b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
