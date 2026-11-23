# firecracker-microvm/firecracker-demo

- Company: Amazon
- GitHub account: [https://github.com/firecracker-microvm](https://github.com/firecracker-microvm)
- Mapping status: official-directory-listed
- Repository: [firecracker-microvm/firecracker-demo](https://github.com/firecracker-microvm/firecracker-demo)
- Default branch: main
- README: [Open upstream README](https://github.com/firecracker-microvm/firecracker-demo/blob/main/README.md)
- README blob SHA: 5053e4e1b102d331d94bfd6d580c6633f765903a
- Repository ID: 158255404
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A demo running 4000 Firecracker microVMs.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T19:36:19+00:00

### Short excerpt (up to 100 words)

> This demo showcases Firecracker's agility and high-density capabiliies. **It's been run on an EC2 i3.metal host (the defaults start 4000 microVMs) with an Ubuntu and an Amazon Linux 2 host OS, from an Ubuntu client.** Deviations from this setup will probably lead to issues and/or sub-par performance. If you want to help us support the demo on more platforms...we take pull requests :) Get this repo on an EC2 Intel metal instance. Open two terminals/ssh-connections to the instance. will show a heatmap of network traffic done by each microVM. python3 microvm-tiles.py will control the rest of the demo. Raise the

### README headings

- Firecracker-demo
- Disclaimer
- Step-by-Step Instructions
- Terminal window 1
- Terminal window 2
- Start 4000 Firecracker microVMs
- start a total of 4k uVMs from 6 parallel threads
- ... wait for it ... should take around 60 seconds ... watch the heatmap
- Pick a microVM and play with it
- get the IP for that microVM
- IP of microVM on other side is *one less*
- stop the workload service
- manually run iperf with a higher bandwidth than the rest
- check out the heatmap
- Plot the 4000 Firecracker microVMs boot times

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Shell | 9,243 |
| Python | 3,534 |

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
- Stars at capture: 286
- Forks at capture: 59
- Last updated: 2026-10-25T22:32:08Z
- Last pushed: 2022-10-18T14:20:32Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/firecracker-microvm/firecracker-demo)
- [README](https://github.com/firecracker-microvm/firecracker-demo/blob/main/README.md)
- [Issues](https://github.com/firecracker-microvm/firecracker-demo/issues)
- [Releases](https://github.com/firecracker-microvm/firecracker-demo/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
