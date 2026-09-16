---
layout: default
title: VeryMath 使用手册
permalink: /handbook/HANDBOOK.zh-CN.html
---

# VeryMath 使用手册

[English](/handbook/HANDBOOK.html)

VeryMath 是一套给 Coding Agent 用的数学工具集合，主要包括下面两类：

- **Skill 包**：装进你的 Coding Agent 后，agent 在遇到对应任务时会自动或按你点名调用。
- **独立程序，例如 agent 的 harness**：独立部署运行的工具，自带界面或命令行。

---

## 一、如何安装一个 Skill

所有 AI4Math Skill 的安装方式都一样：**打开你的 Coding Agent，把一段话发给它，让它自己完成克隆、安装和验证**。不需要你手动敲命令或配路径。

支持的 agent 包括 Codex、Claude Code、OpenCode、Cursor 等任何能读写本地文件、执行终端命令的 Coding Agent。

### 通用模板

把下面这段发给 agent，按需替换仓库地址和要装的包：

```text
请帮我安装这些 AI4Math Skill。

仓库：<仓库地址>
分支：main
要安装的 Skill 路径：
- skills/<包名1>
- skills/<包名2>

步骤：
1. 把仓库克隆或更新到本地。
2. 读 README.md、SKILL.md，以及每个目标 Skill 的入口文件。
3. 如果当前环境支持本地 Skill 发现，把每个含 SKILL.md 的目录装到本环境的 skills 目录。
4. 如果某个 Skill 依赖同级的支撑目录，保持它们在原位。
5. 验证安装后的 Skill 能被发现。
6. 告诉我安装路径、是否需要重启，并给我一条测试指令。
```

Agent 会自己判断当前环境的 skills 目录该放在哪里（Codex 是 `~/.codex/skills`，Claude Code 是 `~/.claude/skills`，OpenCode 是 `~/.config/opencode/skills`，其他 agent 各有配置），你不用关心。

### 示范：安装 `math-paper-reading`

下面以 [AI4Math · Paper Reading](https://github.com/VeryMath/AI4Math-Paper-Reading) 仓库里的 `math-paper-reading` 为例（Skill 在 `skills/math-paper-reading/`）：

**你说：**

```text
请帮我安装 AI4Math 的 math-paper-reading Skill。

仓库：https://github.com/VeryMath/AI4Math-Paper-Reading
分支：main
Skill 路径：skills/math-paper-reading

步骤：
1. 把仓库克隆或更新到本地。
2. 读 README.md、SKILL.md，以及 skills/math-paper-reading/ 的入口文件。
3. 如果当前环境支持本地 Skill 发现，把含 SKILL.md 的该目录装到本环境的 skills 目录。
4. 如果该 Skill 依赖同级的支撑目录，保持它们在原位。
5. 验证安装后的 Skill 能被发现。
6. 告诉我安装路径、是否需要重启，并给我一条测试指令。
```

**Agent 会做：** 克隆仓库 → 读 `skills/math-paper-reading/SKILL.md` → 把该目录装进本机 skills 目录 → 回报路径。

**验证安装：** 新开一个会话，发一条点名调用的指令：

```text
用 math-paper-reading 说明：接到一篇 PDF 数学论文时，你的第一步工作流是什么？
先不要真的去读文件，只按 Skill 里的规定概述流程。
```

如果 agent 的回答明显来自刚安装的 `SKILL.md`（步骤、术语和仓库文档一致），而不是泛泛而谈，说明装好了。

当然，日常使用时不必每次点名 Skill；agent 会根据你的任务自行匹配已安装的相关 Skill。

### 更新和卸载

同样是一句话：

```text
更新我本机安装的 AI4Math Skill：拉取各仓库最新的 main 分支，同步已安装的 Skill 目录，
告诉我哪些有变化。
```

```text
卸载 <包名> 这个 Skill，从本机 skills 目录移除它，保留克隆下来的仓库。
```

### 几点提醒

- **Skill 只是说明书，不是运行环境。** 比如 SageMath Skill 需要本机真的装了 SageMath，Lean Skill 需要 Lean 4 和 mathlib，优化类 Skill 需要对应求解器。这些环境的安装通常也由 Skill 自己引导 agent 完成，但会先征求你同意。
- **涉及下载、装环境、创建 conda 环境的操作，先看清楚再批准。**
- **需要账号登录的环节由你本人完成**，不要把 API key 交给 agent 写进仓库。
- 装完可能需要重启 agent 才能发现新 Skill，agent 会告诉你。

---

## 二、应用程序

### VeryMath 智慧教材

个人部署的课程学习工作台。左边读教材 PDF，右边跟 Copilot 对话。导入自己的教材，连上一个 Coding Agent，就能针对任意章节提问、讲解、出题，并生成思维导图、知识图谱和 LaTeX 课件。所有数据留在你自己的电脑上（默认 `~/.course-copilot/`），用你自己的 Agent 账号。

**核心功能**

- 教材解析：把选定页或章节整理为可读的数字教材，提取正文、公式、图片和目录
- 讲解内容：对概念、定理、算法、例题做分层讲解，可主动配图
- 知识点出题：生成带递进提示和参考答案的练习卡片
- 思维导图 / 知识图谱：层级知识树与概念关系网络，节点可跳回教材原页
- 生成课件：用 LaTeX Beamer 把章节编译成 16:9 的 PDF 课件
- 自由问答：不带固定模板，按你的提问组织讲解和资料
- 辅助资料：每本教材可挂讲义、习题解答、参考文献，支持全文搜索和扫描件 OCR

**环境要求**：Node.js ≥ 22.13；生成课件需要本机有 XeLaTeX、Beamer、ctex 和中文字体；OCR 需要 Tesseract（中文还需 `chi_sim`/`chi_tra` 语言包）和 Poppler。Windows 建议整套装在 WSL2 里。

**安装**：同样是一句话交给 agent——

```text
拉取 https://github.com/VeryMath/VeryMath-textbook-copilot，
按仓库里的 skills/verymath-install/SKILL.md 完成 VeryMath 智慧教材的本机部署：
检查并安装必要依赖，配置内置课程 Skill，连接我现有的 Agent，启动工作台并给我访问地址。
```

Agent 会装依赖、配好内置课程 Skill、连上 Agent 并启动服务，最后返回访问地址（正式运行默认 `http://127.0.0.1:4173`，只监听本机）。打开页面后点「导入教材」选 PDF，再到「工作区设置」连接 Agent 即可。

内置的课程 Skill 有 `textbook-parse`、`explain`、`quiz`、`mindmap`、`knowledge-graph`、`textbook-to-ppt`，加上负责部署的 `verymath-install`。

支持的 Agent：Codex、Claude Code、OpenCode、Cursor、Gemini CLI、Copilot CLI、Qwen Code、Kimi Code、Kiro CLI，选一种就行。

当前版本：v0.1.0（macOS 预览版）、v0.1.1（Windows 预览版）。

详细文档 → [VeryMath-textbook-copilot](https://github.com/VeryMath/VeryMath-textbook-copilot) ｜ [用户手册](https://github.com/VeryMath/VeryMath-textbook-copilot/blob/main/docs/user-guide.md) ｜ [架构参考](https://github.com/VeryMath/VeryMath-textbook-copilot/blob/main/docs/architecture.md) ｜ [Skill 开发](https://github.com/VeryMath/VeryMath-textbook-copilot/blob/main/docs/skill-development.md)

---

### Co-Mathematician

把数学研究对话变成有文件支撑的项目。核心思路是「Coding Agent + 仓库文件系统 + 门控 + 评审循环 = 研究工作台」：主线程扮演项目协调者，研究问题、目标、状态和消息都落在 `workspace/project/`，证明、计算、文献、评审各自成为独立工作流，最终论文只从通过评审的报告渲染出来。

Python 部分只负责初始化文件、追加消息、创建工作流、检查门控和渲染论文——它不跑 agent，agent 是你的 Coding Agent。

**核心机制**

- 目标要标为 `approved` 才能开工作流，草稿目标不可执行
- 工作流分 `proof`、`computation`、`literature`、`review` 四类
- 每份报告要带来源溯源、显式的不确定性、失败尝试记录，以及 `reviews/` 下的独立评审
- 最终产物 `workspace/final/working_paper.md` 是工作论文，不是聊天总结
- 可以把 AI4Math 的领域 Skill 装进项目的 `.agents/skills/`，由协调者按需推荐和移交

**安装**：也是交给 agent——

```text
从 https://github.com/VeryMath/co-mathematician.git 安装 Co-Math，
把 ~/CoMathProjects 设为项目目录，创建一个名为 Muon Convergence 的项目。
返回它的路径，先不要开始研究。
```

然后用你的 Coding Agent 打开那个项目目录，说「Continue this Co-Math project.」即可开始。日常用 `co-math list / resume / next / archive / reopen` 管理项目。

详细文档 → [co-mathematician](https://github.com/VeryMath/co-mathematician)

---

## 三、Skill 仓库一览

### AI4Math · SageMath — 精确符号计算

让 agent 用 SageMath 做可验证的精确计算：先检索内置的 SageMath 参考手册，再写成普通 Python 形式的 Sage 代码，本地执行，最后基于真实运行输出作答。覆盖代数、数论、组合、图论、多项式环、矩阵、微积分、有限域、椭圆曲线、Galois 群、编码理论、密码学、流形、模形式等领域。Windows 用户需要在 WSL 里装和运行 SageMath。


| 包                | 用途                      |
| ---------------- | ----------------------- |
| `sagemath-skill` | 参考检索 + 代码执行 + 结果复现的完整流程 |


详细文档 → [AI4Math-Sagemath-skill](https://github.com/VeryMath/AI4Math-Sagemath-skill)

---

### AI4Math · Auto Research — 自动研究与问题发现

把模糊的研究意图变成结构化问题、有边界的研究运行和经过评审的证明计划。包最多的一个仓库，也包含几个外部研究系统（Rethlas、Archon、Danus）的安装与驱动助手。


| 包                                   | 用途                                                             |
| ----------------------------------- | -------------------------------------------------------------- |
| `discover-math-problems`            | 把模糊背景转成排序过的问题、猜想格、证据账本和工单                                      |
| `proof-blueprint-review`            | 构建证明蓝图，做验证者式评审，输出严格的证明状态报告                                     |
| `open-problem-research-pipeline`    | 文献检索、方法分析、证明框架、报告的分阶段流程                                        |
| `graph-theory-researcher`           | 读图论论文、经用户确认选题、有界研究、产出 LaTeX/PDF                                |
| `agent-laboratory-workflow`         | 部署、校验并启动有边界的 Agent Laboratory 自动研究运行                           |
| `rethlas-helper`                    | 安装 Rethlas 并从任意项目跑自然语言证明生成                                     |
| `archon-helper`                     | 安装 Archon 并跑形式化工作流                                             |
| `danus-helper` / `danus-helper-dsh` | 安装 Danus（OpenCode 版 / DeepSeek Harness 版），跑多智能体数学研究、监控、总结与论文写作 |


详细文档 → [AI4Math-Auto-Research](https://github.com/VeryMath/AI4Math-Auto-Research)

---

### AI4Math · Paper Reading — 论文精读与转化

结构化地读数学论文，抽取定理依赖，并把论文转成可复用的 Skill。


| 包                            | 用途                                     |
| ---------------------------- | -------------------------------------- |
| `math-paper-reading`         | 深读论文、抽取定理依赖、构建证明路径、管理本地文献笔记            |
| `paper-to-skill`             | PDF 预处理、论文分诊、证明模式抽取、跨论文综合，产出新 Skill    |
| `after-ocr`                  | 审校并修复公式密集的 OCR Markdown，带覆盖率、证据日志和多轮校对 |
| `graph-theory-paper-reading` | 图论论文深读，输出带证明树的结构化 LaTeX 报告             |


详细文档 → [AI4Math-Paper-Reading](https://github.com/VeryMath/AI4Math-Paper-Reading)

---

### AI4Math · Writing — 论文写作与课件

从已验证的材料出发写论文，不替代证据核查本身。强调「有据可溯」：每个论断都要能追到来源。


| 包               | 用途                                                        |
| --------------- | --------------------------------------------------------- |
| `paper-writing` | 起草、修订、结构化和审计数学论文，含论断-证据核对、证明义务检查、记号一致性、公式可读性和 LaTeX 投稿前检查 |
| `math-beamer`   | 构建有据可溯的 Beamer 讲稿，选模板、编译、检查排版、维护幻灯片到来源的对照表                |


详细文档 → [AI4Math-Writing](https://github.com/VeryMath/AI4Math-Writing)

---

### AI4Math · Lean Agents — Lean 4 形式化

给 agent 一套检查 Lean 项目、搭 mathlib 工作区、形式化定理陈述、修复证明、补 `sorry` 并本地验证补丁的流程。最终补丁不允许引入 `sorry`、`admit`、新公理或悄悄改动定理陈述。


| 包                    | 用途                                            |
| -------------------- | --------------------------------------------- |
| `lean-setup`         | 安装或检查 Lean 4、`elan`、`lake`，准备可复用的 mathlib 工作区 |
| `lean-formalization` | 形式化定理陈述、修复证明、补 `sorry`、评审 Lean 补丁、协调可选后端      |


`skills/lean-runtime/` 是共享支撑层（脚本、schema、提示词、测试），不单独调用，但安装时要保留在同级目录。Numina、Archon 等外部后端是可选适配器，需要你明确批准才会接入。

详细文档 → [AI4Math-Lean-Agents](https://github.com/VeryMath/AI4Math-Lean-Agents)

---

### AI4Math · Optimization — 优化建模与求解

数学规划建模、求解器选型与环境配置、运行证据报告。


| 包                               | 用途                                   |
| ------------------------------- | ------------------------------------ |
| `optskills`                     | 103 张已发布的 OptSkills 问题原型卡，可独立用于建模和求解 |
| `mixed-integer-programming`     | 含 0-1、整数、连续决策变量的 MILP/MIP 建模         |
| `second-order-cone-programming` | SOCP 建模与基于 cvxpy 的锥优化求解              |
| `osqp-solver`                   | 连续凸 QP 的 OSQP 建模、重复求解、状态门控与独立验证      |
| `cdopt-optimization`            | CDOpt 与流形约束优化的建模、校验、runner 生成与证据报告   |
| `or-solver`                     | 指定求解器的依赖、安装、许可证、环境变量与故障排查            |


分工是：你或建模 Skill 选定求解器，`or-solver` 负责把那个求解器配好。

详细文档 → [AI4Math-Optimization](https://github.com/VeryMath/AI4Math-Optimization)

---

### AI4Math · Computational Mathematics — 计算数学

把数学对象、方程、数据或论文片段变成经过评审的计算表示和可复现证据。


| 包                                   | 用途                             |
| ----------------------------------- | ------------------------------ |
| `invariant-computation`             | 代数、拓扑、几何、TDA 与可认证数值不变量计算的路由与校验 |
| `least-squares`                     | 线性、多项式、非线性、正则化、带约束和贝叶斯最小二乘拟合   |
| `scientific-computing-reproduction` | 复现、诊断、调参、可视化和汇报科研计算代码，带人工审批检查点 |


详细文档 → [AI4Math-Computational-Mathematics](https://github.com/VeryMath/AI4Math-Computational-Mathematics)

---

### AI4Math · Evolving — 演化式实验

目前聚焦有边界的 OpenEvolve 实验会话。


| 包                                | 用途                                          |
| -------------------------------- | ------------------------------------------- |
| `openevolve-experiment-workflow` | 检查或创建 OpenEvolve 项目、校验运行配置、跑短探针、汇总指标、指导迭代改进 |


详细文档 → [AI4Math-Evolving](https://github.com/VeryMath/AI4Math-Evolving)

---

### AI4Math · MathTool — 独立小工具

放独立数学工具和轻量 agent 适配器，每个包有自己的工作流、依赖溯源和测试。


| 包               | 用途                                          | 状态              |
| --------------- | ------------------------------------------- | --------------- |
| `math-glossary` | 构建、评审、备份、导入导出和维护双语数学术语表                     | 已发布 v0.1.0（MIT） |
| `matlab-runner` | 把明确的 MATLAB 任务经 MATLAB MCP 服务器执行，带测试与数值验证证据 | 评审中，未发布         |


详细文档 → [AI4Math-MathTool](https://github.com/VeryMath/AI4Math-MathTool)

---

## 四、官网

VeryMath 项目官网：组织介绍、仓库导航与动态。

- [VeryMath 官网](https://verymath.github.io/)
- [中文使用手册](/handbook/HANDBOOK.zh-CN.html) · [English Handbook](/handbook/HANDBOOK.html)
- [站点源码](https://github.com/VeryMath/verymath.github.io)
