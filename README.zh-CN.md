<p align="center">
  <img src="skills/token-optimizer/assets/logo.svg" alt="Token Optimizer" width="780">
</p>

<p align="center">
  <a href="README.md">English</a> | <strong>中文</strong>
</p>

<p align="center">
  <a href="https://github.com/alexgreensh/token-optimizer/releases/latest"><img src="https://img.shields.io/github/v/release/alexgreensh/token-optimizer?label=version&color=green" alt="最新稳定版本"></a>
  <a href="https://github.com/alexgreensh/token-optimizer/releases"><img src="https://img.shields.io/github/release-date/alexgreensh/token-optimizer?label=last%20release&color=blue" alt="最近发布"></a>
  <a href="https://github.com/alexgreensh/token-optimizer"><img src="https://img.shields.io/badge/Claude_Code-Plugin-blueviolet" alt="Claude Code 插件"></a>
  <a href="https://github.com/alexgreensh/token-optimizer"><img src="https://img.shields.io/badge/CodeBuddy_Code-Plugin-blue" alt="CodeBuddy Code 插件"></a>
  <a href="https://github.com/alexgreensh/token-optimizer/tree/main/openclaw"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Falexgreensh%2Ftoken-optimizer%2Fmain%2Fopenclaw%2Fpackage.json&query=%24.version&prefix=v&label=OpenClaw&color=brightgreen" alt="OpenClaw 版本"></a>
  <a href="https://github.com/alexgreensh/token-optimizer/tree/main/opencode"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Falexgreensh%2Ftoken-optimizer%2Fmain%2Fopencode%2Fpackage.json&query=%24.version&prefix=v&label=OpenCode&color=58a6ff" alt="OpenCode 版本"></a>
  <a href="https://github.com/alexgreensh/token-optimizer/blob/main/docs/codex.md"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Falexgreensh%2Ftoken-optimizer%2Fmain%2F.codex-plugin%2Fplugin.json&query=%24.version&prefix=v&label=Codex&color=orange" alt="Codex 版本"></a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/cuts%20context%20waste-3fb950" alt="减少上下文浪费">
  <img src="https://img.shields.io/badge/survives%20compaction-checkpoint%20%2B%20restore-58a6ff" alt="压缩后存活">
  <img src="https://img.shields.io/badge/saves%20real%20%24-every%20session-2ea043" alt="每次会话省真钱">
  <img src="https://img.shields.io/badge/live%20dashboard-tokens%20%2B%20%24%20%2B%20turns-8B5CF6?logo=chartdotjs&logoColor=white" alt="实时仪表盘">
  <img src="https://img.shields.io/badge/context%20quality-live%20score-blue" alt="实时上下文质量评分">
  <img src="https://img.shields.io/badge/tests-passing-brightgreen" alt="测试通过">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen" alt="零依赖">
  <img src="https://img.shields.io/badge/telemetry-none-brightgreen" alt="零遥测">
  <img src="https://img.shields.io/badge/python-3.9+-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey" alt="平台">
  <a href="https://github.com/alexgreensh/token-optimizer/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-PolyForm%20Noncommercial-blue.svg" alt="许可证: PolyForm Noncommercial"></a>
  <a href="https://github.com/alexgreensh/token-optimizer/stargazers"><img src="https://img.shields.io/github/stars/alexgreensh/token-optimizer" alt="GitHub Stars"></a>
  <a href="https://github.com/alexgreensh/token-optimizer/commits/main"><img src="https://img.shields.io/github/commit-activity/m/alexgreensh/token-optimizer" alt="提交活跃度"></a>
  <a href="https://linkedin.com/in/alexgreensh"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white" alt="在 LinkedIn 联系"></a>
</p>
<p align="center">
  <a href="https://github.com/sponsors/alexgreensh"><img src="https://img.shields.io/badge/%E2%99%A5%20Support%20this%20project%20to%20keep%20it%20open%20source-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="支持本项目保持开源"></a>
</p>

<h2 align="center">省下你浪费的 token。留住你即将丢失的工作。</h2>

<p align="center"><em>它在后台自动运行。你照常工作。想看全局时运行审计即可。</em></p>

<p align="center">
  <a href="https://alexgreensh.github.io/token-optimizer/"><img src="https://img.shields.io/badge/%F0%9F%93%96%20Read%20the%20Docs-alexgreensh.github.io%2Ftoken--optimizer-e85329?style=for-the-badge&logoColor=white" alt="阅读文档"></a>
  <a href="https://alexgreensh.github.io/token-optimizer/start/quickstart/"><img src="https://img.shields.io/badge/Quickstart-2%20minutes-3fb950?style=for-the-badge" alt="2 分钟快速开始"></a>
</p>

## 30 秒简介

Token Optimizer 削减 AI 编程助手浪费的 token，让你的工作扛过会话和压缩，并在实时仪表盘上显示每笔花费的去向。**大部分功能自动运行。安装、跑一次审计，其余交给 hooks。**

**为什么不能只用 Headroom 或 RTK？** 它们压缩命令输出，覆盖 15-25% 的上下文。Token Optimizer 覆盖这部分再加上另外 75%：臃肿的配置、未使用的 skills、过期的 memory、压缩丢失、模型误路由、行为浪费。每笔节省都缓存安全且可计量。仪表盘在每次会话后自动更新。

支持 **Claude Code**（CLI 和 VS Code）、**CodeBuddy Code**、**OpenCode**、**OpenClaw**、**Codex**、**Hermes** 和 **GitHub Copilot**（beta）。Windsurf 和 Cursor 在路线图上。

<p align="center">
  <img src="skills/token-optimizer/assets/hero-terminal.svg" alt="Token Optimizer 快速扫描" width="800">
</p>

## 安装

**Claude Code（推荐）：**

```
/plugin marketplace add alexgreensh/token-optimizer
/plugin install token-optimizer@alexgreensh-token-optimizer
```

然后在 Claude Code 中：`/token-optimizer`

> **安装后请启用自动更新。** Claude Code 默认关闭第三方 marketplace 的自动更新。`/plugin` → **Marketplaces** 标签 → 选择 `alexgreensh-token-optimizer` → **Enable auto-update**。一次性操作，10 秒搞定。
>
> 安装后运行 `/token-optimizer` 一次即可设置 hooks。之后一切自动运行：压缩、检查点、质量评分、仪表盘更新。除非想主动审计，否则不需���再运行任何命令。

**CodeBuddy Code：**

```
/plugin marketplace add alexgreensh/token-optimizer
/plugin install token-optimizer@alexgreensh-token-optimizer
```

然后在 CodeBuddy Code 中：`/token-optimizer`

> 安装后运行 `/token-optimizer` 一次即可设置 hooks。CodeBuddy Code 的配置布局与 Claude Code 一致（`~/.codebuddy` 替代 `~/.claude`，`CODEBUDDY.md` 替代 `CLAUDE.md`），审计引擎直接适用。

<details>
<summary><b>其他平台与安装方式</b></summary>

**Codex：**
```bash
codex plugin marketplace add alexgreensh/token-optimizer
```
然后在 Codex TUI 中：`/plugins` 并安装 Token Optimizer。参见 [`docs/codex.md`](docs/codex.md)。

**OpenCode：** 将 `token-optimizer-opencode` 添加到你的 `opencode.json` 的 `plugin` 数组：
```jsonc
{ "$schema": "https://opencode.ai/config.json", "plugin": ["token-optimizer-opencode"] }
```
参见 [`opencode/README.md`](opencode/README.md)。

**OpenClaw：**
```bash
openclaw plugins install github:alexgreensh/token-optimizer
```
参见 [`openclaw/README.md`](openclaw/README.md)。

**Hermes：**
```bash
git clone https://github.com/alexgreensh/token-optimizer.git
token-optimizer/install.sh --hermes
```
参见 [`hermes/README.md`](hermes/README.md)。

**GitHub Copilot（beta）：**
```bash
git clone --depth 1 https://github.com/alexgreensh/token-optimizer.git
cd token-optimizer
bash install.sh --copilot
```
参见 [`docs/copilot.md`](docs/copilot.md)。

**macOS/Linux 脚本安装（替代 plugin）：**
```bash
tmp="$(mktemp -d)"
release_json="$(curl -fsSL https://api.github.com/repos/alexgreensh/token-optimizer/releases/latest)"
tag="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["tag_name"])' <<<"$release_json")"
git clone --branch "$tag" --depth 1 https://github.com/alexgreensh/token-optimizer.git ~/.claude/token-optimizer
bash ~/.claude/token-optimizer/install.sh
rm -rf "$tmp"
```

**Windows 用户：** 仅使用 plugin 安装。不要在 Windows 上运行 `install.sh`。如果遇到 `EBUSY` 错误，关闭所有 Claude Code 和 Git Bash 窗口，杀掉残留的 `git.exe` 进程，删除 `C:\Users\<you>\.claude\token-optimizer` 和 `C:\Users\<you>\.claude\plugins\marketplaces\alexgreensh-token-optimizer`，然后重试。

**如果 `install.sh` 报错 `$'\r': command not found`**（在强制 LF 行结束之前克隆的副本把脚本转成了 CRLF），去除回车符后重试 — 仓库现在有 `.gitattributes` 在新克隆上防止此问题：
```bash
sed -i 's/\r$//' ~/.claude/token-optimizer/install.sh
# 已经有仓库了？原地重新规范化行结束：
git -C ~/.claude/token-optimizer add --renormalize . && git -C ~/.claude/token-optimizer checkout -- .
```

</details>

<details>
<summary>卸载</summary>

Token Optimizer 是可加可逆的。每个运行时有干净的卸载流程，只移除我们安装的内容，保留你自己的 hooks、配置和会话数据。每个运行时的完整步骤见 **[docs/uninstall.md](docs/uninstall.md)**。

最快路径（Claude Code plugin 安装）：

```
/plugin uninstall token-optimizer@alexgreensh-token-optimizer
```

</details>

## 你能得到什么

**每次会话自动运行，你什么都不用做：**

- 🔄 **智能压缩**：auto-compact 前检查点，之后恢复
- 🗄️ **会话连续性**：跨会话提示、冷恢复、检查点评分
- 📦 **主动压缩**：9 项功能，全部默认开启（delta diff、骨架、bash/搜索压缩、精简输出提示、质量提示、循环检测、活动模式、决策提取）
- 📊 **质量评分**：7 个信号，实时，S–F 字母等级
- 🗃️ **会话数据库**：SQLite，15 张表，完整审计轨迹，零网络
- 🔍 **渐进式披露**：大输出归档，按需展开
- 🧠 **上下文情报摘要**：压缩后重新定位，无需重读
- 🔀 **模型路由提示**：引导到合适的模型层级

**当你主动调用时：**

- 🩺 `/token-optimizer`：完整审计带引导式修复
- 📈 `/token-coach`：30 天趋势分析带具体修复
- ⚡ `quick`：10 秒健康检查
- 🔧 `doctor`：安装检查
- 💰 `savings`：美元节省报告
- 📋 `report`：按组件的 token 明细
- 🌐 `dashboard`：打开完整仪表盘
- 📝 `memory-review`：MEMORY.md 结构审计
- 📂 `expand`：检索归档的工具结果
- 🔙 `resume-lean`：重开冷会话

安装后运行 `/token-optimizer` 一次，其余全部自动。

## 有什么不同

大多数 token 工具压缩命令输出。那覆盖 15-25% 的上下文。另外 75% 没人管。

**压缩覆盖面。** Headroom 和 RTK 压缩 bash 和命令输出。Token Optimizer 压缩输出栈的八个面。状态：🟢 支持，🟡 部分，🔴 不支持。

| 压缩面 | Token Optimizer | Headroom | RTK |
|---|---|---|---|
| **Bash / 命令输出**（git、测试、lint、构建、日志） | 🟢 60+ 模式，凭证安全；pytest 运行 564 → 115 token | 🟢 6 种算法 | 🟢 100+ 过滤器 |
| **搜索 / grep 输出** | 🟢 命中加上计数；500 行 → 20 | 🔴 | 🔴 |
| **表格 / JSON 输出**（jq、yq、csvtool、mlr） | 🟢 保值的列式 | 🟢 SmartCrusher | 🔴 |
| **文件重读，delta 模式** | 🟢 仅 diff；2,000-token 重读 → ~50 | 🔴 | 🔴 |
| **文件重读，结构图** | 🟢 签名和 import 骨架；720KB → 250 token | 🔴 | 🔴 |
| **大型工具结果**（超 4K 字符） | 🟢 归档到磁盘，按需展开 | 🔴 | 🔴 |
| **模型输出冗余** | 🟢 典型 10-15%，实测最高 30-41%，缓存安全 | 🔴 | 🔴 |
| **结构性上下文**（配置、skills、MCP、memory） | 🟢 按组件审计，每个来源评分 | 🔴 | 🔴 |

RTK 覆盖第一个面。Headroom 覆盖第一个和第三个。Token Optimizer 覆盖全部八个，并继续处理压缩之外的事：

- **三种浪费，不是一种。** 结构性（臃肿配置、未用 skills、过期 memory）、运行时（冗余输出、重读）、行为性（模型误路由、缓存过期、重试循环）。[各自如何工作 →](https://alexgreensh.github.io/token-optimizer/features/active-compression/)
- **节省能扛过压缩。** auto-compact 前检查点，之后恢复。没有这个，压缩节省在压缩触发时瞬间消失。
- **衡量是否有帮助。** 前/后 token 差值、四个定价层的美元节省、追踪退化的质量评分。不是"我们压缩了东西"就完事。
- **零基线开销。** 外部进程，上下文中没有常驻指令，没有 MCP 服务器，没有依赖，没有遥测。

<p align="center">
  <img src="skills/token-optimizer/assets/automated-flow.svg" alt="Token Optimizer 每次会话如何自动工作" width="900">
</p>

|  | Token Optimizer | Headroom | RTK | context-mode | `/context` |
|---|---|---|---|---|---|
| **压缩存活** | 🟢 渐进式检查点、恢复、工具输出摘要 | 🔴 | 🔴 | 🟡 仅会话指南 | 🔴 |
| **会话连续性** | 🟢 跨会话提示、冷恢复、检查点评分 | 🔴 | 🔴 | 🟡 会话指南 | 🔴 |
| **模型路由和行为辅导** | 🟢 11 个检测器、subagent 成本分解、反模式 | 🔴 | 🔴 | 🔴 | 🟡 基础建议 |
| **Keep-Warm（缓存 TTL 刷新）** | 🟢 可选的缓存过期前 ping，自动关闭触发线 | 🔴 | 🔴 | 🔴 | 🔴 |
| **历史趋势分析** | 🟢 30 天趋势、质量/成本/缓存/时长关联、模型切换检测 | 🔴 | 🔴 | 🔴 | 🔴 |
| **循环和空转检测** | 🟢 在消耗 token 前捕获行为循环 | 🔴 | 🔴 | 🔴 | 🔴 |
| **上下文质量评分** | 🟢 7 信号质量评分带等级 | 🔴 | 🔴 | 🔴 | 🟡 仅容量百分比 |
| **结构性浪费审计** | 🟢 深度按组件（CLAUDE.md、skills、MCP、memory） | 🔴 | 🔴 | 🔴 | 🟡 仅摘要 |
| **CLAUDE.md 和 MEMORY.md 健康** | 🟢 8 个审计器 + 注意力曲线评分 | 🔴 | 🔴 | 🔴 | 🔴 |
| **衡量压缩是否有效** | 🟢 本地遥测、前/后 token、美元节省 | 🔴 | 🟡 `rtk gain`（仅 token 计数） | 🔴 | 🔴 |
| **多 agent 跨平台分析** | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |
| **缓存安全** | 🟢 从不修改已有上下文前缀 | 🟡 代理模式重写流量 | 🟢 仅 pre-shell | 🟡 MCP 开销 | 🟢 |
| **零基线上下文开销** | 🟢 外部进程，无上下文注入 | 🔴 注入指令 | 🟢 仅 shell 级 | 🔴 MCP 服务器开销 | 🟢 原生 |
| **零运行时依赖** | 🟢 纯 stdlib（Python/TypeScript） | 🟡 Python + Rust + 可选模型 | 🟢 单个 Rust 二进制 | 🟡 需要 SQLite 适配器 | 🟢 N/A |
| **零遥测** | 🟢 | 🟢 | 🟡 可选 | 🟡 视情况 | 🟢 |
| **多平台** | 🟢 Claude Code、CodeBuddy Code、VS Code、Codex、OpenClaw、OpenCode、Hermes、Copilot | 🟢 Claude Code、Cursor、Codex、Aider、Copilot | 🟢 14 个集成 | 🟢 15 个集成 | 🔴 仅 Claude Code |

每一项声明都经过真实会话和 57 个 fixture 压缩套件测试，你可以自己运行。**[完整基准方法论和结果 →](BENCHMARK.md)**

## 仪表盘

![Token Optimizer 仪表盘](skills/token-optimizer/assets/dashboard-demo.gif)

一个 HTML 页面，通过 SessionEnd hook 在每次会话后自动重新生成，无需手动触发。收藏 `http://localhost:24842/token-optimizer`，它永远是最新的。

每轮的 token 明细、四个定价层的成本、带 TTL 混合和命中率的缓存分析、每个会话叠加的质量评分、subagent 成本分解、四个不重叠池的节省追踪器。安装后零配置。[完整仪表盘文档 →](https://alexgreensh.github.io/token-optimizer/reference/dashboard/)

## 省下了什么

节省来自四个不重叠的池，分两层追踪：

| 池 | 覆盖什么 |
|---|---|
| 模型路由 + 缓存 | 更精简的前缀、更轻的模型组合、cache-write 作为路由手段 |
| Subagent 路由 | 侧链成本优化（仅 Claude Code） |
| 压缩回收 | delta 模式、结构图、bash/搜索压缩消除的 token |
| 精简输出回收 | 精简输出提示消除的输出 token |

**两个数字，分开追踪：**

- **已计（~$313/月）**，逐动作记录。每次 Token Optimizer 换入更轻的模型、修剪冗长结果、跳过重复读取，它都加起来：更聪明的习惯 ~$260/月，工作中压缩 ~$53/月。这是逐事件计量的切片，所以更小且精确。
- **全局（~$1,877/月，~18%）**，完整的反事实。如果你按 Token Optimizer 之前的方式工作（~95% Opus），你本应付约 ~$10,585/月，对比现在的 ~$8,708/月。差距主要来自更轻的模型组合（95% Opus 降到 60%，~$1,076/月 主路由 + 缓存），加上更便宜的 subagent（~$741/月）和已计量的压缩回收（~$60/月）。

这两个数字从不相加。已计是带硬凭证的下限。全局是按你冻结的 Token Optimizer 前基线定价的模型。[查看完整方法论 →](BENCHMARK.md)

<p align="center">
  <img src="skills/token-optimizer/assets/real-savings.svg" alt="30 天节省报告：~$313 已计，~$1,877 全局" width="900">
</p>

基于 30 天 684 个会话（快照截至 2026-06-15），按冻结的 Token Optimizer 前基线定价（~95% Opus）。你的数字是你自己的。[查看方法论 →](BENCHMARK.md)

<p align="center">
  <img src="skills/token-optimizer/assets/user-profiles.svg" alt="1M 会话内部发生了什么" width="800">
</p>

## 主动压缩

九项功能主动减少上下文，全部默认开启，全部自动，全部可从仪表盘或 CLI 切换。

底层原理：**PreToolUse hooks** 在每次 Read 和 Bash 调用进入你的上下文前拦截。如果文件已读过，只返回 diff。如果是代码文件重读，结构骨架替代完整内容。如果是 CLI 命令，输出被压缩。**PostToolUse hooks** 将完整原始内容归档到磁盘并记录压缩事件到 SQLite。什么都没丢，一切可检索。**你什么都不用做。hooks 全包。**

![主动压缩概览](skills/token-optimizer/assets/active-compression-hero.svg)

| 功能 | 做什么 | 节省 |
|---|---|---|
| Delta 模式 | 重读只返回变化部分 | 重读 ~20% |
| 结构图 | 未变文件重读返回结构骨架 | ~30%（单文件最高 99%） |
| Bash 压缩 | CLI 输出精简到要点 | ~10% |
| 搜索压缩 | grep/web 结果精简到命中 + 计数 | ~15% |
| 精简输出提示 | 上下文满时引导模型精简输出 | 典型 10-15%，最高 30-41% 输出减少 |
| 质量提示 | 上下文质量下降时警告 | 防止压缩丢失 |
| 循环检测 | 消耗 token 前捕获重试循环 | 按循环计量 |
| 活动模式 | 按会话阶段调整压缩 | 防止决策丢失 |
| 决策提取 | 跨压缩保留决策 | 防止决策丢失 |

从仪表盘 Manage 标签、CLI（`measure.py v5 enable|disable <feature>`）或环境变量切换。`v5` 动词是遗留命令名，控制当前功能。

[阅读各功能如何工作 →](https://alexgreensh.github.io/token-optimizer/features/active-compression/)

<details>
<summary><b>各功能详情</b></summary>

### Delta 模式

当 AI 编辑后重读文件时，Read 调用只返回 diff。真实会话中 65%+ 的 Read 调用是重读。2,000-token 文件重读变成 50-token 的 diff。

![Delta 模式：智能重读](skills/token-optimizer/assets/delta-mode.svg)

禁用：`TOKEN_OPTIMIZER_READ_CACHE_DELTA=0`

### 结构图

当 Claude 重读已看过的代码文件时，Read 调用被阻止并替换为结构摘要：函数签名、类层次、import。720KB Python 文件（180,000 token）变成 250-token 的骨架。

禁用：`TOKEN_OPTIMIZER_READ_CACHE_MODE=shadow`

### 首读骨架

在历史验证的队列中，首次读取大型**代码**文件（Python 或 TypeScript，16KB–256KB）时，Read 返回结构骨架（签名/import）而非完整文件，带一行通知，完整内容永远一步之遥：`expand <key>`、带范围的 Read（`offset`/`limit`）、或直接 Edit。原始内容在任何替换前归档，fail-open — 如果无法归档，返回完整文件。

这仅适用于**代码**。Markdown 等散文在首读时**不**骨架化（自 v5.11.27 起）：仅标题大纲会丢掉关键散文，所以文档永远完整返回。运行时触发线会在代码队列实时编辑率攀升时自动降级为仅测量。

禁用服务（保留测量）：`TOKEN_OPTIMIZER_FIRST_READ_ACTIVE=0`。完全禁用：`TOKEN_OPTIMIZER_FIRST_READ_SHADOW=0`。两者也可通过 `measure.py v5 status` 和仪表盘 Manage 标签查看和切换。

### Bash 输出压缩

重写常见 CLI 命令返回压缩摘要。覆盖 lint、日志 tail、tree、docker pull、长列表、构建输出、测试运行器。564-token 的 pytest 输出变成 115 token。

![Bash 输出压缩](skills/token-optimizer/assets/bash-compression.svg)

禁用：`TOKEN_OPTIMIZER_BASH_COMPRESS=0`

### 搜索结果压缩

当 AI 运行 grep、rg 或 web 搜索返回长结果列表时，输出精简到命中加计数。500 行 grep 结果变成 20 行加摘要。

禁用：`TOKEN_OPTIMIZER_BASH_COMPRESS_SEARCH=0`

### 精简输出提示

当上下文超过 25% 且质量下降时，一段简短提示告诉模型深度思考但保持可见输出精简。实测 A/B 测试显示输出 token 典型减少 10-15%，最高 30-41%，在真实提示上。缓存安全：作为 `additionalContext` 注入，从不修改已有前缀。

禁用：`TOKEN_OPTIMIZER_VERBOSITY_STEER=0`

### 质量提示

实时监控上下文质量。当评分下降 15+ 分或跌破 60 时，一行说明进入上下文。Claude 在下一轮看到它并浮现警告或调整行为。冷却 5 分钟，每会话最多 3 次。

禁用：`TOKEN_OPTIMIZER_QUALITY_NUDGES=0`

### 循环检测

抓住 AI 卡在重试循环上。比较最后 4 条用户消息和最后 5 个工具结果的相似度。置信度 ≥0.7 时触发，每会话上限 2 次说明。节省从实际循环轮内容计量。

禁用：`TOKEN_OPTIMIZER_LOOP_DETECTION=0`

### 活动模式检测

用最后 10 次工具调用将会话分类为五种模式之一（代码、调试、审查、基建、通用）。模式输入压缩指导，让 PRESERVE/DROP 优先级适应你正在做什么。

### 决策提取

实时从工具输出检测决策语句并存入会话数据库。压缩时，这些决策作为 CRITICAL DECISIONS 注入，压缩摘要必须逐字保留。每会话上限 10 条。

### 衡量实际节省

所有压缩功能记录到本地 SQLite 表。什么都不离开你的机器。

```bash
python3 measure.py compression-stats --days 30
```

</details>

## 会话数据库

Token Optimizer 的一切都由两个本地 SQLite 数据库支撑。什么都不离开你的机器。零网络调用。

<p align="center">
  <img src="skills/token-optimizer/assets/session-database-flow.svg" alt="会话数据库流：工具调用压缩、归档、记录到 SQLite、可检索" width="900">
</p>

**每会话 DB**（`~/.claude/token-optimizer/snapshots/session-store/<session>.db`）持有 8 张表，追踪文件读取、工具输出、命令输出、缓存内容、上下文情报事件、活动日志、决策日志、提示服务。WAL 模式支持 hook 进程并发读写。每会话 50MB 上限。

**趋势 DB**（`~/.claude/token-optimizer/snapshots/trends.db`）持有 7 张表，追踪会话历史、每日聚合、skill/模型/subagent 使用、节省事件、压缩事件。按会话 UUID 索引以 O(log n) 连接。这是仪表盘、coach 模式和 30 天趋势分析的支撑。

每次压缩事件、每次节省、每次质量测量都是一行可查询的数据。仪表盘是这数据的只读视图。`measure.py compression-stats` 是一条 SQL 查询。你的数据是你的。

## 渐进式披露

大型工具结果（>4KB）归档到磁盘，替换为简短预览加检索指针。完整输出扛过压缩。当模型需要时，通过 `expand` 拉取原始内容，无需重跑命令，无丢失输出。

这不只是存储。系统追踪多少结果被归档 vs 重新展开，所以你能看到实际保持折叠的净 token。重新展开从节省总额中扣除，你只计算实际保持压缩的部分。

```bash
python3 measure.py expand --list          # 列出归档的工具结果
python3 measure.py expand <tool-use-id>   # 检索特定结果
```

## 会话连续性

压缩很重要，但 Token Optimizer 做的最重要的事是让你的工作跨会话和压缩后仍然存活，且完全自动。

当你结束会话时，Token Optimizer 把状态检查点到 SQLite：活动任务、关键决策、修改的文件、git 分支、最近读取。当你开始新会话时，它按你的提示对所有最近检查点评分，浮现最相关的一个作为提示。你带着上下文恢复，不是从零开始。

**自动发生什么：**

- **跨会话提示**：开始新会话时浮现相关性评分的检查点。提示包含前一会话的任务、决策、文件、分支。全部围栏为 RECOVERED DATA，永远不是指令。
- **冷恢复精简**：重开过期会话而不支付完整 transcript 成本。Token Optimizer 从检查点重建精简上下文。无 LLM 调用，无完整 transcript 冷恢复。从 SQLite 免 token 重建。
- **提示跟随测量**：当连续性提示浮现文件路径且模型随后读取其中一个时，Token Optimizer 记一次避免的探索性搜索。测量的因果，不是猜测。

```bash
python3 measure.py resume-lean                    # 列出可重开的冷会话
python3 measure.py resume-lean <#|session_id> --print  # 输出精简上下文块
```

压缩节省只有在会话扛过压缩时才真正留下。会话连续性让这发生。

## 智能压缩

当 auto-compact 触发时，60-70% 的对话会消失。决策、错误修复序列、agent 状态，全没了。

Token Optimizer 在压缩前检查点会话，并通过 hooks 恢复摘要丢掉的内容，自动。它还注入**上下文情报摘要**：模型已处理的大型工具输出的启发式摘要（触碰的文件路径、见过的错误、行数）。压缩后，模型知道它看过什么，无需重读一切。

**活动模式检测**用最后 10 次工具调用实时分类会话（代码、调试、审查、基建、通用）。模式输入压缩指导，让 PRESERVE/DROP 优先级适应你此刻正在做什么，而非通用启发。

**决策提取**实时从工具输出捕获决策语句并存入会话 DB。压缩时，这些作为 CRITICAL DECISIONS 注入，摘要必须逐字保留。每会话上限 10 条。

压缩节省只有在会话扛过压缩时才真正留下。在 `git status` 上省 token，如果下一次 auto-compact 抹掉让你运行它的决策，就没用。

<p align="center">
  <img src="skills/token-optimizer/assets/quality-nudges-loops.svg" alt="质量提示和循环检测实战" width="800">
</p>

<details>
<summary><b>智能压缩如何工作</b></summary>

### 渐进式检查点

在多个阈值捕获会话状态：20%、35%、50%、65%、80% 上下文填充，加上质量跌破 80、70、50、40。也在 agent 扇出前和大批��辑后快照。恢复时选最丰富的合格检查点。

### 上下文情报摘要

压缩后，Token Optimizer 注入会话最大工具输出的摘要：触碰的文件路径、检测到的错误、行数。启发式生成 <30ms，无 LLM 调用。模型无需重读一切即可重新定位。

```bash
python3 measure.py setup-smart-compact    # 检查点 + 恢复 hooks
```

</details>

## 输出 token：精简 vs 冗长

输出 token 是会话中最昂贵的部分。在 Opus 上它们比输入 token 贵 5 倍，按生成计费，不按缓存读取计费。对简单问题的冗长回答烧掉你本不需要花的钱。

Token Optimizer 通过**精简输出提示**自动处理。当上下文超过 25% 且质量开始下降时，一段简短提示告诉模型深度思考但保持可见输出精简。实测 A/B 测试显示**输出 token 典型减少 10-15%，最高 30-41%**，在真实提示上。

**如何工作：**

- 提示作为 `additionalContext` 注入，从不修改已有前缀，所以缓存保持完整
- 只在上下文填满时触发，不是你还有大量空间时
- 模型仍然思考问题；它只是产生更精简的可见回答
- 随时禁用：`TOKEN_OPTIMIZER_VERBOSITY_STEER=0`

这是 9 项主动压缩功能之一，也是省在输出侧的那项 — 那里 token 最贵。

## 质量评分

质量评分追踪两件事：**资源健康**（你离退化悬崖有多近）和**会话效率**（你的 token 是否在做有用工作）。S 到 F 的字母等级让分诊瞬时完成。

随着上下文填充，质量下降。MRCR 在 256K 和 1M 上下文之间从 93% 降到 76%。你的 AI 随窗口填充可测地变笨。质量评分精确显示那何时发生。

![真实会话质量分解](skills/token-optimizer/assets/quality-example.svg)

状态栏随质量退化变色：绿、黄、橙、红。质量跌破 75 时，会话时长作为警告出现。运行中的 subagent 显示其模型和经过时间。

![状态栏退化](skills/token-optimizer/assets/status-bar.svg)

```bash
python3 measure.py setup-quality-bar      # 一次性安装
```

[阅读评分如何工作 →](https://alexgreensh.github.io/token-optimizer/features/quality-signals/)

<details>
<summary><b>质量评分详情</b></summary>

| 评分 | 信号 | 含义 |
|--------|--------|----------------|
| **资源健康** | 上下文填充、压缩深度、绝对浪费 token | 离退化悬崖多近 |
| **会话效率** | 过期读取、臃肿结果、决策密度、agent 效率 | 会话此刻是否在用好 token |

| 等级 | 范围 | 含义 |
|-------|-------|---------|
| **S** | 90-100 | 峰值效率 |
| **A** | 80-89 | 健康，可小幅优化 |
| **B** | 70-79 | 退化开始 |
| **C** | 55-69 | 显著浪费 |
| **D** | 40-54 | 严重问题 |
| **F** | 0-39 | 上下文在恶化，需立即行动 |

**质量栏消失了？** 运行 Claude Code 的 `/statusline` 会覆盖 Token Optimizer 的条目。SessionStart 自动恢复。开始新会话它就回来。

**想永久关掉？**
```bash
python3 measure.py setup-quality-bar --uninstall
```

</details>

## Coach 模式

```
> /token-coach
```

告诉它你的目标。拿回具体的、按优先级排序的修复，带精确 token 节省。它读你 30 天的会话数据并浮现单一会话看不到的东西：质量下滑、会话变长、缓存命中率下降、每会话成本攀升。

每个洞察都基于你的真实数据。"你的短会话评分 68 vs 长会话 60"比"考虑更短的会话"更有冲击力。Coach 模式还识别项目级优化机会（你从不用的 skills、急切加载的 MCP 服务器、破坏缓存的 CLAUDE.md 模式）并教你如何修复，让未来会话从更精简开始。

[阅读 Coach 模式 →](https://alexgreensh.github.io/token-optimizer/features/coach-mode/)

<details>
<summary><b>Coach 模式详情</b></summary>

### 检测到的历史模式

| 模式 | 检测什么 |
|---|---|
| 质量漂移 | 平均质量逐周下降 |
| 会话时长爬升 | 会话变长，上下文填充更快 |
| 缓存退化 | 缓存命中率下降（以及是否模型切换导致） |
| 等级分布 | 太多 D 级会话堆积 |
| 成本意识 | 每会话成本攀升，带路由建议 |
| 时长-质量关联 | 短会话评分更高，建议拆分长会话 |
| 压缩差距 | 仅影子节省远超主动压缩 |
| 模型切换 | 频繁的会话中模型切换使 prompt 缓存失效 |

### 浪费检测器

11 个自动化检测器分析你的会话模式：

| 检测器 | 抓住什么 |
|---|---|
| PDF/二进制吞入 | 大文件消耗上下文 |
| Web 搜索开销 | 太多 web 结果倾倒进上下文 |
| 重试折腾 | 同一工具带错误重试 3+ 次 |
| 工具级联 | 3+ 连续工具错误 |
| 循环 | 重复相似消息 |
| 过强模型 | Opus 用于简单编辑 |
| 过弱模型 | Haiku 用于复杂任务 |
| 糟糕分解 | 单体 500+ 词提示 |
| 浪费思考 | 小编辑的扩展思考 >2x 输出 |
| 输出浪费 | 对简单操作的冗长回答 |
| 缓存不稳定 | 破坏 prompt 缓存的 CLAUDE.md 模式 |

### Keep-Warm

API 计费会话的可选功能。在你的 prompt 缓存条目即将过期前发出一个微小的缓存读取 ping，刷新其 TTL。成本约前缀的 0.1x，对比恢复时你要付的 1.25-2x 重写。触发线自动关闭如果 ping 不再划算。

```bash
python3 measure.py keepwarm-enable          # 可选（仅 API 计费）
python3 measure.py keepwarm-report            # 净节省、花费、触发线状态
python3 measure.py keepwarm-disable           # 随时退出
```

### 多平台审计器

跨 Claude Code、Codex 和自定义 transcript 设置扫描，识别空闲烧钱、模型误路由和配置臃肿，每个发现带美元节省。

### CLAUDE.md 路由注入

从你的实际使用数据生成模型路由指令并注入 CLAUDE.md。48 小时过期保护自动移除过时建议。

```bash
python3 measure.py inject-routing --dry-run   # 预览
python3 measure.py inject-routing              # 注入
```

</details>

## FAQ

<details>
<summary><b>🔒 它会降低我的上下文质量吗？</b></summary>

不会。结构优化只移除真正未使用的组件。主动压缩控件可通过单条命令或环境变量禁用。质量评分系统实时追踪退化。

</details>

<details>
<summary><b>💾 它会破坏 prompt 缓存吗？</b></summary>

不会。Token Optimizer 从不触碰已经在上下文中的内容。它作用于进入窗口的新内容和压缩边界。你的缓存前缀保持完整，这意味着它省你两次钱：每轮更少输入，且未来每轮更便宜的缓存读取。

</details>

<details>
<summary><b>📡 它会把数据发到别处吗？</b></summary>

没有分析、没有遥测��点、没有产品数据离开你的机器。测量事件是你拥有的本地 SQLite 行。零网络调用。

</details>

<details>
<summary><b>⚠️ 它会影响我的会话吗？</b></summary>

不会。所有 hooks 均为非阻塞的 fail-open 设计。如果 Token Optimizer 脚本出错，你的命令照常运行。

</details>

<details>
<summary><b>📦 有运行时依赖吗？</b></summary>

没有。Claude Code 和 Codex 上纯 Python stdlib。OpenCode 和 OpenClaw 上零运行时依赖的 TypeScript。

</details>

<details>
<summary><b>🔐 install.sh 如何验证文件完整性？</b></summary>

解析最新 GitHub Release 标签，检出该标签，从同一 release 获取 CHECKSUMS.sha256，并验证每个脚本文件。带外验证意味着被入侵的提交无法同时替换代码和校验和。

</details>

## 所有命令

<details>
<summary><b>查看所有命令</b></summary>

| 命令 | 做什么 | 文档 |
|---|---|---|
| `/token-optimizer` | 完整审计带 6 个并行 agent、引导式修复 | [→](https://alexgreensh.github.io/token-optimizer/start/quickstart/) |
| `/token-coach` | 30 天趋势分析、按优先级排序的修复 | [→](https://alexgreensh.github.io/token-optimizer/features/coach-mode/) |
| `quick` | 10 秒健康检查 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `doctor` | 安装检查，10 分制评分 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `dashboard` | 打开 HTML 仪表盘 | [→](https://alexgreensh.github.io/token-optimizer/reference/dashboard/) |
| `savings` | 美元节省报告 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `report` | 按组件 token 明细 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `quality` | 实时会话的上下文质量分析 | [→](https://alexgreensh.github.io/token-optimizer/features/quality-signals/) |
| `trends` | skill 采用、模型组合、开销随时间 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `compression-stats` | 主动压缩的计量节省 | [→](https://alexgreensh.github.io/token-optimizer/features/active-compression/) |
| `memory-review` | MEMORY.md 结构审计 | [→](https://alexgreensh.github.io/token-optimizer/features/memory-health/) |
| `git-context` | 为你当前 diff 建议文件 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `drift` | 对比你上次快照的并排比较 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `conversation` | 每条消息的 token 和成本明细 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `pricing-tier` | 查看或切换定价层 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `expand` | 检索归档的工具结果（渐进式披露） | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `resume-lean` | 免 token 重建重开冷会话 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |

[完整 CLI 参考 →](https://alexgreensh.github.io/token-optimizer/reference/cli/)

</details>

## 许可证

**PolyForm Noncommercial 1.0.0**。源代码可用。个人、研究、教育和非商业使用无需购买许可证。

### 个人 / 爱好 / 研究 / 教育？

放手用。完整源码，本地运行，无需购买许可证。

### 小团队（5 人以下 或 月收入 $20k 以下）？

小团队自动获得免费商业许可证。直接用就行。

### 从个人开始，现在要变成生意了？

你过去的使用完全没问题。许可证在任何书面通知后有内置的 32 天宽限期。准备好时联系获取商业许可证。

### 大公司 / 商业使用？

联系 [Alex Greenshpun](https://linkedin.com/in/alexgreensh) 或 me@alexgreenshpun.com。

---

由 [Alex Greenshpun](https://linkedin.com/in/alexgreensh) 创建。
