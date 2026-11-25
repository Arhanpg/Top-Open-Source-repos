# Tencent/AI-Infra-Guard

- Company: Tencent
- Account: Tencent
- Repository: https://github.com/Tencent/AI-Infra-Guard
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T04:01:08+00:00

## Project purpose

🌐 🇬🇧 English · 🇨🇳 中文

## Why this project is used

A full-stack AI Red Teaming platform securing AI ecosystems via Agent Scan, Skills Scan, MCP scan, AI Infra scan and LLM jailbreak evaluation.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, TypeScript, Go, Jupyter Notebook, HTML, Shell, JavaScript, Dockerfile, CSS
- Frameworks/libraries: Unknown / not established
- Dependency names: PyYAML, aiohttp, deepeval, ecoji, filippo.io/edwards25519, github.com/BurntSushi/toml, github.com/KyleBanks/depth, github.com/Mzack9999/gcache, github.com/Mzack9999/go-http-digest-auth-client, github.com/PuerkitoBio/goquery, github.com/PuerkitoBio/purell, github.com/PuerkitoBio/urlesc, github.com/akrylysov/pogreb, github.com/andybalholm/brotli, github.com/andybalholm/cascadia, github.com/asaskevich/govalidator, github.com/aymerick/douceur, github.com/benbjohnson/clock, github.com/bits-and-blooms/bitset, github.com/bytedance/sonic, github.com/bytedance/sonic/loader, github.com/cloudflare/circl, github.com/cloudwego/base64x, github.com/cpuguy83/go-md2man/v2, github.com/davecgh/go-spew, github.com/dimchansky/utfbom, github.com/docker/go-units, github.com/dsnet/compress, github.com/dustin/go-humanize, github.com/fsnotify/fsnotify, github.com/gabriel-vasile/mimetype, github.com/gaissmai/bart, github.com/gin-contrib/sse, github.com/gin-gonic/gin, github.com/glebarez/go-sqlite, github.com/glebarez/sqlite, github.com/go-openapi/jsonpointer, github.com/go-openapi/jsonreference, github.com/go-openapi/spec, github.com/go-openapi/swag, github.com/go-playground/locales, github.com/go-playground/universal-translator, github.com/go-playground/validator/v10, github.com/go-rod/rod, github.com/go-sql-driver/mysql, github.com/goccy/go-json, github.com/golang/snappy, github.com/google/flatbuffers, github.com/google/uuid, github.com/gorilla/css, github.com/gorilla/websocket, github.com/hashicorp/errwrap, github.com/hashicorp/go-multierror, github.com/hashicorp/go-version, github.com/inconshreveable/mousetrap, github.com/jinzhu/inflection, github.com/jinzhu/now, github.com/josharian/intern, github.com/json-iterator/go, github.com/klauspost/compress, github.com/klauspost/cpuid/v2, github.com/klauspost/pgzip, github.com/leodido/go-urn, github.com/lestrrat-go/strftime, github.com/liushuochen/gotable, github.com/logrusorgru/aurora, github.com/mailru/easyjson, github.com/mark3labs/mcp-go, github.com/mattn/go-isatty, github.com/mholt/archiver/v3, github.com/microcosm-cc/bluemonday, github.com/miekg/dns, github.com/modern-go/concurrent, github.com/modern-go/reflect2, github.com/ncruces/go-strftime, github.com/nwaples/rardecode, github.com/openai/openai-go, github.com/panjf2000/ants/v2, github.com/pelletier/go-toml/v2, github.com/pierrec/lz4/v4, github.com/pkg/errors, github.com/pmezard/go-difflib, github.com/projectdiscovery/blackrock, github.com/projectdiscovery/fastdialer, github.com/projectdiscovery/fdmax, github.com/projectdiscovery/gologger, github.com/projectdiscovery/hmap, github.com/projectdiscovery/networkpolicy, github.com/projectdiscovery/rawhttp, github.com/projectdiscovery/retryabledns, github.com/projectdiscovery/retryablehttp-go, github.com/projectdiscovery/utils, github.com/refraction-networking/utls, github.com/remeh/sizedwaitgroup, github.com/remyoudompheng/bigfft, github.com/rogpeppe/go-internal, github.com/russross/blackfriday/v2, github.com/saintfish/chardet, github.com/sirupsen/logrus, github.com/spaolacci/murmur3, github.com/spf13/cast, github.com/spf13/cobra, github.com/spf13/pflag, github.com/stretchr/testify, grpcio, httpx, jieba, loguru, openai, openpyxl, pandas, pyahocorasick, pyarrow, pydantic, python-dotenv, requests, tabulate, tqdm, websockets, xlrd
- Build/package tools: Docker build configuration, Go module manifest, Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cmd/agent/main.go, cmd/cli/main.go, cmd/yamlcheck/main.go, frontend/src/i18n/index.ts

## Setup and usage

- Other Installation Methods: **Method 2: One-Click Install Script （Recommended）**

## Limitations and caveats

- LLM Security Assessment / Jailbreak: Evaluate a model that exposes an OpenAI-compatible API.
- LLM Security Assessment / Jailbreak: pip install aig-model-scan
- LLM Security Assessment / Jailbreak: --model "gpt-4o-mini" \
- LLM Security Assessment / Jailbreak: --base_url "https://api.openai.com/v1" \
- LLM Security Assessment / Jailbreak: --api_key "your-api-key" \
- LLM Security Assessment / Jailbreak: --max_concurrent 10 \
- 🔗 More Security Tools: If you are interested in code security, we recommend A.S.E (AICGSecEval), the industry's first project-level AI-generated code security evaluation framework open-sourced by the Tencent Wukong Code Security Team.

## Evidence and provenance

- README: https://github.com/Tencent/AI-Infra-Guard/blob/main/README.md
- README SHA: e34866e9523465ec717e40b3d095529aefcb4972
- Manifests: Dockerfile, go.mod, agent-scan/pyproject.toml, agent-scan/requirements.txt, AIG-PromptSecurity/Dockerfile, AIG-PromptSecurity/pyproject.toml
- Sampled source files: cmd/agent/main.go, cmd/cli/main.go, cmd/yamlcheck/main.go, frontend/src/i18n/index.ts
- Git tree state: captured
- Evidence fingerprint: 79956f1b4401ab3819cd9cc9daaa60216b1408976ddbc5c72e19595b144d68ea

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
