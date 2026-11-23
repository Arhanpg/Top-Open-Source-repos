# NVIDIA/ansible-role-nvidia-driver

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/ansible-role-nvidia-driver](https://github.com/NVIDIA/ansible-role-nvidia-driver)
- Default branch: master
- README: [Open upstream README](https://github.com/NVIDIA/ansible-role-nvidia-driver/blob/master/README.md)
- README blob SHA: 1983dc5da5dd8a111e7b5fca8efa8822791a7d29
- Repository ID: 184292101
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:10:58+00:00

### Short excerpt (up to 100 words)

> An Ansible role to install the NVIDIA driver from the NVIDIA CUDA repositories. In the process of installing the NVIDIA driver, this role will reboot the nodes where it runs. Because of this, we strongly recommend that you run `ansible-playbook` from a separate node than the GPU nodes where you are installing the driver. If you attempt to run Ansible on the same node where you are installing the driver, this role will either: * Refuse to proceed with an error like `Running reboot with local connection would reboot the control node` (if running with the `local` connection) * Reboot

### README headings

- ansible-role-nvidia-driver
- Requirements
- Installing
- Role variables
- Red Hat specific variables
- Ubuntu specific variables
- SUSE specific variables
- Example playbook
- Ansible collection dependency
- Supported distributions

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 15,929 |
| Shell | 247 |
| Jinja | 187 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: BSD-3-Clause
- Stars at capture: 136
- Forks at capture: 80
- Last updated: 2026-11-19T03:59:51Z
- Last pushed: 2026-11-20T16:05:25Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/ansible-role-nvidia-driver)
- [README](https://github.com/NVIDIA/ansible-role-nvidia-driver/blob/master/README.md)
- [Issues](https://github.com/NVIDIA/ansible-role-nvidia-driver/issues)
- [Releases](https://github.com/NVIDIA/ansible-role-nvidia-driver/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
