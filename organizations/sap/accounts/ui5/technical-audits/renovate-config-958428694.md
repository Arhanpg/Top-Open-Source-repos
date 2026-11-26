# UI5/renovate-config

- Company: SAP
- Account: UI5
- Repository: https://github.com/UI5/renovate-config
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T07:18:14+00:00

## Project purpose

> A Renovate preset to keep your UI5 application up-to-date.

## Why this project is used

With the UI5 Renovate Preset Config its such as easy to update your UI5 project automatically when a new UI5 version is released.

## Core features

- ui5.yaml files: ui5.yaml files
  - Evidence: README.md#Features
- manifest.json and CommonDataModel.json files: manifest.json and CommonDataModel.json files
  - Evidence: README.md#Features

## Technology stack

- Languages: JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: @commitlint/cli, @commitlint/config-conventional, husky, knip, licensee, prettier
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: .husky/skip.js

## Setup and usage

- Usage: 1. Set up Renovate for your repository.
- Usage: 2. Create a new file called renovate.json at the root level of your project.
- Usage: 3. Add the following content:
- Usage: "$schema": "https://docs.renovatebot.com/renovate-schema.json",
- Usage: "github>ui5/renovate-config"
- Usage: "separateMinorPatch": true
- Usage: **Note:** We recommend setting separateMinorPatch to true to create separate pull requests for patches and minor releases.
- Usage: If your project should only consume Long-Term Support (LTS) releases, use the following content:

## Limitations and caveats

- Security / Disclosure: If you find any bug that might be a security problem, please follow the instructions given in Security Policy on how to report it. Please do not create GitHub issues for security-related concerns or problems.

## Evidence and provenance

- README: https://github.com/UI5/renovate-config/blob/main/README.md
- README SHA: 8f02cfb8a1d298971edd2b094732b11531819397
- Manifests: package.json
- Sampled source files: .husky/skip.js
- Git tree state: captured
- Evidence fingerprint: 40116d4c10ad284f83d557e4183719126a42009cd993343045e070f7144d369b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
