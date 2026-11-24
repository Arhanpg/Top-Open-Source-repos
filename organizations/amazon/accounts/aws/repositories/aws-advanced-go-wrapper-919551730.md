# aws/aws-advanced-go-wrapper

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/aws-advanced-go-wrapper](https://github.com/aws/aws-advanced-go-wrapper)
- Default branch: main
- README: [Open upstream README](https://github.com/aws/aws-advanced-go-wrapper/blob/main/README.md)
- README blob SHA: 1a374b6059d08eb500a00bbfbb286a3fd0f68894
- README bytes captured: 7123
- README truncated at capture limit: False
- Repository ID: 919551730
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The AWS Advanced Go Wrapper is complementary to existing Go drivers and aims to extend the functionality of the driver to enable applications to take full advantage of the features of clustered databases such as Amazon Aurora. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T08:06:52+00:00

### Short excerpt (up to 300 words)

> Hosting a database cluster For more information on

### README headings

- Amazon Web Services (AWS) Advanced Go Wrapper
- About the Wrapper
- What is Failover?
- Benefits of the AWS Advanced Go Wrapper
- Enhanced Failure Monitoring
- Using the AWS Advanced Go Wrapper with plain RDS databases
- Getting Started
- Documentation
- Using the AWS Advanced Go Wrapper
- Known Limitations
- Amazon RDS Blue/Green Deployments
- Getting Help and Opening Issues
- How to Contribute
- Releases
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: About the Wrapper

> Hosting a database cluster

### Getting started and usage: Getting Started

> For more information on

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 2,486,784 |
| Java | 176,937 |
| HTML | 37,644 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- .test/go.mod (capture: captured) — dependency clues: filippo.io/edwards25519, github.com/PuerkitoBio/goquery, github.com/Shopify/toxiproxy, github.com/andybalholm/brotli, github.com/andybalholm/cascadia, github.com/aws/aws-advanced-go-wrapper/auth-helpers, github.com/aws/aws-advanced-go-wrapper/aws-secrets-manager, github.com/aws/aws-advanced-go-wrapper/awssql/v2, github.com/aws/aws-advanced-go-wrapper/bun-pg-driver, github.com/aws/aws-advanced-go-wrapper/custom-endpoint, github.com/aws/aws-advanced-go-wrapper/federated-auth, github.com/aws/aws-advanced-go-wrapper/iam, github.com/aws/aws-advanced-go-wrapper/mysql-driver, github.com/aws/aws-advanced-go-wrapper/okta, github.com/aws/aws-advanced-go-wrapper/otlp, github.com/aws/aws-advanced-go-wrapper/pgx-driver, github.com/aws/aws-advanced-go-wrapper/xray, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config
- auth-helpers/go.mod (capture: captured) — dependency clues: github.com/aws/aws-advanced-go-wrapper/awssql/v2, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/rds/auth, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/rds, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/nicksnyder/go-i18n/v2, golang.org/x/text
- aws-secrets-manager/go.mod (capture: captured) — dependency clues: github.com/aws/aws-advanced-go-wrapper/auth-helpers, github.com/aws/aws-advanced-go-wrapper/awssql/v2, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/rds/auth, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/rds, github.com/aws/aws-sdk-go-v2/service/secretsmanager, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/nicksnyder/go-i18n/v2
- awssql/go.mod (capture: captured) — dependency clues: github.com/nicksnyder/go-i18n/v2, golang.org/x/text
- bun-pg-driver/go.mod (capture: captured) — dependency clues: github.com/aws/aws-advanced-go-wrapper/awssql/v2, github.com/cespare/xxhash/v2, github.com/jinzhu/inflection, github.com/nicksnyder/go-i18n/v2, github.com/puzpuzpuz/xsync/v3, github.com/stretchr/testify, github.com/tmthrgd/go-hex, github.com/uptrace/bun, github.com/uptrace/bun/driver/pgdriver, github.com/vmihailenco/msgpack/v5, github.com/vmihailenco/tagparser/v2, go.opentelemetry.io/otel, go.opentelemetry.io/otel/trace, go.yaml.in/yaml/v3, golang.org/x/crypto, golang.org/x/sys, golang.org/x/text, mellium.im/sasl
- custom-endpoint/go.mod (capture: captured) — dependency clues: github.com/aws/aws-advanced-go-wrapper/auth-helpers, github.com/aws/aws-advanced-go-wrapper/awssql/v2, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/feature/rds/auth, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/rds, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/nicksnyder/go-i18n/v2, golang.org/x/text

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 81
- Forks at capture: 14
- Last updated: 2026-11-12T03:57:02Z
- Last pushed: 2026-11-21T00:17:17Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/aws-advanced-go-wrapper)
- [README](https://github.com/aws/aws-advanced-go-wrapper/blob/main/README.md)
- [Issues](https://github.com/aws/aws-advanced-go-wrapper/issues)
- [Releases](https://github.com/aws/aws-advanced-go-wrapper/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
