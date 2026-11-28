# siemens/agent-router

- Company: Siemens
- Account: Siemens
- Repository: https://github.com/siemens/agent-router
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:07:12+00:00

## Project purpose

An Agentic AI Foundation project. Formerly Envoy AI Gateway .

## Why this project is used

Manages Unified Access to Generative AI Services built on Envoy Gateway

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Go, MDX, TypeScript, CSS, Go Template, Makefile, JavaScript, Python, Shell, Dockerfile
- Frameworks/libraries: Unknown / not established
- Dependency names: 4d63.com/gocheckcompilerdirectives, 4d63.com/gochecknoglobals, @docusaurus/core, @docusaurus/module-type-aliases, @docusaurus/preset-classic, @docusaurus/theme-classic, @docusaurus/theme-mermaid, @docusaurus/tsconfig, @docusaurus/types, @mdx-js/react, @types/glob, al.essio.dev/pkg/shellescape, cel.dev/expr, charm.land/lipgloss/v2, cloud.google.com/go, cloud.google.com/go/auth, cloud.google.com/go/auth/oauth2adapt, cloud.google.com/go/compute/metadata, clsx, codeberg.org/chavacava/garif, codeberg.org/polyfloyd/go-errorlint, dario.cat/mergo, dev.gaijin.team/go/exhaustruct/v4, dev.gaijin.team/go/exhaustruct/v5, dev.gaijin.team/go/golib, github.com/4meepo/tagalign, github.com/Abirdcfly/dupword, github.com/AdaLogics/go-fuzz-headers, github.com/AdminBenni/iota-mixing, github.com/AlwxSin/noinlineerr, github.com/Antonboom/errname, github.com/Antonboom/nilnil, github.com/Antonboom/testifylint, github.com/Azure/azure-sdk-for-go/sdk/azcore, github.com/Azure/azure-sdk-for-go/sdk/azidentity, github.com/Azure/azure-sdk-for-go/sdk/internal, github.com/Azure/go-ansiterm, github.com/AzureAD/microsoft-authentication-library-for-go, github.com/BurntSushi/toml, github.com/ClickHouse/clickhouse-go-linter, github.com/Djarvur/go-err113, github.com/MakeNowJust/heredoc, github.com/Masterminds/goutils, github.com/Masterminds/semver/v3, github.com/Masterminds/sprig/v3, github.com/Masterminds/squirrel, github.com/Masterminds/vcs, github.com/Microsoft/go-winio, github.com/MirrexOne/unqueryvet, github.com/NYTimes/gziphandler, github.com/OpenPeeDeeP/depguard/v2, github.com/ProtonMail/go-crypto, github.com/a8m/envsubst, github.com/alecthomas/chroma/v2, github.com/alecthomas/go-check-sumtype, github.com/alecthomas/kong, github.com/alexflint/go-arg, github.com/alexflint/go-scalar, github.com/alexkohler/nakedret/v2, github.com/alexkohler/prealloc, github.com/alfatraining/structtag, github.com/alingse/asasalint, github.com/alingse/nilnesserr, github.com/andybalholm/brotli, github.com/anthropics/anthropic-sdk-go, github.com/antlr4-go/antlr/v4, github.com/apache/skywalking-eyes, github.com/asaskevich/govalidator, github.com/ashanbrown/forbidigo/v2, github.com/ashanbrown/makezero/v2, github.com/avast/retry-go/v5, github.com/aws/aws-sdk-go, github.com/aws/aws-sdk-go-v2, github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream, github.com/aws/aws-sdk-go-v2/config, github.com/aws/aws-sdk-go-v2/credentials, github.com/aws/aws-sdk-go-v2/feature/ec2/imds, github.com/aws/aws-sdk-go-v2/internal/configsources, github.com/aws/aws-sdk-go-v2/internal/endpoints/v2, github.com/aws/aws-sdk-go-v2/internal/v4a, github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding, github.com/aws/aws-sdk-go-v2/service/internal/presigned-url, github.com/aws/aws-sdk-go-v2/service/signin, github.com/aws/aws-sdk-go-v2/service/sso, github.com/aws/aws-sdk-go-v2/service/ssooidc, github.com/aws/aws-sdk-go-v2/service/sts, github.com/aws/smithy-go, github.com/bahlo/generic-list-go, github.com/beorn7/perks, github.com/bkielbasa/cyclop, github.com/blang/semver/v4, github.com/blizzy78/varnamelen, github.com/bmatcuk/doublestar/v2, github.com/bmatcuk/doublestar/v4, github.com/bombsimon/wsl/v4, github.com/bombsimon/wsl/v5, github.com/breml/bidichk, github.com/breml/errchkjson, github.com/buger/jsonparser, github.com/butuzov/ireturn, github.com/butuzov/mirror, github.com/bytedance/gopkg, github.com/bytedance/sonic, github.com/bytedance/sonic/loader, github.com/catenacyber/perfsprint, github.com/ccojocar/zxcvbn-go, github.com/cenkalti/backoff/v4, github.com/cenkalti/backoff/v5, github.com/cespare/xxhash/v2, github.com/chai2010/gettext-go, github.com/charithe/durationcheck, github.com/charmbracelet/colorprofile, github.com/charmbracelet/ultraviolet, github.com/charmbracelet/x/ansi, github.com/charmbracelet/x/term, github.com/charmbracelet/x/termios, github.com/charmbracelet/x/windows, github.com/ckaznocha/intrange, github.com/clipperhouse/displaywidth, github.com/clipperhouse/uax29/v2
- Build/package tools: Docker build configuration, Go module manifest, npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/aigw/main.go, cmd/controller/main.go, cmd/extproc/main.go, cmd/extproc/mainlib/main.go

## Setup and usage

- Quick start: Run Agent Router as a standalone, OpenAI-compatible router on your laptop with one command:
- Quick start: OPENAI_API_KEY=sk-your-key aigw run
- Quick start: Then point any OpenAI-compatible client at http://localhost:1975/v1. See the CLI guide for installation and provider auto-configuration, or the Getting Started guide to deploy on Kubernetes with Envoy Gateway.
- Usage: When using Agent Router, we refer to a two-tier gateway pattern. **The Tier One Gateway** functions as a centralized entry point, and the **Tier Two Gateway** handles ingress traffic to a self-hosted model serving cluster.
- Usage: - The **Tier One Gateway** handles authentication, top-level routing, and global rate limiting.
- Usage: - The **Tier Two Gateway** provides fine-grained control over self-hosted model access, with endpoint picker support for LLM inference optimization.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/siemens/agent-router/blob/main/README.md
- README SHA: b045824b39b25f59436dd3a5cd6d5193a6065c0c
- Manifests: Dockerfile, go.mod, Makefile, site/package.json, tools/go.mod, site/tools/og-generator/package.json
- Sampled source files: cmd/aigw/main.go, cmd/controller/main.go, cmd/extproc/main.go, cmd/extproc/mainlib/main.go
- Git tree state: captured
- Evidence fingerprint: 69174fa1c8433d2f1c177d431085b38e418d41220f52d3646a3bb08422fd5ffb

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
