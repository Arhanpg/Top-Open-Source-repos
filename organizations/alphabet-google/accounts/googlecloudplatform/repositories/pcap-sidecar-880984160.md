# GoogleCloudPlatform/pcap-sidecar

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/pcap-sidecar](https://github.com/GoogleCloudPlatform/pcap-sidecar)
- Default branch: main
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/pcap-sidecar/blob/main/README.md)
- README blob SHA: 4ea0c8943cdc11cb7641af723e405e609875db76
- README bytes captured: 30907
- README truncated at capture limit: False
- Repository ID: 880984160
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Sidecar to perform packet capturing in Serverless (Cloud Run, Cloud Run functions, App Engine Flex), GKE, & GCE

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T04:23:32+00:00

### Short excerpt (up to 300 words)

> During development, it is Structured Cloud Logging entries The sidecar uses: **tcpdump**/**pcap-cli**

### README headings

- Cloud Run PCAP sidecar
- Motivation
- Features
- Building blocks
- How it works
- Prebuilt image flavors
- How to deploy pcap sidecar to Cloud Run
- Final setup
- Configure pcap sidecar healthchecks
- Available configurations
- Advanced configurations
- Considerations
- Download and Merge all PCAP Files
- How to build the PCAP sidecar yourself
- Using a local environment or [Cloud Shell](https://cloud.google.com/shell/docs/launching-cloud-shell)
- Using [Cloud Build](https://cloud.google.com/build/docs/build-config-file-schema)
- Using with GKE
- Create a cluster
- Configure `kubectl` to point to your cluster
- Configure Google and Kubernetes service accounts
- Create the GKE deployment manifest
- Using with App Engine Flexible

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Motivation

> During development, it is

### Features and capabilities: Features

> Structured Cloud Logging entries

### Architecture and design: How it works

> The sidecar uses: **tcpdump**/**pcap-cli**

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 322,432 |
| Shell | 22,123 |
| Dockerfile | 17,081 |
| Jsonnet | 844 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- _ssh_libpcap/Dockerfile (capture: captured)
- config/Dockerfile (capture: captured)
- config/go.mod (capture: captured) — dependency clues: github.com/fsnotify/fsnotify, github.com/go-viper/mapstructure/v2, github.com/google/go-jsonnet, github.com/knadh/koanf/maps, github.com/knadh/koanf/parsers/json, github.com/knadh/koanf/providers/file, github.com/knadh/koanf/v2, github.com/mitchellh/copystructure, github.com/mitchellh/reflectwalk, github.com/spf13/pflag, github.com/wissance/stringFormatter, go.yaml.in/yaml/v2, golang.org/x/crypto, golang.org/x/sys, sigs.k8s.io/yaml
- gcsfuse/Dockerfile (capture: captured)
- pcap-cli/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 25
- Forks at capture: 5
- Last updated: 2026-06-10T15:41:25Z
- Last pushed: 2026-04-08T21:49:22Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/pcap-sidecar)
- [README](https://github.com/GoogleCloudPlatform/pcap-sidecar/blob/main/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/pcap-sidecar/issues)
- [Releases](https://github.com/GoogleCloudPlatform/pcap-sidecar/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
