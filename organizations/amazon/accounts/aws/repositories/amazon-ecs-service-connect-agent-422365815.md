# aws/amazon-ecs-service-connect-agent

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ecs-service-connect-agent](https://github.com/aws/amazon-ecs-service-connect-agent)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/amazon-ecs-service-connect-agent/blob/main/README.md)
- README blob SHA: 412844436f9ae2775dffa585eacf546bf3829a95
- Repository ID: 422365815
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Amazon ECS Service Connect Agent

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:37+00:00

### Short excerpt (up to 100 words)

> The Amazon ECS Service Connect Agent is a primary component of Amazon ECS Service Connect and AWS App Mesh. It monitors the Envoy proxy and provides a management interface. This management interface serves as a safe endpoint to interact with the Envoy proxy and provides several APIs for health checks, telemetry data and summarizes the operating condition of the proxy. It is used in both ECS Service Connect proxy and App Mesh Envoy Docker Image. On an Amazon Linux AMI. Download Go at https://go.dev/doc/install. In the project's `agent` directory, issue the `make` command to compile the agent binary: $ yum

### README headings

- Amazon ECS Service Connect Agent
- Building the Agent
- Option 1: Local build
- Option 2: Docker build
- Advanced Usage
- Deprecated
- Management APIs
- Contributing
- Security
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 445,467 |
| Makefile | 2,194 |
| Shell | 525 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- agent/go.mod (capture: captured) — dependency clues: github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/aws-xray-sdk-go, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/census-instrumentation/opencensus-proto, github.com/cespare/xxhash/v2, github.com/cncf/xds/go, github.com/davecgh/go-spew
- agent/Makefile (capture: captured)
- agent/vendor/github.com/aws/smithy-go/Makefile (capture: captured)
- agent/vendor/github.com/gorilla/mux/Makefile (capture: captured)
- agent/vendor/github.com/hashicorp/go-retryablehttp/Makefile (capture: captured)
- agent/vendor/github.com/jmespath/go-jmespath/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 43
- Forks at capture: 23
- Last updated: 2026-11-01T17:11:37Z
- Last pushed: 2026-11-17T19:01:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ecs-service-connect-agent)
- [README](https://github.com/aws/amazon-ecs-service-connect-agent/blob/main/README.md)
- [Issues](https://github.com/aws/amazon-ecs-service-connect-agent/issues)
- [Releases](https://github.com/aws/amazon-ecs-service-connect-agent/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
