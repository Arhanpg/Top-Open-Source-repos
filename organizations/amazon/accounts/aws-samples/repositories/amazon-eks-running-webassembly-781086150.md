# aws-samples/amazon-eks-running-webassembly

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-eks-running-webassembly](https://github.com/aws-samples/amazon-eks-running-webassembly)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-eks-running-webassembly/blob/main/README.md)
- README blob SHA: c7630d134c0f2f4d59606d766a92de2076306cb4
- README bytes captured: 11812
- README truncated at capture limit: False
- Repository ID: 781086150
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Run WebAssembly workloads on Amazon EKS

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T06:50:11+00:00

### Short excerpt (up to 300 words)

> This sample code is For security issues or

### README headings

- Run WebAssembly workloads on Amazon EKS
- 🔢 Pre-requisites
- 👷 Building the AMIs
- Building the EKS cluster
- Running an example workload with the Spin runtime
- Building a hello-world image and running it with the WasmEdge runtime
- Wait a few seconds for the pods to start
- Building a microservice with a MariaDB backend
- Create the secret for the database
- Get the IP of your Kubernetes DNS-Service and update the DNS_SERVER variable with it
- See if the pods are running
- Forward the port of the service to localhost
- Initialize the database
- Check for orders (the answer should be empty)
- Download sample orders and create them in our database
- Check for orders again
- Cleaning up
- 🔒 Security
- ⚖️ License Summary

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: ⚖️ License Summary

> This sample code is

### Limitations and security: 🔒 Security

> For security issues or

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 45,199 |
| Shell | 2,043 |
| Dockerfile | 1,155 |
| Rust | 897 |
| Smarty | 353 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- build/hello-world/Cargo.toml (capture: captured) — dependency clues: hyper_wasi, tokio_wasi
- build/hello-world/Dockerfile (capture: captured)
- build/microservice-demo/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 17
- Forks at capture: 1
- Last updated: 2026-01-22T02:15:08Z
- Last pushed: 2024-10-09T12:18:11Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-eks-running-webassembly)
- [README](https://github.com/aws-samples/amazon-eks-running-webassembly/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-eks-running-webassembly/issues)
- [Releases](https://github.com/aws-samples/amazon-eks-running-webassembly/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
