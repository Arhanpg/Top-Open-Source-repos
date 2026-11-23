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
