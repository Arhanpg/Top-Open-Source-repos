# GoogleCloudPlatform/Open_Data_QnA

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/Open_Data_QnA](https://github.com/GoogleCloudPlatform/Open_Data_QnA)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/Open_Data_QnA/blob/main/README.md)
- README blob SHA: 90b1f976d3c63daffc52af51bb190598f734c97c
- README bytes captured: 22617
- README truncated at capture limit: False
- Repository ID: 765294445
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The Open Data QnA python library enables you to chat with your databases by leveraging LLM Agents on Google Cloud.  Open Data QnA enables a conversational approach to interacting with your data by implementing state-of-the-art NL2SQL / Text2SQL methods.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T03:44:31+00:00

### Short excerpt (up to 300 words)

> _______________ _______________ ✨ Overview pip uninstall poetry -y Make sure that Google

### README headings

- Database Connectors
- Vector Stores
- Agents
- Clone the repository and switch to the correct directory
- 🚧 **Prerequisites**
- A) Jupyter Notebook Based Approach
- 💻 **Install Code Dependencies (Create and setup venv)**
- **All commands in this cell to be run on the terminal (typically Ctrl+Shift+`) where your notebooks are running**
- Install poetry
- 1. Run the [1_Setup_OpenDataQnA](/notebooks/1_Setup_OpenDataQnA.ipynb) (Run Once for Initial Setup)
- 2. Run the [2_Run_OpenDataQnA](/notebooks/2_Run_OpenDataQnA.ipynb)
- 3. [Loading Known Good SQL Examples](/notebooks/3_LoadKnownGoodSQL.ipynb)
- B) Command Line Interface (CLI) Based Approach
- 1. Add Configuration values for the solution in [config.ini](/config.ini)
- 2. Creating Virtual Environment and Install Dependencies
- 3. Run [env_setup.py](/env_setup.py) to create vector store based on the configuration you did in Step 1
- 4. Run [opendataqna.py](/opendataqna.py) to run the pipeline you just setup
- Enable the SQL debugger:
- Execute the final generated SQL:
- Change the number of debugging rounds:
- Adjust similarity thresholds:
- C) Using Terraform to deploy the solution
- Data Sources Set Up
- Enable Firebase
- Terraform deployment
- After deployment

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> _______________ _______________ ✨ Overview

### Getting started and usage: Install poetry

> pip uninstall poetry -y

### Technology and requirements: 🚧 **Prerequisites**

> Make sure that Google

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 369,388 |
| Dart | 303,336 |
| Jupyter Notebook | 88,660 |
| HTML | 82,006 |
| TypeScript | 74,272 |
| SCSS | 40,715 |
| HCL | 22,373 |
| Shell | 7,867 |
| Ruby | 1,414 |
| Dockerfile | 901 |
| Swift | 689 |
| Kotlin | 122 |
| Objective-C | 38 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- pyproject.toml (capture: captured) — dependency clues: Flask, Werkzeug, cloud-sql-python-connector, firebase-admin, flask-cors, fsspec, gcsfs, google, google-api-python-client, google-cloud, google-cloud-aiplatform, google-cloud-bigquery, google-cloud-bigquery-connection, google-cloud-firestore, gunicorn, ipykernel, langchain, pandas, pandas-gbq, pg8000
- frontend/package.json (capture: captured) — dependency clues: @angular-devkit/build-angular, @angular/animations, @angular/cdk, @angular/cli, @angular/common, @angular/compiler, @angular/compiler-cli, @angular/core, @angular/fire, @angular/forms, @angular/material, @angular/platform-browser, @angular/platform-browser-dynamic, @angular/platform-server, @angular/router, @angular/ssr, @types/express, @types/jasmine, @types/node, angular-google-charts
- frontend/frontend-flutter/android/build.gradle (capture: captured)
- frontend/frontend-flutter/android/app/build.gradle (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 231
- Forks at capture: 77
- Last updated: 2026-11-18T19:49:00Z
- Last pushed: 2026-11-18T18:54:55Z
- Topics: gemini, genai, nl2sql, opendataqna, sql

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/Open_Data_QnA)
- [README](https://github.com/GoogleCloudPlatform/Open_Data_QnA/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/Open_Data_QnA/issues)
- [Releases](https://github.com/GoogleCloudPlatform/Open_Data_QnA/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
