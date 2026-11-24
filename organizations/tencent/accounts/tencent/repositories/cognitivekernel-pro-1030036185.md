# Tencent/CognitiveKernel-Pro

- Company: Tencent
- GitHub account: [https://github.com/Tencent](https://github.com/Tencent)
- Mapping status: verified
- Repository: [Tencent/CognitiveKernel-Pro](https://github.com/Tencent/CognitiveKernel-Pro)
- Default branch: main
- README: [Open upstream README](https://github.com/Tencent/CognitiveKernel-Pro/blob/main/readme.md)
- README blob SHA: 3cea0211f6ac615fd8ee21a5c8656897dea860a6
- README bytes captured: 17976
- README truncated at capture limit: False
- Repository ID: 1030036185
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Deep Research Agent CognitiveKernel-Pro from Tencent AI Lab. Paper: https://arxiv.org/pdf/2508.00414

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T04:30:42+00:00

### Short excerpt (up to 300 words)

> No README excerpt captured. Use the upstream README link.

### README headings

- Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training
- Updates
- Running Cognitive Kernel-Pro (CogKernel-Pro for short) Agent
- Environment
- Python
- Web Server (Powered by Playwright)
- Example (A simple example)
- Assume we have set up a vllm model server and a web-browser server (currently these are active: WEB_IP
- run simple test
- use "NO_NULL_STDIN=1" for easier debugging
- you can also remove `--input` field to directly input your task from stdin
- you can also remove `-mpdb` flag to run the program directly instead of in debugging mode
- Example (Experimenting on the GAIA dataset)
- Step 1: prepare data
- decompress the gaia data (or you can download it by yourself from huggingface)
- -> assume all the gaia related input files are at the same DIR as the input json meta-file
- Step 2: prepare web service (recommending using a PC or laptop to enable better network connection)
- -> prepare things according to "./ck_web/_web/run_local.sh"
- Step 3: prepare a vllm instance for model calling
- use gpt
- or use claude
- Step 4: Setup search engine
- either using google api
- or simply use DuckDuckGo
- Step 5: run
- it will be more stable to run a new web-browser for each web call, setup WEB_PORT (web browser service's port) and WEB_DIR (main dir of the web browser service)
- moreover, it is slightly better to use non-boxed screenshot (make sure to update the latest `server.js` and set screenshot_boxed=False)
- Step 6: analyze and check the output
- Extra Running Config
- calling claude+thinking for the outside main-agent

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

No selected README section excerpts were captured.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 312,276 |
| JavaScript | 37,311 |
| Shell | 2,523 |
| Dockerfile | 1,126 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- ck_pro/ck_web/_web/Dockerfile (capture: captured)
- ck_pro/ck_web/_web/package.json (capture: captured) — dependency clues: async-mutex, express, js-yaml, playwright, playwright-extra, puppeteer-extra-plugin-stealth, uuid

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 533
- Forks at capture: 57
- Last updated: 2026-11-16T14:10:10Z
- Last pushed: 2026-10-21T09:01:41Z
- Topics: agent, llm

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Tencent/CognitiveKernel-Pro)
- [README](https://github.com/Tencent/CognitiveKernel-Pro/blob/main/readme.md)
- [Issues](https://github.com/Tencent/CognitiveKernel-Pro/issues)
- [Releases](https://github.com/Tencent/CognitiveKernel-Pro/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
