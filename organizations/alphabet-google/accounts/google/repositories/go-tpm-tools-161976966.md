# google/go-tpm-tools

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/go-tpm-tools](https://github.com/google/go-tpm-tools)
- Default branch: main
- README: [Open upstream README](https://github.com/google/go-tpm-tools/blob/main/README.md)
- README blob SHA: 35a32f7de3a658b199cbc2274446c3109d508362
- README bytes captured: 6702
- README truncated at capture limit: False
- Repository ID: 161976966
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Go packages built on go-tpm providing a high-level API for using TPMs

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T03:45:19+00:00

### Short excerpt (up to 300 words)

> gotpm can be directly

### README headings

- Go-TPM tools [![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/google/go-tpm-tools)](https://github.com/google/go-tpm-tools/releases)
- Use prebuilt `gotpm` binary
- VERSION: 0.4.4 ARCH: Linux_x86_64
- You may need to copy the binary to a directory with executable permissions.
- NOTE: on Container-Optimized OS, /var/lib/google/ is executable
- Building and Installing `gotpm`
- gotpm will be installed to $GOBIN
- gotpm will be in the cmd/gotpm subdirectory of the repo
- Minimum Required Go Version
- `openssl` errors when building `simulator`
- Linux
- Ubuntu/Debian based systems
- Redhat/Centos based systems
- Arch Linux (headers/library in the same package)
- macOS
- Windows
- Custom install location
- Add OpenSSL to the include and library path at the command line
- Add OpenSSL to the include and library path in the code
- No TPM 1.2 support
- Confidential VMs with Intel TDX
- Legal

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Getting started and usage: Building and Installing `gotpm`

> gotpm can be directly

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 3,725,353 |
| Go | 1,359,588 |
| Shell | 112,413 |
| Dockerfile | 10,766 |
| M4 | 7,621 |
| Makefile | 2,879 |
| Python | 1,822 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/GoogleCloudPlatform/confidential-space/server, github.com/davecgh/go-spew, github.com/google/go-attestation, github.com/google/go-cmp, github.com/google/go-configfs-tsm, github.com/google/go-eventlog, github.com/google/go-sev-guest, github.com/google/go-tdx-guest, github.com/google/go-tpm, github.com/google/logger, github.com/google/uuid, github.com/pmezard/go-difflib, github.com/stretchr/testify, go.uber.org/multierr, golang.org/x/crypto, golang.org/x/sys, google.golang.org/protobuf
- agent/go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/confidentialcomputing, github.com/GoogleCloudPlatform/confidential-space/server, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/golang-jwt/jwt/v4, github.com/google/go-attestation, github.com/google/go-cmp, github.com/google/go-configfs-tsm, github.com/google/go-eventlog, github.com/google/go-sev-guest, github.com/google/go-tdx-guest, github.com/google/go-tpm, github.com/google/go-tpm-tools, github.com/google/go-tpm-tools/verifier
- cmd/go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/confidentialcomputing, cloud.google.com/go/logging, cloud.google.com/go/longrunning, github.com/GoogleCloudPlatform/confidential-space/server, github.com/cespare/xxhash/v2, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/golang-jwt/jwt/v4, github.com/golang/groupcache, github.com/golang/protobuf, github.com/google/gce-tcb-verifier, github.com/google/gce-tcb-verifier/gcetcbendorsement, github.com/google/go-attestation
- launcher/go.mod (capture: captured) — dependency clues: cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/confidentialcomputing, cloud.google.com/go/logging, cloud.google.com/go/longrunning, cos.googlesource.com/cos/tools.git, cyphar.com/go-pathrs, github.com/AdaLogics/go-fuzz-headers, github.com/AdamKorcz/go-118-fuzz-build, github.com/GoogleCloudPlatform/confidential-space/server, github.com/GoogleCloudPlatform/key-protection-module, github.com/GoogleCloudPlatform/key-protection-module/keymanager/attestation_service, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/NVIDIA/go-nvml, github.com/cenkalti/backoff/v4, github.com/cespare/xxhash/v2, github.com/containerd/cgroups/v3
- verifier/go.mod (capture: captured) — dependency clues: cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/confidentialcomputing, github.com/GoogleCloudPlatform/confidential-space/server, github.com/cespare/xxhash/v2, github.com/davecgh/go-spew, github.com/felixge/httpsnoop, github.com/go-logr/logr, github.com/go-logr/stdr, github.com/golang-jwt/jwt/v4, github.com/google/go-attestation, github.com/google/go-cmp, github.com/google/go-configfs-tsm, github.com/google/go-eventlog, github.com/google/go-sev-guest, github.com/google/go-tdx-guest, github.com/google/go-tpm, github.com/google/go-tpm-tools, github.com/google/logger
- launcher/image/measure/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 312
- Forks at capture: 123
- Last updated: 2026-11-19T21:12:35Z
- Last pushed: 2026-11-20T22:26:54Z
- Topics: go, golang, remote-attestation, security, tpm, tpm2

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/go-tpm-tools)
- [README](https://github.com/google/go-tpm-tools/blob/main/README.md)
- [Issues](https://github.com/google/go-tpm-tools/issues)
- [Releases](https://github.com/google/go-tpm-tools/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
