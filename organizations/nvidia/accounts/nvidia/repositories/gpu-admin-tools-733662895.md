# NVIDIA/gpu-admin-tools

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/gpu-admin-tools](https://github.com/NVIDIA/gpu-admin-tools)
- Default branch: main
- README: [Open upstream README](https://github.com/NVIDIA/gpu-admin-tools/blob/main/README.md)
- README blob SHA: 94a86dd5d2c71ba179e206266d6ab568b4375505
- README bytes captured: 25505
- README truncated at capture limit: False
- Repository ID: 733662895
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

GPU Admin Tools. Includes Confidential Computing controls for H100, and other functionality

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-25T06:00:15+00:00

### Short excerpt (up to 300 words)

> sudo python3 nvidia_gpu_tools.py --help

### README headings

- NVIDIA GPU Admin Tools
- Most Commonly Used Examples
- Query the CC mode of all GPUs the system
- Query the CC mode of first 4 GPUs the system
- Enable CC mode on all GPUs
- Disable CC mode on a specific GPU in the system
- Query the BMSAI mode of all GPUs the system
- Enable BMSAI mode on all GPUs
- Disable BMSAI mode on a specific GPU in the system
- Generic debug dump from GPU
- Debug dump of NVLINK state
- Device discovery and selection
- MMIO through vfio-pci
- Prepare GPUs for QEMU with VFIO
- 1. Show the selected GPU, related devices, readiness, and next action.
- 2. Preview the driver changes. This does not modify the host.
- 3. Prepare the GPU for QEMU, then launch the guest.
- 4. After the guest has stopped, return the GPU to its host driver.
- Relationship to VFIO MMIO access
- Multi-GPU passthrough
- Inspect and preview every selected GPU and IOMMU group before changing drivers.
- Bind the complete set, then restore the same set after the guest stops.
- Equivalent selector for the first two GPUs discovered through sysfs.
- When the GPU shares an IOMMU group
- Usage

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Usage

> sudo python3 nvidia_gpu_tools.py --help

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 9,386,209 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 104
- Forks at capture: 45
- Last updated: 2026-11-18T10:13:22Z
- Last pushed: 2026-09-30T17:41:08Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/gpu-admin-tools)
- [README](https://github.com/NVIDIA/gpu-admin-tools/blob/main/README.md)
- [Issues](https://github.com/NVIDIA/gpu-admin-tools/issues)
- [Releases](https://github.com/NVIDIA/gpu-admin-tools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
