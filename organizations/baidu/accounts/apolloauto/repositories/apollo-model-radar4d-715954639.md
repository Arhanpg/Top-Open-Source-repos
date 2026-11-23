# ApolloAuto/apollo-model-radar4d

- Company: Baidu
- GitHub account: [https://github.com/ApolloAuto](https://github.com/ApolloAuto)
- Mapping status: official-project-linked
- Repository: [ApolloAuto/apollo-model-radar4d](https://github.com/ApolloAuto/apollo-model-radar4d)
- Default branch: master
- README: [Open upstream README](https://github.com/ApolloAuto/apollo-model-radar4d/blob/master/README.md)
- README blob SHA: 5a5cc63ed25e61256dd6dd52f6501ab746b770ba
- Repository ID: 715954639
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:51:14+00:00

### Short excerpt (up to 100 words)

> Prepare your own dataset, and modify the dataset path in "tools/cfgs/dataset_configs/radar4d_dataset.yaml" Please refer to INSTALL.md for the installation of OpenPCDet. python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/radar4d_dataset.yaml python train.py --cfg_file cfgs/kitti_models/radar_object_detection.yaml --extra_tag radar_detection_all python test.py --cfg_file cfgs/kitti_models/radar_object_detection.yaml --batch_size 1 --eval_tag radar_detection_all --ckpt ../output/kitti_models/radar_object_detection/radar_detection_all/ckpt/checkpoint_epoch_80.pth --save_to_file python convert2libtorch.py --ckpt ../output/kitti_models/radar_object_detection/radar_detection_all/ckpt/checkpoint_epoch_80.pth --output_path ./radar_detection_all.zip @ARTICLE{apalffy2022, author={Palffy, Andras and Pool, Ewoud and Baratam, Srimannarayana and Kooij, Julian F. P. and Gavrila, Dariu M.}, journal={IEEE Robotics and Automation Letters}, title={Multi-Class Road User Detection With 3+1D Radar in the View-of-Delft Dataset}, year={2022}, volume={7}, number={2}, pages={4961-4968}, doi={10.1109/LRA.2022.3147324}} `OpenPCDet` is a clear, simple, self-contained open source project for LiDAR-based 3D object

### README headings

- Apollo
- Prepare the 4d radar dataset
- Install OpenPCDet
- How to prepare the dataset
- How to train
- How to test
- How to export the trained model
- References
- OpenPCDet
- Overview
- Changelog
- Introduction
- What does `OpenPCDet` toolbox do?
- `OpenPCDet` design pattern
- Currently Supported Features
- Model Zoo
- KITTI 3D Object Detection Baselines
- NuScenes 3D Object Detection Baselines
- Waymo Open Dataset Baselines
- Other datasets
- Installation
- Quick Demo
- Getting Started
- License
- Acknowledgement
- Citation
- Contribution

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 540,367 |
| Cuda | 77,081 |
| C++ | 46,016 |
| C | 3,847 |
| Shell | 1,954 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: easydict, numba, numpy, pyyaml, scikit-image, tensorboardX, torch, tqdm
- setup.py (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 22
- Forks at capture: 4
- Last updated: 2026-08-07T05:23:57Z
- Last pushed: 2023-11-10T07:11:26Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ApolloAuto/apollo-model-radar4d)
- [README](https://github.com/ApolloAuto/apollo-model-radar4d/blob/master/README.md)
- [Issues](https://github.com/ApolloAuto/apollo-model-radar4d/issues)
- [Releases](https://github.com/ApolloAuto/apollo-model-radar4d/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
