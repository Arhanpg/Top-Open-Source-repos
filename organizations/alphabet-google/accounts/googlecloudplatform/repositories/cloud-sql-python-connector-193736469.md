# GoogleCloudPlatform/cloud-sql-python-connector

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/cloud-sql-python-connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/README.md)
- README blob SHA: dd4d5aed593b2d466371601d2478669dc638e133
- README bytes captured: 33408
- README truncated at capture limit: False
- Repository ID: 193736469
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A Python library for connecting securely to your Cloud SQL instances.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T20:47:58+00:00

### Short excerpt (up to 300 words)

> The _Cloud SQL Python You can install this Hybrid post-quantum key exchange

### README headings

- Installation
- MySQL
- Postgres
- pg8000
- psycopg
- asyncpg
- SQL Server
- APIs and Services
- Credentials
- Usage
- How to use this Connector
- initialize Connector object
- initialize SQLAlchemy connection pool with Connector
- Or with Postgres (psycopg):
- insert statement
- Configuring the Connector
- Note: all parameters below are optional
- Using Connector as a Context Manager
- initialize Cloud SQL Python Connector as context manager
- Configuring a Lazy Refresh (Cloud Run, Cloud Functions etc.)
- Specifying IP Address Type
- Automatic IAM Database Authentication
- SQL Server (MSSQL)
- Active Directory Authentication
- Using Advanced Disaster Recovery and DNS domain names to identify instances
- Using Advanced Recovery Write Endpoint DNS Name
- Configure your DNS Records
- Configure the connector
- initialize Cloud SQL Python Connector with `resolver=DnsResolver`
- Automatic failover using DNS domain names

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> The _Cloud SQL Python

### Getting started and usage: Installation

> You can install this

### Limitations and security: Backwards compatibility

> Hybrid post-quantum key exchange

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 548,261 |
| Shell | 5,785 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured) — dependency clues: PyMySQL, Requests, aiohttp, asyncpg, cryptography, dnspython, google-auth, google-cloud-sql, pg8000, psycopg, python-tds
- requirements.txt (capture: captured) — dependency clues: PyMySQL, certifi, cryptography, filelock, google-auth, google-cloud-sql, idna, packaging, pip, virtualenv
- samples/cloudrun/mysql/Dockerfile (capture: captured)
- samples/cloudrun/mysql/requirements.txt (capture: captured) — dependency clues: Flask, cloud-sql-python-connector, google-cloud-secret-manager, gunicorn, sqlalchemy
- samples/cloudrun/postgres/Dockerfile (capture: captured)
- samples/cloudrun/postgres/requirements.txt (capture: captured) — dependency clues: Flask, cloud-sql-python-connector, google-cloud-secret-manager, gunicorn, sqlalchemy

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 346
- Forks at capture: 92
- Last updated: 2026-11-19T21:26:54Z
- Last pushed: 2026-11-23T18:32:24Z
- Topics: cloud-sql, libraries, python

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)
- [README](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues)
- [Releases](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
