# GoogleCloudPlatform/ces-twilio-adapter

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/ces-twilio-adapter](https://github.com/GoogleCloudPlatform/ces-twilio-adapter)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/ces-twilio-adapter/blob/main/README.md)
- README blob SHA: c38a680a0274746a31ce800363995da7169b9109
- README bytes captured: 21438
- README truncated at capture limit: False
- Repository ID: 1072151628
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T05:27:34+00:00

### Short excerpt (up to 300 words)

> Rich Communication Services (RCS) Google Cloud SDK (gcloud)

### README headings

- CES Twilio Adapter
- Table of Contents
- What is RCS?
- Deployment to Cloud Run
- 1. Prerequisites
- 2. Configuration
- MUST BE EDITED
- USUALLY EDITED AFTER FIRST DEPLOYMENT
- TWILIO CONFIGURATION
- SECRET CONFIGURATION (see Secrets and Authentication section)
- The full path to the secret containing the OAuth2 token for the agent.
- The full path to the secret containing your Twilio Auth Token.
- PHONE NUMBER MAPPING CONFIGURATION (see "Phone Number to Agent Mapping" section)
- Choose ONE of the following methods.
- 1. Firestore (recommended for production)
- 2. Local JSON file (for development/testing)
- NUMBERS_CONFIG_FILE="number_mappings.json"
- GENERALLY UNCHANGED
- 3. Phone Number to Agent Mapping
- Method 1: Firestore (Recommended for Production)
- Method 2: Local JSON File (for Development/Testing)
- 4. Secrets and Authentication Setup
- Twilio Auth Token Secret
- Authentication to the Conversational AI Agent
- Method 1: Application Default Credentials (Default)
- Method 2: Token from Secret Manager (Override)
- 5. Grant IAM Permissions
- 6. Deploy the Service
- 7. Final Configuration
- Local Development & Testing

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: What is RCS?

> Rich Communication Services (RCS)

### Technology and requirements: 1. Prerequisites

> Google Cloud SDK (gcloud)

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 44,197 |
| Shell | 3,540 |
| Dockerfile | 1,416 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: black, flake8, isort
- requirements.txt (capture: captured) — dependency clues: audioop-lts, fastapi, google-auth, google-cloud-firestore, google-cloud-secret-manager, gunicorn, python-dotenv, python-multipart, twilio, uvicorn, websockets

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 12
- Forks at capture: 13
- Last updated: 2026-08-25T19:23:22Z
- Last pushed: 2026-05-22T13:48:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/ces-twilio-adapter)
- [README](https://github.com/GoogleCloudPlatform/ces-twilio-adapter/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/ces-twilio-adapter/issues)
- [Releases](https://github.com/GoogleCloudPlatform/ces-twilio-adapter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
