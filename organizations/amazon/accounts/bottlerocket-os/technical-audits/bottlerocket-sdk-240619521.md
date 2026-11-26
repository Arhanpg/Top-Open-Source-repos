# bottlerocket-os/bottlerocket-sdk

- Company: Amazon
- Account: bottlerocket-os
- Repository: https://github.com/bottlerocket-os/bottlerocket-sdk
- Default branch: develop
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T06:58:20+00:00

## Project purpose

This is the SDK for Bottlerocket.

## Why this project is used

A software development kit for Bottlerocket

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, Dockerfile, Shell, Rust, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: anyhow, askalono, cargo_metadata, cel.dev/expr, clap, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, cloud.google.com/go/iam, cloud.google.com/go/monitoring, cloud.google.com/go/storage, cyphar.com/go-pathrs, dario.cat/mergo, github.com/BurntSushi/toml, github.com/CycloneDX/cyclonedx-go, github.com/DataDog/zstd, github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp, github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric, github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Microsoft/go-winio, github.com/Microsoft/hcsshim, github.com/OneOfOne/xxhash, github.com/ProtonMail/go-crypto, github.com/STARRY-S/zip, github.com/acobaugh/osrelease, github.com/adrg/xdg, github.com/agext/levenshtein, github.com/anchore/clio, github.com/anchore/fangs, github.com/anchore/go-collections, github.com/anchore/go-homedir, github.com/anchore/go-logger, github.com/anchore/go-lzo, github.com/anchore/go-macholibre, github.com/anchore/go-rpmdb, github.com/anchore/go-struct-converter, github.com/anchore/go-sync, github.com/anchore/go-version, github.com/anchore/packageurl-go, github.com/anchore/stereoscope, github.com/anchore/syft, github.com/andybalholm/brotli, github.com/apparentlymart/go-textseg/v15, github.com/aquasecurity/go-pep440-version, github.com/aquasecurity/go-version, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/checksum, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/internal/s3shared, github.com/aws/aws-sdk-go-v2/service/s3, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/aymanbagabas/go-osc52/v2, github.com/becheran/wildmatch-go, github.com/bgentry/go-netrc, github.com/bitnami/go-version, github.com/blakesmith/ar, github.com/bmatcuk/doublestar/v4, github.com/bodgit/plumbing, github.com/bodgit/sevenzip, github.com/bodgit/windows, github.com/cespare/xxhash/v2, github.com/charmbracelet/colorprofile, github.com/charmbracelet/lipgloss, github.com/charmbracelet/x/ansi, github.com/charmbracelet/x/cellbuf, github.com/charmbracelet/x/term, github.com/clipperhouse/displaywidth, github.com/clipperhouse/uax29/v2, github.com/cloudflare/circl, github.com/cncf/xds/go, github.com/containerd/cgroups/v3, github.com/containerd/containerd/api, github.com/containerd/containerd/v2, github.com/containerd/continuity, github.com/containerd/errdefs, github.com/containerd/errdefs/pkg, github.com/containerd/fifo, github.com/containerd/log, github.com/containerd/platforms, github.com/containerd/plugin, github.com/containerd/ttrpc, github.com/containerd/typeurl/v2, github.com/cyphar/filepath-securejoin, github.com/davecgh/go-spew, github.com/deitch/magic, github.com/diskfs/go-diskfs, github.com/distribution/reference, github.com/docker/cli, ignore, maplit, semver, serde, spdx, tempfile, toml, twox-hash, walkdir
- Build/package tools: Cargo manifest, Docker build configuration, Go module manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: license-scan/src/main.rs, sbomtool/cmd/sbomtool/main.go, license-scan/src/license_store.rs, sbomtool/cmd/sbomtool/generate_test.go

## Setup and usage

No setup information established.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/bottlerocket-os/bottlerocket-sdk/blob/develop/README.md
- README SHA: 2a8eaa1262a9c3227826b7d6d119473474465d4d
- Manifests: Dockerfile, Makefile, license-scan/Cargo.toml, license-scan/Makefile, sbomtool/go.mod, sbomtool/Makefile
- Sampled source files: license-scan/src/main.rs, sbomtool/cmd/sbomtool/main.go, license-scan/src/license_store.rs, sbomtool/cmd/sbomtool/generate_test.go
- Git tree state: captured
- Evidence fingerprint: 6640f3f880e960fd3cf7b8d1ad119b05c4c3fde615ddcbf115c826cc035ddb3b

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
