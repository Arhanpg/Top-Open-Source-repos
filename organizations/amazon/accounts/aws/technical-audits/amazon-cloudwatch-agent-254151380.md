# aws/amazon-cloudwatch-agent

- Company: Amazon
- Account: aws
- Repository: https://github.com/aws/amazon-cloudwatch-agent
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T06:56:00+00:00

## Project purpose

The Amazon CloudWatch Agent is software developed for the CloudWatch Agent

## Why this project is used

CloudWatch Agent enables you to collect and export host-level metrics and logs on instances running Linux or Windows server.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Shell, Makefile, PowerShell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute, cloud.google.com/go/compute/metadata, collectd.org, github.com/Azure/azure-sdk-for-go, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/go-autorest/autorest, github.com/Azure/go-autorest/autorest/adal, github.com/Azure/go-ntlmssp, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/BurntSushi/toml, github.com/Code-Hex/go-generics-cache, github.com/DataDog/datadog-agent/pkg/obfuscate, github.com/DataDog/datadog-go/v5, github.com/DataDog/go-sqllexer, github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp, github.com/Jeffail/gabs, github.com/Masterminds/semver/v3, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/Shopify/sarama, github.com/Showmax/go-fqdn, github.com/alecthomas/participle, github.com/alecthomas/participle/v2, github.com/alecthomas/units, github.com/alexbrainman/sspi, github.com/amazon-contributing/opentelemetry-collector-contrib/extension/awsmiddleware, github.com/amazon-contributing/opentelemetry-collector-contrib/override/aws, github.com/antchfx/jsonquery, github.com/antchfx/xmlquery, github.com/antchfx/xpath, github.com/apache/arrow/go/v12, github.com/apache/arrow/go/v15, github.com/apache/thrift, github.com/armon/go-metrics, github.com/aws/aws-msk-iam-sasl-signer-go, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/ini, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/amp, github.com/aws/aws-sdk-go-v2/service/autoscaling, github.com/aws/aws-sdk-go-v2/service/cloudwatch, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/ec2, github.com/aws/aws-sdk-go-v2/service/ecs, github.com/aws/aws-sdk-go-v2/service/efs, github.com/aws/aws-sdk-go-v2/service/eks, github.com/aws/aws-sdk-go-v2/service/elasticache, github.com/aws/aws-sdk-go-v2/service/iam, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/kafka, github.com/aws/aws-sdk-go-v2/service/lightsail, github.com/aws/aws-sdk-go-v2/service/rds, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/ssm, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/aws-sdk-go-v2/service/xray, github.com/aws/smithy-go, github.com/bahlo/generic-list-go, github.com/bboreham/go-loser, github.com/benbjohnson/clock, github.com/beorn7/perks, github.com/bigkevmcd/go-configparser, github.com/blang/semver/v4, github.com/bmatcuk/doublestar/v4, github.com/buger/jsonparser, github.com/bytedance/sonic, github.com/bytedance/sonic/loader, github.com/caio/go-tdigest, github.com/cenkalti/backoff/v4, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/cloudwego/base64x, github.com/cloudwego/iasm, github.com/cncf/xds/go, github.com/containerd/cgroups/v3, github.com/containerd/containerd/api, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/containerd/log, github.com/containerd/ttrpc, github.com/containerd/typeurl/v2, github.com/coreos/go-semver, github.com/coreos/go-systemd/v22, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/deckarep/golang-set/v2, github.com/dennwc/varint, github.com/digitalocean/go-metadata, github.com/digitalocean/godo, github.com/distribution/reference, github.com/docker/docker, github.com/docker/go-connections, github.com/jmespath/go-jmespath, github.com/pmezard/go-difflib, github.com/stretchr/objx, github.com/stretchr/testify, gopkg.in/yaml.v3
- Build/package tools: Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/amazon-cloudwatch-agent-config-wizard/wizard.go, cmd/amazon-cloudwatch-agent/amazon-cloudwatch-agent.go, cmd/amazon-cloudwatch-agent/amazon-cloudwatch-agent_test.go, cmd/amazon-cloudwatch-agent/featuregates.go

## Setup and usage

- Usage data: By default, the CloudWatch agent sends health and performance data about itself to CloudWatch whenever it publishes metrics or logs to CloudWatch. This data incurs no costs to you. You can prevent the agent from sending this data by specifying false for usage_data in the agent section of the configuration. If you omit this parameter, the default of

## Limitations and caveats

- Security disclosures: If you think you’ve found a potential security issue, please do not post it in the Issues. Instead, please follow the instructions here or email AWS security directly.

## Evidence and provenance

- README: https://github.com/aws/amazon-cloudwatch-agent/blob/main/README.md
- README SHA: 54714cf293dcc928eb8f3ab3454c3dc3d6874602
- Manifests: go.mod, Makefile, amazon-cloudwatch-container-insights/cloudwatch-agent-dockerfile/Dockerfile, tool/clean/go.mod, amazon-cloudwatch-container-insights/cloudwatch-agent-dockerfile/localal2/Dockerfile, amazon-cloudwatch-container-insights/cloudwatch-agent-dockerfile/localbin/Dockerfile
- Sampled source files: cmd/amazon-cloudwatch-agent-config-wizard/wizard.go, cmd/amazon-cloudwatch-agent/amazon-cloudwatch-agent.go, cmd/amazon-cloudwatch-agent/amazon-cloudwatch-agent_test.go, cmd/amazon-cloudwatch-agent/featuregates.go
- Git tree state: captured
- Evidence fingerprint: 5fef216ad60c09856b7513f6c5dfcc03e29f66f8b689c018aebd27192c04badf

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
