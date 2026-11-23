# Kyma — Modular Kubernetes-Based Application Platform

- **Company association:** SAP
- **Upstream GitHub account:** [kyma-project](https://github.com/kyma-project)
- **Repository:** [kyma-project/kyma](https://github.com/kyma-project/kyma)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/kyma-project/kyma/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `be042d40a8d7fdfd2edf5853caedb78f3fdefc8f`
- **Account relationship:** SAP's verified GitHub profile lists this account as a dedicated organization for the named project/product area.

## Project overview

Kyma is an opinionated set of Kubernetes-based modular building blocks for developing and running enterprise-grade cloud-native applications. The README describes it as an open path into the SAP ecosystem and a foundation of SAP BTP Kyma runtime, while allowing modules to be used on a user's own Kubernetes cluster.

## Features and capabilities documented by the README

- Provides modular capabilities that can be added or removed independently rather than requiring a monolithic Kyma installation.
- Serverless module for running lightweight functions in a scalable and cost-efficient way.
- Application connectivity that securely registers external application APIs and events.
- Istio-based service-to-service communication and proxying.
- Service management for using cloud services from GCP, Azure and AWS in Kyma scenarios.
- API Gateway module for secure API exposure.
- Telemetry module for collecting and forwarding observability data to telemetry backends.
- CLI and UI workflows for connecting an application to a Kubernetes cluster; the repository also links ready-to-use examples.

## Technology stack

Kubernetes; Go (the README's contributor FAQ discusses Go tooling); SAP BTP Kyma runtime; Gardener-managed Kubernetes; Istio; serverless functions; application connector; telemetry; Gomega and Testify are named in the Go testing FAQ. Kyma is modular, so the actual runtime stack depends on the selected modules.

## Getting started

Use the Quick Install guide and choose the modules required for the target Kubernetes cluster. The README directs developers to the Kyma Modules catalogue and the separate examples repository. Follow module-specific installation and lifecycle instructions rather than an old monolithic release guide.

## Lifecycle, compatibility and operational considerations

**Lifecycle change:** the README explicitly states that global/monolithic Kyma releases are discontinued after the modular transformation. Each module is now developed and delivered independently; consumers subscribe to individual module repositories and add/remove modules without installing the monolithic Kyma. The README says the project remains actively maintained and is supported by SAP.

## Evaluation guidance

Check the exact upstream release, build/dependency manifests, supported platforms/toolchain, licence, operational prerequisites and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/kyma-project/kyma)
- [README](https://github.com/kyma-project/kyma/blob/main/README.md)
- [Issues](https://github.com/kyma-project/kyma/issues)
- [Releases](https://github.com/kyma-project/kyma/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology claims are limited to the README and company-profile evidence; unsupported implementation details are not inferred.*
