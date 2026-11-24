# PaddlePaddle/ElasticCTR

- Company: Baidu
- GitHub account: [https://github.com/PaddlePaddle](https://github.com/PaddlePaddle)
- Mapping status: official-project-linked
- Repository: [PaddlePaddle/ElasticCTR](https://github.com/PaddlePaddle/ElasticCTR)
- Default branch: master
- README: [Open upstream README](https://github.com/PaddlePaddle/ElasticCTR/blob/master/README.md)
- README blob SHA: 3aa69b02901dff447dcb27447623b7615ba9bcde
- Repository ID: 225549581
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

ElasticCTR，即飞桨弹性计算推荐系统，是基于Kubernetes的企业级推荐系统开源解决方案。该方案融合了百度业务场景下持续打磨的高精度CTR模型、飞桨开源框架的大规模分布式训练能力、工业级稀疏参数弹性调度服务，帮助用户在Kubernetes环境中一键完成推荐系统部署，具备高性能、工业级部署、端到端体验的特点，并且作为开源套件，满足二次深度开发的需求。

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:32+00:00

### Short excerpt (up to 100 words)

> ElasticCTR是分布式训练CTR预估任务和Serving流程一键部署的方案，用户只需配置数据源、样本格式即可完成一系列的训练与预测任务 * 1. 总体概览 * 2. 配置集群 * 3. 一键部署教程 * 4. 训练进度追踪 * 5. 预测服务 本项目提供了端到端的CTR训练和二次开发的解决方案，主要特点如下： 1.快速部署 ElasticCTR当前提供的方案是基于百度云的Kubernetes集群进行部署，用户可以很容易扩展到其他原生的Kubernetes环境运行ElasticCTR。 2.高性能 ElasticCTR采用PaddlePaddle提供的全异步分布式训练方式，在保证模型训练效果的前提下，近乎线性的扩展能力可以大幅度节省训练资源。在线服务方面，ElasticCTR采用Paddle Serving中高吞吐、低延迟的稀疏参数预估引擎，高并发条件下是常见开源组件吞吐量的10倍以上。 3.可定制 用户可以通过统一的配置文件，修改训练中的训练方式和基本配置，包括在离线训练方式、训练过程可视化指标、HDFS上的存储配置等。除了通过修改统一配置文件进行训练任务配置外，ElasticCTR采用全开源软件栈，方便用户进行快速的二次开发和改造。底层的Kubernetes、Volcano可以轻松实现对上层任务的灵活调度策略；基于PaddlePaddle的灵活组网能力、飞桨的分布式训练引擎Fleet和远程预估服务Paddle Serving，用户可以对训练模型、并行训练的模式、远程预估服务进行快速迭代；MLFlow提供的训练任务可视化能力，用户可以快速增加系统监控需要的各种指标。 本方案整体结构请参照这篇文章 ElasticCTR架构 运行本方案前，需要用户已经搭建好k8s集群，并安装好volcano组件。k8s环境部署比较复杂，本文不涉及。百度智能云CCE容器引擎申请后即可使用，百度云上创建k8s的方法用户可以参考这篇文档百度云创建k8s教程及使用指南。此外，Elastic CTR还支持在其他云上部署，可以参考以下两篇文档华为云创建k8s集群，aws创建k8s集群. 准备好K8S集群之后，我们需要配置HDFS作为数据集的来源HDFS配置教程 您可以使用我们提供的脚本elastic-control.sh来完成部署，在运行脚本前，请确保您的机器装有python3并通过pip安装了mlflow，安装mlflow的命令如下： python3 -m pip install mlflow -i https://pypi.tuna.tsinghua.edu.cn/simple 脚本的使用方式如下： bash elastic-control.sh [COMMAND] [OPTIONS] 其中可选的命令(COMMAND)如下： - **-c|--config_client** 检索客户端二进制文件用于发送预测服务请求并接收预测结果 - **-r|--config_resource** 定义训练配置 - **-a|--apply** 应用配置并启动训练 - **-l|--log** 打印训练状态，请确保您已经启动了训练 在定义训练配置时，您需要添加附加选项(OPTIONS)来指定配置的资源，可选的配置如下： - **-u|--cpu** 每个训练节点的CPU核心数 - **-m|--mem** 每个节点的内存容量 - **-t|--trainer** trainer节点的数量 - **-p|--pserver** parameter-server节点的数量 - **-b|--cube** cube分片数 - **-hd|--hdfs_address** 存储数据文件的HDFS地址 注意：您的数据文件的格式应为以下示例格式： $show $click $feasign0:$slot0 $feasign1:$slot1 $feasign2:$slot2...... 举例如下： 1 0 17241709254077376921:0 132683728328325035:1 9179429492816205016:2 12045056225382541705:3 - **-f|--datafile** 数据路径文件，需要指明HDFS地址并指定起始与截止日期（截止日期可选） - **-s|--slot_conf** 特征槽位配置文件，请注意文件后缀必须为'.txt' 以下是`data.config`文件，其中`START_DATE_HR`和`END_DATE_HR`就是我们在上一步配置HDFS的路径。 export HDFS_ADDRESS="hdfs://${IP}:9000" # HDFS地址 export

### README headings

- ElasticCTR
- <span id='head1'>1. 总体概览</span>
- <span id='head2'>2. 配置集群</span>
- <span id='head3'>3. 一键部署教程</span>
- <span id='head4'>4. 训练进度追踪</span>
- <span id='head5'>5. 预测服务</span>

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Python | 55,067 |
| Shell | 28,804 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 188
- Forks at capture: 45
- Last updated: 2026-10-06T08:55:39Z
- Last pushed: 2020-07-11T05:12:47Z
- Topics: ctr, hdfs, k8s, personalization, ranking, recommender-system

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/PaddlePaddle/ElasticCTR)
- [README](https://github.com/PaddlePaddle/ElasticCTR/blob/master/README.md)
- [Issues](https://github.com/PaddlePaddle/ElasticCTR/issues)
- [Releases](https://github.com/PaddlePaddle/ElasticCTR/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
