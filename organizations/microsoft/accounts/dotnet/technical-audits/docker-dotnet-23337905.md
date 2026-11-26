# dotnet/Docker.DotNet

- Company: Microsoft
- Account: dotnet
- Repository: https://github.com/dotnet/Docker.DotNet
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:49:01+00:00

## Project purpose

﻿# .NET Client for Docker Remote API

## Why this project is used

:whale: .NET (C#) Client Library for Docker API

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C#, Go, Batchfile
- Frameworks/libraries: Unknown / not established
- Dependency names: github.com/davecgh/go-spew, github.com/docker/docker, github.com/docker/go-connections, github.com/docker/go-units, github.com/gogo/protobuf, github.com/google/go-cmp, github.com/kr/text, github.com/moby/term, github.com/morikuni/aec, github.com/opencontainers/go-digest, github.com/opencontainers/image-spec, github.com/stretchr/testify, golang.org/x/sys, golang.org/x/xerrors, gopkg.in/check.v1, gopkg.in/yaml.v3, gotest.tools/v3
- Build/package tools: Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/Docker.DotNet.BasicAuth/BasicAuthCredentials.cs, src/Docker.DotNet.BasicAuth/BasicAuthHandler.cs, src/Docker.DotNet.BasicAuth/MaybeSecureString.cs, src/Docker.DotNet.X509/CertificateCredentials.cs

## Setup and usage

- Installation: [](https://www.nuget.org/packages/Docker.DotNet)
- Installation: You can add this library to your project using [NuGet][nuget].
- Installation: **Package Manager Console**
- Installation: Run the following command in the “Package Manager Console”:
- Installation: > PM> Install-Package Docker.DotNet
- Installation: Right click to your project in Visual Studio, choose “Manage NuGet Packages” and search for ‘Docker.DotNet’ and click ‘Install’.
- Installation: ([see NuGet Gallery][nuget-gallery].)
- Installation: **.NET Core Command Line Interface**

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/dotnet/Docker.DotNet/blob/master/README.md
- README SHA: f54f82752d2386a6e7d2c01906efed0f6db4784a
- Manifests: tools/specgen/go.mod
- Sampled source files: src/Docker.DotNet.BasicAuth/BasicAuthCredentials.cs, src/Docker.DotNet.BasicAuth/BasicAuthHandler.cs, src/Docker.DotNet.BasicAuth/MaybeSecureString.cs, src/Docker.DotNet.X509/CertificateCredentials.cs
- Git tree state: captured
- Evidence fingerprint: 36df9e30675cfdb0a90bbb60f51fb8b7d6d05262cb27e3638e6daf65989d7fc9

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
