# aws-observability/amp-cardinality-insights

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/amp-cardinality-insights](https://github.com/aws-observability/amp-cardinality-insights)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/amp-cardinality-insights/blob/main/README.md)
- README blob SHA: f898cfc314f3e2a5ab4d6af43a1bc60b6da08749
- Repository ID: 882446177
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:38:05+00:00

### Short excerpt (up to 100 words)

> This project helps you have visibility into high cardinality metrics from an Amazon Managed Service for Prometheus workspace. **Amazon Managed Service for Prometheus - Cardinality insights** is maintained by AWS Solution Architects. It is not part of an AWS service and support is provided as best-effort by the community. To post feedback, submit feature ideas, or report bugs, please use the Issues section of this GitHub repo. If you are interested in contributing, see the Contribution guide. This project proposes a serverless solution that you deploy and operate on your account. You give read/write permissions to your workspace and: -

### README headings

- Cardinality insights - Amazon Managed Service for Prometheus
- Support & Feedback
- How it works
- Architecture
- Costs
- Deploy
- Import Grafana dashboard
- Teardown
- stack name should be amp-cardinality-insights if you didn't specified your own

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 17,528 |
| Python | 1,465 |
| Shell | 1,241 |
| Smarty | 548 |
| Makefile | 412 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- lambda/Makefile (capture: captured)
- lambda/aggregate-counts/go.mod (capture: captured) — dependency clues: github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/google/uuid, github.com/jmespath/go-jmespath, github.com/pmezard/go-difflib, github.com/stretchr/testify, go.uber.org/multierr, go.uber.org/zap, gopkg.in/yaml.v3
- lambda/aggregate-counts/Makefile (capture: captured)
- lambda/count-metrics/go.mod (capture: captured) — dependency clues: github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go, github.com/google/uuid, github.com/stretchr/testify, go.uber.org/multierr, go.uber.org/zap
- lambda/count-metrics/Makefile (capture: captured)
- lambda/metric-names/go.mod (capture: captured) — dependency clues: github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go, github.com/google/uuid, github.com/stretchr/testify, go.uber.org/multierr, go.uber.org/zap

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 4
- Forks at capture: 1
- Last updated: 2026-10-04T10:40:06Z
- Last pushed: 2024-11-19T08:17:10Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/amp-cardinality-insights)
- [README](https://github.com/aws-observability/amp-cardinality-insights/blob/main/README.md)
- [Issues](https://github.com/aws-observability/amp-cardinality-insights/issues)
- [Releases](https://github.com/aws-observability/amp-cardinality-insights/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
