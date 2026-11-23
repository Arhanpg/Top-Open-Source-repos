# aws-samples/acmpca-hierarchy

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/acmpca-hierarchy](https://github.com/aws-samples/acmpca-hierarchy)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/acmpca-hierarchy/blob/main/README.md)
- README blob SHA: 28bb25e6b63c7be65d3d6347f1aea64fb8ed0522
- Repository ID: 379958518
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

An AWS CloudFormation template for the rapid deployment of a multi-level CA hierarchy and consistent provisioning experience. Optionally use AWS Resource Access Manager (AWS RAM) to securely share the CA within your AWS Organizations, centralizing the CA while using the AWS RAM to manage the permissions.  Optionally use Amazon S3 to store the CRL and access logs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:26:48+00:00

### Short excerpt (up to 100 words)

> Large organizations often build a public key infrastructure (PKI) inside the AWS cloud, intended for private use within an organization. With AWS Private Certificate Authority (AWS Private CA), you create your own CA hierarchy and issue certificates with it for authenticating internal users, computers, applications, services, servers, and other devices, and for signing computer code. Certificates issued by a private CA are trusted only within your organization, not on the public internet. AWS Resource Access Manager (AWS RAM) allows you to securely share AWS resources within your AWS Organization. Private CA Cross-Account Sharing, gives you the ability to grant permissions

### README headings

- AWS Private Certificate Authority (AWS Private CA) shared to AWS Organizations via AWS Resource Access Manager (AWS RAM)
- Usage
- Limitations
- Prerequisites
- Alternatives
- Test Cases
- Certificate Lifecycle Tests
- Request Certificate. Use the CA ARN from the output of AWS CloudFormation template stack.
- Export Certificate. Use the certificate ARN from the response of request-certificate
- Describe Certificate. See if it is eligible for renewal
- Renew Certificate, see if renewal is successful using describe-certificate
- Delete Certificate
- Test Cleanup
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

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 6
- Forks at capture: 3
- Last updated: 2026-07-07T16:54:22Z
- Last pushed: 2026-07-07T16:54:13Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/acmpca-hierarchy)
- [README](https://github.com/aws-samples/acmpca-hierarchy/blob/main/README.md)
- [Issues](https://github.com/aws-samples/acmpca-hierarchy/issues)
- [Releases](https://github.com/aws-samples/acmpca-hierarchy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
