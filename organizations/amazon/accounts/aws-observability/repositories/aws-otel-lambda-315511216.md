# aws-observability/aws-otel-lambda

- Company: Amazon
- GitHub account: [https://github.com/aws-observability](https://github.com/aws-observability)
- Mapping status: official-directory-listed
- Repository: [aws-observability/aws-otel-lambda](https://github.com/aws-observability/aws-otel-lambda)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-observability/aws-otel-lambda/blob/main/README.md)
- README blob SHA: bdeaadd10221ce8202712ddcfc42b5646d761160
- Repository ID: 315511216
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

AWS Distro for OpenTelemetry - AWS Lambda

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:07:46+00:00

### Short excerpt (up to 100 words)

> As a downstream Repo of opentelemetry-lambda, ___aws-otel-lambda___ publishes AWS managed OpenTelemetry Lambda layers that are preconfigured for use with AWS services and bundle the reduced ADOT Collector. Users can onboard to OpenTelemetry in their existing Lambda functions by adding these ready-made layers directly. - Python layer **aws-otel-python-<amd64|arm64>-ver-1-32-0** contains OpenTelemetry Python `v1.32.0` and ADOT Collector for Lambda `v0.49.0` - Nodejs layer **aws-otel-nodejs-<amd64|arm64>-ver-1-30-2** contains OpenTelemetry JavaScript Core `v1.30.0` with AWS Lambda Instrumentation `v0.50.3` and ADOT Collector for Lambda `v0.49.0` - Java-Wrapper layer **aws-otel-java-wrapper-<amd64|arm64>-ver-1-32-0** contains OpenTelemetry Java `v1.32.0` and ADOT Collector for Lambda `v0.49.0` - Java-Agent layer **aws-otel-java-agent-<amd64|arm64>-ver-1-32-0** contains AWS Distro for OpenTelemetry

### README headings

- AWS managed OpenTelemetry Lambda Layers
- Sample Apps
- ADOT Lambda Layer available components
- Security
- Support
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| HCL | 72,573 |
| Java | 13,323 |
| Shell | 10,263 |
| Python | 8,014 |
| Go | 4,180 |
| TypeScript | 2,559 |
| C# | 1,793 |
| JavaScript | 1,223 |
| Makefile | 667 |
| Dockerfile | 112 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- java/build.gradle.kts (capture: captured)
- nodejs/wrapper-adot/package.json (capture: captured) — dependency clues: @opentelemetry/api, @opentelemetry/core, @opentelemetry/id-generator-aws-xray, @opentelemetry/propagator-aws-xray, @opentelemetry/propagator-b3, @opentelemetry/sdk-trace-base, @opentelemetry/sdk-trace-node, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, eslint, eslint-plugin-header, eslint-plugin-import, gts, rimraf, typescript
- adot/collector/lambdacomponents/go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/Microsoft/go-winio, github.com/alecthomas/units, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url
- adot/collector/lambdacomponents/Makefile (capture: captured)
- adot/utils/soak/Dockerfile (capture: captured)
- python/sample-apps/function/requirements.txt (capture: captured) — dependency clues: boto3, requests

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 178
- Forks at capture: 70
- Last updated: 2026-09-25T22:21:17Z
- Last pushed: 2026-11-14T03:35:11Z
- Topics: awslambda, observability, opensource, opentelemetry, opentelemetry-api

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-observability/aws-otel-lambda)
- [README](https://github.com/aws-observability/aws-otel-lambda/blob/main/README.md)
- [Issues](https://github.com/aws-observability/aws-otel-lambda/issues)
- [Releases](https://github.com/aws-observability/aws-otel-lambda/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
