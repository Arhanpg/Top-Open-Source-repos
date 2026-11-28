# google/go-tdx-guest

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/go-tdx-guest](https://github.com/google/go-tdx-guest)
- Default branch: main
- README: [Open upstream README](https://github.com/google/go-tdx-guest/blob/main/README.md)
- README blob SHA: c413e467b254756b908a17c89c024e26784f36e9
- README bytes captured: 6239
- README truncated at capture limit: False
- Repository ID: 657499126
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

go-tdx-guest offers a library to wrap the /dev/tdx-guest device in Linux, as well as a library for attestation verification of fundamental components of an attestation quote.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T03:41:17+00:00

### Short excerpt (up to 300 words)

> This project offers libraries for a simple wrapper around quote providing tools such as the go-configfs-tsm library, or the /dev/tdx_guest device in Linux, as well

### README headings

- TDX Guest
- `client`
- `func GetQuoteProvider() (*LinuxConfigFsQuoteProvider, error)`
- `func OpenDevice() (*LinuxDevice, error)`
- `func GetQuote(quoteProvider any, reportData [64]byte) (any, error)`
- `func (d Device) Close() error`
- `verify`
- `func TdxQuote(quote *pb.QuoteV4, options *Options) error`
- `Options` type
- `rtmr`
- `func ExtendEventLog(rtmrIndex int, hashAlgo crypto.Hash, eventLog []byte) error`
- `func ExtendDigest(rtmrIndex int, digest []byte) error`
- License
- Links
- Disclaimers

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Introduction: TDX Guest

> This project offers libraries for a simple wrapper around quote providing tools such as the go-configfs-tsm library, or the /dev/tdx_guest device in Linux, as well

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Go | 489,218 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- go.mod (capture: captured) — dependency clues: github.com/fxamacker/cbor/v2, github.com/google/go-cmp, github.com/google/go-configfs-tsm, github.com/google/go-eventlog, github.com/google/go-sev-guest, github.com/google/go-tpm, github.com/google/logger, github.com/veraison/go-cose, github.com/x448/float16, go.uber.org/multierr, golang.org/x/crypto, golang.org/x/sys, google.golang.org/protobuf

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 102
- Forks at capture: 48
- Last updated: 2026-11-23T07:10:14Z
- Last pushed: 2026-11-18T22:32:40Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/go-tdx-guest)
- [README](https://github.com/google/go-tdx-guest/blob/main/README.md)
- [Issues](https://github.com/google/go-tdx-guest/issues)
- [Releases](https://github.com/google/go-tdx-guest/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
