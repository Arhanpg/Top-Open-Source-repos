# aws-samples/amazon-aggregation-query-proxy

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-aggregation-query-proxy](https://github.com/aws-samples/amazon-aggregation-query-proxy)
- Default branch: main
- README: [Open upstream README](https://github.com/aws-samples/amazon-aggregation-query-proxy/blob/main/README.md)
- README blob SHA: a116797f93f6033c895a9bbed05ba8a5b6d94cf8
- README bytes captured: 15839
- README truncated at capture limit: False
- Repository ID: 499349843
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Aggregation query proxy is a scalable sidecar application that sits between a customer application and Amazon Keyspaces/DynamoDB. It allows you to run bounded aggregation queries against Amazon Keyspaces and DynamoDB services.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:48:04+00:00

### Short excerpt (up to 300 words)

> Java 21 and Maven As a best practice

### README headings

- Aggregation-query-proxy
- Requirements
- Configuration
- API clients
- Amazon Keyspaces
- Amazon DynamoDB
- Build
- Run
- Deploy on ECS Fargate
- Querying
- Limitations
- How a query is split
- Aggregation engines
- Accepted statements
- Error responses
- Example: Amazon Keyspaces
- Example: Amazon DynamoDB
- Observability
- Tests
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Technology and requirements: Requirements

> Java 21 and Maven

### Limitations and security: Limitations

> As a best practice

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Java | 288,335 |
| Python | 12,162 |
| Dockerfile | 2,353 |
| Shell | 1,260 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pom.xml (capture: captured) — dependency clues: amazon-aggregation-query-proxy
- build-script/Dockerfile (capture: captured)
- query-app/pom.xml (capture: captured) — dependency clues: aws-sigv4-auth-cassandra-java-driver-plugin, bom, commons-lang3, dropwizard-auth, dropwizard-bom, dropwizard-core, dropwizard-dependencies, dropwizard-testing, duckdb_jdbc, dynamodb, jackson-databind, java-driver-core, junit-jupiter, kotlin-bom, kotlin-stdlib, maven-compiler-plugin, maven-enforcer-plugin, maven-jar-plugin, maven-shade-plugin, maven-surefire-plugin
- query-app/src/test/locust/ddb/requirements.txt (capture: captured) — dependency clues: boto3, locust

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT-0
- Stars at capture: 8
- Forks at capture: 1
- Last updated: 2026-11-09T13:47:36Z
- Last pushed: 2026-11-20T08:24:48Z
- Topics: aggregation, cassandra, dynamodb, keyspaces

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-aggregation-query-proxy)
- [README](https://github.com/aws-samples/amazon-aggregation-query-proxy/blob/main/README.md)
- [Issues](https://github.com/aws-samples/amazon-aggregation-query-proxy/issues)
- [Releases](https://github.com/aws-samples/amazon-aggregation-query-proxy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
