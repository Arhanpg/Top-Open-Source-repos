# PaddlePaddle/FastDeploy

- Company: Baidu
- GitHub account: [https://github.com/PaddlePaddle](https://github.com/PaddlePaddle)
- Mapping status: official-project-linked
- Repository: [PaddlePaddle/FastDeploy](https://github.com/PaddlePaddle/FastDeploy)
- Default branch: develop
- README: [Open upstream README](https://github.com/PaddlePaddle/FastDeploy/blob/develop/README.md)
- README blob SHA: 336426870626616e13f977f1ec24f61b976c4af7
- Repository ID: 507861208
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

High-performance Inference and Deployment Toolkit for LLMs and VLMs based on PaddlePaddle

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:41+00:00

### Short excerpt (up to 100 words)

> **[2026-03] FastDeploy v2.5 全新发布!** 新增Qwen3-VL与Qwen3-VL MoE模型部署支持，新增W4AFP8量化方法，增强强化学习训练支持能力，包含170+项Bug修复与性能优化，升级全部内容参阅 v2.5 ReleaseNote。 **[2026-01] FastDeploy v2.4**: 新增 DeepSeek V3 与 Qwen3-MoE 模型的 PD 分离部署，增强MTP 投机解码能力，全面优化多硬件平台上的 MoE 推理与多模态前缀缓存性能，升级全部内容参阅 v2.4 ReleaseNote。 **[2025-11] FastDeploy v2.3**: 新增ERNIE-4.5-VL-28B-A3B-Thinking与PaddleOCR-VL-0.9B两大重磅模型在多硬件平台上的部署支持，进一步优化全方位推理性能，以及带来更多部署功能和易用性的提升，升级全部内容参阅v2.3 ReleaseNote。 **[2025-09] FastDeploy v2.2**: HuggingFace生态模型兼容，性能进一步优化，更新增对baidu/ERNIE-21B-A3B-Thinking支持! **[2025-08] FastDeploy v2.1**:全新的KV Cache调度策略，更多模型支持PD分离和CUDA Graph，昆仑、海光等更多硬件支持增强，全方面优化服务和推理引擎的性能。 **FastDeploy** 是基于飞桨（PaddlePaddle）的大语言模型（LLM）与视觉语言模型（VLM）推理部署工具包，提供**开箱即用的生产级部署方案**，核心技术特性包括： - 🚀 **负载均衡式PD分解**：工业级解决方案，支持上下文缓存与动态实例角色切换，在保障SLO达标和吞吐量的同时优化资源利用率 - 🔄 **统一KV缓存传输**：轻量级高性能传输库，支持智能NVLink/RDMA选择 - 🤝 **OpenAI API服务与vLLM兼容**：单命令部署，兼容vLLM接口 - 🧮 **全量化格式支持**：W8A16、W8A8、W4A16、W4A8、W2A16、FP8等 - ⏩ **高级加速技术**：推测解码、多令牌预测（MTP）及分块预填充 - 🖥️ **多硬件支持**：NVIDIA GPU、昆仑芯XPU、海光DCU、天数智芯GPU、燧原GCU、沐曦GPU、英特尔Gaudi等 - 操作系统: Linux - Python: 3.10 ~ 3.12 FastDeploy 支持在**英伟达（NVIDIA）GPU**、**昆仑芯（Kunlunxin）XPU**、**天数（Iluvatar）GPU**、**燧原（Enflame）GCU**、**海光（Hygon）DCU** 以及其他硬件上进行推理部署。详细安装说明如下： - 英伟达 GPU - 昆仑芯 XPU - 天数 CoreX - 燧原 S60 - 海光 DCU - 沐曦 GPU - 英特尔 Gaudi 通过我们的文档了解如何使用 FastDeploy： - 10分钟快速部署 - ERNIE-4.5 部署 -

### README headings

- FastDeploy 飞桨大模型高效部署套件
- 最新活动
- 关于
- 要求
- 安装
- 入门指南
- 支持模型列表
- 进阶用法
- 致谢

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 14,538,248 |
| C++ | 4,138,660 |
| Cuda | 4,076,701 |
| Go | 204,988 |
| Shell | 168,915 |
| C | 21,982 |
| CMake | 14,368 |
| Makefile | 666 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- pyproject.toml (capture: captured)
- requirements.txt (capture: captured) — dependency clues: aiozmq, aistudio_sdk, crcmod, cupy-cuda12x, einops, etcd3, fast_dataindex, fastapi, flake8, flashinfer-python-paddle, gradio, gunicorn, httpx, modelscope, moviepy, msgpack, msgspec, openai, opentelemetry-api, opentelemetry-distro
- setup.py (capture: captured)
- benchmarks/requirements.txt (capture: captured) — dependency clues: Pillow, aiohttp, numpy, pyyaml, requests, tqdm
- docs/requirements.txt (capture: captured) — dependency clues: mkdocs, mkdocs-get-deps, mkdocs-material, mkdocs-material-extensions, mkdocs-multilang, mkdocs-static-i18n
- fastdeploy/golang_router/go.mod (capture: captured) — dependency clues: github.com/beorn7/perks, github.com/bytedance/sonic, github.com/cespare/xxhash/v2, github.com/chenzhuoyu/base64x, github.com/davecgh/go-spew, github.com/gabriel-vasile/mimetype, github.com/gin-contrib/sse, github.com/gin-gonic/gin, github.com/go-playground/locales, github.com/go-playground/universal-translator, github.com/go-playground/validator/v10, github.com/goccy/go-json, github.com/google/go-cmp, github.com/json-iterator/go, github.com/klauspost/compress, github.com/klauspost/cpuid/v2, github.com/leodido/go-urn, github.com/mattn/go-isatty, github.com/modern-go/concurrent, github.com/modern-go/reflect2

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 3723
- Forks at capture: 756
- Last updated: 2026-11-22T15:43:37Z
- Last pushed: 2026-09-24T14:17:31Z
- Topics: ernie, ernie-45, ernie-45-vl, inference, llm, llm-serving, openai, serving, vllm

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/PaddlePaddle/FastDeploy)
- [README](https://github.com/PaddlePaddle/FastDeploy/blob/develop/README.md)
- [Issues](https://github.com/PaddlePaddle/FastDeploy/issues)
- [Releases](https://github.com/PaddlePaddle/FastDeploy/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
