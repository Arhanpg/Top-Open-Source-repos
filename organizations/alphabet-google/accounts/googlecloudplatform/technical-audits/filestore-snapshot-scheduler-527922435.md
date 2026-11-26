# GoogleCloudPlatform/Filestore-Snapshot-Scheduler

- Company: Alphabet (Google)
- Account: GoogleCloudPlatform
- Repository: https://github.com/GoogleCloudPlatform/Filestore-Snapshot-Scheduler
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:52:05+00:00

## Project purpose

A cloud solution for automating a snapshots scheduling process for GCP Filestore managed-service.

## Why this project is used

A cloud solution for automating a snapshots scheduling process for GCP Filestore managed-service.

## Core features

- A single user-defined retention policy can be applied on multiple: A single user-defined retention policy can be applied on multiple
  - Evidence: README.md#Capabilities
- Multiple user-defined retention policies can be applied on a single: Multiple user-defined retention policies can be applied on a single
  - Evidence: README.md#Capabilities

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: google-api-python-client, google-cloud-logging, jsonschema, monotonic, oauth2client, requests, werkzeug
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: scheduler/main.py, scheduler/__init__.py, scheduler/filestore_instance.py

## Setup and usage

- Getting Started: Refer to this public tutorial.

## Limitations and caveats

- Known Limitations: 1. Filestore Enterprise instance supports up to 240 snapshots.
- Known Limitations: 2. The function only deletes a single snapshot when needed, even if there are
- Known Limitations: more scheduler snapshots than defined in the retention policy configuration file,
- Known Limitations: or if the retention policy configuration file is updated to keep fewer snapshots
- Known Limitations: 3. Reducing the number of snapshots in the configuration file, will not result
- Known Limitations: in deleting multiple snapshots in the instance.
- Known Limitations: Instead, delete the redundant snapshots manually.

## Evidence and provenance

- README: https://github.com/GoogleCloudPlatform/Filestore-Snapshot-Scheduler/blob/main/README.md
- README SHA: 598f0f794ba9c1e5de317406523af21f9597a9e1
- Manifests: scheduler/requirements.txt
- Sampled source files: scheduler/main.py, scheduler/__init__.py, scheduler/filestore_instance.py
- Git tree state: captured
- Evidence fingerprint: b77e1474eee7177ff5120f54840031ebfa54c2f99e17fe6f437e8676d333582d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
