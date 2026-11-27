# aws-samples/Automated-Oracle-E-Business-Suite-DR-Switchover

- Company: Amazon
- Account: aws-samples
- Repository: https://github.com/aws-samples/Automated-Oracle-E-Business-Suite-DR-Switchover
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:26:09+00:00

## Project purpose

Many Organizations are running Oracle E-Business Suite, which in most cases is considered a core application within the organization. Oracle E-Business Suite is a business application suite that includes financial, supply chain, human resources, and customer relationship management modules. Due to the application’s critical nature, It is imperative to architect Oracle E-Business Suite for high availability and to develop the ability to switchover the application and database as quickly as possible by removing personal dependencies. It is critical for organizations to ensure high availability of Oracle E-Business Suite applications in order to minimize downtime and maintain business continuity. One method for achieving high availability is to perform an EBS application switchover. This document will go over how to perform an Oracle E-Business Suite application and database switchover.

## Why this project is used

Oracle E-Business Suite DR Switchover

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: aws-cdk-lib, boto3, constructs
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: app.py, atsobject/ats_obj_stack.py, atsobject/lambda/ATS-EBS-ELBSwitch/lambda_function.py, atsobject/lambda/ATS-EBS-FetchPrimaryDb/lambda_function.py

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-samples/Automated-Oracle-E-Business-Suite-DR-Switchover/blob/main/README.md
- README SHA: 93edf8db268cb72726352084f87e92192814e5ae
- Manifests: requirements.txt
- Sampled source files: app.py, atsobject/ats_obj_stack.py, atsobject/lambda/ATS-EBS-ELBSwitch/lambda_function.py, atsobject/lambda/ATS-EBS-FetchPrimaryDb/lambda_function.py
- Git tree state: captured
- Evidence fingerprint: 9f86ce31138a3de8cb9db6c69bb772e438b99f6be9079fbad7343309d2482b5e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
