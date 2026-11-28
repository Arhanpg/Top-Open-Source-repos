# Azure/cluster-api-for-slinky

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/cluster-api-for-slinky](https://github.com/Azure/cluster-api-for-slinky)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/cluster-api-for-slinky/blob/main/README.md)
- README blob SHA: abab4b502a44f21819108a2bfac3ca30850ecf12
- README bytes captured: 18523
- README truncated at capture limit: False
- Repository ID: 962303891
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Kubernetes Cluster API for Slinky

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:19:55+00:00

### Short excerpt (up to 300 words)

> The Cluster API (CAPI) Currently only local clusters The local stack is Install the following: Do not report security

### README headings

- Cluster API for Slinky
- What is Cluster API for Slinky (CA4S)
- Getting started
- Prerequisites
- Recommended local setup
- From PowerShell on Windows — global WSL2 settings (mirrored networking):
- Inside your WSL2 distro — per-distro settings (enable systemd):
- install native Docker
- Then from PowerShell on Windows, restart the WSL2 VM so both files take effect:
- Reopen the distro; systemd will start dockerd. Re-login to pick up docker group.
- Verify:  wslinfo --networking-mode   # should print: mirrored
- Local Python environment (Pulumi + tests)
- Bringing up the local stack
- CONTEXT=$(pulumi stack output context -s local)
- PKO_INIT_STACK=$(pulumi stack output pko_init_stack -s local)
- kubectl --context "$CONTEXT" -n pulumi-kubernetes-operator get stack "$PKO_INIT_STACK" -w
- REGISTRY_PORT=$(pulumi stack output registry_port -s local)
- kubectl cluster-info --context "$CONTEXT"
- echo "local registry at localhost:${REGISTRY_PORT}"
- pulumi stack output gitops_url -s local
- pulumi stack output gitops_url_external -s local
- pulumi stack output pko_flux_source_name -s local
- request="manual-$(date +%s)"
- kubectl --context "$CONTEXT" -n pulumi-kubernetes-operator annotate gitrepository gitops-source \
- reconcile.fluxcd.io/requestedAt="$request" --overwrite
- kubectl --context "$CONTEXT" -n pulumi-kubernetes-operator wait gitrepository/gitops-source \
- --for=jsonpath='{.status.lastHandledReconcileAt}'="$request" --timeout=180s
- request="manual-$(date +%s)"
- kubectl --context "$CONTEXT" -n pulumi-kubernetes-operator annotate stack "$PKO_INIT_STACK" \
- pulumi.com/reconciliation-request="$request" --overwrite

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: What is Cluster API for Slinky (CA4S)

> The Cluster API (CAPI)

### Getting started and usage: Getting started

> Currently only local clusters

### Architecture and design: Components

> The local stack is

### Technology and requirements: Prerequisites

> Install the following:

### Limitations and security: Security

> Do not report security

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 926,340 |
| Shell | 343 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: azure-containerregistry, azure-identity, azure-mgmt-core, cryptography, oras, pulumi, pulumi-azure-native, pulumi-kubernetes, pulumi-random, pydantic, pytest, pytest-mock, requests, responses, tomli-w
- pulumi/pyproject.toml (capture: captured)
- pulumi/sdks/awx/pyproject.toml (capture: captured) — dependency clues: parver, pulumi, semver, typing-extensions
- pulumi/sdks/capi-core/pyproject.toml (capture: captured) — dependency clues: parver, pulumi, pulumi-kubernetes, requests, semver, typing-extensions
- pulumi/sdks/flux/pyproject.toml (capture: captured) — dependency clues: parver, pulumi, pulumi-kubernetes, requests, semver, typing-extensions
- pulumi/sdks/gitea/pyproject.toml (capture: captured) — dependency clues: parver, pulumi, semver, typing-extensions

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 1
- Forks at capture: 0
- Last updated: 2026-09-24T20:47:39Z
- Last pushed: 2026-10-28T23:55:51Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/cluster-api-for-slinky)
- [README](https://github.com/Azure/cluster-api-for-slinky/blob/main/README.md)
- [Issues](https://github.com/Azure/cluster-api-for-slinky/issues)
- [Releases](https://github.com/Azure/cluster-api-for-slinky/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
