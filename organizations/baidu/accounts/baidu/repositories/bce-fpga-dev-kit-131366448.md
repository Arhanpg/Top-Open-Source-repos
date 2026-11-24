# baidu/bce-fpga-dev-kit

- Company: Baidu
- GitHub account: [https://github.com/baidu](https://github.com/baidu)
- Mapping status: verified
- Repository: [baidu/bce-fpga-dev-kit](https://github.com/baidu/bce-fpga-dev-kit)
- Default branch: master
- README: [Open upstream README](https://github.com/baidu/bce-fpga-dev-kit/blob/master/README.md)
- README blob SHA: 45cf58876369e6edeb0e59b1c33c61eb203b67d6
- Repository ID: 131366448
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:36:05+00:00

### Short excerpt (up to 100 words)

> 1. 概览 1. 已支持/待开发特性列表 1. ChangeLog 1. HDK简介 1. SDK简介 1. 联系交流 百度FPGA云服务器是配备了现场可编程门阵列(FPGA)的虚拟机实例。每个实例提供了一片20nm Xilinx UltraScale FPGA，其中包含多达150万个逻辑单元和5520个数字信号处理(DSP)引擎，并独享8GB板载四通道DDR4-2400 ECC内存以及与主机间的PCIe Gen3 x8链路。FPGA丰富的逻辑计算资源和高速IO接口，赋予了您的应用充足的性能提升空间，尤为适合解决诸如基因检测、财务分析这类涉及高性能计算(HPC)的复杂科学、工程问题。使用百度FPGA云服务器，您无需耗费精力设计、购买或运维硬件，可以节省这些额外步骤带来的成本。 您可以在百度FPGA云开发环境上快速灵活地对软硬件进行编程，通过协同设计来为您的应用创建自定义加速。您也可以选择云市场上百度或第三方厂商提供的成熟普适加速方案，如神经网络计算、多媒体处理、数据加解密等，参照简易步骤在FPGA云服务器上部署后轻松提升应用性能。 百度FPGA云开发环境旨在为开发者提供一个稳定可靠、便捷易用的FPGA软硬件编程环境。它分为HDK(Hardware Development Kit)和SDK(Software Development Kit)两部分，其中囊括了开发、模拟、调试和编译代码所需的各种资源。基于此，开发者能轻松构建FPGA自定义逻辑，并可将已有设计顺利移植到百度FPGA云服务器。 * 更完善的自定义逻辑仿真支持 * 多PCIe Function支持 * SDAccel开发环境支持 * FPGA云市场支持 * RP端AXI-Stream接口支持 * 更多型号FPGA如Xilinx VU9P和Altera S10支持 **百度云会不定期升级FPGA静态逻辑，并对应更新该工具包，其中可能包含新增特性支持或Bug修复。升级后旧版本的工具包将不再被支持。请关注本节更新公告，并及时从https://github.com/Cwndmiao/bce-fpga-dev-kit/releases下载最新版本的工具包。** **建议您在使用百度FPGA云开发环境前仔细阅读HDK和SDK目录下的使用文档。如果您在使用百度FPGA云开发环境的过程中遇到了任何问题，请首先参考Q&A，其中罗列了一部分已知问题的解决方法。** 如果您有任何百度FPGA云开发环境相关的Bug报告或发展建议，请通过以下任一方式联系百度云，我们会尽早回复。 * 在https://github.com/Cwndmiao/bce-fpga-dev-kit/issues提交Github Issues * 在https://gitter.im/bce-fpga-dev-kit/Lobby留言 * 发送邮件至<a href="mailto:miaotianxiang@baidu.com">miaotianxiang</a>或<a href="mailto:ruanyuan@baidu.com">ruanyuan</a>

### README headings

- 百度FPGA云开发环境软硬件工具包
- 目录
- 概览
- 已支持/待开发特性列表
- 已支持特性
- 待开发特性
- ChangeLog
- HDK简介
- SDK简介
- 联系交流

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| VHDL | 41,325,207 |
| SystemVerilog | 8,091,203 |
| Verilog | 1,143,061 |
| Tcl | 428,921 |
| C | 388,240 |
| C++ | 113,843 |
| Shell | 35,392 |
| Filebench WML | 13,680 |
| CMake | 4,338 |
| Makefile | 2,441 |
| Coq | 865 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- hdk/xvc_server/Makefile (capture: captured)
- sdk/llapi/CMakeLists.txt (capture: captured)
- sdk/mgmt_tool/CMakeLists.txt (capture: captured)
- sdk/linux_kernel_driver/driver/Makefile (capture: captured)
- sdk/linux_kernel_driver/sample/CMakeLists.txt (capture: captured)
- sdk/linux_kernel_driver/tests/Makefile (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 10
- Forks at capture: 8
- Last updated: 2025-08-30T14:38:36Z
- Last pushed: 2018-04-28T03:07:49Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/baidu/bce-fpga-dev-kit)
- [README](https://github.com/baidu/bce-fpga-dev-kit/blob/master/README.md)
- [Issues](https://github.com/baidu/bce-fpga-dev-kit/issues)
- [Releases](https://github.com/baidu/bce-fpga-dev-kit/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
