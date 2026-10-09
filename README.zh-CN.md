# physics-to-math-research

**版本：** `0.1-alpha.2`

**状态：** 公开 Alpha 测试版

GitHub 主 [README.md](README.md) 现已采用中英文同页对照。本文件继续保留，作为纯中文阅读入口。

一个面向科学问题数学化、claim 完整性审查与有界诊断推导的中英双语 Skill。

> 在开始用数学求解科学问题之前，我们是否构造了正确的数学问题？得到的数学结果是否真的支持研究者提出的科学 claim？

## 项目简介

使用本 Skill 检查科学问题、数学表述及其结论之间的衔接。欢迎 alpha 用户用真实问题试用并报告可复现的失败；当前验证仍然有限。

> 文档用于解释和导航。[SKILL.md](SKILL.md) 是当前版本唯一的运行时规范来源。如果文档与其冲突，以 `SKILL.md` 为准。

## 这个 Skill 做什么

- 审查科学或物理问题是否被恰当地构造成数学问题。
- 检查实质性建模承诺、语义映射和推断步骤是否有适当且明确的依据（warrant）。如果改变一个承诺可能改变 claim 的含义、状态、范围、支持程度或可识别性，它就是实质性的（material）。
- 检查数学结论是否被无依据地升级为更强的物理、因果或机制性 claim。
- 通过有界诊断性推导检验 claim 的支持程度，并暴露数学表述的关键依赖结构。
- 在 `v0.1-alpha.2` 中，如果任务仍因缺少与 claim 相关的操作性步骤而未完成，且该步骤由现有信息支持、在表述或诊断范围内可行，则完成其中最小的必要步骤，明确做什么、怎么做，而不是仅指出还需要某项分析。

这不要求每个问题都给出定量分析流程，也不授权求解完整问题。若进一步推进需要无依据的承诺，则停止。

## 为什么建立这个 Skill

科研工作可能在现象与数学之间的转换环节出现以下错误：

- 把相关性报告为因果关系。
- 把 proxy 当作它所代表的潜在真实量。
- 把模型类别内部成立的结果升级为不受限制的物理结论。
- 把数学定理报告为经验事实。

数学上的漂亮或严格本身并不保证科学正确性。本 Skill 旨在减少这些具体的表述与 claim 完整性失败。

## 什么时候使用

- 将科学或物理问题数学化，或审查已有表述。
- 审查 claim 的承诺、映射、推断步骤或状态。
- 进行检验数学表述能否支持目标 claim 所需的有限推导。

## 什么时候不适合使用

- 以完整定理证明、符号代数、因果发现、完整统计方法学、文献综述、模拟、实验优化或论文写作为目的的任务。
- 没有需要表述的科学问题，也没有需要审查的 claim 的任务。

## 核心思想

四条冻结的 Core 规则指导本 Skill：

1. **Problem provisionality / 问题暂定性**
2. **Material commitment accountability / 实质承诺可追责性**
3. **Relative identifiability / 相对可识别性**
4. **Dependency audit / 依赖条件审查**

详见双语的 [Core 解释](references/core-principles.md)和[可观察审计契约（OAC）](references/observable-audit-contract.md)。

OAC 是一个外部可审查性契约，说明审查者应能从相关结果中判断什么。它不是推理流水线、思维链协议或固定答案模板。

## 典型输入

提供简短的科学问题、目标 claim 及已有证据或前提。例如，假设 `y` 是测量量，`x` 是潜在量，标定数据中二者高度相关。以下推断在当前实验中是否成立？

$$y_1 > y_2 \quad\Longrightarrow\quad x_1 > x_2$$

## 典型输出

按 claim 逐条评估其含义与范围、实质承诺与依据、支持状态，以及可能改变该状态的决定性证据或条件。需要时提供有依据且有界的操作性步骤。

相关区分可能包括观测、假设、模型选择、数学结果、经验适用性、物理解释，以及尚缺失的判别证据。这些是示例，不是强制的固定 ontology 或输出模板。

## 安装

将 Skill 目录复制或链接到 skill 库中。推荐安装目录结构保持如下：

```text
Multi_Skills/
└── physics-to-math-research/
    ├── SKILL.md
    ├── README.md
    ├── README.zh-CN.md
    └── references/
        ├── core-principles.md
        └── observable-audit-contract.md
```

Claude Code 是一个安装示例：可将目录放入或链接到其用户级 skill 目录。对于其他 Agent，如果环境支持相应指令加载方式，可以显式加载 `SKILL.md`。这不表示自动兼容；该目录结构不预设特定操作系统或模型提供商。

## 使用方式

- 显式激活或加载 Skill。
- 提供科学问题、目标 claim，以及已有证据或前提。
- Skill 按问题实际需要应用规则，不强制固定推理流水线。
- `SKILL.md` 定义准确的运行时行为。

## 参与贡献

**Bring a real scientific problem. You do not need Core/OAC terminology to participate.**

**带一个真实科学问题来。参与无需先理解 Core/OAC 术语。**

Start in [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) → [Research Problems](https://github.com/ZWY-research/physics-to-math-research/discussions/new?category=general) (currently General). Report reproducible failures in [Issues](https://github.com/ZWY-research/physics-to-math-research/issues/new/choose), preserve mature cases in the [Casebook](cases/README.md), and see [CONTRIBUTING.md](CONTRIBUTING.md) or [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md). Either Chinese or English is sufficient.

从 [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) → [Research Problems 科学问题](https://github.com/ZWY-research/physics-to-math-research/discussions/new?category=general)（目前为 General 分类）开始。在 [Issues](https://github.com/ZWY-research/physics-to-math-research/issues/new/choose) 报告可复现 failure，在 [Casebook](cases/README.md) 沉淀成熟案例；详见 [CONTRIBUTING.md](CONTRIBUTING.md) 或 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。可使用中文或英文。

**Issue 和 Pull Request 均可使用中文或英文提交，贡献者无需同时提供两种语言。**

**现阶段最有价值的贡献，是一个真实、可复现的科学问题失败案例。**

欢迎分享真实科学问题、可复现的 Skill 失败、特定学科边界案例、过度怀疑、过早停止、无依据的 claim 升级，以及方法论或文档改进。参与不要求先理解 Core/OAC 术语。

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 或 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。打开 [Issue 入口](https://github.com/ZWY-research/physics-to-math-research/issues/new/choose)，可报告 Skill 失效、提出改进建议或提交空白 issue。维护者可协助同步语言；Skill 的实质性规范变更须在合并前完成双语语义等价性审查。

采用 [Apache License 2.0](LICENSE)。版本变更见 [CHANGELOG.md](CHANGELOG.md)。

## 科研应用与验证

查看[科研应用与验证登记表](RESEARCH_APPLICATIONS.md)，持续记录科研问题、经作者确认使用 Skill 的论文及能力证据。背景参考文献单独登记。使用或发表本身不构成验证；HL-3 候选目前为 `planned`（计划中）。

## Evaluation Reports & Skill Improvement / 测试与能力改进档案

[测试档案](evaluation-reports/)记录 Skill 实际能力测试、ON/OFF 比较、重要数学失败、成对 regression、修复前后行为，以及未发现可靠缺陷的负结果。每项测试对应一个独立 Markdown 报告；已有可公开访问的完整证据优先链接，避免重复维护。公开证据不完整时须说明复现限制。

首项为[材料本构四格测试](evaluation-reports/2026-10-09-constitutive-four-cell.md)：v0.1-alpha.2，GPT-6.1 Sol / High；两种条件均完成有依据的推导，未观察到实质 ON/OFF 优劣或可靠 Skill failure。测试可以得到成功、失败、持平或不确定结果；每份报告须给出最终优化决策。单项测试不构成整体有效性验证。

**Evidence Attribution / 证据归因：** 测试报告必须区分独立 Skill ON/OFF 运行产生的证据，以及后续人工指导、额外工具或领域专项流程得到的结果。没有独立证据时，不得将后续科研成果归因于 Skill 的增量作用。

**版本演化约定：** Test → Evidence → Failure Review → Minimal Revision → Regression → Version Update.

- **无可靠 failure：**保存测试报告，不修改 SKILL.md、不新增无必要规则、不升级版本。
- **候选 failure：**先记录可复现条件，判断是否属于 Skill 实际问题、现有规则是否已覆盖，优先设计最小有效 regression；未确认前不修改 Core。
- **确认修复：**先完成最小候选行为修订及适当 regression，检查中英文语义等价性与既有能力是否退化。验收后应用正式 SKILL.md 修改、更新版本标识与 [CHANGELOG](CHANGELOG.md)，关联原 failure 编号、修改和修复前后回归证据，再按当前发布流程创建版本或 tag。

只有发现有证据支持的改进需要且实际修改运行行为，才升级 Skill 版本。未来 alpha 阶段行为修订可考虑 v0.1-alpha.3；本次仍保持 v0.1-alpha.2 冻结。单纯增加测试报告、修正文档或新增案例，不自动触发行为版本升级。

## 当前验证状态

### `v0.1-alpha.1` — 历史证据

已完成架构冻结、一次实现审计及首轮 A–E 定向回归。A–E 覆盖测量与语义衔接、相对可识别性、局部与全局依赖、数学与经验状态，以及模型类别承诺。在一个测试环境中通过：Claude Code、DeepSeek API、`deepseek-v4-pro`。

### 初始 Value Benchmark

五个自然科学任务通过盲评比较 Skill ON/OFF 回答。总体偏好中 Skill 在五个任务中的四个获得优选；该小规模 benchmark 未观察到认识论正确性损失。科研实用性评估在 Task 01（等离子体输运问题）暴露了一个弱点。

这些 alpha.1 结果仅涉及五个任务、一个测试模型与环境、每个条件单次运行，以及一位盲评者。它们是初步且与版本绑定的证据，不是普适验证。

### 基于失败案例的修订

Task 01 的实用性弱点经针对性分析后，在两组 Codex 定向复现配对中再次出现。复现所用模型与运行工具不同于原 benchmark，不能证明同模型可靠性或某句措辞的因果机制。这些证据推动了停止指引的窄范围澄清，而非 Core/OAC 重设计。

### `v0.1-alpha.2` — 针对性修复

当前版本包含该修复。被接受的候选版本通过了针对性 pre-commit 检查：有依据的继续推进、证据不足时停止、纯数学任务完成后自然停止，以及中英文实质语义等价性。每个行为案例运行一次；这些检查不是可靠性估计。

现有证据**不能证明**普适科学正确性、跨模型可靠性、广泛跨学科普适性、重复运行稳定性，或任意任务上的完整中英行为等价性。

## 局限性

Skill 无法凭空提供缺失的领域知识、经验证据或依据，也不能保证科学真理。它不会自动证明用户的理论、确认物理机制或选择最复杂的数学。它不能替代领域专家，也不是通用自主科研 Agent。

## 项目结构

公开仓库包含以下运行时规范、解释文档和贡献模板。任何文档都不在 `SKILL.md` 之外增加运行规则。

```text
physics-to-math-research/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── RESEARCH_APPLICATIONS.md
├── evaluation-reports/
│   └── 2026-10-09-constitutive-four-cell.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CONTRIBUTING.zh-CN.md
├── AGENTS.md
├── references/
│   ├── core-principles.md
│   └── observable-audit-contract.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── skill-failure.yml
    │   ├── improvement.yml
    │   └── config.yml
    └── PULL_REQUEST_TEMPLATE.md
```
