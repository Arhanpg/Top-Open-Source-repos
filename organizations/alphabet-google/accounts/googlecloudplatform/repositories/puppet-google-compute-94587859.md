# GoogleCloudPlatform/puppet-google-compute

- Company: Alphabet (Google)
- GitHub account: [https://github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)
- Mapping status: official-project-linked
- Repository: [GoogleCloudPlatform/puppet-google-compute](https://github.com/GoogleCloudPlatform/puppet-google-compute)
- Default branch: master
- README: [Open upstream README](https://github.com/GoogleCloudPlatform/puppet-google-compute/blob/master/README.md)
- README blob SHA: a974ee6d76a916f4558336fd6e2edb77b0bc0b84
- README bytes captured: 226742
- README truncated at capture limit: False
- Repository ID: 94587859
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:16:30+00:00

### Short excerpt (up to 300 words)

> This Puppet module manages A list of features gcompute_address_ip('my-server', 'us-central1', 'myproject', $fn_auth) This module has been

### README headings

- Google Compute Engine Puppet Module
- Table of Contents
- Module Description
- Setup
- Usage
- Credentials
- Examples
- `gcompute_address`
- `gcompute_backend_bucket`
- `gcompute_backend_service`
- Backend Service requires various other services to be setup beforehand. Please
- make sure they are defined as well:
- - gcompute_instance_group { ... }
- - Health check
- `gcompute_disk_type`
- `gcompute_disk`
- `gcompute_firewall`
- `gcompute_forwarding_rule`
- `gcompute_global_address`
- `gcompute_global_forwarding_rule`
- `gcompute_http_health_check`
- `gcompute_https_health_check`
- `gcompute_health_check`
- `gcompute_instance_template`
- Power Tips:
- 1) Remember to define the resources needed to allocate the VM:
- a) gcompute_disk_type (to be used in 'diskType' property)
- b) gcompute_machine_type (to be used in 'machine_type' property)
- c) gcompute_network (to be used in 'network_interfaces' property)
- d) gcompute_subnetwork (to be used in the 'subnetwork' property)

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Module Description

> This Puppet module manages

### Features and capabilities: `guest_os_features`

> A list of features

### Getting started and usage: Examples

> gcompute_address_ip('my-server', 'us-central1', 'myproject', $fn_auth)

### Limitations and security: Limitations

> This module has been

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Ruby | 2,963,106 |
| Puppet | 187,102 |
| Shell | 7,259 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Gemfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 6
- Forks at capture: 5
- Last updated: 2025-06-30T19:58:20Z
- Last pushed: 2022-10-06T00:38:01Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/GoogleCloudPlatform/puppet-google-compute)
- [README](https://github.com/GoogleCloudPlatform/puppet-google-compute/blob/master/README.md)
- [Issues](https://github.com/GoogleCloudPlatform/puppet-google-compute/issues)
- [Releases](https://github.com/GoogleCloudPlatform/puppet-google-compute/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
