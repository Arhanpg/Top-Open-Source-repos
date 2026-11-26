# awslabs/DRS-Settings-Tool

- Company: Amazon
- Account: awslabs
- Repository: https://github.com/awslabs/DRS-Settings-Tool
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:40:21+00:00

## Project purpose

This tool was created to help change settings in bulk for multiple Elastic Disaster Recovery Service(DRS) Source Servers.

## Why this project is used

This tool was created to help change settings in bulk for multiple Elastic Disaster Recovery Service(DRS) Source Servers.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: Unknown / not established
- Build/package tools: Unknown / not established
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: classes/basic_launch_settings.py, classes/launch_template_settings.py, classes/replication_settings.py, classes/source_server_info.py

## Setup and usage

- Installation: - Clone or download the desired file format locally on the computer in which you have the AWS credentials file configured, and ensure AWS Endpoint connectivity for API calls.
- Usage: 1. Ensure you configured your AWS credentials file and are pointing to the correct region. You can do this by setting the appropriate region in your credentials profile specific config settings (noted in the pre-requisites).
- Usage: 2. Run the "get_settings.py" file. You will be prompted to enter the "Target Account ID". The "Target Account" will be the account in which your source servers would launch into during recovery. For single account use, use that single account number. For accounts with DRS source servers that are extended, use the account number where the servers ar
- Usage: 3. Open the "DRS_Settings.csv" file in the CSV file editor of choice(Microsoft Excel for example), and make all the desired changes for each source server. **NOTE** It is important that you do NOT modify the "DRS_Settings_DO_NOT_EDIT.csv" file as we will use this as a comparison to limit AWS API calls being made for servers that have not been chang
- Usage: 4. Run the "update_settings.py" file to update the settings for all your Source Servers in DRS.
- Usage: 5. A log will be generated in the directory named "DRS-Update-Tool.log", for troubleshooting purposes.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/awslabs/DRS-Settings-Tool/blob/main/README.md
- README SHA: e7a3939f974dd0f474c8e6bc34ce8f2f1a27a74b
- Manifests: none
- Sampled source files: classes/basic_launch_settings.py, classes/launch_template_settings.py, classes/replication_settings.py, classes/source_server_info.py
- Git tree state: captured
- Evidence fingerprint: 46dbf07445f835281212081e0ccc853fd1c248ac917bcc457653ea82a7a6a5d5

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
