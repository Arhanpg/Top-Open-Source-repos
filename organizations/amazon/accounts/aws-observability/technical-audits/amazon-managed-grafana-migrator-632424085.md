# aws-observability/amazon-managed-grafana-migrator

- Company: Amazon
- Account: aws-observability
- Repository: https://github.com/aws-observability/amazon-managed-grafana-migrator
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T03:46:03+00:00

## Project purpose

🎉 May-15-24: v0.2.0 supports Grafana Service Accounts for v9 and v10 workspaces. See [Amazon Managed Grafana announces support for Grafana version 10.4]()

## Why this project is used

CLI migration utility to migrate Grafana content to Amazon Managed Grafana

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/aws/aws-sdk-go, github.com/davecgh/go-spew, github.com/fatih/color, github.com/golang/mock, github.com/grafana/grafana-api-golang-client, github.com/hashicorp/go-cleanhttp, github.com/inconshreveable/mousetrap, github.com/jmespath/go-jmespath, github.com/mattn/go-colorable, github.com/mattn/go-isatty, github.com/pmezard/go-difflib, github.com/spf13/cobra, github.com/spf13/pflag, github.com/stretchr/testify, golang.org/x/sys, gopkg.in/yaml.v3
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: main.go, internal/pkg/app/alert_rules.go, internal/pkg/app/app.go, internal/pkg/app/app_test.go

## Setup and usage

- Installation: Build from latest release. This requires Go (1.21 +) installed on your environement.
- Installation: go install github.com/aws-observability/amazon-managed-grafana-migrator@latest
- Installation: This command above will build the binary into your Go path ($HOME/go/bin).
- Installation: Make sure to add your Go bin in your $PATH to run the command.
- Installation: For Linux, this is usually export PATH=$PATH:$HOME/go/bin.
- Installation: You can also download the pre-compiled binary for your OS and CPU architecture
- Installation: from our GitHub releases.
- Installation: Example on Amazon Linux:

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/aws-observability/amazon-managed-grafana-migrator/blob/main/README.md
- README SHA: c5763ee35b25495506ab5f8dd247119f427bf250
- Manifests: go.mod
- Sampled source files: main.go, internal/pkg/app/alert_rules.go, internal/pkg/app/app.go, internal/pkg/app/app_test.go
- Git tree state: captured
- Evidence fingerprint: b93c99588ecbd460b0882635b02dd5ffed3fa8af633a63c329626a6c082e8ba4

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
