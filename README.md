# physics-to-math-research

**Version / 版本：** `0.2-alpha.0`

**Status / 状态：** Public alpha / 公开 Alpha 测试版

A bilingual Skill for constructive scientific-to-mathematical formulation, task-relevant derivation, and claim-integrity auditing.

一个面向建设性科学问题数学化、任务相关推导与 claim 完整性审查的中英双语 Skill。

> Before solving a scientific problem mathematically, have we formulated the right mathematical problem, and does the resulting mathematics actually support the scientific claim being made?
>
> 在开始用数学求解科学问题之前，我们是否构造了正确的数学问题？得到的数学结果是否真的支持研究者提出的科学 claim？

## Overview / 项目简介

Use this Skill to formulate mathematical questions from scientific observations, complete feasible conditional derivations, and examine the bridge from mathematical results to physical conclusions. Alpha users are invited to try real problems and report reproducible failures; current validation is limited.

使用本 Skill 从科学观察构造数学问题、完成可行的条件性推导，并检查数学结果与物理结论之间的衔接。欢迎 alpha 用户用真实问题试用并报告可复现的失败；当前验证仍然有限。

> Documentation is explanatory. [SKILL.md](SKILL.md) is the single normative runtime source for this version. If documentation conflicts with it, `SKILL.md` prevails.
>
> 文档用于解释和导航。[SKILL.md](SKILL.md) 是当前版本唯一的运行时规范来源。如果文档与其冲突，以 `SKILL.md` 为准。

For uninterrupted Chinese reading, see [README.zh-CN.md](README.zh-CN.md). Both views explain the same Skill.

如偏好连续中文阅读，可使用 [README.zh-CN.md](README.zh-CN.md)。两个阅读入口解释的是同一个 Skill。

## Discipline adapters (experimental) / 学科适配层（实验性）

The canonical [SKILL.md](SKILL.md) remains the single general research protocol. Domain guidance is optional supporting material, not a separate Skill or a default mathematical model.

现行 [SKILL.md](SKILL.md) 仍是统一科研协议。领域指导是可选支持材料，不是独立 Skill，也不规定默认数学模型。

The first experimental pilot is [Physics](references/disciplines/physics.md), governed by the [Discipline Adapter Contract](docs/discipline-adapter-contract.md). It may be explicitly supplied alongside the Skill when physics-specific distinctions materially affect the task. It is not automatically loaded by the current runtime protocol.

首个实验性试点为[物理学适配层](references/disciplines/physics.md)，受[学科适配契约](docs/discipline-adapter-contract.md)约束。只有在物理学特有的语义或约束实质影响任务时才按需显式提供；当前运行协议不会自动加载。

This is an unvalidated extension. [Contrast fixtures](tests/physics-adapter-contrast.md) are specified but not executed. No demonstrated incremental benefit is claimed.

这是尚未验证的扩展。已制定[对照测试](tests/physics-adapter-contrast.md)，但尚未执行，不宣称已获得增量收益。

## What this Skill does / 这个 Skill 做什么

- Construct a precise mathematical question from scientific observations or constraints, or audit an existing formulation/claim.
- Complete feasible task-relevant derivations under explicit premises, delivering checkable results and load-bearing conditions.
- Check material commitments, semantic correspondence and warrants; separate mathematical consequences, physical applicability and unverified mechanisms.
- Keep provisional models exploratory; unresolved physical identification alone does not block feasible conditional mathematics.
- Perform authorized, available tool checks when they can materially affect a consequential result; see [verification limits](references/mathematical-verification.md).

Not every task needs a new formula or theorem. Stop when the deliverable and conditions reach the support of available information, or a specific blocker prevents justified progress; do not extend into an entire research programme.

- 从科学观察或约束构造明确的数学问题，也可审查已有 formulation/claim。
- 完成明确前提支持、能推进当前研究问题的任务相关推导，交付可核查的数学成果及关键条件。
- 检查实质性承诺、语义对应与推理依据，区分数学后果、物理适用性及未经验证的机制解释。
- 暂定模型保持为探索性假设；物理机制未识别本身不阻断可行条件性数学工作。
- 当已授权且可用的工具核查能够实质影响关键结果时实际执行；详见[数学核查边界](references/mathematical-verification.md)。

不要求每项任务产生新公式或定理。成果及关键条件达到当前信息支持程度，或具体障碍阻止有依据推进时停止；不扩展为完整研究计划。

## Why it exists / 为什么建立这个 Skill

Scientific work can fail at the boundary between phenomena and mathematics:

科研工作可能在现象与数学之间的转换环节出现以下错误：

- Correlation is reported as causation. / 把相关性报告为因果关系。
- A proxy is treated as the latent quantity it represents. / 把 proxy 当作它所代表的潜在真实量。
- A model-class-relative result becomes an unrestricted physical statement. / 把模型类别内部成立的结果升级为不受限制的物理结论。
- A mathematical theorem is reported as an empirical finding. / 把数学定理报告为经验事实。

Mathematical elegance or rigor does not by itself guarantee scientific correctness. The Skill aims to reduce these specific formulation and claim-integrity failures.

数学上的漂亮或严格本身并不保证科学正确性。本 Skill 旨在减少这些具体的表述与 claim 完整性失败。

## When to use it / 什么时候使用

- Open scientific-to-mathematical formulation, existing formulation/claim audits, or feasible conditional derivation for the current task.
- No pre-specified target claim is required. Respect audit-only requests without forcing new modeling.

- 开放式科学数学化、已有 formulation/claim 审查或当前任务所需的可行条件性推导。
- 用户无需预先给出 target claim。仅要求审查时，尊重原任务，不强制重新建模。

## When not to use it / 什么时候不适合使用

- Tasks primarily requesting unrestricted theorem-proving services, symbolic algebra systems, causal discovery, complete statistical methodology, literature review, simulation, experiment optimization or paper writing. Feasible conditional derivation for the current formulation task remains in scope.
- Tasks with no scientific-to-mathematical question, task-relevant derivation or formulation/claim to audit.

- 以无限制定理证明服务、符号代数系统、因果发现、完整统计方法学、文献综述、模拟、实验优化或论文写作为主要目的的任务。当前数学化研究所需的可行条件性推导仍在范围内。
- 没有科学数学化问题、任务相关推导或待审 formulation/claim 的任务。

## Core idea / 核心思想

Four frozen Core rules guide the Skill:

四条冻结的 Core 规则指导本 Skill：

1. **Problem provisionality / 问题暂定性**
2. **Material commitment accountability / 实质承诺可追责性**
3. **Relative identifiability / 相对可识别性**
4. **Dependency audit / 依赖条件审查**

See the bilingual [Core explanations](references/core-principles.md) and [Observable Audit Contract (OAC)](references/observable-audit-contract.md).

详见双语的 [Core 解释](references/core-principles.md)和[可观察审计契约（OAC）](references/observable-audit-contract.md)。

The OAC is an external auditability contract: it describes what a reviewer must be able to judge from relevant results. It is not a reasoning pipeline, a chain-of-thought protocol, or a fixed answer template.

OAC 是一个外部可审查性契约，说明审查者应能从相关结果中判断什么。它不是推理流水线、思维链协议或固定答案模板。

## Typical input / 典型输入

Provide scientific observations, research constraints or an existing formulation/claim, with available evidence or premises; an open task need not start with a target claim. For example, suppose `y` is measured and `x` is latent, and calibration data show strong correlation. Does the following implication hold in the present experiment?

提供科学观察、研究约束或已有 formulation/claim，以及证据或前提；开放任务无需先给 target claim。例如，假设 `y` 是测量量，`x` 是潜在量，标定数据中二者高度相关。以下推断在当前实验中是否成立？

$$y_1 > y_2 \quad\Longrightarrow\quad x_1 > x_2$$

## Typical output / 典型输出

The task determines the deliverable: a precise mathematical question and checkable result, with semantic correspondence, material premises, load-bearing conditions and physical applicability boundaries. An audit-only request is respected without forcing new modeling.

按任务交付明确的数学问题与可核查成果，说明语义对应、实质前提、关键条件与物理适用边界。仅要求 claim 审查时尊重该任务，不强制重新建模。

Relevant distinctions may include observation, assumption, model choice, mathematical consequence, empirical applicability, physical interpretation, and an unresolved discriminator. These are examples, not a mandatory fixed ontology or output template.

相关区分可能包括观测、假设、模型选择、数学结果、经验适用性、物理解释，以及尚缺失的判别证据。这些是示例，不是强制的固定 ontology 或输出模板。

## Installation / 安装

Copy or link the Skill directory into a skill library. The recommended installation layout remains:

将 Skill 目录复制或链接到 skill 库中。推荐安装目录结构保持如下：

```text
Multi_Skills/
└── physics-to-math-research/
    ├── SKILL.md
    ├── README.md
    ├── README.zh-CN.md
    └── references/
        ├── core-principles.md
        ├── observable-audit-contract.md
        └── mathematical-verification.md
```

Claude Code is one installation example: the directory can be placed in or linked into its user-level skill directory. Other agents may explicitly load `SKILL.md` where their environment supports this form of instruction use. This is not a claim of automatic compatibility; the layout assumes no particular operating system or model provider.

Claude Code 是一个安装示例：可将目录放入或链接到其用户级 skill 目录。对于其他 Agent，如果环境支持相应指令加载方式，可以显式加载 `SKILL.md`。这不表示自动兼容；该目录结构不预设特定操作系统或模型提供商。

## Usage / 使用方式

- Explicitly activate or load the Skill. / 显式激活或加载 Skill。
- Provide scientific observations, a research question or a claim to audit, with available evidence or premises. / 提供科学观察、研究问题或待审 claim，以及已有证据或前提。
- The Skill applies its rules to what the problem requires; no fixed reasoning pipeline is imposed. / Skill 按问题实际需要应用规则，不强制固定推理流水线。
- `SKILL.md` defines exact runtime behavior. / `SKILL.md` 定义准确的运行时行为。

## Contributing / 参与贡献

**Bring a real scientific problem. You do not need Core/OAC terminology to participate.**

**带一个真实科学问题来。参与无需先理解 Core/OAC 术语。**

Start in [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) → [Research Problems](https://github.com/ZWY-research/physics-to-math-research/discussions/new?category=general) (currently General). Report reproducible failures in [Issues](https://github.com/ZWY-research/physics-to-math-research/issues/new/choose), preserve mature cases in the [Casebook](cases/README.md), and see [CONTRIBUTING.md](CONTRIBUTING.md) or [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md). Either Chinese or English is sufficient.

从 [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) → [Research Problems 科学问题](https://github.com/ZWY-research/physics-to-math-research/discussions/new?category=general)（目前为 General 分类）开始。在 [Issues](https://github.com/ZWY-research/physics-to-math-research/issues/new/choose) 报告可复现 failure，在 [Casebook](cases/README.md) 沉淀成熟案例；详见 [CONTRIBUTING.md](CONTRIBUTING.md) 或 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。可使用中文或英文。

**Issues and pull requests are welcome in either Chinese or English. Contributors do not need to provide both languages.**

**Issue 和 Pull Request 均可使用中文或英文提交，贡献者无需同时提供两种语言。**

**The most valuable contribution at this stage is a real, reproducible scientific failure case.**

**现阶段最有价值的贡献，是一个真实、可复现的科学问题失败案例。**

We welcome real scientific problems, reproducible Skill failures, domain-specific edge cases, excessive skepticism, premature stopping, unsupported claim strengthening, and methodology or documentation improvements. You do not need to know Core/OAC terminology to participate.

欢迎分享真实科学问题、可复现的 Skill 失败、特定学科边界案例、过度怀疑、过早停止、无依据的 claim 升级，以及方法论或文档改进。参与不要求先理解 Core/OAC 术语。

See [CONTRIBUTING.md](CONTRIBUTING.md) or [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md). Open the [issue chooser](https://github.com/ZWY-research/physics-to-math-research/issues/new/choose) for a Skill failure, improvement proposal, or blank issue. Maintainers may synchronize languages; material normative Skill changes require bilingual semantic-equivalence review before merge.

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 或 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。打开 [Issue 入口](https://github.com/ZWY-research/physics-to-math-research/issues/new/choose)，可报告 Skill 失效、提出改进建议或提交空白 issue。维护者可协助同步语言；Skill 的实质性规范变更须在合并前完成双语语义等价性审查。

Licensed under [Apache License 2.0](LICENSE). Version changes are listed in [CHANGELOG.md](CHANGELOG.md).

采用 [Apache License 2.0](LICENSE)。版本变更见 [CHANGELOG.md](CHANGELOG.md)。

## Research Applications & Validation / 科研应用与验证

See the [Research Applications & Validation register](RESEARCH_APPLICATIONS.md) for research problems, author-confirmed publications using the Skill, and capability evidence. Background references are recorded separately. Use or publication alone does not establish validation; the HL-3 candidate is currently `planned`.

查看[科研应用与验证登记表](RESEARCH_APPLICATIONS.md)，持续记录科研问题、经作者确认使用 Skill 的论文及能力证据。背景参考文献单独登记。使用或发表本身不构成验证；HL-3 候选目前为 `planned`（计划中）。

## Evaluation Reports & Skill Improvement / 测试与能力改进档案

The [evaluation reports](evaluation-reports/) archive records actual capability tests, ON/OFF comparisons, mathematical failures, paired regressions, behavior before/after repairs, and results with no reliable defect. Each test has one independent Markdown report; evidence already publicly accessible elsewhere is linked rather than duplicated. Incomplete public evidence must state reproduction limits.

[测试档案](evaluation-reports/)记录实际能力测试、ON/OFF 比较、数学失败、成对回归、修复前后行为及未发现可靠缺陷的结果。每项测试对应一个独立 Markdown 报告；已有可公开访问的完整证据优先链接，不重复维护。公开证据不完整时须说明复现限制。

Report filenames use `YYYY-MM-DD-[scientific-topic]-[research-question].md`: the actual completion date and a short lowercase, hyphenated scientific question, rather than the test method. Test IDs, sources, methods, and Skill versions stay inside each report.

报告文件名采用 `YYYY-MM-DD-[scientific-topic]-[research-question].md`：使用实际完成日期和简短的小写英文连字符科学问题名称，不以测试方法为主要名称。测试 ID、文献、方法及 Skill 版本保留在报告内部。

Start with [Can calibration evidence identify material response? / 标定证据能否识别材料响应？](evaluation-reports/2026-10-09-can-calibration-evidence-identify-material-response.md): v0.1-alpha.2, GPT-6.1 Sol / High; both conditions completed the warranted derivations, with no substantive ON/OFF advantage or reliable Skill failure observed. Outcomes may be success, failure, tie, or uncertainty. Every report ends with an optimization decision; a test alone does not validate overall effectiveness.

首项为[标定证据能否识别材料响应？](evaluation-reports/2026-10-09-can-calibration-evidence-identify-material-response.md)：v0.1-alpha.2，GPT-6.1 Sol / High；两种条件均完成有依据的推导，未观察到实质 ON/OFF 优劣或可靠 Skill failure。结果可以是成功、失败、持平或不确定。每份报告须给出最终优化决策；测试本身不构成整体有效性验证。

The [tokamak turbulence evaluation](evaluation-reports/2026-10-09-can-linear-stability-rule-out-sustained-tokamak-turbulence.md) asks whether linear stability can rule out sustained finite-amplitude turbulence. One ON/OFF pair was indistinguishable on all seven review dimensions; incremental benefit was not established. Both answers share a gap in explicit small-perturbation nonlinear stability conditions.

[托卡马克湍流测试](evaluation-reports/2026-10-09-can-linear-stability-rule-out-sustained-tokamak-turbulence.md)检验线性稳定性能否排除有限幅持续湍流。单次 ON/OFF 比较的七维评价均无法区分，未建立增量优势；两答共同缺少显式的小扰动非线性稳定条件分析。

The [ITG gradient-scan evaluation](evaluation-reports/2026-10-09-can-itg-gradient-scans-distinguish-turbulent-states.md) compares open-ended problem discovery and mathematical formulation. ON was slightly better on claim validity; the other six dimensions were indistinguishable. This weak signal does not establish reliable incremental benefit; ON added 3333 input tokens. No core or version change.

[ITG 梯度扫描测试](evaluation-reports/2026-10-09-can-itg-gradient-scans-distinguish-turbulent-states.md)比较开放式问题发现与数学构造：ON 在 claim validity 略优，其余六维无法区分；弱正向信号尚未建立可靠增量价值，额外输入3333 tokens。不修改核心或版本。

**Evidence Attribution:** Test reports must distinguish evidence produced by independent Skill ON/OFF runs from results obtained through subsequent human guidance, additional tools, or domain-specific workflows. Without independent evidence, subsequent research outcomes must not be attributed to the Skill's incremental contribution.

**Evidence Attribution / 证据归因：** 测试报告必须区分独立 Skill ON/OFF 运行产生的证据，以及后续人工指导、额外工具或领域专项流程得到的结果。没有独立证据时，不得将后续科研成果归因于 Skill 的增量作用。

**Version governance:** failure-driven repairs follow Test → Evidence → Failure Review → Minimal Revision → Regression → Version Update. Without a reliable failure, do not invent a repair rationale or unnecessary rules.

An experimental capability upgrade with an explicit architectural reason and verifiable goals is also allowed. It must pass the available prior correctness regressions and disclose missing coverage, without lowering existing criteria. A published version must not be described as having proven incremental benefit without independent controlled evidence. Actual runtime changes warrant version updates; reports or explanatory corrections alone do not.

Candidate failures require reproducible conditions, rule/necessity review and the smallest confirmed repair. Runtime changes require bilingual review, regressions and a [CHANGELOG](CHANGELOG.md) update. v0.2-alpha.0 is an explicitly authorized constructive capability upgrade, not a confirmed failure repair.

**版本治理：**失败驱动修复遵循 Test → Evidence → Failure Review → Minimal Revision → Regression → Version Update。没有可靠 failure 时，不虚构修复理由或新增无必要规则。

也允许基于明确架构理由和可验证能力目标进行实验性能力升级。新版须通过可取得的既有正确性回归，并明确披露缺失的测试覆盖；不得降低原判据。没有独立对照证据，不得宣称发布版本已证明具有增量优势。实际运行行为修改才触发版本更新；增加报告或修改解释文档本身不触发。

候选 failure 须保存可复现条件、核对现有规则及任务必要性，确认后优先最小修复。运行变更均须进行双语语义检查、回归与 [CHANGELOG](CHANGELOG.md) 更新。此次 v0.2-alpha.0 是明确授权的建设性能力升级，不是已确认 failure repair。

## Validation status / 当前验证状态

### `v0.2-alpha.0` — experimental capability upgrade / 实验性能力升级

The available three historical cases and all six new paired branches passed; YAML/reference validation and native discovery/full loading passed. Older Batch1 inputs are missing, so its historical PASS is not a current rerun. Two held-out B/C/D tasks found no necessary-result advantage for D or reliable stable incremental benefit. Model tool execution was blocked in the nested smoke environment. See the [validation record](docs/v0.2-alpha.0-validation.md) for results, costs and limits.

可取得的三项历史案例及新增三组共六个分支通过；YAML/参考验证、原生发现与完整加载通过。较早Batch1输入缺失，其历史PASS不是本次重跑。两个留出B/C/D任务未发现D的必要成果优势或可靠稳定增量收益；嵌套smoke环境阻挡模型工具执行。详见[验证记录](docs/v0.2-alpha.0-validation.md)中的结果、成本与限制。

### `v0.1-alpha.1` — historical evidence / 历史证据

Architecture freeze, an implementation audit, and the initial A–E targeted regression were completed. A–E covered measurement/semantic bridges, relative identifiability, local/global dependencies, mathematical versus empirical status, and model-class commitments. They passed in one tested environment: Claude Code, DeepSeek API, `deepseek-v4-pro`.

已完成架构冻结、一次实现审计及首轮 A–E 定向回归。A–E 覆盖测量与语义衔接、相对可识别性、局部与全局依赖、数学与经验状态，以及模型类别承诺。在一个测试环境中通过：Claude Code、DeepSeek API、`deepseek-v4-pro`。

### Initial Value Benchmark / 初始 Value Benchmark

Five natural scientific tasks compared Skill ON/OFF responses through blind evaluation. The Skill was preferred overall on four of five tasks; no epistemic-correctness loss was observed in that small benchmark. Research usefulness exposed a weakness on Task 01, the plasma-transport problem.

五个自然科学任务通过盲评比较 Skill ON/OFF 回答。总体偏好中 Skill 在五个任务中的四个获得优选；该小规模 benchmark 未观察到认识论正确性损失。科研实用性评估在 Task 01（等离子体输运问题）暴露了一个弱点。

These alpha.1 results used only five tasks, one tested model/environment, single runs per condition, and one blind evaluator. They are preliminary, version-specific evidence, not general validation.

这些 alpha.1 结果仅涉及五个任务、一个测试模型与环境、每个条件单次运行，以及一位盲评者。它们是初步且与版本绑定的证据，不是普适验证。

### Failure-driven revision / 基于失败案例的修订

Task 01's usefulness weakness was investigated and recurred in two targeted Codex replication pairs. These used a different model/harness from the original benchmark; they do not establish same-model reliability or a causal wording mechanism. The evidence motivated a narrow stopping-guidance clarification, not a Core/OAC redesign.

Task 01 的实用性弱点经针对性分析后，在两组 Codex 定向复现配对中再次出现。复现所用模型与运行工具不同于原 benchmark，不能证明同模型可靠性或某句措辞的因果机制。这些证据推动了停止指引的窄范围澄清，而非 Core/OAC 重设计。

### `v0.1-alpha.2` — targeted repair / 针对性修复

That historical version contains the repair. The accepted candidate passed targeted pre-commit checks for warranted continuation, stopping with insufficient evidence, natural completion of a mathematical-only task, and Chinese–English material semantic equivalence. There was one run per behavioral case; these checks are not reliability estimates.

该历史版本包含该修复。被接受的候选版本通过了针对性 pre-commit 检查：有依据的继续推进、证据不足时停止、纯数学任务完成后自然停止，以及中英文实质语义等价性。每个行为案例运行一次；这些检查不是可靠性估计。

Current evidence does **not** establish universal scientific correctness, cross-model reliability, broad cross-domain generality, repeated-run stability, or full Chinese–English behavioral equivalence across arbitrary tasks.

现有证据**不能证明**普适科学正确性、跨模型可靠性、广泛跨学科普适性、重复运行稳定性，或任意任务上的完整中英行为等价性。

## Limitations / 局限性

The Skill cannot supply missing domain knowledge, empirical evidence, or warrants, and cannot guarantee scientific truth. It does not automatically prove a user's theory, confirm a physical mechanism, or select the most complex mathematics. It does not replace domain experts or act as a universal autonomous research agent.

Skill 无法凭空提供缺失的领域知识、经验证据或依据，也不能保证科学真理。它不会自动证明用户的理论、确认物理机制或选择最复杂的数学。它不能替代领域专家，也不是通用自主科研 Agent。

## Project structure / 项目结构

The public repository contains the runtime specification, explanatory documents, and contribution templates below. None of these documents adds runtime rules beyond `SKILL.md`.

公开仓库包含以下运行时规范、解释文档和贡献模板。任何文档都不在 `SKILL.md` 之外增加运行规则。

```text
physics-to-math-research/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── RESEARCH_APPLICATIONS.md
├── evaluation-reports/
│   ├── 2026-10-09-can-calibration-evidence-identify-material-response.md
│   ├── 2026-10-09-can-linear-stability-rule-out-sustained-tokamak-turbulence.md
│   └── 2026-10-09-can-itg-gradient-scans-distinguish-turbulent-states.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CONTRIBUTING.zh-CN.md
├── AGENTS.md
├── references/
│   ├── core-principles.md
│   ├── observable-audit-contract.md
│   └── mathematical-verification.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── skill-failure.yml
    │   ├── improvement.yml
    │   └── config.yml
    └── PULL_REQUEST_TEMPLATE.md
```
