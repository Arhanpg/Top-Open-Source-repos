# awslabs/Legacy-Code-Migration-Pipeline

- Company: Amazon
- Account: awslabs
- Repository: https://github.com/awslabs/Legacy-Code-Migration-Pipeline
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:03:52+00:00

## Project purpose

A comprehensive multi-agent framework for migrating legacy code using a **3-layer orchestration architecture**. This framework provides a standardized approach to analyze, plan, and execute legacy code migrations with AI-powered automation through hierarchical agent coordination.

## Why this project is used

gen ai asisted code migration for legacy systems

## Core features

- **Standardized Project Structure**: Automated project setup with consistent folder organization: **Standardized Project Structure**: Automated project setup with consistent folder organization
  - Evidence: README.md#Migration Capabilities
- **AI-Powered Analysis**: Intelligent source code and database analysis: **AI-Powered Analysis**: Intelligent source code and database analysis
  - Evidence: README.md#Migration Capabilities
- **Workpackage Management**: Structured approach to breaking down migration tasks: **Workpackage Management**: Structured approach to breaking down migration tasks
  - Evidence: README.md#Migration Capabilities
- **Template-Driven Workflows**: Pre-built templates for reports, tracking, and documentation: **Template-Driven Workflows**: Pre-built templates for reports, tracking, and documentation
  - Evidence: README.md#Migration Capabilities
- **Validation Framework**: Built-in deliverable validation and quality assurance: **Validation Framework**: Built-in deliverable validation and quality assurance
  - Evidence: README.md#Migration Capabilities
- **Configuration Management**: Flexible path configuration system: **Configuration Management**: Flexible path configuration system
  - Evidence: README.md#Migration Capabilities
- Installs required dependencies (tmux 3.3+, uv, CAO): Installs required dependencies (tmux 3.3+, uv, CAO)
  - Evidence: README.md#CAO Installation Features
- Validates system prerequisites: Validates system prerequisites
  - Evidence: README.md#CAO Installation Features
- Sets up CAO for use across all projects: Sets up CAO for use across all projects
  - Evidence: README.md#CAO Installation Features
- Discovers and installs all 28 agents from the project's agents directory: Discovers and installs all 28 agents from the project's agents directory
  - Evidence: README.md#CAO Installation Features
- Supports provider selection (Kiro CLI default, Amazon Q CLI, Claude Code): Supports provider selection (Kiro CLI default, Amazon Q CLI, Claude Code)
  - Evidence: README.md#CAO Installation Features
- Can be run at any time to install or update agents: Can be run at any time to install or update agents
  - Evidence: README.md#CAO Installation Features
- Provides organized agent listing with team structure visibility: Provides organized agent listing with team structure visibility
  - Evidence: README.md#CAO Installation Features
- Supports multiple agent installation sources (built-in, local files, URLs): Supports multiple agent installation sources (built-in, local files, URLs)
  - Evidence: README.md#CAO Installation Features
- Shows command preview before execution for transparency: Shows command preview before execution for transparency
  - Evidence: README.md#CAO Installation Features

## Technology stack

- Languages: Python, JavaScript, CSS, HTML, Shell, REXX, JCL
- Frameworks/libraries: Unknown / not established
- Dependency names: Flask, PyYAML, Werkzeug, beautifulsoup4, black, flake8, html2text, hypothesis, lxml, markdownify, mypy, pytest, pytest-cov, pytest-mock, pyyaml, requests, responses, setuptools, wheel
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: structure/tools/framework-tools/tools/database_analyzer/__main__.py, structure/tools/framework-tools/tools/database_analyzer/cli.py, structure/tools/framework-tools/tools/legacy_analyzer/__main__.py, structure/tools/framework-tools/tools/legacy_analyzer/cli.py

## Setup and usage

- One-Command Installation: For the fastest setup, use the all-in-one installation script:
- One-Command Installation: ./install_all.sh my_migration_project
- One-Command Installation: This single command will:
- One-Command Installation: 1. Install CAO and its dependencies
- One-Command Installation: 2. Create your project structure
- One-Command Installation: 3. Install all 28 agents
- Manual Step-by-Step Installation: If you prefer more control, follow these steps:
- CAO Installation Features: The installation process is now separated into two parts:

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/awslabs/Legacy-Code-Migration-Pipeline/blob/main/README.md
- README SHA: a83e2edc51cd49101496faaac8d4b37e215a3de4
- Manifests: requirements.txt, structure/web-dashboard/requirements.txt, structure/tools/framework-tools/requirements.txt, structure/tools/framework-tools/setup.py, structure/tools/framework-tools/tools/database_analyzer/requirements.txt, structure/tools/framework-tools/tools/legacy_analyzer/requirements.txt
- Sampled source files: structure/tools/framework-tools/tools/database_analyzer/__main__.py, structure/tools/framework-tools/tools/database_analyzer/cli.py, structure/tools/framework-tools/tools/legacy_analyzer/__main__.py, structure/tools/framework-tools/tools/legacy_analyzer/cli.py
- Git tree state: captured
- Evidence fingerprint: cd1fa2d3cf7af442c95fb759190e83042c40cd20e1ec056c6add6d7021b85679

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
