# Containerization

- Company association: Apple
- Upstream GitHub account: [apple](https://github.com/apple)
- Repository: [apple/containerization](https://github.com/apple/containerization)
- Default branch: main
- README: [Open upstream README](https://github.com/apple/containerization/blob/main/README.md)
- Review status: README inspected and summarized
- README blob SHA: f658b08ddadf787997ad24b6b6cd4b05ca476f8a
- Relationship note: The repository is maintained under Apple's primary public GitHub organization.

## Project overview

A Swift package that exposes APIs for running Linux containers inside lightweight virtual machines. On Apple silicon macOS it uses Apple's Virtualization framework; the README also documents a Linux backend based on cloud-hypervisor and KVM.

## Features and capabilities documented by the README

- Manages OCI images and interacts with remote container registries.
- Creates and populates ext4 filesystems and provides Netlink socket APIs.
- Spawns lightweight VMs, configures runtime environments and launches containerized processes.
- Provides an optimized Linux kernel configuration and a guest init system, vminitd, exposing a gRPC API over vsock.
- Supports Rosetta 2 for linux/amd64 containers on Apple silicon.
- Abstracts virtual-machine backends and documents macOS Virtualization.framework plus Linux cloud-hypervisor/KVM implementations.
- Provides cctl as a playground for OCI image, registry, rootfs and container-run workflows.

## Technology stack

Swift package; Apple Virtualization.framework on macOS/Apple silicon; Linux cloud-hypervisor and KVM; virtio-blk, virtio-fs/virtiofsd and TAP networking for the Linux backend; gRPC/Protobuf; Swift Package Manager; make build/test targets. README lists grpc-swift and swift-protobuf.

## Getting started

The README lists Apple silicon, macOS 26 and Xcode 26 as build requirements. Install the separate apple/container CLI, then use make all, make test integration and make docs. Integration tests require a Linux kernel; a make fetch-default-kernel target is provided.

## Lifecycle, compatibility and operational considerations

The README identifies version 0.1.0 as the first official release and warns that earlier versions have no source-stability guarantees. Stability is guaranteed only within minor versions; pin an upper minor bound when needed. The Linux backend requires host setup such as KVM access and, where applicable, cloud-hypervisor, virtiofsd and TAP/bridge/NAT networking.

## Evaluation guidance

Check the current upstream release, dependency manifests, exact platform/toolchain requirements, licence and security guidance before adoption. This dossier summarizes the inspected README; it is not a full source-code, dependency-vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/apple/containerization)
- [README](https://github.com/apple/containerization/blob/main/README.md)
- [Issues](https://github.com/apple/containerization/issues)
- [Releases](https://github.com/apple/containerization/releases)

Evidence note: the README blob SHA identifies the upstream README revision inspected. Technology details not established by the README or official project page are left unspecified.
