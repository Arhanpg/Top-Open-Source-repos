# awslabs/chaos-machine

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/chaos-machine](https://github.com/awslabs/chaos-machine)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/chaos-machine/blob/main/README.md)
- README blob SHA: e8ecb301c47822b9c3fd3050b75ad2cee7ce8d08
- README bytes captured: 24986
- README truncated at capture limit: False
- Repository ID: 946146729
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Chaos Machine is a complete chaos engineering workflow that enables customers to run controlled chaos experiments with the AWS Fault Injection Service and test hypotheses related to system behavior using metrics and alarms from CloudWatch and Prometheus.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T05:20:23+00:00

### Short excerpt (up to 300 words)

> Review the architecture diagram

### README headings

- Chaos Machine
- Architecture
- Usage
- Chaos machine input and execution
- Experiment templates
- Examples
- Execution inputs
- Prometheus
- Running a test
- Step Functions console:
- Pytest
- Precommit
- Requirements
- Providers
- Modules
- Resources
- Inputs
- Outputs

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage

> Review the architecture diagram

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 25,338 |
| HCL | 17,325 |
| Makefile | 1,607 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)
- requirements.txt (capture: captured) — dependency clues: pre-commit
- examples/tests/requirements.txt (capture: captured) — dependency clues: boto3, pytest, pytest-xdist
- lambda/layer/requirements.txt (capture: captured) — dependency clues: jsonschema
- examples/experiments/ec2-cpu-stress/requirements.txt (capture: captured) — dependency clues: boto3, flask, psutil, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 11
- Forks at capture: 1
- Last updated: 2026-11-10T10:44:36Z
- Last pushed: 2025-10-15T23:13:08Z
- Topics: chaos-engineering, chaos-testing, fault-injection, fault-injection-service, fis

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/chaos-machine)
- [README](https://github.com/awslabs/chaos-machine/blob/main/README.md)
- [Issues](https://github.com/awslabs/chaos-machine/issues)
- [Releases](https://github.com/awslabs/chaos-machine/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
