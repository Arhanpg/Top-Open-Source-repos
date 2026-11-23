# container

<sub>Company: Apple · Repository: [apple/container](https://github.com/apple/container) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

`container` is a command-line tool for creating and running Linux containers as lightweight virtual machines on a Mac. The README says it is written in Swift and optimized for Apple silicon.

**Problem it addresses:** developers on Apple-silicon Macs need a way to run Linux workloads and standard container images locally. This tool offers a Mac-native workflow while keeping images compatible with the Open Container Initiative (OCI) image format.

## How it works

The project consumes and produces OCI-compatible container images. That means users can pull images from standard container registries, run them locally, and push images they build back to registries. The README explains that the tool uses Apple's separate [Containerization Swift package](https://github.com/apple/containerization) for low-level container, image and process management.

A simple documented run command is:

```bash
container run --rm alpine echo hello
```

The example pulls the Alpine image, runs it in a lightweight Linux virtual machine, prints the supplied output and removes the container after it exits.

## Requirements and platform scope

The README identifies the following requirements:

- A Mac with Apple silicon.
- macOS 26 or later.
- The system service must be started before normal use.

The maintainers state that the project uses virtualization and networking capabilities introduced or enhanced in macOS 26 and do not support older macOS releases. This is a firm platform constraint, not merely a suggested configuration.

## Main capabilities

- Create and run Linux containers on Mac.
- Use OCI-compatible images and standard container registries.
- Build and publish images that can be consumed by other OCI-compatible applications.
- Manage the container system service.
- Install signed release packages.
- Upgrade, downgrade and uninstall through documented scripts.
- Follow tutorials for building and publishing an image.

## Technology profile

| Area | README-supported details |
|---|---|
| Implementation language | Swift |
| Host platform | macOS 26+ |
| Hardware | Apple silicon |
| Workload environment | Linux containers in lightweight virtual machines |
| Image format | OCI-compatible container images |
| Low-level package | Apple's Containerization Swift package |
| User interface | Command-line tool and system service |

## Installation and lifecycle commands

The README recommends downloading the signed installer from GitHub Releases. After installation, start the system service:

```bash
container system start
```

For upgrade or downgrade operations, the README instructs users to stop the existing service first. The repository also provides scripts for updating and uninstalling the tool. Refer to the upstream instructions for the exact flags and release version.

## Where it fits

- Local development of Linux container workloads on Apple-silicon Macs.
- Testing OCI images before publishing them to a registry.
- Building and running small Linux services locally.
- Exploring a Mac-native container runtime based on virtualized Linux environments.

This tool's scope is specifically documented around Mac and Apple silicon. It should not be treated as a cross-platform replacement for container engines on Linux or Windows without separate support evidence.

## Upstream references

- [Repository](https://github.com/apple/container)
- [Primary README](https://github.com/apple/container/blob/main/README.md)
- [Releases](https://github.com/apple/container/releases)
- [Containerization Swift package](https://github.com/apple/containerization)
- [Getting started tutorial](https://github.com/apple/container/blob/main/docs/tutorials/start-here.md)

**Evidence note:** README blob inspected: `7077937f1c3d362ab32a6488cc9e2f9164b001c8`.
