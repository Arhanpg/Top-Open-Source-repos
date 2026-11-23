# aws-samples/access-internal-alb-through-aws-global-accelerator

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/access-internal-alb-through-aws-global-accelerator](https://github.com/aws-samples/access-internal-alb-through-aws-global-accelerator)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/access-internal-alb-through-aws-global-accelerator/blob/main/README.md)
- README blob SHA: 65d02e4d6f2692204f0a97695ba2854b96ef34cb
- Repository ID: 311883308
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The purpose of this repository is to demo how to access an internal Application Load Balancer (ALB) through AWS Global Accelerator.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:11:23+00:00

### Short excerpt (up to 100 words)

> The purpose of this repository is to demo how to access an internal Application Load Balancer (ALB) through AWS Global Accelerator. AWS CloudFormation template (main.yml) will deploy a Virtual Private Cloud(VPC) with 2 Public and 2 Private subnets within the VPC. Later it will create an Internal Application Load Balancer attached to an Auto Scaling Group where it will serve a simple PHP application and echo real-client IP using HTTP_X_FORWARDED_FOR header. The access to this PHP application is done through AWS Global Accelerator. You can read more in this blog post. Click on the **Launch Stack** button below to launch

### README headings

- Access Internal Application Load Balancer through AWS Global Accelerator
- Architecture
- Launch the AWS CloudFormation Stack
- How to Access Your Application
- Clean up
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Unknown | Not captured |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 4
- Forks at capture: 2
- Last updated: 2026-01-22T00:57:16Z
- Last pushed: 2021-09-13T06:43:38Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/access-internal-alb-through-aws-global-accelerator)
- [README](https://github.com/aws-samples/access-internal-alb-through-aws-global-accelerator/blob/main/README.md)
- [Issues](https://github.com/aws-samples/access-internal-alb-through-aws-global-accelerator/issues)
- [Releases](https://github.com/aws-samples/access-internal-alb-through-aws-global-accelerator/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
