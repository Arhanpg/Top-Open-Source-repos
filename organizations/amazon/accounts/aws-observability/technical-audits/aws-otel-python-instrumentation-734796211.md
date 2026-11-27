# aws-observability/aws-otel-python-instrumentation

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/aws-otel-python-instrumentation
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:25:46+00:00

## Project purpose

This project is a redistribution of the OpenTelemetry Distro for Python, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest. The exception to this is support for Application Signals.

## Why this project is used

This project is a redistribution of the OpenTelemetry Distro for Python, preconfigured for use with AWS services. Please check out that project too to get a better understanding of the underlying internals. You won't see much code in this repository since we only apply some small configuration changes, and our OpenTelemetry friends takes care of the rest. The exception to this is support for Application Signals.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Java, Dockerfile, Shell, Rust, HCL, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: bytecode, cachetools, certifi, docker, grpcio, jsonschema, opentelemetry-api, opentelemetry-distro, opentelemetry-exporter-otlp-proto-common, opentelemetry-exporter-otlp-proto-grpc, opentelemetry-exporter-otlp-proto-http, opentelemetry-instrumentation, opentelemetry-instrumentation-aio-pika, opentelemetry-instrumentation-aiohttp-client, opentelemetry-instrumentation-aiokafka, opentelemetry-instrumentation-aiopg, opentelemetry-instrumentation-asgi, opentelemetry-instrumentation-asyncpg, opentelemetry-instrumentation-aws-lambda, opentelemetry-instrumentation-boto3sqs, opentelemetry-instrumentation-botocore, opentelemetry-instrumentation-cassandra, opentelemetry-instrumentation-celery, opentelemetry-instrumentation-confluent-kafka, opentelemetry-instrumentation-dbapi, opentelemetry-instrumentation-django, opentelemetry-instrumentation-falcon, opentelemetry-instrumentation-fastapi, opentelemetry-instrumentation-flask, opentelemetry-instrumentation-grpc, opentelemetry-instrumentation-httpx, opentelemetry-instrumentation-jinja2, opentelemetry-instrumentation-kafka-python, opentelemetry-instrumentation-logging, opentelemetry-instrumentation-mysql, opentelemetry-instrumentation-mysqlclient, opentelemetry-instrumentation-pika, opentelemetry-instrumentation-psycopg2, opentelemetry-instrumentation-pymemcache, opentelemetry-instrumentation-pymongo, opentelemetry-instrumentation-pymysql, opentelemetry-instrumentation-pyramid, opentelemetry-instrumentation-redis, opentelemetry-instrumentation-remoulade, opentelemetry-instrumentation-requests, opentelemetry-instrumentation-sqlalchemy, opentelemetry-instrumentation-sqlite3, opentelemetry-instrumentation-starlette, opentelemetry-instrumentation-system-metrics, opentelemetry-instrumentation-threading, opentelemetry-instrumentation-tornado, opentelemetry-instrumentation-tortoiseorm, opentelemetry-instrumentation-urllib, opentelemetry-instrumentation-urllib3, opentelemetry-instrumentation-wsgi, opentelemetry-processor-baggage, opentelemetry-propagator-aws-xray, opentelemetry-propagator-b3, opentelemetry-propagator-jaeger, opentelemetry-propagator-ot-trace, opentelemetry-proto, opentelemetry-sdk, opentelemetry-sdk-extension-aws, opentelemetry-semantic-conventions, protobuf, python-dateutil, pyyaml, requests, testcontainers, typing-extensions, urllib3
- Build/package tools: Gradle Kotlin build file, Docker build configuration, Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: tools/cp-utility/src/main.rs, contract-tests/images/applications/cloudwatch-plugin-otel/server.py, aws-opentelemetry-distro/src/amazon/opentelemetry/distro/_aws_attribute_keys.py, aws-opentelemetry-distro/src/amazon/opentelemetry/distro/_aws_metric_attribute_generator.py

## Setup and usage

- Getting Started: Check out the getting started documentation.

## Limitations and caveats

- Security issue notifications: If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our vulnerability reporting page. Please do **not** create a public github issue.

## Evidence and provenance

- README: https://github.com/aws-observability/aws-otel-python-instrumentation/blob/main/README.md
- README SHA: 1ca9642c193a973d69505b1c4a3caad12b9c3c20
- Manifests: Dockerfile, pyproject.toml, aws-opentelemetry-distro/pyproject.toml, cloudwatch-plugin-otel/pyproject.toml, performance-tests/build.gradle.kts, contract-tests/tests/pyproject.toml
- Sampled source files: tools/cp-utility/src/main.rs, contract-tests/images/applications/cloudwatch-plugin-otel/server.py, aws-opentelemetry-distro/src/amazon/opentelemetry/distro/_aws_attribute_keys.py, aws-opentelemetry-distro/src/amazon/opentelemetry/distro/_aws_metric_attribute_generator.py
- Git tree state: captured
- Evidence fingerprint: 89472cd6ad376f3eecb37ffa4aaf6c1bb6a5e7e759d36b2a6b0f28acd1724ca7

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
