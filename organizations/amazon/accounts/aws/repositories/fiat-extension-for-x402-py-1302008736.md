# aws/fiat-extension-for-x402-py

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/fiat-extension-for-x402-py](https://github.com/aws/fiat-extension-for-x402-py)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/fiat-extension-for-x402-py/blob/main/README.md)
- README blob SHA: c99c4b45fa27bbbd5bf9a9fc4dcc5fc6bd6c7d7e
- README bytes captured: 16265
- README truncated at capture limit: False
- Repository ID: 1302008736
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Marketplace Agentic Commerce payment schemes for the x402 protocol (Python)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T22:13:22+00:00

### Short excerpt (up to 300 words)

> Install this package with Verification is stateless: a

### README headings

- Fiat Extension for x402 (Python)
- How a payment works
- Install
- Quick start (FastAPI)
- Seller: signs quotes with a KMS key (ECC_NIST_P384, SIGN_VERIFY).
- Facilitator: verifies payment tokens, here in the seller's own process.
- Quick start (Flask)
- signer, verifier and routes as above
- Set up with an AI coding agent
- Quote signing
- An AWS KMS key
- Your own key with a JWKS URL
- 1. Load the key. The algorithm follows the key: P-256/P-384/P-521, or RSA
- of at least 2048 bits.
- 2. Serve the public key. Leave this route out of the payment routes.
- 3. Point the facilitator at the JWKS.
- Local development and tests
- Configuration
- Product ID
- Seller key resolution
- Payment token verification
- DPoP
- Failure reasons
- Running the facilitator separately
- Versioning
- Development
- Security
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install

> Install this package with

### Limitations and security: Security

> Verification is stateless: a

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 274,498 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: boto3, build, cryptography, fastapi, flask, httpx, moto, mypy, pyjwt, pytest, pytest-asyncio, pytest-cov, respx, ruff, x402
- examples/lambda_seller/requirements.txt (capture: captured) — dependency clues: mangum

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 0
- Forks at capture: 0
- Last updated: 2026-11-12T19:03:05Z
- Last pushed: 2026-11-19T21:40:07Z
- Topics: agentic-commerce, aws, aws-marketplace, payments, python, x402

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/fiat-extension-for-x402-py)
- [README](https://github.com/aws/fiat-extension-for-x402-py/blob/main/README.md)
- [Issues](https://github.com/aws/fiat-extension-for-x402-py/issues)
- [Releases](https://github.com/aws/fiat-extension-for-x402-py/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
