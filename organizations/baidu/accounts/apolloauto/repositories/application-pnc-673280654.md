# ApolloAuto/application-pnc

- Company: Baidu
- GitHub account: [https://github.com/ApolloAuto](https://github.com/ApolloAuto)
- Mapping status: official-project-linked
- Repository: [ApolloAuto/application-pnc](https://github.com/ApolloAuto/application-pnc)
- Default branch: main
- README: [Open upstream README](https://github.com/ApolloAuto/application-pnc/blob/main/README.md)
- README blob SHA: e81de2f7beb72c6e724c236eef72d57949b4cd85
- Repository ID: 673280654
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

base project for Apollo PnC developers

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:43:51+00:00

### Short excerpt (up to 100 words)

> Apollob包管理开发调试样例工程，使用方法参考包管理安装方式 . ├── core # 依赖包配置，包括apollo核心包，以及一些工具包 ├── profiles # 整车应用配置，以单lidar、双camera车型为例 ├── .env* # 环境配置文件，包括容器名、镜像源等 ├── .workspace.json* # 软件包源配置文件，包括依赖的软件版本号 ├── .buildtool* # 编译配置文件 ├── setup.sh # 用于切换x86_64和aarch64架构配置 ├── kill_all.sh # 停止所有apollo相关进程 └── WORKSPACE # bazel 的配置 如果您没有安装过Apollo环境管理工具，请参考 安装 Apollo 环境管理工具 进行安装。 如果您之前安装过AEM版本，10.0版本需要升级aem到最新版本，请现在宿主机环境执行: sudo apt upate sudo apt install apollo-neo-env-manager-dev --reinstall 如果第一次安装，请在`git clone`后执行以下命令： bash setup.sh aem start aem enter buildtool build buildtool map get sunnyvale aem profile use sample aem bootstrap restart --plus 如果是从旧版升级（9.0.0-rc-r1或更老的版本），请在退出容器后`git pull`更新代码，然后执行以下命令： bash setup.sh aem enter buildtool upgrade buildtool build buildtool map get sunnyvale aem profile use sample aem bootstrap restart --plus

### README headings

- Apollo Core Workspace
- 文件目录组织
- 安装步骤
- 更新AEM版本
- 初次安装
- 首先切换环境配置
- 启动容器
- 进入容器
- 安装软件包
- 下载地图（此处下载sunnyvale，如果需要其他地图，可以用buildtool map list查看可供下载的地图）
- 切换车辆配置 (您可以参考profiles目录下的sample编写自己的profile配置)
- 启动Dreamview+
- 从旧版本升级
- 首先切换环境配置
- 进入容器
- 升级工具
- 升级已经安装的软件包
- 下载地图（此处下载sunnyvale，如果需要其他地图，可以用buildtool map list查看可供下载的地图）
- 切换车辆配置 (您可以参考profiles目录下的sample编写自己的profile配置)
- 启动Dreamview+

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Starlark | 2,716 |
| Shell | 719 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: Unknown
- Stars at capture: 25
- Forks at capture: 15
- Last updated: 2026-07-23T07:18:04Z
- Last pushed: 2026-04-07T09:01:53Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/ApolloAuto/application-pnc)
- [README](https://github.com/ApolloAuto/application-pnc/blob/main/README.md)
- [Issues](https://github.com/ApolloAuto/application-pnc/issues)
- [Releases](https://github.com/ApolloAuto/application-pnc/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
