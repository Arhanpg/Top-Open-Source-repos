# MindConnect NodeJS — Insights Hub / Industrial IoT SDK

- **Company association:** Siemens
- **Upstream GitHub account:** [mindsphere](https://github.com/mindsphere)
- **Repository:** [mindsphere/mindconnect-nodejs](https://github.com/mindsphere/mindconnect-nodejs)
- **Default branch:** `master`
- **README:** [Open upstream README](https://github.com/mindsphere/mindconnect-nodejs/blob/master/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `53cd9842af0ac90c3e416c930a9ba8be8e3e00dd`
- **Account relationship:** Siemens's official Open Source portal lists this product-specific account; the account's repositories are not assumed to be all Siemens-authored or legally owned.

## Project overview

A Node.js/TypeScript library, SDK, command-line interface and development proxy for connecting Industrial IoT agents and applications to Siemens Insights Hub (formerly MindSphere). It supports agent onboarding, asset data modelling, data mapping and telemetry upload.

## Features and capabilities documented by the README

- Provides a Node.js library for onboarding MindConnect agents and exchanging industrial telemetry with Insights Hub.
- Offers a TypeScript SDK for Insights Hub asset and data-model APIs.
- Includes a CLI for starter projects, agent tokens, service credentials, asset operations and other developer tasks.
- Provides starter generators for JavaScript and TypeScript projects.
- Supports configuring an agent, onboarding it, generating data-source configuration and mapping telemetry to asset variables.
- Supports single and bulk telemetry upload workflows and a development proxy for local development against the platform.
- Links full library, SDK and CLI documentation and npm distribution.

## Technology stack

Node.js; TypeScript and JavaScript; npm package @mindconnect/mindconnect-nodejs; TypeScript SDK; CLI; Insights Hub/Xcelerator gateway APIs; OAuth/service credentials; agent onboarding and telemetry APIs. The README documents separate legacy and new gateway URL schemes.

## Getting started

Install the package from npm and use the CLI starter-ts or starter-js command to generate a project. Follow the version-matched documentation to configure the tenant/gateway, credentials and agent onboarding before sending telemetry.

## Lifecycle, compatibility and operational considerations

**Breaking gateway compatibility:** version 4.0.0 and later require the new `siemens.app` URL scheme and do not work with tenants still using legacy `mindsphere.io` URLs. Keep version 3.x for legacy tenants. The README says v4 support for new Xcelerator deployments is best-effort; it recommends that on-premise/private-cloud installations stay on 3.x until the migration stabilizes. Protect the local configuration folder because it stores client secrets.

## Evaluation guidance

Check the exact upstream release, build/dependency manifests, supported platforms/toolchain, licence, operational prerequisites and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/mindsphere/mindconnect-nodejs)
- [README](https://github.com/mindsphere/mindconnect-nodejs/blob/master/README.md)
- [Issues](https://github.com/mindsphere/mindconnect-nodejs/issues)
- [Releases](https://github.com/mindsphere/mindconnect-nodejs/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology claims are limited to the README and company-profile evidence; unsupported implementation details are not inferred.*
