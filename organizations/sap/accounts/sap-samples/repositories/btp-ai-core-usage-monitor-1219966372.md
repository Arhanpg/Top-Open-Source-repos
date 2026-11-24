# SAP-samples/btp-ai-core-usage-monitor

- Company: SAP
- GitHub account: [https://github.com/SAP-samples](https://github.com/SAP-samples)
- Mapping status: official-directory-listed
- Repository: [SAP-samples/btp-ai-core-usage-monitor](https://github.com/SAP-samples/btp-ai-core-usage-monitor)
- Default branch: main
- README: [Open upstream README](https://github.com/SAP-samples/btp-ai-core-usage-monitor/blob/main/README.md)
- README blob SHA: 721bd611d6eb8b90900fe0d7616bcc262f3b1d02
- README bytes captured: 24505
- README truncated at capture limit: False
- Repository ID: 1219966372
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Python background agent that runs on SAP BTP Cloud Foundry and monitors daily AI Core capacity unit consumption. When consumption approaches a configured monthly spending limit, it sends notifications via SMTP email or SAP Alert Notification Service (ANS).

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T06:46:03+00:00

### Short excerpt (up to 300 words)

> pip install -r requirements.txt ┌─────────────────────────────────────────────────────────────┐ │ SAP BTP 1. **SAP BTP subaccount** The app uses **SAP

### README headings

- AI Core Consumption Monitor
- How It Works
- Project Structure
- Configuration Reference
- Prerequisites
- Step-by-Step Deployment
- 1. Create the XSUAA service instance
- 2. Create and bind the UAS service instance
- 3. Configure notifications
- 4. Deploy
- 5. Set secrets
- Only required if ENABLE_SMTP=true:
- Only required when using explicit credentials (not CF service binding):
- cf restart is sufficient after cf set-env (no rebuild needed)
- Use cf restage only if you changed services: bindings or requirements.txt
- 6. Verify
- Check app is running – the output shows the assigned random route
- Get just the URL
- View logs
- Check health endpoint (no auth required)
- Get a Bearer token from XSUAA (clientid/clientsecret from the xsuaa service key)
- View last monitoring result
- Manually trigger a check (dry run – no emails sent)
- Manually trigger a real check (sends notifications if thresholds are met)
- Multi-team Monitoring
- Team A — resource group "default", 50 CU limit
- Team B — resource group "research", 30 CU limit
- API Endpoints
- `/trigger` request body (optional)
- `/status` response example

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Install dependencies

> pip install -r requirements.txt

### Architecture and design: How It Works

> ┌─────────────────────────────────────────────────────────────┐ │ SAP BTP

### Technology and requirements: Prerequisites

> 1. **SAP BTP subaccount**

### Limitations and security: Security

> The app uses **SAP

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 66,229 |
| Procfile | 83 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: APScheduler, Flask, gunicorn, python-dotenv, requests, sap-xssec

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 5
- Forks at capture: 2
- Last updated: 2026-09-01T11:25:37Z
- Last pushed: 2026-11-09T10:49:30Z
- Topics: alert-notifications, cloud-foundry, cost-monitoring, flask, python, sap-ai-core, sap-btp, sap-samples, spending-alerts, usage-analytics

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/SAP-samples/btp-ai-core-usage-monitor)
- [README](https://github.com/SAP-samples/btp-ai-core-usage-monitor/blob/main/README.md)
- [Issues](https://github.com/SAP-samples/btp-ai-core-usage-monitor/issues)
- [Releases](https://github.com/SAP-samples/btp-ai-core-usage-monitor/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
