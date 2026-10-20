# physics-to-math-research

**Version / 版本：** `0.2.10` · **Status / 状态：** Experimental / 实验性版本

## Mission / 项目使命

This project helps AI formulate and advance general mathematical questions grounded in physical phenomena and other scientific observations. It emphasizes explicit observations and assumptions, minimal sufficient mathematical structures, checkable conditional derivations, counterexamples, validity conditions, and physical applicability boundaries.

本项目旨在帮助 AI 从物理现象及其他科学观察中发现、构造并推进具有研究价值的一般数学问题。通过明确观测与假设、选择最小足够的数学结构、完成条件性推导，并检查反例、成立条件和物理适用边界，使研究结果可核查、可复现、可质疑。

The project addresses physics and other sciences without depending on a particular device, model or mathematical branch; the aim is a research-relevant question and supported conditional mathematical progress.

项目面向物理及其他科学问题，不依赖特定装置、模型或数学分支；目标是寻找有研究意义的问题，完成当前条件支持的数学成果。

This is project orientation, not an additional runtime rule. “Minimal sufficient” means structure adequate for the question; it does not prescribe a minimization procedure or prefer simplicity over necessary complexity. The Skill does not guarantee new mathematics or establish real physical mechanisms. A stable incremental advantage has not been demonstrated.

这是项目使命说明，不增加运行时规则。“最小足够”指结构足以支持当前问题，不规定结构最小化流程，也不以简单替代必要复杂性。Skill 不保证发现新数学或证实真实物理机制，目前也未建立稳定增量优势。

[SKILL.md](SKILL.md) remains the sole normative runtime source; READMEs, review protocols and tool references are explanatory. For continuous Chinese reading, see [README.zh-CN.md](README.zh-CN.md).

[SKILL.md](SKILL.md) 仍是唯一运行时规范；README、审查协议与工具参考均用于解释和导航。连续中文入口见 [README.zh-CN.md](README.zh-CN.md)。

**[Research Dashboard / Research Observatory — 科研进展与证据看板](https://zwy-research.github.io/physics-to-math-research/)**

Explore completed research audits, mathematical results, Skill validation status and open questions, with evidence traceable to original GitHub records.

展示已完成科研审查、数学成果、Skill 验证状态以及尚未解决的问题；每项证据均可追溯到 GitHub 原始记录。

**Selected Research & Constructive Mathematical Audits / 精选研究与建设性数学审查**

[Reviewed Papers: 1](literature-audits/README.md) / [已审查论文：1 篇](literature-audits/README.md)

We select scientifically important or methodologically instructive studies for focused physical-to-mathematical reconstruction. Each audit explains why the work matters, identifies its original contribution, reconstructs selected mathematical claims, and explores their conditions, limitations and possible generalizations.

An audit is not a pass/fail verdict on the paper or its authors. Limited scope, unresolved scientific questions or untested extensions do not by themselves indicate an error. Genuine mathematical errors or unsupported physical extrapolations must still be recorded with evidence. Authors and researchers may voluntarily contribute clarifications, counterexamples, alternative formulations and new directions; this does not imply their awareness, endorsement or participation.

我们精选具有重要科学贡献或方法论启发价值的研究，独立重建其中关键的物理—数学转换。每篇报告首先说明该研究为什么值得关注及其原创贡献，再记录明确数学命题的复现、成立条件、局限与可能的一般化。

审查不是对论文或作者作通过／失败评定。审查范围有限、科学问题尚未解决或某些推广尚待验证，本身不代表原论文存在错误；真实数学错误或无根据的物理外推仍须按证据记录。欢迎作者与研究者自愿澄清物理前提、检验数学结论、提出反例及拓展新问题，不暗示作者已知晓、认可或参与审查。

The count covers distinct papers accepted through independent, limited-scope review; it does not verify every conclusion or establish incremental Skill capability.

数量仅统计完成限定范围独立审查的不同论文，不代表全部结论已验证，也不构成 Skill 增量能力证明。

Research in progress: **Angioni et al. (2012)** — [Stage A source evidence](cases/angioni-2012/source-evidence.md) and [initial ChatGPT review](cases/angioni-2012/2026-10-15-angioni-2012-source-evidence-review.md) retain their historical attribution. [C1: momentum-transport identifiability](cases/angioni-2012/c1-skill-on-v0.2.7-research-result.md) and [C2: zero-flux density-gradient self-consistency](cases/angioni-2012/c2-skill-on-v0.2.8-research-result.md) are now archived with [ChatGPT conditional mathematical review decisions](cases/angioni-2012/c1-c2-mathematical-review.md): C1 accepted with limitations; C2 accepted. Both read frozen Skill texts through explicit Git blobs; C1 had prior reference-review exposure. No credible Skill OFF control or incremental gain is established. These are conditional mathematical results, not new physical mechanisms or full-paper validation; Reviewed Papers remains 1.

Research in progress: **Fable et al. (2010)** — [Stage A source evidence](cases/fable-2010/source-evidence.md), [complete spectral-response report](cases/fable-2010/skill-on-p1-v0.2.9/research-result.md), and [ChatGPT mathematical review](cases/fable-2010/mathematical-review.md): **ACCEPT WITH LIMITATIONS**. Explicit Git-blob loading of frozen Skill v0.2.9; actual gyrokinetic response ordering and incremental Skill gain are NOT ESTABLISHED. Reviewed Papers remains 1.

## From Science to Mathematics / 从科学问题到数学成果

**Question / 科学问题。** Why does an object warmer than its surroundings gradually cool, and can a simple mathematical relation describe it?

为什么温度高于环境的物体逐渐冷却？能否用简单数学关系描述这个过程？

**Assumptions / 建模假设。** Assume constant ambient temperature $T_{\mathrm{env}}$, approximately uniform internal temperature, and a cooling rate proportional to the temperature difference, with constant $k>0$ and initial temperature $T_0$.

假设环境温度 $T_{\mathrm{env}}$ 恒定，内部温度近似均匀，并采用冷却速率与温差成比例的模型假设；常数 $k>0$，初始温度为 $T_0$。

$$
\frac{dT}{dt}=-k(T-T_{\mathrm{env}}).
$$

**Conditional result / 条件性数学结果。** Under these assumptions, with $T(0)=T_0$:

在这些假设及 $T(0)=T_0$ 下：

$$
T(t)=T_{\mathrm{env}}+(T_0-T_{\mathrm{env}})\exp(-kt).
$$

**Boundary / 适用边界。** This teaching model does not describe every cooling process; a successful fit alone does not prove a physical mechanism. It illustrates mathematical formulation, without prescribing differential equations as the default. See the [two-level cooling explanation](examples/research-delivery-cooling.md) and the preserved [integrated-density demonstration](examples/integrated-density.md). Neither example is capability validation.

本教学模型不适用于所有冷却过程；一次拟合成功本身不能证明物理机制。它展示科学问题如何数学化，不规定默认使用微分方程。详见[双层冷却解释](examples/research-delivery-cooling.md)及完整保留的[密度积分演示](examples/integrated-density.md)。两例均不构成能力验证。

## How to Use / 如何使用

Copy and fill in either example. You do not need to know Core/OAC first; not every task needs a new theorem.

复制并填写任一示例即可。无需预先了解 Core/OAC，也不强制所有任务产生新定理。

```text
Please use the physics-to-math-research Skill.

My scientific observation is: [fill in observations]
Known measurements and constraints: [fill in]
The question I want to study: [fill in]

Formulate the most research-relevant mathematical question supported by the current conditions. Complete feasible mathematical derivations or counterexample analysis, and state validity conditions, failure boundaries and limits of physical interpretation. Do not assume a particular theory or mathematical structure by default.
```

```text
请使用 physics-to-math-research Skill。

我的科学观察是：[填写观察]
已知测量与约束：[填写]
希望研究的问题：[填写]

请构造最有研究价值且当前条件支持的数学问题，完成可行的数学推导或反例分析，并说明成立条件、失败边界与物理解释限制。不要默认特定理论或数学结构。
```

## Research Deliverables / 科研成果表达

Ask for the purpose you need; these examples are not a mandatory sequence:

按需要提出用途；以下示例不是强制流程：

- **Read & Understand / 理解文献与方法：** “Explain the method and its limits; do not start new research.” / “解释方法与局限，不开展新研究。”
- **Research & Derive / 构造和推进数学研究：** “Derive the conditional result supported by these assumptions.” / “推导这些假设支持的条件性结果。”
- **Write & Communicate / 整理已有科研成果：** “Present these established results as an academic paragraph.” / “将这些已有成果整理为学术段落。”

Scientific writing defaults to a clear, concise, evidence-oriented Nature-style approach; please specify Nature Communications, Nature Physics, another journal or a different writing style if preferred. Ordinary explanations are not forced into that style. A substantial delivery can offer accessible and technical accounts with the same evidence and conclusions, without automatically creating two files. See [research delivery guidance](references/research-deliverables.md).

科研写作默认采用 Nature 类期刊的清晰、简洁、证据导向风格；如果需要 Nature Communications、Nature Physics、其他期刊或不同的写作风格，请直接指定。普通解释不强制采用此风格。完整交付可提供证据和结论一致的通俗版与专业版，不自动生成两个文件。详见[科研交付说明](references/research-deliverables.md)。

## Share Your Results / 分享科研结果

Successes, failures, ties and uncertain outcomes are all welcome. Participation is entirely voluntary: no conversation is automatically read or sent; you decide whether and what to submit. Do not submit unauthorized papers, private research data, credentials or sensitive information. Either Chinese or English is sufficient; contributors need not provide both.

欢迎成功、失败、持平及不确定的科研使用结果。反馈完全自愿；不会自动读取或发送对话，是否提交及提交什么由用户自主决定。请勿提交未经授权的论文、私人科研数据、凭证或敏感信息。可使用中文或英文，无需同时提供双语版本。

- [GitHub Issues / 问题反馈](https://github.com/ZWY-research/physics-to-math-research/issues)
- [GitHub Discussions / 科研讨论](https://github.com/ZWY-research/physics-to-math-research/discussions)
- Public contact email / 公开联系邮箱：82787647@qq.com — [Draft feedback email / 撰写反馈邮件](mailto:82787647@qq.com?subject=physics-to-math-research%20feedback)

The email link only prefills the subject `physics-to-math-research feedback`; it does not send email. Suggested feedback: scientific question, Skill version, model/environment, mathematical result, concrete reasons it helped or did not help, and the smallest reproduction information you permit to be public.

邮件链接仅预填主题 `physics-to-math-research feedback`，不会发送邮件。建议包含：科学问题、Skill 版本、模型与环境、数学结果、有益或无益的具体原因，以及允许公开的最小复现信息。

## Research Review / 研究审查

Two independent archives serve different purposes: [evaluation-reports](evaluation-reports/README.md) records Skill behavior evaluations; [literature-audits](literature-audits/README.md) records mathematical reviews of journal papers and preprints under the [literature audit protocol](docs/literature-audit-protocol.md). A publication or successful mathematical review alone is not evidence of incremental Skill capability. Existing reports retain their original versions, conditions and limitations; each paper audit states its completed and unreviewed scope.

两类档案相互独立：[evaluation-reports](evaluation-reports/README.md) 记录 Skill 自身行为评估；[literature-audits](literature-audits/README.md) 按[论文数学审查协议](docs/literature-audit-protocol.md)记录期刊论文及预印本的数学审查。论文发表或数学审查成功本身不是 Skill 增量能力证据。已有报告保留原始版本、测试条件及证据限制；每篇论文审查分别声明已完成和未审查的范围。

## Mathematical Tools / 数学工具

Choose tools by mathematical task, rather than discipline labels; start with the [task-to-tool reference](references/tools/index.md) and optional [Python setup guide](references/tools/python-setup.md). Installing the Skill does not automatically install mathematical software. Use an appropriate tool only when the user's task needs it and its use is authorized. These references are read on demand and do not add runtime rules.

按数学任务而非学科标签选择工具，见[数学任务与工具导航](references/tools/index.md)及按需使用的 [Python 环境配置说明](references/tools/python-setup.md)。安装 Skill 不会自动安装数学软件；只有用户任务需要且已授权时才使用相应工具。这些文档按需参考，不增加运行时规则。

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

$$
y_1 > y_2 \quad\Longrightarrow\quad x_1 > x_2
$$

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

An experimental capability upgrade with an explicit architectural reason and verifiable goals is also allowed. It must pass the available prior correctness regressions and disclose missing coverage, without lowering existing criteria. A published version must not be described as having proven incremental benefit without independent controlled evidence. Every published update to the repository's main branch, including changes to runtime instructions, documentation, tests, references, or research records, requires a project version increment and a CHANGELOG entry. Historical version identifiers and version-specific validation evidence remain unchanged. A version increment alone does not establish a runtime capability improvement.

Candidate failures require reproducible conditions, rule/necessity review and the smallest confirmed repair. Runtime changes require bilingual review, regressions and a [CHANGELOG](CHANGELOG.md) update. v0.2-alpha.0 is an explicitly authorized constructive capability upgrade, not a confirmed failure repair.

**版本治理：**失败驱动修复遵循 Test → Evidence → Failure Review → Minimal Revision → Regression → Version Update。没有可靠 failure 时，不虚构修复理由或新增无必要规则。

也允许基于明确架构理由和可验证能力目标进行实验性能力升级。新版须通过可取得的既有正确性回归，并明确披露缺失的测试覆盖；不得降低原判据。没有独立对照证据，不得宣称发布版本已证明具有增量优势。今后每次正式更新仓库 main 分支，无论修改运行规范、文档、测试、参考文件或科研记录，都必须同步递增项目版本号，并在 CHANGELOG 中记录。历史版本标识及其对应的验证证据保持不变。版本递增本身不代表运行能力提升。

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
│   ├── README.md
│   ├── physics/plasma-and-fusion/README.md
│   ├── 2026-10-09-can-calibration-evidence-identify-material-response.md
│   ├── 2026-10-09-can-linear-stability-rule-out-sustained-tokamak-turbulence.md
│   └── 2026-10-09-can-itg-gradient-scans-distinguish-turbulent-states.md
├── literature-audits/README.md
├── docs/
│   ├── literature-audit-protocol.md
│   └── decisions/2026-10-12-research-onboarding-and-tools.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CONTRIBUTING.zh-CN.md
├── AGENTS.md
├── references/
│   ├── core-principles.md
│   ├── observable-audit-contract.md
│   ├── mathematical-verification.md
│   ├── disciplines/physics.md
│   └── tools/
│       ├── index.md
│       └── python-setup.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── skill-failure.yml
    │   ├── improvement.yml
    │   └── config.yml
    └── PULL_REQUEST_TEMPLATE.md
```

## Research Inspirations & Attribution

This project studies publicly available mathematical research and formalization practices from OpenAI Math, Mathlib4 and Physlib. The initial review covers documentation, artifact organization and verification conventions. It has not established independent replication of selected proofs, adoption of their reasoning methods, or measurable improvements to this Skill. These are external research references, not collaborators or endorsers.

[OpenAI Math](https://github.com/openai/math) · [Mathlib4](https://github.com/leanprover-community/mathlib4) · [Physlib](https://github.com/leanprover-community/physlib).

[Sources, licenses and review limits / 来源、许可证与查阅限制](docs/research-method-sources.md) · [Full report reader / 站内全文阅读](https://zwy-research.github.io/physics-to-math-research/skill-evaluations/).
