# PaddlePaddle/PaddleSleeve

- Company: Baidu
- GitHub account: [https://github.com/PaddlePaddle](https://github.com/PaddlePaddle)
- Mapping status: official-project-linked
- Repository: [PaddlePaddle/PaddleSleeve](https://github.com/PaddlePaddle/PaddleSleeve)
- Default branch: main
- README: [Open upstream README](https://github.com/PaddlePaddle/PaddleSleeve/blob/main/README.md)
- README blob SHA: d1e6f4e1bfad06c12c01533adb21f4270a5c1802
- README bytes captured: 9101
- README truncated at capture limit: False
- Repository ID: 365999954
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

PaddleSleeve

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T09:35:04+00:00

### Short excerpt (up to 300 words)

> PaddleSleeve === **PaddleSleeve是基于百度开源深度学习平台飞桨的安全与隐私工具**，为AI产业实践提供丰富、有效、易用的模型安全及隐私评测及保护能力。 PaddleSleeve作为一款贴近实践应用与现实风险的AI安全和隐私工具，具备以下特性： CodeSecurity为飞桨深度学习框架提供了代码漏洞挖掘的方法与相关示例。飞桨等深度学习框架主要由Python和C++编写，可能存在堆栈溢出、数组越界等代码安全缺陷，会对框架的安全性与稳定性产生重要影响。CodeSecurity模块通过分析源代码、模糊测试等方式，充分挖掘框架中存在的安全缺陷以及规范性缺陷，并将漏洞挖掘方案贡献开源社区，以期与社区众多开发者和安全研究者一同提升飞桨框架代码的代码质量与安全性。 目前，CodeSecurity模块包含两个部分： Fuzzing：采用atheris+libfuzzer，对PaddlePaddle API进行模糊测试，动态、快速地发现框架在运行中存在的漏洞；

### README headings

- 主要功能
- 技术特色
- 对抗样本生成与防御 AdvBox
- 鲁棒性评测 Robustness
- 模型隐私风险测试与评估 PrivBox
- 隐私增强 PrivacyGuard ##
- 代码安全审计 CodeSecurity ##
- 端模型保护框架 Paddle-LiTEE ##
- 版权和许可证

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> PaddleSleeve === **PaddleSleeve是基于百度开源深度学习平台飞桨的安全与隐私工具**，为AI产业实践提供丰富、有效、易用的模型安全及隐私评测及保护能力。 PaddleSleeve作为一款贴近实践应用与现实风险的AI安全和隐私工具，具备以下特性：

### Limitations and security: 代码安全审计 CodeSecurity

> CodeSecurity为飞桨深度学习框架提供了代码漏洞挖掘的方法与相关示例。飞桨等深度学习框架主要由Python和C++编写，可能存在堆栈溢出、数组越界等代码安全缺陷，会对框架的安全性与稳定性产生重要影响。CodeSecurity模块通过分析源代码、模糊测试等方式，充分挖掘框架中存在的安全缺陷以及规范性缺陷，并将漏洞挖掘方案贡献开源社区，以期与社区众多开发者和安全研究者一同提升飞桨框架代码的代码质量与安全性。 目前，CodeSecurity模块包含两个部分： Fuzzing：采用atheris+libfuzzer，对PaddlePaddle API进行模糊测试，动态、快速地发现框架在运行中存在的漏洞；

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 9,814,615 |
| C++ | 1,784,191 |
| Rust | 220,603 |
| C | 31,459 |
| Cuda | 27,776 |
| CodeQL | 12,291 |
| Linker Script | 10,600 |
| Makefile | 9,082 |
| CMake | 4,794 |
| Shell | 2,686 |
| Cython | 2,576 |
| Dockerfile | 1,906 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- PrivBox/setup.py (capture: captured)
- Robustness/setup.py (capture: captured)
- AdvBox/attack_defence_text/requirements.txt (capture: captured) — dependency clues: numpy, paddlepaddle_gpu, pandas, pygame, pypinyin, scikit_learn, tensorflow, torch, tqdm, transformers
- AdvBox/obj_detection/requirements.txt (capture: captured) — dependency clues: matplotlib, opencv-python, pandas, pycocotools, scipy, tqdm
- Robustness/LaneDetection_Evaluation/requirements.txt (capture: captured) — dependency clues: numpy, opencv-python, torch, torchvision
- CodeSecurity/fuzzing/op_fuzzing/Dockerfile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 78
- Forks at capture: 22
- Last updated: 2026-06-30T16:40:28Z
- Last pushed: 2026-02-03T07:08:47Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/PaddlePaddle/PaddleSleeve)
- [README](https://github.com/PaddlePaddle/PaddleSleeve/blob/main/README.md)
- [Issues](https://github.com/PaddlePaddle/PaddleSleeve/issues)
- [Releases](https://github.com/PaddlePaddle/PaddleSleeve/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
