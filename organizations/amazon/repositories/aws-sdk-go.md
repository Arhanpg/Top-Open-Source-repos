# AWS SDK for Go v1 — end of support

- **Company:** Amazon / AWS
- **GitHub owner:** [aws](https://github.com/aws)
- **Repository:** [aws/aws-sdk-go](https://github.com/aws/aws-sdk-go)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/aws/aws-sdk-go/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `54d51fd596897aab9e6087a3ff0771eb0559bc28`

## Project overview

AWS SDK for Go v1 provided Go clients and shared utilities for calling AWS service APIs. The repository's current README announces that v1 reached end of support on 31 July 2025 and recommends migration to AWS SDK for Go v2.

## Features and capabilities documented by the README

- The SDK was composed of a shared core under the aws package and service-specific clients under the service directory.
- Core packages included configuration, logging, error handling, credentials providers, endpoint/region metadata, sessions, request sending and retry logic.
- Service clients exposed Go types and utilities for calling AWS service APIs.
- README examples demonstrate S3 PutObject with a context-based timeout and error handling.
- The SDK documented credential and region configuration, API requests, pagination and resource waiters.

## Technology stack

Go; module path github.com/aws/aws-sdk-go; AWS service clients; session/configuration and credential-provider packages; Apache License 2.0.

## Getting started

For existing v1 applications, consult the linked AWS end-of-support announcement and migration guide. New development should use AWS SDK for Go v2, as the README recommends.

## Lifecycle, compatibility and operational notes

The README explicitly states that AWS SDK for Go v1 entered end-of-support on 31 July 2025 and will not receive further updates. It is not the recommended SDK for new development; preserve this record to help identify and migrate legacy Go applications.

## Evaluation guidance

Check the current release, upstream documentation, dependency manifests, supported platforms, licence and maintenance policy before adoption. This README-based dossier is not a complete source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/aws/aws-sdk-go)
- [README](https://github.com/aws/aws-sdk-go/blob/main/README.md)
- [Issues](https://github.com/aws/aws-sdk-go/issues)
- [Releases](https://github.com/aws/aws-sdk-go/releases)

*Evidence note: the README blob SHA identifies the upstream revision inspected. Technology and lifecycle claims are limited to the README evidence; additional manifest and source verification remains separate.*
