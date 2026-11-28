# google/go-sev-guest

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/go-sev-guest](https://github.com/google/go-sev-guest)
- Default branch: main
- README: [Open upstream README](https://github.com/google/go-sev-guest/blob/main/README.md)
- README blob SHA: 9397a7f477a3434f523784d2a0b6bfc18ab002e2
- README bytes captured: 10698
- README truncated at capture limit: False
- Repository ID: 525452605
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

go-sev-guest offers a library to wrap the /dev/sev-guest device in Linux, as well as a library for attestation verification of fundamental components of an attestation report.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T03:37:17+00:00

### Short excerpt (up to 300 words)

> This function uses the

### README headings

- SEV Guest
- `client`
- `func OpenDevice() (*LinuxDevice, error)`
- `func GetExtendedReport(d Device, reportData [64]byte) (*pb.Attestation, error)`
- `func GetDerivedKeyAcknowledgingItsLimitations(d Device, request *SnpDerivedKeyReq) ([]byte, error)`
- `func (d Device) Close() error`
- `func (d Device) Product() *spb.SevProduct`
- `verify`
- `func SnpAttestation(attestation *spb.Attestation, options *Options) error`
- `Options` type
- `AMDRootCerts` type
- `validate`
- `func SnpAttestation(attestation *spb.Attestation, options *Options) error`
- The `Option` type
- License
- Links
- Disclaimers

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Limitations and security: `func GetDerivedKeyAcknowledgingItsLimitations(d Device, request *SnpDerivedKeyReq) ([]byte, error)`

> This function uses the

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 494,615 |
| Assembly | 822 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/golang/protobuf, github.com/google/go-cmp, github.com/google/go-configfs-tsm, github.com/google/logger, github.com/google/uuid, go.uber.org/multierr, golang.org/x/crypto, golang.org/x/sys, golang.org/x/xerrors, google.golang.org/protobuf

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 79
- Forks at capture: 38
- Last updated: 2026-11-10T21:36:02Z
- Last pushed: 2026-11-20T00:30:43Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/go-sev-guest)
- [README](https://github.com/google/go-sev-guest/blob/main/README.md)
- [Issues](https://github.com/google/go-sev-guest/issues)
- [Releases](https://github.com/google/go-sev-guest/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
