# aws-observability/aws-application-signals-test-framework

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-application-signals-test-framework](https://github.com/aws-observability/aws-application-signals-test-framework)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-application-signals-test-framework/blob/main/README.md)
- README blob SHA: 31a429ad1992aafcc116ddcd28de9046e8f43a06
- Repository ID: 749937747
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:38:13+00:00

### Short excerpt (up to 100 words)

> This repository uses pre-commit to automatically format Terraform files. Install pre-commit: pip install pre-commit Install the git hooks: pre-commit install Now Terraform files will be automatically formatted when you commit. This guide will give a step by step instruction on how to test changes made to Java/Python E2E testing resources before pushing a PR. The guide will include the following: - Setting up IAM roles and an EKS cluster - Setting up VPC settings and IAM role for EC2 instances - Buliding sample app images/files and putting them into ECRs/S3 buckets - Forking a repository and setting up necessary secrets

### README headings

- aws-application-signals-test-framework
- Development Setup
- Pre-commit Hooks
- How to Run Lambda Java Performance Test
- How to Test E2E Resource Changes
- 1. Create an IAM Role with OIDC Identity Provider
- Create an OIDC Provider
- Create an IAM role
- Add Additional Permission
- 2. Create EKS Clusters
- Setup Environment with the Appropriate Roles and Permissions.
- Create a new Cluster
- Install AWS Load Balancer Controller Add-on
- Create a New Cluster and Install the AWS Load Balancer Controller Add-on for All Regions
- 3. Setting up Environment for EC2 Tests
- Create IAM Role for EC2 Instance
- Setting Up Default VPC
- 4. Building Sample App to ECR
- 5. Building Sample App to S3 Bucket
- 6. Setting up repository
- 7. Running the tests
- E2E Testing Resources
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Mustache | 964,464 |
| HCL | 606,088 |
| Python | 293,100 |
| Java | 222,675 |
| TypeScript | 50,438 |
| Shell | 38,657 |
| C# | 27,121 |
| JavaScript | 18,013 |
| Smarty | 15,524 |
| PowerShell | 12,713 |
| Dockerfile | 9,489 |
| ASP.NET | 1,248 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- buildSrc/build.gradle.kts (capture: captured)
- validator/build.gradle.kts (capture: captured)
- mcp-testing/evals/requirements.txt (capture: captured) — dependency clues: boto3, loguru, mcp
- sample-apps/traffic-generator/Dockerfile (capture: captured)
- sample-apps/traffic-generator/package.json (capture: captured) — dependency clues: axios
- sample-apps/dotnet/asp_frontend_service/asp_frontend_service.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 8
- Forks at capture: 29
- Last updated: 2026-11-06T18:43:53Z
- Last pushed: 2026-11-23T19:04:56Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-application-signals-test-framework)
- [README](https://github.com/aws-observability/aws-application-signals-test-framework/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-application-signals-test-framework/issues)
- [Releases](https://github.com/aws-observability/aws-application-signals-test-framework/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
