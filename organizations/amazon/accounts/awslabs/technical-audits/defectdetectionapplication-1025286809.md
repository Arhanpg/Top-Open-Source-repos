# awslabs/DefectDetectionApplication

- Company: Amazon
- Account: awslabs
- Repository: https://github.com/awslabs/DefectDetectionApplication
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:47:26+00:00

## Project purpose

The Defect Detection Application (DDA) is an edge-deployed computer vision solution for quality assurance in discrete manufacturing environments. Originally developed by the AWS EdgeML service team, DDA is now available as an open-source project under the stewardship of the AWS Manufacturing TFC and Auto/Manufacturing IBU.

## Why this project is used

Defect Detection Application - A Edge Based Industrial Inspection System - AWS Solution Guidance

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, TypeScript, Shell, C++, Jupyter Notebook, Dockerfile, CMake, SWIG, CSS, JavaScript, HTML, PowerShell, C, Mako, Batchfile, SCSS, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: @playwright/test, PyYAML, boto3, botocore, fast-check, jsdom, numpy, onnx, onnxruntime, onnxslim, typescript, ultralytics, vite, vitest
- Build/package tools: npm-compatible manifest, Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: edge-cv-portal/frontend/src/pages/node-designer/index.ts, edge-cv-portal/frontend/src/pages/workflows/index.ts, edge-cv-portal/frontend/src/types/index.ts, src/backend/app.py

## Setup and usage

- IAM Permissions for Installation: Installing DDA does not need an administrator user. An administrator does a one-time setup in each account (create the policies, bootstrap CDK with them, create an installer role); the person installing DDA then runs every step with the installer role. The policy documents are in edge-cv-portal/iam/.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/awslabs/DefectDetectionApplication/blob/main/README.md
- README SHA: 948590122ab6db2baadb6f3a102b1f4a2d5286a8
- Manifests: pyproject.toml, setup.py, hmi/package.json, com.dda.InferenceUploader/artifacts/requirements.txt, datasets/detection_training/requirements.txt, edge-cv-portal/backend/requirements.txt
- Sampled source files: edge-cv-portal/frontend/src/pages/node-designer/index.ts, edge-cv-portal/frontend/src/pages/workflows/index.ts, edge-cv-portal/frontend/src/types/index.ts, src/backend/app.py
- Git tree state: captured
- Evidence fingerprint: 40c2801397d38ed8860d63b8d848611188872b575e770e41e83bda9e45b72a03

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
