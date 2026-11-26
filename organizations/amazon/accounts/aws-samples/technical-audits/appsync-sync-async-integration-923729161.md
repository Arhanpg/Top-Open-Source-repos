# aws-samples/AppSync_Sync_Async_Integration

- Company: Amazon
- Account: aws-samples
- Repository: https://github.com/aws-samples/AppSync_Sync_Async_Integration
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:53:57+00:00

## Project purpose

This is a demo application that consists of an API converting a synchronous request coming from the client into an asynchronous request to the backend using AppSync Events. In order to simulate an asynchronous backend processing, we are using an asynchronous AWS Step Functions workflow, which receives an event with Name and Surname as input, waits 10 seconds and then posts an event with the full name at the AppSync Event channel. While the asynchrnous procesing is execute, the synchronous API subscribes to the AppSync channel in order to be notified when the event arrives there.

## Why this project is used

This is a demo application that consists of an API converting a synchronous request coming from the client into an asynchronous request to the backend using AppSync Events. In order to simulate an asynchronous backend processing, we are using an asynchronous AWS Step Functions workflow, which receives an event with Name and Surname as input, waits 10 seconds and then posts an event with the full name at the AppSync Event channel. While the asynchrnous procesing is execute, the synchronous API subscribes to the AppSync channel in order to be notified when the event arrives there.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Unknown / not established
- Frameworks/libraries: Unknown / not established
- Dependency names: websocket-client
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: function/app.py, function/secretsmanager.py, function/websocket_handler.py, function/workflow.py

## Setup and usage

No setup information established.

## Limitations and caveats

- Security Considerations: - API Gateway endpoints are publicly accessible
- Security Considerations: - Lambda function has restricted IAM permissions
- Security Considerations: - Secrets are managed through AWS Secrets Manager
- Security Considerations: - All sensitive data is encrypted at rest
- Security Considerations: - API authentication is handled via API keys

## Evidence and provenance

- README: https://github.com/aws-samples/AppSync_Sync_Async_Integration/blob/main/README.md
- README SHA: 356718e42b18edbb956dc23ac4d0cc57341f61e2
- Manifests: function/requirements.txt
- Sampled source files: function/app.py, function/secretsmanager.py, function/websocket_handler.py, function/workflow.py
- Git tree state: captured
- Evidence fingerprint: da14ceae0d6323f01b3093e348831efcb1c518bdc2d322d99538e2ba7b593dce

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
