# aws-observability/aws-otel-lambda

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-lambda
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T07:06:09+00:00

## Project purpose

As a downstream Repo of opentelemetry-lambda, ___aws-otel-lambda___ publishes AWS managed OpenTelemetry Lambda layers that are preconfigured for use with AWS services and bundle the reduced ADOT Collector. Users can onboard to OpenTelemetry in their existing Lambda functions by adding these ready-made layers directly.

## Why this project is used

AWS Distro for OpenTelemetry - AWS Lambda

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: HCL, Java, Shell, Python, Go, TypeScript, C#, JavaScript, Makefile, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: @opentelemetry/api, @opentelemetry/core, @opentelemetry/id-generator-aws-xray, @opentelemetry/propagator-aws-xray, @opentelemetry/propagator-b3, @opentelemetry/sdk-trace-base, @opentelemetry/sdk-trace-node, @types/node, @typescript-eslint/eslint-plugin, @typescript-eslint/parser, boto3, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, eslint, eslint-plugin-header, eslint-plugin-import, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/Microsoft/go-winio, github.com/alecthomas/units, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/aws-sdk-go-v2/service/xray, github.com/aws/smithy-go, github.com/beorn7/perks, github.com/cenkalti/backoff/v5, github.com/cenkalti/backoff/v7, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/dennwc/varint, github.com/ebitengine/purego, github.com/felixge/httpsnoop, github.com/foxboron/go-tpm-keyfiles, github.com/fsnotify/fsnotify, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/go-ole/go-ole, github.com/go-viper/mapstructure/v2, github.com/gobwas/glob, github.com/gogo/protobuf, github.com/golang-jwt/jwt/v5, github.com/golang/snappy, github.com/google/go-tpm, github.com/google/s2a-go, github.com/google/uuid, github.com/googleapis/enterprise-certificate-proxy, github.com/googleapis/gax-go/v2, github.com/grafana/regexp, github.com/grpc-ecosystem/grpc-gateway/v2, github.com/hashicorp/go-version, github.com/hashicorp/golang-lru/v2, github.com/inconshreveable/mousetrap, github.com/jpillora/backoff, github.com/json-iterator/go, github.com/klauspost/compress, github.com/knadh/koanf/maps, github.com/knadh/koanf/providers/confmap, github.com/knadh/koanf/v2, github.com/kylelemons/godebug, github.com/lufia/plan9stats, github.com/mitchellh/copystructure, github.com/mitchellh/reflectwalk, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/munnerz/goautoneg, github.com/mwitkow/go-conntrack, github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsemfexporter, github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsxrayexporter, github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusremotewriteexporter, github.com/open-telemetry/opentelemetry-collector-contrib/extension/sigv4authextension, github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/awsutil, github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/cwlogs, github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/metrics, github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/xray, github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal, github.com/open-telemetry/opentelemetry-collector-contrib/pkg/resourcetotelemetry, github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/prometheus, github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/prometheusremotewrite, github.com/pierrec/lz4/v4, github.com/pkg/browser, github.com/pmezard/go-difflib, github.com/power-devops/perfstat, github.com/prometheus/client_golang, github.com/prometheus/client_golang/exp, github.com/prometheus/client_model, github.com/prometheus/common, github.com/prometheus/otlptranslator, github.com/prometheus/procfs, github.com/prometheus/prometheus, github.com/prometheus/sigv4, github.com/rs/cors, github.com/shirou/gopsutil/v4, github.com/spf13/cobra, github.com/spf13/pflag, github.com/stretchr/testify, github.com/tidwall/gjson, github.com/tidwall/match, github.com/tidwall/pretty, gts, requests, rimraf, typescript
- Build/package tools: Gradle Kotlin build file, Docker build configuration, Go module manifest, npm-compatible manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: adot/nodejs/sample-apps/aws-sdk/lambda/index.ts, java/src/main/java/software/amazon/opentelemetry/lambda/AwsLambdaXrayContextAutoConfigurationCustomizerProvider.java, java/src/main/java/software/amazon/opentelemetry/lambda/AwsOtelTracerProviderConfigurer.java, nodejs/wrapper-adot/src/adot-extension.ts

## Setup and usage

No setup information established.

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-lambda/blob/main/README.md
- README SHA: bdeaadd10221ce8202712ddcfc42b5646d761160
- Manifests: java/build.gradle.kts, nodejs/wrapper-adot/package.json, adot/collector/lambdacomponents/go.mod, adot/collector/lambdacomponents/Makefile, adot/utils/soak/Dockerfile, python/sample-apps/function/requirements.txt
- Sampled source files: adot/nodejs/sample-apps/aws-sdk/lambda/index.ts, java/src/main/java/software/amazon/opentelemetry/lambda/AwsLambdaXrayContextAutoConfigurationCustomizerProvider.java, java/src/main/java/software/amazon/opentelemetry/lambda/AwsOtelTracerProviderConfigurer.java, nodejs/wrapper-adot/src/adot-extension.ts
- Git tree state: captured
- Evidence fingerprint: 03596ac967d8a14d715d25e54fec0977e0eda0bea34d400dab67bdfb8f675610

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
