# google/fscryptctl

- Company: Alphabet (Google)
- GitHub account: [https://github.com/google](https://github.com/google)
- Mapping status: verified
- Repository: [google/fscryptctl](https://github.com/google/fscryptctl)
- Default branch: master
- README: [Open upstream README](https://github.com/google/fscryptctl/blob/master/README.md)
- README blob SHA: 2adb21dfda0c136b877537794ad88b866ee2aadc
- README bytes captured: 7956
- README truncated at capture limit: False
- Repository ID: 96370379
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Small C tool for Linux filesystem encryption

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-27T19:53:55+00:00

### Short excerpt (up to 300 words)

> fscryptctl has the following To build, run make. fscryptctl doesn't link to

### README headings

- fscryptctl
- Table of Contents
- Building and Installing
- Runtime Dependencies
- Features
- Example Usage
- Create an ext4 filesystem that supports encryption.
- (Alternatively, use `tune2fs -O encrypt` on an existing ext4 filesystem.)
- (For f2fs, use `mkfs.f2fs -O encrypt` or `fsck.f2fs -O encrypt`.)
- Mount the filesystem.  Optionally add any desired mount options, such as
- `-o inlinecrypt` to make use of inline crypto hardware.
- Generate a random 512-bit key and store it in a file.
- Add the key to the filesystem.
- Get the status of the key on the filesystem.
- Create an encrypted directory that uses the key.
- Show the directory's encryption policy that was just set.
- Create some files in the encrypted directory.
- Remove the encryption key from the filesystem.
- (Alternatively, unmounting the filesystem will remove the key too.)
- Get the status of the key on the filesystem.
- The directory is now locked.  So the filenames are shown in encrypted form,
- and files can't be opened or created.
- Re-adding the key restores access to the files.
- Example Usage with Hardware-Wrapped Key
- Contributing
- Legal

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Features and capabilities: Features

> fscryptctl has the following

### Getting started and usage: Building and Installing

> To build, run make.

### Technology and requirements: Runtime Dependencies

> fscryptctl doesn't link to

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C | 38,995 |
| Python | 30,498 |
| Makefile | 4,463 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 148
- Forks at capture: 36
- Last updated: 2026-10-26T15:41:49Z
- Last pushed: 2025-11-04T17:44:03Z
- Topics: c, cryptography, ext4-filesystem, filesystem, filesystem-encryption

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/google/fscryptctl)
- [README](https://github.com/google/fscryptctl/blob/master/README.md)
- [Issues](https://github.com/google/fscryptctl/issues)
- [Releases](https://github.com/google/fscryptctl/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
