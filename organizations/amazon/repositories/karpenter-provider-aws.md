# Karpenter AWS Provider

- **Company grouping:** Amazon / AWS
- **GitHub organization:** [aws](https://github.com/aws)
- **Repository:** [aws/karpenter-provider-aws](https://github.com/aws/karpenter-provider-aws)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/aws/karpenter-provider-aws/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `3e22dc31bf1df204bf7d8c8e776c24bc1befbbb8`

## Project overview

The README describes Karpenter as an open-source node-provisioning project for Kubernetes. It watches for pods the Kubernetes scheduler marks unschedulable, evaluates their scheduling requirements and provisions nodes that can run them.

## Features and capabilities

- Watches for pending/unschedulable pods and reacts to scheduling demand.
- Evaluates resource requests, node selectors, affinities, tolerations and topology-spread constraints.
- Provisions nodes that satisfy pod scheduling requirements.
- Removes nodes when they are no longer needed, aiming to improve cluster efficiency and cost.
- Links Karpenter documentation, community discussions, working-group meetings and talks.

## Technology stack

Kubernetes node provisioning and autoscaling; the README includes a Go Report Card badge and an Apache 2.0 licence badge. The overview does not provide a complete list of provider implementation dependencies.

## Getting started

Begin with the official Karpenter documentation and the AWS provider-specific installation guide. Configure cluster identity, node-provisioning permissions and workload scheduling constraints before enabling production node provisioning.

## Cloud, security and operational considerations

This is infrastructure control-plane software that can create and terminate compute instances. Review IAM permissions, disruption budgets, topology constraints, capacity availability and cost implications before production use. The README summary is not a substitute for version-specific deployment instructions.

## Evaluation guidance

Review the version-specific AWS documentation, IAM requirements, deployment template and resource-cleanup procedure before running this project in an AWS account. Validate the costs of any cloud resources created by examples or controllers. This dossier summarizes the upstream README and is not a complete source-code, cloud-security or infrastructure review.

## Upstream references

- [Repository](https://github.com/aws/karpenter-provider-aws)
- [README](https://github.com/aws/karpenter-provider-aws/blob/default/README.md)
- [Issues](https://github.com/aws/karpenter-provider-aws/issues)
- [Releases](https://github.com/aws/karpenter-provider-aws/releases)

*Evidence note: README blob SHA above identifies the upstream revision inspected. Technology details are limited to the README's evidence; a full dependency and infrastructure-manifest audit remains outstanding.*
