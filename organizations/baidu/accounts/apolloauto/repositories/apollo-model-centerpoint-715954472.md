# ApolloAuto/apollo-model-centerpoint

- Company: Baidu
- GitHub account: [https://github.com/ApolloAuto](https://github.com/ApolloAuto)
- Mapping status: official-project-linked
- Repository: [ApolloAuto/apollo-model-centerpoint](https://github.com/ApolloAuto/apollo-model-centerpoint)
- Default branch: master
- README: [Open upstream README](https://github.com/ApolloAuto/apollo-model-centerpoint/blob/master/README.md)
- README blob SHA: 7624954e301c10615586efae948ce1ece611b909
- Repository ID: 715954472
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:51:13+00:00

### Short excerpt (up to 100 words)

> 该项目提供了开源自动驾驶平台Apollo中Lidar 3D目标检测算法CenterPoint的训练和部署代码。 CenterPoint是Anchor-Free的三维物体检测器，以点云作为输入，将三维物体在Bird-View下的中心点作为关键点，基于关键点检测的方式回归物体的尺寸、方向和速度。相比于Anchor-Based的三维物体检测器，CenterPoint不需要人为设定Anchor尺寸，面向物体尺寸多样不一的场景时其精度表现更高，且简易的模型设计使其在性能上也表现更加高效。 Apollo对CenterPoint进行了一系列优化工作，检测效果和泛化能力都获得大幅提升，可以提供复杂城市道路场景下实时、准确、稳定的3D目标检测效果。 模型端： * **更好的检测效果，更强的泛化能力**。使用百万真实路测数据对CenterPoint进行训练和优化，精度和召回率相较于应用最多的CNNSeg模型提升了20%+，检测能力和泛化能力显著提升。 * **新增城市道路标识检测能力**。提供了锥桶、水马、防撞桶、指示牌等目标的检测能力，极大地保障了自动驾驶的安全性。 * **降低训练开发成本，提升易用性**。代码中新增功能：冻结网络层finetune训练、fp16训练、自定义数据集训练评测等功能，更加简单易上手。 部署端： * **显著提升近处行人目标和小目标的召回率**。对前后处理、配置、模型推理进行了针对性调优和处理，修复了推理端结果不一致问题，行人和小目标召回率提升。 * **输出polygon，增强跟踪稳定性**。优化了障碍物点云的获取逻辑，使centerpoint可输出准确polygon信息，进一步增强了跟踪的稳定性。 * **大幅降低模型推理耗时和GPU占用**。提供了tensorrt + fp16推理 & int8推理的功能和教程，在保持模型检测效果前提下，大幅降低了模型的推理耗时和GPU占用，在低算力平台运行可满足实时性要求。 检测结果可视化 模型文件下载地址 开发者可基于该代码进行二次开发，快速方便地完成： * **学习研究**：使用公开数据集KITTI和NuScenes对CenterPoint进行训练、评测、导出、部署。 * **增量训练**：使用自定义数据集对CenterPoint进行增量训练，提升在用户自定义场景中的检测效果。 * **Apollo感知赛事**：使用Apolloscape数据集对CenterPoint进行训练，顺利完成Apollo感知赛事。 环境配置和安装教程详尽installation 完整训练流程和配置详见 centerpoint，下面以KITTI数据集为例进行简单介绍。 先准备KITTI数据集，请在官网进行下载。将数据解压后按照下方的目录结构进行组织： kitti_dataset_root │ |—— test.txt │ |—— train.txt │ |—— trainval.txt │ |—— val.txt 在Paddle3D的目录下创建软链接 `datasets/KITTI`，指向到上面的数据集目录: mkdir datasets ln -s /path/to/kitti_dataset_root ./datasets mv ./datasets/kitti_dataset_root ./datasets/KITTI 生成训练时数据增强所需的真值库: python tools/create_det_gt_database.py --dataset_name kitti --dataset_root ./datasets/KITTI --save_dir ./datasets/KITTI kitti_train_gt_database 使用8张GPU训练KITTI数据集： python -m paddle.distributed.launch --gpus 0,1,2,3,4,5,6,7 tools/train.py --config configs/centerpoint/centerpoint_pillars_016voxel_kitti.yml --save_dir ./output_kitti --num_workers 4 --save_interval 5 模型评测 python tools/evaluate.py --config configs/centerpoint/centerpoint_pillars_016voxel_kitti.yml --model ./output_kitti/epoch_160/model.pdparams --batch_size 1 --num_workers 4 导出推理模型，将训练时保存的动态图模型文件导出成推理引擎能够加载的静态图模型文件。 python tools/export.py --config configs/centerpoint/centerpoint_pillars_02voxel_nuscenes_10sweep.yml

### README headings

- Apollo CenterPoint
- 介绍
- 开发
- 其他资料
- Paddle3D
- 🌈简介
- ✨主要特性
- 🧩灵活的框架设计
- 📱丰富的模型库
- 🎗️端到端全流程
- 🏆无缝衔接Apollo
- 📣最新进展
- 👫开源社区
- 📱模型库
- 🔥使用教程
- 💡产业实践范例
- 📝许可证

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 1,813,766 |
| C++ | 369,153 |
| Cuda | 358,808 |
| CMake | 71,344 |
| Shell | 32,309 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: colorlog, easydict, filelock, h5py, numba, numpy, nuscenes-devkit, opencv-python, paddledet, paddleseg, pandas, pillow, pyquaternion, pyyaml, rarfile, scikit-image, scikit-learn, visualdl
- setup.py (capture: captured)
- paddle3d/ops/setup.py (capture: captured)
- deploy/caddn/cpp/CMakeLists.txt (capture: captured)
- deploy/centerpoint/cpp/CMakeLists.txt (capture: captured)
- deploy/iassd/cpp/CMakeLists.txt (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 47
- Forks at capture: 7
- Last updated: 2026-07-27T01:51:35Z
- Last pushed: 2023-11-14T02:37:16Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ApolloAuto/apollo-model-centerpoint)
- [README](https://github.com/ApolloAuto/apollo-model-centerpoint/blob/master/README.md)
- [Issues](https://github.com/ApolloAuto/apollo-model-centerpoint/issues)
- [Releases](https://github.com/ApolloAuto/apollo-model-centerpoint/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
