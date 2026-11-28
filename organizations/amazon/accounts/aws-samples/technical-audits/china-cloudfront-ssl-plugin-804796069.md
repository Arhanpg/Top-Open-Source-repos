# aws-samples/China-CloudFront-SSL-Plugin

- Company: Amazon
- Account: aws-samples
- Repository: https://github.com/aws-samples/China-CloudFront-SSL-Plugin
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:09:28+00:00

## Project purpose

1. In China CloudFront SSL Plugin V1, each stack can only manage one project (i.e., one domain name collection). To manage multiple domain name collections, multiple stacks need to be deployed. In contrast, the stack of China CloudFront SSL Plugin V2 can manage multiple projects (i.e., multiple domain name collections). 2. The certificate management interface of the first version of the China CloudFront SSL plugin is an API management page built on Swagger UI. To perform operations such as listing certificates or deleting certificates, you need to initiate API requests in the certificate management interface. In addition, in the first version, there is no security verification for externally used APIs. 3. In China CloudFront SSL Plugin V1, each stack can only manage one project (i.e., one domain names collection). To manage multiple domain names collections, multiple stacks need to be de

## Why this project is used

1. In China CloudFront SSL Plugin V1, each stack can only manage one project (i.e., one domain name collection). To manage multiple domain name collections, multiple stacks need to be deployed. In contrast, the stack of China CloudFront SSL Plugin V2 can manage multiple projects (i.e., multiple domain name collections). 2. The certificate management interface of the first version of the China CloudFront SSL plugin is an API management page built on Swagger UI. To perform operations such as listing certificates or deleting certificates, you need to initiate API requests in the certificate management interface. In addition, in the first version, there is no security verification for externally used APIs. 3. In China CloudFront SSL Plugin V1, each stack can only manage one project (i.e., one domain names collection). To manage multiple domain names collections, multiple stacks need to be de

## Core features

- Almost Free*: Built using serverless architecture and open-source tools, it incurs charges based on the invocation of serverless services, with a default of eve: Almost Free*: Built using serverless architecture and open-source tools, it incurs charges based on the invocation of serverless services, with a default of every 80 days.
  - Evidence: README.md#Features
- _*This solution adopts a serverless architecture, nearly zero cost with each certificate issuance, such as serverless resource execution costs, a small amount o: _*This solution adopts a serverless architecture, nearly zero cost with each certificate issuance, such as serverless resource execution costs, a small amount of Amazon S3 storage fees, and Amazon CloudWatch log storage fees. However, due to the domain control validation required for certificate issuance, there's a fee of 3.575 RMB per month for using Amazon Route 53 for domain hosting._
  - Evidence: README.md#Features
- Out-of-the-Box: Deployment and certificate issuance for the solution can be completed in just 3 minutes. It supports certificate download, integration with Amaz: Out-of-the-Box: Deployment and certificate issuance for the solution can be completed in just 3 minutes. It supports certificate download, integration with Amazon CloudFront, and automatic updates.
  - Evidence: README.md#Features
- Fully Open Source: All code within this solution is provided in an open-source manner, allowing for customization based on your specific needs.: Fully Open Source: All code within this solution is provided in an open-source manner, allowing for customization based on your specific needs.
  - Evidence: README.md#Features

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: @types/jest, @types/node, aws-cdk, aws-cdk-lib, aws-sdk, boto3, certbot, certbot-dns-route53, constructs, express, jest, serverless-http, swagger-ui-express, ts-jest, ts-node, typescript
- Build/package tools: Docker build configuration, npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: lambda/api-explorer/app.js, lambda/CertBot/certbot/app.py, lambda/ManageCert/DeleteCert/app.py, lambda/ManageCert/ListCert/app.py

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-samples/China-CloudFront-SSL-Plugin/blob/main/README.md
- README SHA: 55eea656f5b8fe262493980fd3e074aa744d65fa
- Manifests: cdk/package.json, lambda/api-explorer/Dockerfile, lambda/api-explorer/package.json, lambda/CertBot/certbot/Dockerfile, lambda/CertBot/certbot/requirements.txt, lambda/ManageCert/DeleteCert/Dockerfile
- Sampled source files: lambda/api-explorer/app.js, lambda/CertBot/certbot/app.py, lambda/ManageCert/DeleteCert/app.py, lambda/ManageCert/ListCert/app.py
- Git tree state: captured
- Evidence fingerprint: df6af540d800db7ef14ac2736303959e519a90e699730c49b9d48e26ddc9adf7

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
