# bottlerocket-os/bottlerocket-update-operator

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-update-operator
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:21:51+00:00

## Project purpose

The Bottlerocket update operator (or, for short, Brupop) is a Kubernetes operator that coordinates Bottlerocket updates on hosts in a cluster. When installed, the Bottlerocket update operator starts a controller deployment on one node, an agent daemon set on every Bottlerocket node, and an Update Operator API Server deployment. The controller orchestrates updates across your cluster, while the agent is responsible for periodically querying for Bottlerocket updates, draining the node, and performing the update when asked by the controller. The agent performs all cluster object mutation operations via the API Server, which performs additional authorization using the Kubernetes TokenReview API -- ensuring that any request associated with a node is being made by the agent pod running on that node. Further, cert-manager is required in order for the API server to use a CA certificate to commun

## Why this project is used

A Kubernetes operator for automated updates to Bottlerocket

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust, Shell, Makefile, Dockerfile, Mustache
- Frameworks/libraries: Unknown / not established
- Dependency names: actix-web, apiserver, async-trait, awc, chrono, cron, futures, governor, http, k8s-openapi, kube, lazy_static, log, maplit, mockall, models, nonzero_ext, opentelemetry, opentelemetry-instrumentation-actix-web, opentelemetry-prometheus, opentelemetry_sdk, prometheus, regex, reqwest, rustls, rustls-pemfile, schemars, semver, serde, serde_json, serde_plain, snafu, tokio, tokio-retry, tracing, tracing-actix-web, validator
- Build/package tools: Cargo manifest, Docker build configuration
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: agent/src/lib.rs, agent/src/main.rs, apiserver/src/api/mod.rs, apiserver/src/auth/mod.rs

## Setup and usage

- Installation: 1. Brupop uses cert-manager to manage self-signed certificates used by the Bottlerocket update operator. To install cert-manager:
- Installation: https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml
- Installation: Or if you're using helm:

## Limitations and caveats

- Version Support Policy: As per our policy, Brupop follows the semantic versioning (semver) principles, ensuring that any updates in minor versions do not introduce any breaking or backward-incompatible changes. However, please note that we only provide security patches for the latest minor version. Therefore, it is highly recommended to always keep your Brupop installatio
- Version Support Policy: For example: If v1.3.0 is the latest Brupop release, then, v1.3 (latest minor version) will be considered as supported and v1.3.0 (latest available version) will be the recommended version of Brupop to be installed. When v1.3.1 is released, then that version will be considered as recommended.
- Current Limitations: - Monitoring on newly-rebooted nodes is limited.
- Current Limitations: We are considering an approach in which custom health checks can be configured to run after reboots. (https://github.com/bottlerocket-os/bottlerocket/issues/503)
- Current Limitations: - Node labels are not automatically applied to allow scheduling (https://github.com/bottlerocket-os/bottlerocket/issues/504)
- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-update-operator/blob/develop/README.md
- README SHA: 42bb367d2e83cd5e15d85f2e5a86e11a0a60923f
- Manifests: Cargo.toml, Dockerfile, Makefile, agent/Cargo.toml, apiserver/Cargo.toml, controller/Cargo.toml
- Sampled source files: agent/src/lib.rs, agent/src/main.rs, apiserver/src/api/mod.rs, apiserver/src/auth/mod.rs
- Git tree state: captured
- Evidence fingerprint: f4f70ba130faeaf81a36fbf28e87d8f080650e9e9828de205921d2d68e47dc8c

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
