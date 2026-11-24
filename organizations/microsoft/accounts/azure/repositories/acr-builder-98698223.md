# Azure/acr-builder

- Company: Microsoft
- GitHub account: [https://github.com/Azure](https://github.com/Azure)
- Mapping status: official-project-linked
- Repository: [Azure/acr-builder](https://github.com/Azure/acr-builder)
- Default branch: main
- README: [Open upstream README](https://github.com/Azure/acr-builder/blob/main/README.md)
- README blob SHA: 69d3575b4cfd08eab40444d19ed9ab0abf405976
- Repository ID: 98698223
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Azure Container Registry Build Runner

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:40:44+00:00

### Short excerpt (up to 100 words)

> ACR Builder is the backbone behind Azure Container Registry Tasks. It can be used to automate container image patching and execute arbitrary containers for complex workflows. You can find examples of how to create multi-step tasks here. For a list of all available YAML properties, please review the Task schema. To understand templating and how to provide custom values to your runs, review templates. - Docker With Docker, execute the following commands from the root of the repository. Linux: $ docker build -f Dockerfile -t acb . Windows: $ docker build -f Windows.Dockerfile -t acb . $ acb --help NAME:

### README headings

- ACR builder
- Task Schema
- Templating
- Requirements
- Building
- Usage
- Building an image
- Running a task
- Rendering a template locally
- F5 experience on VSCode
- Create a source volume for your workspace (i.e. your context, Dockerfiles, Task yaml files)
- Create a home volume for Docker to find your registry credentials.
- Create `launch.json` file in your `.vscode` folder:

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 366,417 |
| Dockerfile | 9,114 |
| Makefile | 2,881 |
| Shell | 212 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- go.mod (capture: captured) — dependency clues: github.com/AdaLogics/go-fuzz-headers, github.com/Azure/azure-sdk-for-go, github.com/Azure/go-autorest, github.com/Azure/go-autorest/autorest, github.com/Azure/go-autorest/autorest/adal, github.com/Azure/go-autorest/autorest/azure/auth, github.com/Azure/go-autorest/autorest/azure/cli, github.com/Azure/go-autorest/autorest/date, github.com/Azure/go-autorest/autorest/to, github.com/Azure/go-autorest/autorest/validation, github.com/Azure/go-autorest/logger, github.com/Azure/go-autorest/tracing, github.com/Masterminds/goutils, github.com/Masterminds/semver, github.com/Masterminds/sprig, github.com/cespare/xxhash/v2, github.com/containerd/containerd, github.com/containerd/errdefs, github.com/containerd/log, github.com/containerd/platforms
- Makefile (capture: captured)
- baseimages/docker-cli/Dockerfile (capture: captured)
- vendor/go.opentelemetry.io/otel/Makefile (capture: captured)
- vendor/go.opentelemetry.io/otel/requirements.txt (capture: captured) — dependency clues: codespell

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 41
- Forks at capture: 46
- Last updated: 2026-11-12T05:58:26Z
- Last pushed: 2026-11-22T06:19:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Azure/acr-builder)
- [README](https://github.com/Azure/acr-builder/blob/main/README.md)
- [Issues](https://github.com/Azure/acr-builder/issues)
- [Releases](https://github.com/Azure/acr-builder/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
