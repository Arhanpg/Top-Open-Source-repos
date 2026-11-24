# PaddlePaddle/PaddleYOLO

- Company: Baidu
- GitHub account: [https://github.com/PaddlePaddle](https://github.com/PaddlePaddle)
- Mapping status: official-project-linked
- Repository: [PaddlePaddle/PaddleYOLO](https://github.com/PaddlePaddle/PaddleYOLO)
- Default branch: develop
- README: [Open upstream README](https://github.com/PaddlePaddle/PaddleYOLO/blob/develop/README.md)
- README blob SHA: 13bc5abd16288879b57402ac1075520b3d8fb1fb
- README bytes captured: 26552
- README truncated at capture limit: False
- Repository ID: 513505410
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

🚀🚀🚀 YOLO series of PaddlePaddle implementation, PP-YOLOE+, RT-DETR, YOLOv5, YOLOv6, YOLOv7, YOLOv8, YOLOv10, YOLO11, YOLOX, YOLOv5u, YOLOv7u, YOLOv6Lite, RTMDet and so on. 🚀🚀🚀

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T19:51:53+00:00

### Short excerpt (up to 300 words)

> 简体中文 | English

### README headings

- 简介
- 教程
- weights=https://bj.bcebos.com/v1/paddledet/models/${job_name}.pdparams
- 1.训练（单卡/多卡），加 --eval 表示边训边评估，加 --amp 表示混合精度训练
- CUDA_VISIBLE_DEVICES=0 python tools/train.py -c ${config} --eval --amp
- 2.评估，加 --classwise 表示输出每一类mAP
- 3.预测 (单张图/图片文件夹）
- CUDA_VISIBLE_DEVICES=0 python tools/infer.py -c ${config} -o weights=${weights} --infer_dir=demo/ --draw_threshold=0.5
- weights=https://bj.bcebos.com/v1/paddledet/models/${job_name}.pdparams
- 4.导出模型，以下3种模式选一种
- 普通导出，加trt表示用于trt加速，对NMS和silu激活函数提速明显
- exclude_post_process去除后处理导出，返回和YOLOv5导出ONNX时相同格式的concat后的1个Tensor，是未缩放回原图的坐标+分类置信度
- CUDA_VISIBLE_DEVICES=0 python tools/export_model.py -c ${config} -o weights=${weights} exclude_post_process=True # trt=True
- exclude_nms去除NMS导出，返回2个Tensor，是缩放回原图后的坐标和分类置信度
- CUDA_VISIBLE_DEVICES=0 python tools/export_model.py -c ${config} -o weights=${weights} exclude_nms=True # trt=True
- 5.部署预测，注意不能使用 去除后处理 或 去除NMS 导出后的模型去预测
- 6.部署测速，加 “--run_mode=trt_fp16” 表示在TensorRT FP16模式下测速，注意如需用到 trt_fp16 则必须为加 trt=True 导出的模型
- 7.onnx导出，一般结合 exclude_post_process去除后处理导出的模型
- 8.onnx trt测速
- 更新日志
- <img src="https://user-images.githubusercontent.com/48054808/157793354-6e7f381a-0aa6-4bb7-845c-9acf2ecc05c3.png" width="20"/> 产品动态
- <img title="" src="https://user-images.githubusercontent.com/48054808/157795569-9fc77c85-732f-4870-9be0-99a7fe2cff27.png" alt="" width="20"> 简介
- <img src="https://user-images.githubusercontent.com/48054808/157799599-e6a66855-bac6-4e75-b9c0-96e13cb9612f.png" width="20"/> 特性
- <img title="" src="https://user-images.githubusercontent.com/48054808/157800467-2a9946ad-30d1-49a9-b9db-ba33413d9c90.png" alt="" width="20"> 技术交流
- <img src="https://user-images.githubusercontent.com/48054808/157827140-03ffaff7-7d14-48b4-9440-c38986ea378c.png" width="20"/> 套件结构概览
- <img src="https://user-images.githubusercontent.com/48054808/157801371-9a9a8c65-1690-4123-985a-e0559a7f9494.png" width="20"/> 模型性能概览
- <img src="https://user-images.githubusercontent.com/48054808/157829890-a535b8a6-631c-4c87-b861-64d4b32b2d6a.png" width="20"/> 模型库
- [PP-YOLOE+](./configs/ppyoloe)系列 推荐场景：Nvidia V100, T4等云端GPU和Jetson系列等边缘端设备
- 前沿检测算法
- <img src="https://user-images.githubusercontent.com/48054808/157828296-d5eb0ccb-23ea-40f5-9957-29853d7d13a9.png" width="20"/> 文档教程

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Project overview: Introduction

> 简体中文 | English

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 2,536,258 |
| C++ | 508,276 |
| Shell | 100,725 |
| Cuda | 47,270 |
| CMake | 18,466 |
| Makefile | 9,691 |
| Linker Script | 8,141 |
| C | 4,600 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- requirements.txt (capture: captured) — dependency clues: Cython, PyYAML, numpy, opencv-python, pycocotools, scipy, setuptools, shapely, terminaltables, tqdm, typeguard, visualdl
- setup.py (capture: captured)
- .travis/requirements.txt (capture: captured) — dependency clues: cython, llvmlite, numba, shapely, tqdm
- test_tipc/requirements.txt (capture: captured) — dependency clues: GPUtil, onnx, onnxruntime, paddle2onnx, paddleslim, psutil, pynvml
- deploy/cpp/CMakeLists.txt (capture: captured)
- deploy/lite/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: GPL-3.0
- Stars at capture: 666
- Forks at capture: 156
- Last updated: 2026-10-28T06:59:53Z
- Last pushed: 2026-01-14T13:39:39Z
- Topics: instance-segmentation, object-detection, paddleyolo, ppyolo, ppyoloe, ppyolov2, rt-detr, rtmdet, yolo, yolo11, yolov10, yolov3, yolov5, yolov5u, yolov6, yolov6lite, yolov7, yolov7u, yolov8, yolox

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/PaddlePaddle/PaddleYOLO)
- [README](https://github.com/PaddlePaddle/PaddleYOLO/blob/develop/README.md)
- [Issues](https://github.com/PaddlePaddle/PaddleYOLO/issues)
- [Releases](https://github.com/PaddlePaddle/PaddleYOLO/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
