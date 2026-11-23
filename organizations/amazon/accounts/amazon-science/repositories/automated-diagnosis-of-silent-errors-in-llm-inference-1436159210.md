# amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference

- Company: Amazon
- GitHub account: [https://github.com/amazon-science](https://github.com/amazon-science)
- Mapping status: official-directory-listed
- Repository: [amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference](https://github.com/amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference)
- Default branch: main
- README: [Open upstream README](https://github.com/amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference/blob/main/README.md)
- README blob SHA: fbd8da3f6377fecde0d71f044caf5248510dacdc
- Repository ID: 1436159210
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:29:30+00:00

### Short excerpt (up to 100 words)

> **ICML 2026** · Paper (arXiv) · ICML poster Yile Gu<sup>1</sup>, Zhen Zhang<sup>2</sup>, Shaowei Zhu<sup>2</sup>, Xinwei Fu<sup>2</sup>, Jun Wu<sup>2</sup>, Yida Wang<sup>2</sup>, Baris Kasikci<sup>1</sup> Ekka is an LLM agent that diagnoses **accuracy bugs in LLM inference engines** (vLLM, SGLang). Given a bug report and a model that produces different outputs in a target engine than in a reference implementation (Hugging Face `transformers` / `diffusers`), Ekka: 1. **Collects activations** from both frameworks on the same prompt (`drivers/`, `activation_collector/`). 2. **Maps components** between the two model implementations (for example HF `self_attn.q_proj/k_proj/v_proj` ↔ vLLM `self_attn.qkv_proj`). 3. **Aligns activations**: writes and validates code that reshapes each

### README headings

- Ekka: Automated Diagnosis of Silent Errors in LLM Inference
- Repository layout
- Setup
- 1. Python environments
- Agent + evaluator
- Reference (Hugging Face) driver
- Target engines: the activation hooks live in Ekka's forks of the engines.
- vLLM:   https://github.com/IKACE/vLLM   (e.g. branch v0.11.0-baseline-docker)
- SGLang: https://github.com/IKACE/SGLang (e.g. branch v0.5.6-baseline-docker)
- Install each fork in its own environment (`pip install -e .` for vLLM, `pip install -e python` for SGLang).
- 2. Paths
- 3. LLM backend
- Running a bug case
- 1) Collect activations (reference bf16 + fp32, then the target engine)
- The HF driver must be launched with torchrun (it reads RANK/WORLD_SIZE), even on one GPU.
- multi-GPU HF runs: torchrun --nproc-per-node <N> ...
- Each driver config needs `activation_collector.enabled: true` and a save_path equal to the diagnosis
- config's activation_path; keep generation at 1 token so all runs capture the same prefill pass.
- The vLLM fork always writes the `vllm_activation` prefix and ignores `save_prefix`.
- vision-language cases: drivers/driver_hf_v2_vl.py and drivers/driver_sglang_vl.py
- 2) Build class indexes the agent uses to look up source code
- 3) Diagnose
- -> $CASE/diagnosis_output_<timestamp>/ (component_mapping.json, alignment_results.json,
- detection_result.json, diagnosis_log.log, ...)
- 4) Evaluate
- Troubleshooting
- Adding a bug case
- Baselines
- Citation
- License

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,037,355 |
| Shell | 15,974 |
| Dockerfile | 4,703 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- docker-scripts/Dockerfile (capture: captured)
- agent-langgraph/my_agent/requirements.txt (capture: captured) — dependency clues: langchain, langchain-anthropic, langchain-aws, langchain-community, langchain-core, langgraph, matplotlib, numpy, python-dotenv, pyyaml, torch, transformers

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 1
- Forks at capture: 1
- Last updated: 2026-11-03T05:52:55Z
- Last pushed: 2026-11-03T03:56:46Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference)
- [README](https://github.com/amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference/blob/main/README.md)
- [Issues](https://github.com/amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference/issues)
- [Releases](https://github.com/amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
