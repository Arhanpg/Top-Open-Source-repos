# kyma-project/dev-toolbox

- Company: SAP
- Account: kyma-project
- Repository: https://github.com/kyma-project/dev-toolbox
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:23:08+00:00

## Project purpose

The dev-toolbox project contains the most useful binaries in one image. It is an Alpine-based image that can be used, for example, as a script executor inside a cluster or base image for devcontainers.

## Why this project is used

The dev-toolbox project contains the most useful binaries in one image. It is an Alpine-based image that can be used, for example, as a script executor inside a cluster or base image for devcontainers.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Dockerfile, Makefile, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: none

## Setup and usage

- Usage: > Because dev-toolbox is in an early development state, we would suggest using the latest built image that contains all fixes and smaller improvements:
- Usage: europe-docker.pkg.dev/kyma-project/prod/dev-toolbox:main
- Usage: To run a local container, use the following command:
- Usage: docker run -it --rm europe-docker.pkg.dev/kyma-project/prod/dev-toolbox:main
- Usage: If you are looking for a way to run dev-toolbox inside the cluster, apply the required resources:
- Usage: kubectl apply -f https://raw.githubusercontent.com/kyma-project/dev-toolbox/refs/heads/main/hack/resources.yaml
- Usage: For integration of dev-toolbox with the devcontainers, use the following configuration.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/kyma-project/dev-toolbox/blob/main/README.md
- README SHA: 5b2df3246b0a38b9adfc8b8afac1aed55921dadc
- Manifests: Dockerfile, Makefile
- Sampled source files: none
- Git tree state: captured
- Evidence fingerprint: 2fcc352af509258b1d2ef9fd426390498cf8bca831537dcccbe966ae80de17f6

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
