# awslabs/LogParserForKarpenter

- Company: Amazon
- GitHub account: [https://github.com/awslabs](https://github.com/awslabs)
- Mapping status: official-directory-listed
- Repository: [awslabs/LogParserForKarpenter](https://github.com/awslabs/LogParserForKarpenter)
- Default branch: main
- README: [Open upstream README](https://github.com/awslabs/LogParserForKarpenter/blob/main/README.md)
- README blob SHA: bbde75eb028345040067d27f03fd32d8b00c62ef
- README bytes captured: 16449
- README truncated at capture limit: False
- Repository ID: 967291757
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Log parser for Karpenter controller logs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T04:19:30+00:00

### Short excerpt (up to 300 words)

> ./bin/lp4kchain lp4k-output.csv output.png **Options:** See CONTRIBUTING for more

### README headings

- Log Parser for Karpenter (LogParserForKarpenter)
- Parse only events between 12:00 and 14:00
- Parse everything from 16:00 onwards
- Nodeclaim Replacement Tracking
- S3 Upload Configuration
- Enable S3 upload
- Run lp4k with file input
- Or run in K8s streaming mode
- To start using LogParserForKarpenter
- lp4kcm
- Read ConfigMap from a specific context
- Or use the environment variable
- Analyse LogParserForKarpenter output
- Automated Analysis
- lp4kstats
- Generate Markdown report to stdout via pipe
- Generate Markdown report to file
- Generate HTML report (recommended — fully rendered charts, no external tools needed)
- Generate HTML with 1-minute interval and bar charts
- lp4kchain
- Generate Mermaid source (.mmd) to stdout via pipe
- Generate Mermaid source to file
- Generate PNG directly (requires mmdc, see doc/lp4kchain-install.md)
- Show all chains including short 1-to-1 replacements
- Show chains with at least 4 nodes, up to 20 chains
- Manual Analysis
- indexed header
- print nodeclaim[index/column=1], nodereadytime[13],nodereadytimesec[14]
- search for specific value sof a specific nodeclaim
- combine directly with lp4k and raw Karpenter controller logs

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Generate PNG directly (requires mmdc, see doc/lp4kchain-install.md)

> ./bin/lp4kchain lp4k-output.csv output.png **Options:**

### Limitations and security: Security

> See CONTRIBUTING for more

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 104,698 |
| Makefile | 2,410 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/andrew-d/go-termutil, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 23
- Forks at capture: 2
- Last updated: 2026-10-06T15:09:13Z
- Last pushed: 2026-07-06T14:17:01Z
- Topics: k8s, karpenter

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/awslabs/LogParserForKarpenter)
- [README](https://github.com/awslabs/LogParserForKarpenter/blob/main/README.md)
- [Issues](https://github.com/awslabs/LogParserForKarpenter/issues)
- [Releases](https://github.com/awslabs/LogParserForKarpenter/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
