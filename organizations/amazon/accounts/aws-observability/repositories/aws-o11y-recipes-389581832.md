# aws-observability/aws-o11y-recipes

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-o11y-recipes](https://github.com/aws-observability/aws-o11y-recipes)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-o11y-recipes/blob/main/README.md)
- README blob SHA: 8263cdb9498391b6bdd6b2158c85bd8a45467d32
- Repository ID: 389581832
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

recipes for observability solutions at AWS 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:38:15+00:00

### Short excerpt (up to 100 words)

> This repo has been archived and the project merged into https://github.com/aws-observability/observability-best-practices. *** See [aws-observability.github.io/aws-o11y-recipes/][recipes-live]. See CONTRIBUTING for more information. This library is licensed under the MIT-0 License. See the LICENSE file. To write recipes we're using [MkDocs][mkdocs] with the [Material][mkdocs-material] theme. MkDocs is a static site generator, converting the Markdown files you edit to static HTML pages which are then served as via GitHub pages In order to locally preview the recipes site you need to have MkDocs installed: * Make sure to upgrade pip installer pip3 install --upgrade pip pip --version * Install mkdocs pip install mkdocs * Validate

### README headings

- IMPORTANT NOTE
- AWS o11y recipes
- Security
- License
- Writing recipes
- Local preview
- Publishing

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 24,246 |
| TypeScript | 5,613 |
| Python | 5,141 |
| Shell | 3,246 |
| JavaScript | 1,092 |
| HTML | 892 |
| Dockerfile | 421 |
| Makefile | 266 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- sandbox/CWMetricStreamExporter/Makefile (capture: captured)
- sandbox/CWMetricStreamExporter/package.json (capture: captured)
- sandbox/ho11y/Dockerfile (capture: captured)
- sandbox/ho11y/go.mod (capture: captured) — dependency clues: github.com/bitly/go-simplejson, github.com/bmizerany/assert, github.com/c2h5oh/datasize, github.com/catalint/datasize, github.com/gorilla/mux, github.com/prometheus/client_golang, github.com/sirupsen/logrus, go.opentelemetry.io/contrib/instrumentation/github.com/gorilla/mux/otelmux, go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp, go.opentelemetry.io/contrib/propagators/aws, go.opentelemetry.io/otel, go.opentelemetry.io/otel/exporters/otlp, go.opentelemetry.io/otel/sdk, go.opentelemetry.io/otel/sdk/metric, go.opentelemetry.io/otel/trace
- sandbox/CWMetricStreamExporter/cdk/package.json (capture: captured) — dependency clues: @aws-cdk/assert, @aws-cdk/aws-iam, @aws-cdk/aws-kinesisfirehose, @aws-cdk/aws-kinesisfirehose-destinations, @aws-cdk/core, @types/jest, @types/js-yaml, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, aws-cdk, eslint, eslint-config-airbnb-base, eslint-plugin-import, jest, js-yaml, source-map-support, ts-jest, ts-node, typescript
- sandbox/CWMetricStreamExporter/lambda/go.mod (capture: captured) — dependency clues: github.com/aws/aws-lambda-go, github.com/aws/aws-sdk-go, github.com/gogo/protobuf, github.com/golang/snappy, github.com/prometheus/prometheus, golang.org/x/net, google.golang.org/genproto, google.golang.org/grpc, google.golang.org/protobuf

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 110
- Forks at capture: 36
- Last updated: 2026-10-22T12:54:11Z
- Last pushed: 2023-01-11T14:23:43Z
- Topics: amazon-web-services, aws, cloudwatch, fluentbit, grafana, observability, opentelemetry, prometheus

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-o11y-recipes)
- [README](https://github.com/aws-observability/aws-o11y-recipes/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-o11y-recipes/issues)
- [Releases](https://github.com/aws-observability/aws-o11y-recipes/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
