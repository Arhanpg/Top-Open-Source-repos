# Online Boutique — Cloud-First Microservices Demo

- Company association: Alphabet / Google
- Upstream GitHub account: [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Repository: [GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo)
- Default branch: `main`
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: `eac25ffad58f8ad16bca0bb854dc1231922bcc5c`
- Account relationship: The repository is hosted under the separately inventoried GoogleCloudPlatform account, which Google Cloud documentation links for its cloud samples.

## Project overview

A cloud-first web e-commerce demo application that lets users browse products, add items to a cart and complete a sample checkout. Google uses it to demonstrate application modernization and cloud-native deployment patterns; the README says it can run on any Kubernetes cluster.

## Features and capabilities documented by the README

- Composes 11 microservices written in different languages and communicating over gRPC.
- Includes frontend, cart, product catalogue, currency conversion, payment, shipping, email, checkout, recommendation, advertising and load-generation services.
- Uses Redis for cart storage; product catalogue data is loaded from JSON; checkout orchestrates payment, shipping and email service calls.
- Provides a Locust-based load generator that imitates realistic shopping flows.
- Includes a GKE quickstart and deployment variations for Terraform, Istio/Cloud Service Mesh and non-GKE Kubernetes such as Minikube and Kind.
- Documents an optional Gemini-powered shopping assistant that can recommend products from an image.
- Shows Google Cloud service integrations including GKE, Cloud Operations, Spanner, Memorystore, AlloyDB and Gemini.

## Technology stack

Polyglot microservices: Go, C#, Node.js, Python and Java; gRPC and Protocol Buffers; Redis; JSON catalogue data; Kubernetes; GKE; optional Istio/Cloud Service Mesh, Cloud Operations, Spanner, Memorystore and Gemini integrations. Python/Locust is used for load generation.

## Getting started

The README's GKE quickstart requires a Google Cloud project and shell tools including gcloud, git and kubectl. It creates a GKE cluster, deploys release/kubernetes-manifests.yaml, waits for pods, then exposes the frontend service. The README also links local development and non-GKE deployment guidance.

## Lifecycle, compatibility and operational considerations

This is a demonstration workload, not a production commerce platform. The README marks payment and shipping as mock operations and email as a mock sender; do not treat a demo checkout as a real payment or fulfilment integration. The load generator and external service dependencies should be reviewed before exposing a deployment.

## Evaluation guidance

Check the exact upstream release/branch, environment prerequisites, licence and security guidance before adopting the project. For archived or superseded repositories, follow the stated successor path. This dossier summarizes the inspected README and repository metadata; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/GoogleCloudPlatform/microservices-demo)
- [README](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/microservices-demo/issues)
- [Releases](https://github.com/GoogleCloudPlatform/microservices-demo/releases)

Evidence note: the README blob SHA identifies the upstream revision inspected. Lifecycle statements are cross-checked against the current repository metadata where noted.
