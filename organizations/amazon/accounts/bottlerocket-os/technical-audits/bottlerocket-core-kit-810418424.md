# bottlerocket-os/bottlerocket-core-kit

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-core-kit
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:22:34+00:00

## Project purpose

This is the core kit for Bottlerocket. It includes many common dependencies for downstream package and variant builds.

## Why this project is used

A kit with core software packaged for Bottlerocket

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Rust, Go, Shell, Makefile, JavaScript
- Frameworks/libraries: Unknown / not established
- Dependency names: amazon-ecs-cni-plugins, amazon-ssm-agent, amazon-vpc-cni-plugins, aws-iam-authenticator, aws-otel-collector, aws-signer-notation-plugin, aws-signing-helper, bash, binutils, chrony, cni, cni-plugins, conntrack-tools, containerd-1_7, containerd-2_2, containerd-2_3, coreutils, cri-tools, dbus-broker, docker-cli-25, docker-cli-29, docker-engine-25, docker-engine-29, docker-init, dranet, e2fsprogs, early-boot-config, ecr-credential-helper, ecr-credential-provider-1_31, ecr-credential-provider-1_32, ecr-credential-provider-1_33, ecr-credential-provider-1_34, ecr-credential-provider-1_35, ecr-credential-provider-1_36, ecr-credential-provider-1_37, ecs-agent, ecs-gpu-init, erofs-utils, ethtool, filesystem, findutils, glibc, grep, host-ctr, hwloc, iproute, iptables, iputils, kexec-tools, keyutils, kmod, kubernetes-1_31, kubernetes-1_32, kubernetes-1_33, kubernetes-1_34, kubernetes-1_35, kubernetes-1_36, kubernetes-1_37, libacl, libaio, libattr, libaudit, libbpf, libcap, libcrypto, libcryptsetup, libdevmapper, libelf, libffi, libgcc, libglib, libinih, libisal, libjansson, libjson-c, libmnl, libncurses, libnetfilter_conntrack, libnetfilter_cthelper, libnetfilter_cttimeout, libnetfilter_queue, libnfnetlink, libnftnl, libnl, libnvidia-container, libnvme, libpcre, libpopt, libseccomp, libselinux, libsemanage, libsepol, libstd-rust, libtirpc, libtss2, liburcu, libxcrypt, libz, libzstd, login
- Build/package tools: Cargo manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: sources/api/apiclient/src/lib.rs, sources/api/apiclient/src/main.rs, sources/api/apiserver/src/lib.rs, sources/api/apiserver/src/server/mod.rs

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-core-kit/blob/develop/README.md
- README SHA: 1f3ef5b98b6c7c69069deb0adfdf68be41da4616
- Manifests: Cargo.toml, Makefile, sources/Cargo.toml, kits/bottlerocket-core-kit/Cargo.toml, packages/amazon-ecs-cni-plugins/Cargo.toml, packages/amazon-ssm-agent/Cargo.toml
- Sampled source files: sources/api/apiclient/src/lib.rs, sources/api/apiclient/src/main.rs, sources/api/apiserver/src/lib.rs, sources/api/apiserver/src/server/mod.rs
- Git tree state: captured
- Evidence fingerprint: 0291da29227f0338c10f1d627a1cc1197aa6ea949541c0dad1c554b88f6670d3

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
