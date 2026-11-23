# aws/amazon-ecs-logs-collector

- Company: Amazon
- GitHub account: [https://github.com/aws](https://github.com/aws)
- Mapping status: verified
- Repository: [aws/amazon-ecs-logs-collector](https://github.com/aws/amazon-ecs-logs-collector)
- Default branch: master
- README: [Open upstream README](https://github.com/aws/amazon-ecs-logs-collector/blob/master/README.md)
- README blob SHA: 815886328ca0ac155471491467ba0fd0070feb1d
- Repository ID: 69396876
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

The script will be used to collect general os logs as well as Docker and ecs-agent logs, it also support to enable debug mode for docker and ecs-agent in Amazon Linux. 

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:25:34+00:00

### Short excerpt (up to 100 words)

> This project was created to collect Amazon ECS log files and Operating System log files for troubleshooting Amazon ECS customer support cases. The following functions are supported: * Collect Operating System logs * Collect Operating System settings * Collect Docker logs * Collect Amazon ECS agent Logs * Collect GPU information on NVIDIA GPU-based instances * Enable debug mode for Docker and the Amazon ECS agent (only available for Systemd init systems and Amazon Linux) * Create a tar zip file in the same folder as the script Run this project as the root user: curl -O https://raw.githubusercontent.com/aws/amazon-ecs-logs-collector/master/ecs-logs-collector.sh bash ecs-logs-collector.sh

### README headings

- ECS Logs Collector
- Usage
- ls collect*
- Retrieving the logs
- Important
- GPU information
- Example output
- bash ecs-logs-collector.sh --help
- Example output in normal mode
- bash ecs-logs-collector.sh
- Example output in enable-debug mode
- bash ecs-logs-collector.sh --mode=enable-debug
- Contributing
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 26,777 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 191
- Forks at capture: 78
- Last updated: 2026-07-08T22:41:36Z
- Last pushed: 2026-07-08T22:41:31Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws/amazon-ecs-logs-collector)
- [README](https://github.com/aws/amazon-ecs-logs-collector/blob/master/README.md)
- [Issues](https://github.com/aws/amazon-ecs-logs-collector/issues)
- [Releases](https://github.com/aws/amazon-ecs-logs-collector/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
