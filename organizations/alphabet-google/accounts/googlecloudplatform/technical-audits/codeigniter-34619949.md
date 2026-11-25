# GoogleCloudPlatform/CodeIgniter

- Company: Alphabet (Google)
- Account: GoogleCloudPlatform
- Repository: https://github.com/GoogleCloudPlatform/CodeIgniter
- Default branch: 3.0.0-stable
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:28:02+00:00

## Project purpose

This repository contains a modified CodeIgniter framework and a starter app for Google App Engine.

## Why this project is used

Open Source PHP Framework for GAE (originally from EllisLab)

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: mikey179/vfsStream
- Build/package tools: Composer manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: system/core/Benchmark.php, system/core/CodeIgniter.php, system/core/Common.php, system/core/compat/hash.php

## Setup and usage

- Installation: 1. Clone the repository with
- Installation: git clone https://github.com/GoogleCloudPlatform/CodeIgniter.git
- Installation: 1. Follow the PHP Tutorial if you have never used App Engine before.
- Installation: 1. Create a CloudSQL instance based on these instructions. Also create a database for storing CodeIgniter models.
- Installation: 1. Replace , and in app.yaml with the corresponding value for your Google Cloud project and ClouSQL instance.
- Installation: 1. Install composer if you haven't done so previously. Run the following command from your project root to install all required dependencies
- Installation: php composer.phar install
- Installation: 1. Access your app using http://your_app_id.appspot.com and you should see CodeIgniter's default welcome page.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/GoogleCloudPlatform/CodeIgniter/blob/3.0.0-stable/README.md
- README SHA: f0c04d8d938697b423526c2e0c2d5159ec7e7bb4
- Manifests: composer.json
- Sampled source files: system/core/Benchmark.php, system/core/CodeIgniter.php, system/core/Common.php, system/core/compat/hash.php
- Git tree state: captured
- Evidence fingerprint: ee5fd585af5705db686269b1beed3b889aca44129127c4640d5c17ab8767871a

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
