# awslabs/aws-service-eol-data

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/aws-service-eol-data](https://github.com/awslabs/aws-service-eol-data)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/aws-service-eol-data/blob/main/README.md)
- README blob SHA: 418809550cb79893e8cf8db0d6ee4248205ed2e9
- README bytes captured: 28955
- README truncated at capture limit: False
- Repository ID: 1372112781
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Machine-readable JSON dataset of AWS service version end-of-support and extended-support dates across EKS, RDS, Aurora, Lambda, ElastiCache, OpenSearch, MSK, Amazon MQ, and DocumentDB. Each entry includes lifecycle status, dates, post-support behavior, a confidence level, and a source URL. Sourced from official AWS documentation.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-26T03:10:21+00:00

### Short excerpt (up to 300 words)

> Model modality and live **Upgrade planning and roadmaps** See SECURITY.md.

### README headings

- AWS Service End-of-Life Data
- Why This Exists
- Examples of use cases
- File Location
- Schema
- Top-level fields
- Field Reference
- Joining to your inventory
- `lifecycleEvents[]`
- `behavior` (what happens at an event)
- Status Values
- Provenance
- Corrected dates
- Reading dates and status
- Usage Examples
- Find versions entering Extended Support within 90 days
- Cross-reference your RDS fleet
- Scan EKS clusters across regions
- Lambda runtime check in CI/CD
- Fails closed if the runtime is not found or is past support.
- What happens after support ends
- Covered Services
- Companion dataset: cost
- Companion lookup: Bedrock model capability (modality)
- join: eol entry.version == fm modelId  ->  inputModalities / outputModalities / modelLifecycle.status
- normalize throughput suffixes (:24k/:300k) off the modelId before joining
- Update Cadence
- Contributing
- Important: Validation for Critical Decisions
- Disclaimer

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Companion lookup: Bedrock model capability (modality)

> Model modality and live

### Getting started and usage: Examples of use cases

> **Upgrade planning and roadmaps**

### Limitations and security: Security

> See SECURITY.md.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Unknown | Not captured |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 30
- Forks at capture: 2
- Last updated: 2026-11-20T11:42:35Z
- Last pushed: 2026-10-24T19:50:55Z
- Topics: aurora, aws, dataset, deprecation, documentdb, eks, elasticache, elasticsearch, end-of-life, end-of-support, eol, json, lambda, lifecycle, msk, opensearch, rds, upgrade-planner

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/aws-service-eol-data)
- [README](https://github.com/awslabs/aws-service-eol-data/blob/main/README.md)
- [Issues](https://github.com/awslabs/aws-service-eol-data/issues)
- [Releases](https://github.com/awslabs/aws-service-eol-data/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
