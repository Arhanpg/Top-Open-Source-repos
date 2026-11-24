# NVIDIA/bios-settings-mgr

- Company: NVIDIA
- GitHub account: [https://github.com/NVIDIA](https://github.com/NVIDIA)
- Mapping status: verified
- Repository: [NVIDIA/bios-settings-mgr](https://github.com/NVIDIA/bios-settings-mgr)
- Default branch: develop
- README: [Open upstream README](https://github.com/NVIDIA/bios-settings-mgr/blob/develop/README.md)
- README blob SHA: b1e53bfafdf3be738d6ae8312f2d1efc4ef1bc73
- Repository ID: 796778882
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:34:37+00:00

### Short excerpt (up to 100 words)

> The **biosconfig_manager** service enables users to view and modify the BIOS setup configuration parameters remotely through the Baseboard Management Controller (BMC) at any host state. Changes to these parameters will take effect upon the next system reboot or immediately, depending on the host firmware. For more details, please refer to [design document][rbmc-design-document]. - **Remote management** of BIOS settings. - **Immediate updates** or scheduled changes upon reboot. - **Reset BIOS Settings** support through the dbus. - **ChangePassword** support to change the BIOS setup password. The Manager interface exposes methods and properties to Get & Set BIOS attributes via [dbus][pdi-manager-bios]. xyz.openbmc_project.BIOSConfigManager /xyz/openbmc_project/bios_config/manager

### README headings

- Remote BIOS Configuration
- Overview
- Features
- RBC Manager Interface
- Service Name
- Object Path
- Interface Name
- Methods
- Properties
- Signature of `BaseBIOSTable`
- Examples
- Initialization of `BaseBIOSTable`
- BIOS with PLDM as Communication Protocol
- BIOS with IPMI as Communication Protocol
- RBC Password Interface
- Service Name
- Object Path
- Interface Name
- Methods
- Properties
- RBC SecureBoot Interface
- Object Path
- Properties
- SecureBoot with Redfish Host Interface as Communication Protocol

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C++ | 392,342 |
| Meson | 8,955 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: True
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 4
- Forks at capture: 3
- Last updated: 2026-11-11T15:37:38Z
- Last pushed: 2026-11-13T05:38:32Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/NVIDIA/bios-settings-mgr)
- [README](https://github.com/NVIDIA/bios-settings-mgr/blob/develop/README.md)
- [Issues](https://github.com/NVIDIA/bios-settings-mgr/issues)
- [Releases](https://github.com/NVIDIA/bios-settings-mgr/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
