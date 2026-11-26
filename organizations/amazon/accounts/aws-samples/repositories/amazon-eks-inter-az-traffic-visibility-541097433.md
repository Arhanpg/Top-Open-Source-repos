# aws-samples/amazon-eks-inter-az-traffic-visibility

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-inter-az-traffic-visibility](https://github.com/aws-samples/amazon-eks-inter-az-traffic-visibility)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-inter-az-traffic-visibility/blob/main/README.md)
- README blob SHA: db51dea92e1f0f53606364ea123fe8d3793d9f2f
- README bytes captured: 10198
- README truncated at capture limit: False
- Repository ID: 541097433
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The project implements an Amazon EKS Cross-AZ Pod to Pod network bytes visability It is based on this blog: https://aws.amazon.com/blogs/containers/getting-visibility-into-your-amazon-eks-cross-az-pod-to-pod-network-bytes/

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:24:59+00:00

### Short excerpt (up to 300 words)

> Our solution is based An AWS Account Shell See CONTRIBUTING for more

### README headings

- Amazon EKS cross-az traffic visibility
- Solution overview
- Prerequisites
- Step 1: Deploy an Amazon EKS Cluster
- **Set the environment**
- **Generate the ClusterConfig**
- Deploy the Cluster
- Get the Worker nodes, Pods and their topology zone data
- Clone the application repo
- Deploy the demo application
- Validate the demo application
- Validate that the server pods are spread across Nodes and AZs
- Step 1.5: [Optional] Determine the app label selector
- Step 2: Deploy the CDK Stack
- Deploy the stack
- Authorise the AWS Lambda function (k8s client)
- Append a role mapping to `ConfigMap/aws-auth`
- Validate
- Step 3: Viewing the process and results Interactively
- Non-Interactive flow of the solution
- Considerations
- Usage Guide
- 1. Verification (Manual Trigger)
- 1. Start Analysis Pipeline
- 2. Wait ~1-2 minutes for execution to complete
- 3. Query Results
- 2. Automated Monitoring
- Cleanup
- Destroy the CDK Stack
- Destroy the EKS cluster

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Solution overview

> Our solution is based

### Technology and requirements: Prerequisites

> An AWS Account Shell

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 44,768 |
| Shell | 4,891 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- package.json (capture: captured) — dependency clues: aws-cdk
- requirements.txt (capture: captured) — dependency clues: attrs, aws-cdk-asset-awscli-v1, aws-cdk-asset-kubectl-v20, aws-cdk-asset-node-proxy-agent-v6, aws-cdk-aws-glue-alpha, aws-cdk-aws-lambda-python-alpha, aws-cdk-lib, cattrs, cdk-nag, constructs, importlib-resources, jsii, publication, python-dateutil, six, typeguard, typing-extensions
- pod_metadata_extractor/runtime/requirements.txt (capture: captured) — dependency clues: boto3, botocore, cachetools, certifi, charset-normalizer, google-auth, idna, jmespath, kubernetes, oauthlib, pyasn1, pyasn1-modules, python-dateutil, pyyaml, requests, requests-oauthlib, rsa, s3transfer, six, urllib3

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 43
- Forks at capture: 17
- Last updated: 2026-04-23T09:11:21Z
- Last pushed: 2026-02-12T09:14:58Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-inter-az-traffic-visibility)
- [README](https://github.com/aws-samples/amazon-eks-inter-az-traffic-visibility/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-inter-az-traffic-visibility/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-inter-az-traffic-visibility/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
