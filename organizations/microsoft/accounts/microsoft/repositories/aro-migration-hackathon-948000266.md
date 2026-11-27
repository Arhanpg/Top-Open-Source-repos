# microsoft/aro-migration-hackathon

- Company: Microsoft
- GitHub account: [https://github.com/microsoft](https://github.com/microsoft)
- Mapping status: verified
- Repository: [microsoft/aro-migration-hackathon](https://github.com/microsoft/aro-migration-hackathon)
- Default branch: main
- README: [Open upstream README](https://github.com/microsoft/aro-migration-hackathon/blob/main/docs/readme.md)
- README blob SHA: b37f72edfad0ce2848b65dcdb644c3387f1cb6ad
- README bytes captured: 16389
- README truncated at capture limit: False
- Repository ID: 948000266
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Hackathon content prepared for a joint Red Hat and GitHub + Azure Hackathon. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:53:30+00:00

### Short excerpt (up to 300 words)

> Welcome to the Azure The Task Manager application Before starting, ensure you oc adm policy add-scc-to-user

### README headings

- ARO Migration Hackathon Guide
- Overview
- Prerequisites
- Getting Started
- 1. Fork & Clone the Repository
- 2. Set Up Azure Resources
- Make the script executable
- Run the setup script
- Understanding the Application
- 1. Application Architecture
- 2. Running Locally with Docker Compose
- Understanding Docker Compose
- Application Architecture
- 3. Exploring the Database (Optional)
- 4. Testing the API (Optional)
- Get all tasks
- Create a new task
- Update a task (replace TASK_ID with actual ID)
- Delete a task (replace TASK_ID with actual ID)
- Hackathon Challenges
- Challenge 1: Containerisation and ARO Deployment
- PreReq: Set ACR value in your manifests
- Navigate back to the repository root
- Option 1: Deploy Using the OpenShift CLI
- Step 1: Build and Push Container Images
- Log in to your ACR.
- Navigate to the frontend directory
- Build using the OpenShift-specific Dockerfile
- Push the frontend image
- Navigate to the backend directory

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Overview

> Welcome to the Azure

### Architecture and design: 1. Application Architecture

> The Task Manager application

### Technology and requirements: Prerequisites

> Before starting, ensure you

### Limitations and security: Add security context constraints to allow service account to create frontend pod with custom security contexts for nginx.conf

> oc adm policy add-scc-to-user

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 16,643 |
| JavaScript | 6,905 |
| CSS | 1,897 |
| HTML | 464 |
| Dockerfile | 440 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- on-prem-app/backend/Dockerfile (capture: captured)
- on-prem-app/backend/package.json (capture: captured) — dependency clues: cors, express, jest, mongoose, nodemon
- on-prem-app/frontend/Dockerfile (capture: captured)
- on-prem-app/frontend/package.json (capture: captured) — dependency clues: react, react-dom, react-scripts

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 5
- Forks at capture: 10
- Last updated: 2026-09-22T06:25:52Z
- Last pushed: 2026-07-10T12:50:50Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/microsoft/aro-migration-hackathon)
- [README](https://github.com/microsoft/aro-migration-hackathon/blob/main/docs/readme.md)
- [Issues](https://github.com/microsoft/aro-migration-hackathon/issues)
- [Releases](https://github.com/microsoft/aro-migration-hackathon/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
