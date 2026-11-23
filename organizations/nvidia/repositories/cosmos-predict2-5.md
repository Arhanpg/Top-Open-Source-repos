# NVIDIA Cosmos-Predict2.5

- **Company:** NVIDIA
- **GitHub account:** [nvidia-cosmos](https://github.com/nvidia-cosmos)
- **Repository:** [nvidia-cosmos/cosmos-predict2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5)
- **Default branch:** `main`
- **README:** [Open upstream README](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `1686690d7aef76d6c42d164d02002c739b35582b`

## Project overview

A family of world foundation models for predicting future physical-world states in video from multimodal inputs. The README describes Cosmos-Predict2.5 as a flow-based model that unifies Text2World, Image2World and Video2World in one model and uses Cosmos-Reason1 as its text encoder.

## Features and capabilities documented by the README

- Provides pre-trained, post-trained and distilled base checkpoints in 2B and 14B model sizes.
- Supports text plus image or video inputs for the base prediction models.
- Includes a multi-view autonomous-driving variant with seven-camera-view support.
- Provides robot/action-conditioned and robot multiview variants, including policy-oriented checkpoints.
- Links inference, post-training, distillation, Diffusers integration and task-specific guides.
- Links model artifacts through NVIDIA's Hugging Face collections and provides a cookbook path for recipes.

## Technology stack

World foundation models; flow-based video prediction; Cosmos-Reason1 vision-language model used as text encoder; 2B and 14B model checkpoints; Hugging Face model artifacts; documented Diffusers integration. The README describes the model family and model variants but the exact Python/PyTorch/CUDA environment must be taken from the linked version-specific setup guide.

## Getting started

The README links setup, troubleshooting, inference, post-training and distillation guides. It directs users to the Cosmos 3 repository for current releases, technical reports, tutorials and ecosystem updates.

## Lifecycle, compatibility and operational considerations

**Lifecycle warning:** the README says Cosmos-Predict2.5 is no longer under active development and will receive only limited maintenance. Future model releases, features, documentation and community support are focused on Cosmos 3, and the README encourages migration. Source code is Apache 2.0; model weights use the NVIDIA Open Model License. Do not conflate source-code licensing with model-weight licensing.

## Evaluation guidance

Review the release-specific installation documentation, exact software/hardware requirements, dependency manifests, licence terms and security guidance before using the project in production. Benchmark claims should be tested on the actual target hardware and workload. This dossier is based on the upstream README; it is not a full source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/nvidia-cosmos/cosmos-predict2.5)
- [README](https://github.com/nvidia-cosmos/cosmos-predict2.5/blob/main/README.md)
- [Issues](https://github.com/nvidia-cosmos/cosmos-predict2.5/issues)
- [Releases](https://github.com/nvidia-cosmos/cosmos-predict2.5/releases)

*Evidence note: the README blob SHA identifies the upstream version inspected. Details not supported by the README are left unspecified or directed to version-specific documentation.*
