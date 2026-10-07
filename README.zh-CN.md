# physics-to-math-research

English: [README.md](README.md)

**版本：** 0.1-alpha.2（冻结工件 frozen artifact）

**Alpha 状态：** 欢迎科研试用与反馈。邀请 alpha 用户报告真实失效案例；现有验证仍然有限。

> 文档仅作解释之用。[SKILL.md](SKILL.md) 是本版本的唯一规范性来源（single normative source）；本文档与其不一致之处，以 `SKILL.md` 为准。

## 这个 Skill 做什么

`physics-to-math-research` 把科学或物理问题转化为经过审查的数学表述，并审计相应 claim 的完整性，需要时辅以诊断性推导：

- 审计一个问题是否被正确地表述为数学问题；
- 检查 material 的 modeling commitment、语义映射和推断步骤是否带有适当的显式 warrant；
- 检查数学结论是否被过度升级为更强的物理、因果或机制性结论；
- 只做必要程度的诊断性推导，以检验一个 formulation 能否支持目标 claim，并暴露其 load-bearing 结构。

## 为什么存在

科研工作常在现象与其数学表述的边界处失败：相关性被报告为因果性，proxy 被当作它所指代的 latent 量，model-class 内的结果被报告为关于物理系统的无限制陈述，数学定理被报告为经验发现。

这个 Skill 的设计目的，是减少这类具体的科学表述与 claim 完整性失败。

## 什么时候用

- 需要把一个科学或物理问题表述为数学问题，或审查已有的表述；
- 需要审计某个 claim 的 modeling commitment、语义映射、推断步骤或 status；
- 需要有限推导来检验一个表述能否支持目标 claim。

## 什么时候不用

- 超出其范围的任务：完整定理证明、文献综述、实验设计、模拟、统计方法学、论文写作；
- 没有需要表述的科学问题，也没有需要审计的 claim。

## 核心思想

这个 Skill 建立在四条固定核心规则上——问题暂定性、material 承诺问责、相对可识别性、依赖审计——外加一个让结果可被外部审计的 Observable Audit Contract（OAC）。

高层概述与逐条解释见：

- [references/core-principles.md](references/core-principles.md) — 四条 Core 规则，中英双语。
- [references/observable-audit-contract.md](references/observable-audit-contract.md) — OAC 各条目，中英双语。

OAC 不是推理流水线、不是思维链协议、也不是输出模板：它是一份关于"外部审查者必须能在结果中判断什么"的契约。

## 典型输入

一份简短的科学问题陈述，加上目标 claim，以及该 claim 所依据的证据或前提。例如：*"y 已测量而 x 是 latent；校准中 y 与 x 强相关；能否推出在本次实验中 y1 > y2 蕴含 x1 > x2？"*

## 典型输出

按 claim 逐条给出的评估：每个 materially distinct claim 陈述什么、含义是什么，依赖哪些 commitment 和 warrant，哪些是 established、conditional 或 underdetermined，以及什么决定性证据或条件会改变该 status。

## 安装

把 skill 目录复制或链接到某个 skill 库中。推荐结构：

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

在 Claude Code 中，可以把 skill 目录放入（或链接到）用户级 skill 目录。上述布局只是建议，不是平台要求；它不预设 Windows、OneDrive、Claude Code 或任何特定模型提供商。

## 使用

显式激活该 Skill，并提供问题陈述与目标 claim，以及手头的证据或前提。该 Skill 不规定固定流水线；它按问题的实际需要应用其规则，并给出 claim 级的 status 评估。确切的运行行为由 `SKILL.md` 定义。

## 参与贡献

欢迎使用中文或英文提交 issue 和 pull request，无需同时提供双语版本。详见 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。在 GitHub 中选择 **Issues → New issue**，可使用 [Skill 失效](.github/ISSUE_TEMPLATE/skill-failure.yml)或[改进建议](.github/ISSUE_TEMPLATE/improvement.yml)表单，也可提交空白 issue。

采用 [Apache License 2.0](LICENSE)。版本变更见 [CHANGELOG.md](CHANGELOG.md)。

## 验证状态

**v0.1-alpha.1 — 仅完成初步定向验证。**

目前已完成：

- 架构冻结（四条 Core 规则、OAC、范围边界）；
- 一次实现审计；
- 一轮初步定向行为回归（A–E 配对），覆盖：测量/语义 bridge、相对可识别性、局部/全局依赖、数学与经验 status、model-class commitment；
- 在一个已测试环境中（Claude Code harness、DeepSeek API、deepseek-v4-pro），A–E 配对通过了这轮首轮定向回归。

这些是初步的单轮定向测试，不是重复运行的可靠性估计。现有证据不构成：

- 跨模型、跨 harness、跨提供商的正确性证据；
- 广泛的跨领域验证；
- 重复运行稳定性；
- 中英双语行为等价性验证。

## 局限性

这个 Skill 不保证科学结论正确。它不是：

- 自动证明用户理论的工具；
- 自动选择最复杂数学的工具；
- 自动确认物理机制的工具；
- 领域专家的替代品；
- 通用自主科研代理（universal autonomous research agent）。

它审计的是表述与 claim 完整性；它无法提供某个 claim 可能需要的领域知识、warrant 或实验证据。

## 项目结构

```text
physics-to-math-research/
├── SKILL.md                             # 冻结的运行时规范（规范性来源）
├── README.md                            # 英文说明
├── README.zh-CN.md                      # 本文件
└── references/
    ├── core-principles.md               # 四条 Core 规则的解释
    └── observable-audit-contract.md     # OAC 条目的解释
```
