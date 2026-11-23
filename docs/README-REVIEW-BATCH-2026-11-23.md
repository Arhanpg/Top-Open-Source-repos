# README review batch — 23 November 2026

## Summary

This batch adds **22 new repository-specific Markdown briefs** from direct inspection of upstream README files. The five company folders have updated their repository indexes and profile pages.

| Company / GitHub account | New briefs | Total README briefs in account folder after this batch |
|---|---:|---:|
| Microsoft / microsoft | 5 | 16 |
| Alphabet / Google / google | 5 | 7 |
| Apple / apple | 4 | 6 |
| NVIDIA / NVIDIA | 5 | 7 |
| Amazon / AWS / aws | 3 | 4 |
| **Total** | **22** | **40** |

## New repository briefs

### Microsoft
- [Visual Studio Code — Code - OSS](../organizations/microsoft/repositories/vscode.md) — [upstream](https://github.com/microsoft/vscode)
- [Windows Terminal, Console and Command-Line](../organizations/microsoft/repositories/terminal.md) — [upstream](https://github.com/microsoft/terminal)
- [Generative AI for Beginners](../organizations/microsoft/repositories/generative-ai-for-beginners.md) — [upstream](https://github.com/microsoft/generative-ai-for-beginners)
- [Web Development for Beginners](../organizations/microsoft/repositories/web-dev-for-beginners.md) — [upstream](https://github.com/microsoft/Web-Dev-For-Beginners)
- [AI Agents for Beginners](../organizations/microsoft/repositories/ai-agents-for-beginners.md) — [upstream](https://github.com/microsoft/ai-agents-for-beginners)

### Google
- [zx — JavaScript shell scripting utility](../organizations/alphabet-google/repositories/zx.md) — [upstream](https://github.com/google/zx)
- [Google Style Guides](../organizations/alphabet-google/repositories/styleguide.md) — [upstream](https://github.com/google/styleguide)
- [GoogleTest and GoogleMock](../organizations/alphabet-google/repositories/googletest.md) — [upstream](https://github.com/google/googletest)
- [LevelDB](../organizations/alphabet-google/repositories/leveldb.md) — [upstream](https://github.com/google/leveldb)
- [Comprehensive Rust](../organizations/alphabet-google/repositories/comprehensive-rust.md) — [upstream](https://github.com/google/comprehensive-rust)

### Apple
- [XNU — Darwin kernel](../organizations/apple/repositories/darwin-xnu.md) — [upstream](https://github.com/apple/darwin-xnu)
- [SwiftNIO](../organizations/apple/repositories/swift-nio.md) — [upstream](https://github.com/apple/swift-nio)
- [Swift Algorithms](../organizations/apple/repositories/swift-algorithms.md) — [upstream](https://github.com/apple/swift-algorithms)
- [Core ML Tools](../organizations/apple/repositories/coremltools.md) — [upstream](https://github.com/apple/coremltools)

### NVIDIA
- [NVIDIA Linux Open GPU Kernel Modules](../organizations/nvidia/repositories/open-gpu-kernel-modules.md) — [upstream](https://github.com/NVIDIA/open-gpu-kernel-modules)
- [nvidia-docker — deprecated](../organizations/nvidia/repositories/nvidia-docker.md) — [upstream](https://github.com/NVIDIA/nvidia-docker)
- [NVIDIA Deep Learning Examples](../organizations/nvidia/repositories/deeplearningexamples.md) — [upstream](https://github.com/NVIDIA/DeepLearningExamples)
- [NVIDIA Cosmos](../organizations/nvidia/repositories/cosmos.md) — [upstream](https://github.com/NVIDIA/cosmos)
- [TensorRT Open Source Software](../organizations/nvidia/repositories/tensorrt.md) — [upstream](https://github.com/NVIDIA/TensorRT)

### Amazon / AWS
- [Amazon SageMaker Examples](../organizations/amazon/repositories/amazon-sagemaker-examples.md) — [upstream](https://github.com/aws/amazon-sagemaker-examples)
- [AWS SAM Transform](../organizations/amazon/repositories/serverless-application-model.md) — [upstream](https://github.com/aws/serverless-application-model)
- [Karpenter AWS Provider](../organizations/amazon/repositories/karpenter-provider-aws.md) — [upstream](https://github.com/aws/karpenter-provider-aws)

## Lifecycle and adoption findings retained

- **Google LevelDB:** upstream README says maintenance is very limited; only critical fixes or changes required by internally supported clients are expected.
- **NVIDIA nvidia-docker:** upstream README says the repository is archived and deprecated, and directs users to NVIDIA Container Toolkit.
- **Apple SwiftNIO:** README says SwiftNIO 1 is end-of-life and recommends SwiftNIO 2.
- **Microsoft Generative AI for Beginners:** README says GitHub Models was retired at the end of July 2026 and directs learners to Microsoft Foundry Models.
- **Microsoft Visual Studio Code:** Code - OSS is MIT-licensed; the branded Visual Studio Code distribution adds Microsoft-specific customizations under a separate product licence.

## Discovery snapshots

Dated first-page search snapshots are saved for each starting account:

- [Microsoft](../organizations/microsoft/discovery/search-page-1-2026-11-23.json)
- [Google](../organizations/alphabet-google/discovery/search-page-1-2026-11-23.json)
- [Apple](../organizations/apple/discovery/search-page-1-2026-11-23.json)
- [NVIDIA](../organizations/nvidia/discovery/search-page-1-2026-11-23.json)
- [AWS](../organizations/amazon/discovery/search-page-1-2026-11-23.json)

Each snapshot contains up to 100 ranked search results. The combined 500 results are discovery candidates, **not 500 audited repositories**, and they do not prove any organization's inventory is complete. GitHub search is not a substitute for paginating the public organization/user repository endpoint.

## Evidence boundaries

The project summaries are based on directly inspected upstream README content. Each project page records the README blob SHA used. A full build/dependency-manifest and source-code review was not performed for every project; technology details are limited to README-supported claims. These dossiers are not security, dependency-vulnerability, performance or architecture audits.

## Remaining work toward complete coverage

1. Discover every official GitHub organization/user account associated with the companies, including product, research, cloud, subsidiary and acquired-business accounts.
2. Complete paginated public repository inventories for every verified account, retaining archived repositories and forks.
3. Capture README, language statistics and relevant dependency/build manifests for every inventoried repository.
4. Interpret the captured evidence and document repositories with readable READMEs; explicitly record README-unavailable repositories.
5. Mark an account complete only after the final public-repository page is reached. Mark a company complete only after official account discovery and all account inventories are complete.


## Continued README review — additional six projects

A follow-on pass added six more README-reviewed dossiers:

- [Microsoft Machine Learning for Beginners](../organizations/microsoft/repositories/ml-for-beginners.md)
- [Microsoft AutoGen — archived](../organizations/microsoft/repositories/autogen.md)
- [Google FlatBuffers](../organizations/alphabet-google/repositories/flatbuffers.md)
- [Apple Turi Create](../organizations/apple/repositories/turicreate.md)
- [AWS SDK for Go v1 — end of support](../organizations/amazon/repositories/aws-sdk-go.md)
- [NVIDIA Container Toolkit](../organizations/nvidia/repositories/nvidia-container-toolkit.md)

The five starting account folders now contain **46 detailed README-based project briefs** in total: Microsoft 18, Google 8, Apple 7, NVIDIA 8 and AWS 5.

### Additional lifecycle findings

- **Microsoft AutoGen:** upstream README marks the repository archived and no longer maintained, with no further bug fixes, security fixes, features or support. It directs new users to Microsoft Agent Framework.
- **AWS SDK for Go v1:** upstream README says it reached end-of-support on 31 July 2025 and recommends AWS SDK for Go v2.
- **Apple Turi Create:** README lists Python 2.7 and Python 3.5–3.8 as its supported versions; verify current package support before adopting it.
- **NVIDIA Container Toolkit:** README documents the maintained toolkit as the supported path for GPU-accelerated containers and the replacement for nvidia-docker.

These additions increase README documentation coverage, but do not change the inventory status: the 500 first-page search results are still discovery candidates, not complete repository inventories.


## NVIDIA project-linked account README review — 24 November 2026

Five additional upstream README reviews were completed for project accounts linked from NVIDIA's official open-source hub:

- [Isaac ROS Visual SLAM](../organizations/nvidia/repositories/isaac-ros-visual-slam.md) — GPU-accelerated ROS 2 visual localization and mapping.
- [Cosmos-Predict2.5](../organizations/nvidia/repositories/cosmos-predict2-5.md) — world-state video prediction; README says limited maintenance and directs users to Cosmos 3.
- [cuGraph](../organizations/nvidia/repositories/cugraph.md) — GPU-accelerated graph analytics within RAPIDS.
- [Dynamo](../organizations/nvidia/repositories/dynamo.md) — datacenter-scale distributed inference orchestration.
- [Triton Inference Server](../organizations/nvidia/repositories/triton-inference-server.md) — multi-framework inference serving.

The NVIDIA company folder now has 13 README-based project briefs, including the original and additional selected repositories. These are manually interpreted project summaries; they do not represent every repository in the 6 mapped NVIDIA-related accounts.


## Five additional NVIDIA README reviews — 24 November 2026

The NVIDIA project-linked account review added five individual technical briefs:

- [Isaac ROS Visual SLAM](../organizations/nvidia/repositories/isaac-ros-visual-slam.md)
- [Cosmos-Predict2.5](../organizations/nvidia/repositories/cosmos-predict2-5.md)
- [cuGraph](../organizations/nvidia/repositories/cugraph.md)
- [Dynamo](../organizations/nvidia/repositories/dynamo.md)
- [Triton Inference Server](../organizations/nvidia/repositories/triton-inference-server.md)

The manually interpreted project-dossier count across the five company folders is now **51**: Microsoft 18, Google 8, Apple 7, NVIDIA 13 and Amazon/AWS 5.


## Apple Open Source project reviews — 24 November 2026

Five further Apple project README briefs were added:

- [Password Manager Resources](../organizations/apple/repositories/password-manager-resources.md) — shared compatibility datasets and parser code for password managers.
- [ServiceTalk](../organizations/apple/repositories/servicetalk.md) — JVM networking framework based on Netty.
- [Containerization](../organizations/apple/repositories/containerization.md) — Swift APIs for Linux containers inside lightweight VMs.
- [Swift Programming Language](../organizations/apple/repositories/swift-language.md) — primary source repository for the Swift language.
- [MLX](../organizations/apple/repositories/mlx.md) — Apple-silicon machine-learning array framework.

Apple's official Open Source catalogue links Swift and MLX under the separate swiftlang and ml-explore accounts, respectively. The five company folders now contain **56 manually interpreted README-based project briefs**: Microsoft 18, Google 8, Apple 12, NVIDIA 13 and Amazon/AWS 5.


## Baidu and Tencent README review batch — 24 November 2026

Five additional project dossiers were added after inspecting the upstream READMEs:

### Baidu-affiliated accounts
- [PaddleOCR](../organizations/baidu/repositories/paddleocr.md) — multilingual OCR and document parsing.
- [Apollo](../organizations/baidu/repositories/apollo.md) — autonomous-driving platform software and developer tooling.
- [XuperChain](../organizations/baidu/repositories/xuperchain.md) — modular blockchain infrastructure and smart-contract execution.

### Tencent
- [WeKnora](../organizations/tencent/repositories/weknora.md) — RAG, agent and enterprise knowledge platform.
- [ncnn](../organizations/tencent/repositories/ncnn.md) — cross-platform mobile/edge neural-network inference.

The curated company folders now contain **61 manually interpreted README-based project briefs**: Microsoft 18, Google 8, Apple 12, NVIDIA 13, Amazon/AWS 5, Baidu 3 and Tencent 2.
