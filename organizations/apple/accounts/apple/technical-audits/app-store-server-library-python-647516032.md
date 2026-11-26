# apple/app-store-server-library-python

- Company: Apple
- Account: apple
- Repository: https://github.com/apple/app-store-server-library-python
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:34:05+00:00

## Project purpose

The Python server library for the App Store Server API, App Store Server Notifications, Retention Messaging API, and Advanced Commerce API. Also available in Swift, Node.js, and Java.

## Why this project is used

The Python server library for the App Store Server API and App Store Server Notifications.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Lua
- Frameworks/libraries: Unknown / not established
- Dependency names: PyJWT, asn1, attrs, cattrs, cryptography, httpx, pyOpenSSL, requests, sphinx
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: appstoreserverlibrary/__init__.py, appstoreserverlibrary/jws_signature_creator.py, appstoreserverlibrary/models/__init__.py, appstoreserverlibrary/models/AbstractAdvancedCommerceBaseItem.py

## Setup and usage

- API Usage: from appstoreserverlibrary.api_client import AppStoreServerAPIClient, APIException
- API Usage: from appstoreserverlibrary.models.Environment import Environment
- API Usage: private_key = read_private_key("/path/to/key/SubscriptionKey_ABCDEFGHIJ.p8") # Implementation will vary
- API Usage: key_id = "ABCDEFGHIJ"
- API Usage: issuer_id = "99b16628-15e4-4668-972b-eeff55eeff55"
- API Usage: bundle_id = "com.example"
- API Usage: environment = Environment.SANDBOX
- API Usage: client = AppStoreServerAPIClient(private_key, key_id, issuer_id, bundle_id, environment)

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/apple/app-store-server-library-python/blob/main/README.md
- README SHA: 8acdf5ceb1127bac8919d496d98ad376624aeedd
- Manifests: pyproject.toml, requirements.txt, docs/requirements.txt
- Sampled source files: appstoreserverlibrary/__init__.py, appstoreserverlibrary/jws_signature_creator.py, appstoreserverlibrary/models/__init__.py, appstoreserverlibrary/models/AbstractAdvancedCommerceBaseItem.py
- Git tree state: captured
- Evidence fingerprint: eef66117da7e7871f6ac371f5b851013b4aec7b41d2ed8e8b55ddc84b979b498

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
