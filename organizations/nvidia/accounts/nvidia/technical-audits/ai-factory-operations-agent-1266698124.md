# NVIDIA/AI-Factory-Operations-Agent

- Company: NVIDIA
- Account: NVIDIA
- Repository: https://github.com/NVIDIA/AI-Factory-Operations-Agent
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:25:06+00:00

## Project purpose

Deploy specialized AI agents to investigate cluster issues and streamline governed AI factory operations.

## Why this project is used

Deploy AI agents to investigate cluster issues and streamline governed AI factory operations.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: TypeScript, JavaScript, Python, Shell, HTML, Go Template
- Frameworks/libraries: Unknown / not established
- Dependency names: myst-parser, nvidia-sphinx-theme, pyyaml, sphinx, sphinx-copybutton
- Build/package tools: npm-compatible manifest, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: helm/mosaic-stack/files/openclaw-seed/extensions/automation-guard/index.ts, helm/mosaic-stack/files/openclaw-seed/extensions/bcm/index.ts, helm/mosaic-stack/files/openclaw-seed/extensions/dcgm/index.ts, helm/mosaic-stack/files/openclaw-seed/extensions/diagnostic-agent/index.ts

## Setup and usage

- Getting Started: The documentation site can be built locally from the guides in this repository. See Building the documentation.
- Getting Started: In the early access stage, the published Helm chart and container images require an early access invitation to the private NGC registry; nvcr.io login alone does not grant pull access. To request access before installing, complete the onboarding form or email ai-factory-operations-agent@nvidia.com. You can also contact your NVIDIA account team.
- Getting Started: Use the complete installation guide for your environment:
- Getting Started: - NVIDIA Mission Control installation
- Getting Started: - Base Command Manager installation without Kubernetes
- Getting Started: - Custom installation and module configuration
- Usage: After installation, forward the AI Factory Operations Agent UI service:
- Usage: kubectl -n aifoa port-forward svc/mosaic-ui 3000:3000

## Limitations and caveats

- Security: - Vulnerability disclosure: SECURITY.md
- Security: - Do not file public issues for security reports.

## Evidence and provenance

- README: https://github.com/NVIDIA/AI-Factory-Operations-Agent/blob/main/README.md
- README SHA: 7df62de00e1aca39f6030c2e4242295f916b0a89
- Manifests: docs/pyproject.toml, helm/mosaic-stack/files/openclaw-seed/extensions/automation-guard/package.json, helm/mosaic-stack/files/openclaw-seed/extensions/bcm/package.json, helm/mosaic-stack/files/openclaw-seed/extensions/dcgm/package.json, helm/mosaic-stack/files/openclaw-seed/extensions/diagnostic-agent/package.json, helm/mosaic-stack/files/openclaw-seed/extensions/grafana/package.json
- Sampled source files: helm/mosaic-stack/files/openclaw-seed/extensions/automation-guard/index.ts, helm/mosaic-stack/files/openclaw-seed/extensions/bcm/index.ts, helm/mosaic-stack/files/openclaw-seed/extensions/dcgm/index.ts, helm/mosaic-stack/files/openclaw-seed/extensions/diagnostic-agent/index.ts
- Git tree state: captured
- Evidence fingerprint: e5111955ae84e110550d63063e57a3a9ba328f500fda8c2e60ec806f835b7321

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
