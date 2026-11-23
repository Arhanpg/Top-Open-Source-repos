# Tencent/AILightGame

- Company: Tencent
- GitHub account: [https://github.com/Tencent](https://github.com/Tencent)
- Mapping status: verified
- Repository: [Tencent/AILightGame](https://github.com/Tencent/AILightGame)
- Default branch: main
- README: [Open upstream README](https://github.com/Tencent/AILightGame/blob/main/README.md)
- README blob SHA: e7d27119b1eb858d1bcafcb72f23af8070666404
- Repository ID: 1288038160
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

No GitHub description supplied.

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-23T20:41:45+00:00

### Short excerpt (up to 100 words)

> AILightGame 的目标是：让 AI（或开发者）能够根据自然语言需求，快速匹配到最合适的游戏模板，并通过**数据配置 + 逻辑脚本**的方式，低成本地定制出一款可运行的轻量游戏。 - **数据驱动**：角色、技能、子弹、Buff、关卡、交互物、UI 等全部通过 `*Configs.lua` 配置声明，逻辑与数据分离。 - **配置热覆盖**：通过 `unified_data_control_config.json` + `DataManager` 在不改动模板配置源码的前提下覆盖数值。 - **完整子系统**：内置角色、AI、主动/被动技能、子弹、物理、Buff、装备、关卡、交互物、UI、网络、排行榜、云存储等系统。 - **Hyper 能力封装**：`LightGameLib` 将 Hyper 引擎能力（相机、粒子、音频、动画、样条线、浮动文字等）封装为易用的 Lua 库。 - **AI 友好**：`index.json` 提供带关键词与权重的模板匹配索引；每个模板附带 `template.json`（匹配提示）、`GameDesignDoc.md`（设计文档）与 `code_summary.md`（代码摘要），便于 AI 理解与二次开发。 - **6 套完整模板**：涵盖动作、生存、自走棋、回合制、射击、塔防等主流玩法原型。 AILightGame/ ├── FrameScript/ # 游戏核心框架（引擎侧 Lua 运行时） │ ├── Main.lua # Lua 环境启动入口，加载全局模块 │ ├── Launcher.lua # 逻辑启动器，初始化所有子系统 & 分发输入/Tick │ ├── Global/ # 全局基础设施 │ │ ├── EventSys.lua # 事件系统 │ │ ├── LogicScriptMgr.lua # 逻辑脚本管理器（驱动 LogicTick） │ │ ├── InputMgr.lua # 输入管理（键鼠分发） │ │ ├── GlobalEnums.lua # 全局枚举 │ │ ├── Utils.lua / json.lua # 工具与 JSON 解析 │ │ └──

### README headings

- AILightGame
- 特性
- 目录结构
- 核心框架（FrameScript）
- 启动流程
- 全局单例（部分）
- 数据驱动与配置覆盖
- 游戏模板（GameTemplates）
- 模板选型（index.json）
- 单个模板的结构
- 技术栈
- 快速上手
- 许可证

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Lua | 14,364,093 |
| Python | 34,606 |
| Shell | 2,289 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- AtomicCapabilityTemplates/ci/requirements.txt (capture: captured) — dependency clues: cos-python-sdk-v5
- SceneTemplates/ci/requirements.txt (capture: captured) — dependency clues: cos-python-sdk-v5
- SubsystemTemplates/ci/requirements.txt (capture: captured) — dependency clues: cos-python-sdk-v5

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: NOASSERTION
- Stars at capture: 10
- Forks at capture: 3
- Last updated: 2026-11-04T16:44:20Z
- Last pushed: 2026-09-30T01:30:29Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/Tencent/AILightGame)
- [README](https://github.com/Tencent/AILightGame/blob/main/README.md)
- [Issues](https://github.com/Tencent/AILightGame/issues)
- [Releases](https://github.com/Tencent/AILightGame/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
