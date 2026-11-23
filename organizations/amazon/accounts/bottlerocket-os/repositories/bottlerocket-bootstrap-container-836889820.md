# bottlerocket-os/bottlerocket-bootstrap-container

- Company: Amazon
- GitHub account: [https://github.com/bottlerocket-os](https://github.com/bottlerocket-os)
- Mapping status: official-directory-listed
- Repository: [bottlerocket-os/bottlerocket-bootstrap-container](https://github.com/bottlerocket-os/bottlerocket-bootstrap-container)
- Default branch: develop
- README: [Open upstream README](https://github.com/bottlerocket-os/bottlerocket-bootstrap-container/blob/develop/README.md)
- README blob SHA: e6aa559a099d2d5b9829dbf563f5b4bbea2defea
- Repository ID: 836889820
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:35:56+00:00

### Short excerpt (up to 100 words)

> This is the bootstrap container for the Bottlerocket operating system. This container image allows the user to provide their own script to run bootstrap commands to setup their own configuration during runtime. For more information on settings, please refer to the Bottlerocket Documentation in order to configure your files. The automatically updated bootstrap container source will be used by default, if source is not specified in the configuration. To use default container image, create a TOML file with the following configurations. mode="once" user-data="user-base64-encoded-bootstrap-script" Below is the configuration to use the custom source. source="<URI to ECR Repository for this Bootstrap Container>"

### README headings

- Bottlerocket Bootstrap Container
- Using the Container Image
- Sample TOML configuration
- Example Walkthrough
- Create the directory
- Set API client configurations
- Load kernel module
- Checking logs

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 7,437 |
| Makefile | 4,395 |
| Dockerfile | 2,455 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Dockerfile (capture: captured)
- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 9
- Forks at capture: 14
- Last updated: 2026-10-19T20:27:53Z
- Last pushed: 2026-11-13T18:57:34Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/bottlerocket-os/bottlerocket-bootstrap-container)
- [README](https://github.com/bottlerocket-os/bottlerocket-bootstrap-container/blob/develop/README.md)
- [Issues](https://github.com/bottlerocket-os/bottlerocket-bootstrap-container/issues)
- [Releases](https://github.com/bottlerocket-os/bottlerocket-bootstrap-container/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
