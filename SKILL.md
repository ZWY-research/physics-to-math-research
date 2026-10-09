---
name: physics-to-math-research
description: >-
  Formulate scientific or physical observations as mathematical research questions,
  develop task-relevant conditional results, and audit mathematical claims and
  physical applicability. Not an unrestricted theorem-proving or general research service.
metadata:
  version: "0.2-alpha.0"
---

# physics-to-math-research — v0.2-alpha.0

## Purpose & Scope / 目的与范围

Constructive scientific-to-mathematical formulation, task-relevant derivation, and claim-integrity audit.
建设性的科学问题数学化、任务相关推导与 claim 完整性审查。

Formulate questions grounded in scientific observations or constraints, define the mathematical objects and their physical correspondence, and complete feasible task-relevant derivations under explicit premises. Check results through their load-bearing conditions and relevant counterexamples; distinguish mathematical consequences from unverified physical interpretations.
根据科学观察或约束构造问题，定义数学对象及其物理对应，并在明确前提下完成可行的任务相关推导。通过关键成立条件与相关反例核查结果，区分数学后果与未经验证的物理解释。

This is not an unrestricted theorem-proving service, symbolic algebra system, causal discovery system, complete statistical methodology framework, literature review workflow, simulation framework, experiment optimizer, universal scientific ontology, publication-writing system, or autonomous research agent. Conditional propositions needed for the current mathematical research task may be derived when reasonably feasible; this does not authorize solving an entire research programme.
本 Skill 不是无限制的定理证明服务、符号代数系统、因果发现系统、完整统计方法学框架、文献综述流程、模拟框架、实验优化器、通用科学本体、论文写作系统或自主科研 Agent。允许合理可行地推导当前数学化研究任务需要的条件性命题；这不授权完成整个研究计划。

## When to use / 何时使用

- Formulate an open mathematical research question from scientific observations or constraints; the user need not supply a target claim. 根据科学观察或约束构造开放式数学研究问题；用户无需预先提供 target claim。
- Audit an existing formulation or claim, respecting an audit-only request rather than forcing new modeling. 审查已有 formulation 或 claim；尊重仅审查的任务，不强制重新建模。
- Derive a feasible conditional mathematical result that advances the current scientific-to-mathematical task. 推导能够推进当前科学数学化任务的可行条件性数学结果。

## When not to use / 何时不用

- The task primarily asks for one of the excluded unrestricted services above. 任务主要要求上述排除的无限制服务之一。
- There is no scientific-to-mathematical question, task-relevant derivation, or formulation/claim to audit. 没有科学数学化问题、任务相关推导或需要审查的 formulation/claim。

## Core Rules / 核心规则

The four rules below are fixed: do not add, remove, or merge. 以下四条规则已冻结：不得增加、删除或合并。

### Core 1 — Problem provisionality / 问题暂定性

Treat the initial problem statement, target claim, and interpretation of its quantities as provisional — not as correct premises — until checked for material mis-specification.
初始问题、目标 claim 及其 quantity 的解释，在检查是否存在会实质改变结论的问题错设（material mis-specification）之前，只能作为暂定表述，不能直接视为正确前提。

### Core 2 — Material commitment accountability / 实质性承诺问责

Every material claim-relevant modeling commitment, semantic mapping, or inferential step requires an appropriate explicit warrant.
任何会实质影响目标 claim 的建模承诺、语义映射或推理步骤，都必须具有适当且明确的依据（warrant）。

A commitment, mapping, or inference is material if changing it could change the claim's meaning, truth/status, scope, support strength, or identifiability. Notation substitutions, equivalent algebraic transforms, and unit conversions are not material and create no audit burden.
如果改变某个 commitment、mapping 或 inference 可能改变 claim 的 meaning、truth/status、scope、support strength 或 identifiability，则它是 material。普通的 notation substitution、等价代数变换、单位转换不构成审计负担。

### Core 3 — Relative identifiability / 相对可识别性

Do not select among stated admissible alternatives when available evidence cannot distinguish alternatives that imply materially different answers to the target claim. Any identification claim is relative to the stated admissible class, unless that class is warranted as exhaustive for the stated claim and scope.
当现有证据无法区分若干 admissible alternatives，而这些 alternatives 对目标 claim 给出实质不同答案时，不得任意选择其中一个。任何"已识别""唯一识别"的结论都只能相对于明确声明的 admissible class 成立，除非有适当依据表明该 class 对当前 claim 和 scope 已经足够穷尽。

This does not license unlimited skepticism: do not refuse identification merely because unknown models are always logically possible; further review is needed only with a specific, relevant reason to suspect an omitted alternative.
同时不要走向无限怀疑：不要因为逻辑上永远可能存在未知模型，就永远拒绝 identification；只有存在具体、相关的遗漏 alternative 理由时才需要进一步审查。

### Core 4 — Dependency audit / 依赖审计

Audit the load-bearing prerequisites of the inference, mathematical operation, or interpretive step actually used — not a fixed rigor checklist.
审查实际使用的推理、数学操作或解释步骤真正依赖的关键成立条件，而不是机械执行固定的数学严谨性 checklist。

- derivative → check the differentiability the conclusion actually needs。使用 derivative → 检查结论真正需要的 differentiability。
- inverse → check the relevant existence / uniqueness / conditioning。使用 inverse → 检查相关 existence / uniqueness / conditioning。
- invariance → check the allowed transformations。声称 invariance → 检查允许的 transformation。
- do not mechanically check compactness, topology, smoothness, bifurcation for every problem。不要对每个问题机械检查 compactness、topology、smoothness、bifurcation。

## Execution Guidance / 执行指引

Not a fixed pipeline; apply the Cores to what the problem actually requires.
不是固定流水线；按问题实际所需应用四条 Core。

### Task-relevant derivation / 任务相关推导

**Productive Mathematical Progress / 建设性数学推进**

For open scientific-to-mathematical tasks, formulate a precise question grounded in the stated observations or constraints. When explicit, task-relevant premises permit a feasible step that materially advances the question, complete it to a checkable mathematical result rather than merely recommending it. Provisional hypotheses are allowed, but their mathematical consequences must not be presented as established physical facts.
对于开放式科学问题的数学化任务，应根据已有观察或约束构造明确的数学问题。当明确且与任务相关的前提允许完成能够实质推进该问题的数学步骤时，应实际完成至可核查的数学结果，而非仅建议后续分析。允许暂定假设，但不得将其数学后果当作已经证实的物理事实。

Results may include a conditional theorem, bound, counterexample, non-identifiability or impossibility result, useful computational construction, or testable difference between models. These are possibilities, not a checklist; not every task needs a new formula or theorem. A provisional premise must have a stated task-relevant basis and remain an exploratory assumption, not silently become an empirical warrant (Core 2).
成果可包括条件性定理、数学界、反例、不可识别性或不可能性结果、有用途的计算构造或可检验的模型间差异。这些是可能形式，不是 checklist；并非每项任务都需要新公式或定理。暂定前提须有明确的任务相关依据，并保持为探索性假设，不能静默变成经验依据（Core 2）。

### Mathematical structure / 数学结构

"Minimal sufficient mathematical structure" is not a Core rule. Use structures with clear definitions, explicit relations to observations, research quantities or constraints, and a practical contribution to the current question. Do not introduce functions, spaces, operators or equations merely to look mathematical. Retain warranted competing formulations and necessary complex structure.
"Minimal sufficient mathematical structure" 不是 Core 规则。采用定义清楚、与观察、研究量或约束有明确关系、并对当前问题有实际贡献的结构。不得仅为显得数学化而引入函数、空间、算子或方程。保留有依据的竞争性 formulation 及必要的复杂结构。

### Counterexamples / 反例

No exhaustive counterexample search. When relevant, test supplied or newly formulated propositions with domain-compatible witnesses or alternatives that can change the conclusion or expose its dependencies. Do not invent irrelevant alternatives to manufacture skepticism.
不作穷尽式反例搜索。必要时用与问题域相容、能改变结论或暴露依赖的见证或替代解释，检查给定或新构造的命题。不得虚构不相关备选方案以制造怀疑。

### Conditional verification / 条件性核查

When an authorized, available, reliable tool can materially check a load-bearing mathematical result and the check could change the current conclusion, perform it. Do not treat numerical sampling as a general proof, invent unavailable verification, or use tool-call frequency as a capability metric. For verification limits when relevant, see [references/mathematical-verification.md](references/mathematical-verification.md).
当已授权、可用且可靠的工具能够实质性核查关键数学结果，且核查可能改变当前结论时，应实际执行。不得将数值抽样当作一般性证明、虚构不可执行的验证，或以工具调用频率衡量能力。需要时参见[数学核查边界](references/mathematical-verification.md)。

### Prohibited defaults / 禁止的默认结构

Do not impose as defaults or mandatory structures: 不得作为默认或强制结构引入：

1. a state / parameter / observable ontology 本体三分
2. equilibrium equations 平衡方程
3. the implicit function theorem 隐函数定理
4. bifurcation analysis 分岔分析
5. statistics / ML 统计 / 机器学习
6. causal models 因果模型
7. a measurement model of the form y = M(x) + ε 形如 y = M(x) + ε 的测量模型
8. warrant graphs warrant 图
9. a linear reasoning pipeline 线性推理流水线
10. output of full internal reasoning / chain of thought 输出完整内部推理 / 思维链
11. a search for a "minimal mathematical structure" 寻找"最小数学结构"
12. an exhaustive counterexample search 穷尽式反例搜索
13. a default "underdetermined" verdict for all problems 默认所有问题均 underdetermined
14. complex mathematics preferred over simple formulations 默认复杂数学优于简单 formulation
15. simple formulations preferred over necessary complex structure 默认简单 formulation 优于必要的复杂结构

## Observable Audit Requirements / 可观察审计要求

The Observable Audit Contract (OAC) is an external auditability contract for the result — not a reasoning pipeline, not a chain-of-thought protocol, not a fixed output template. When relevant, an external reviewer must be able to judge:
OAC 是对结果的 external auditability contract——不是推理流水线，不是 chain-of-thought 协议，不是固定输出模板。当相关时，外部 reviewer 必须能够判断：

1. **Claim identity / claim 身份** — which materially distinct claim is examined, its scope, and whether the original claim was kept, modified, weakened, split, or rejected. Do not force one status onto the whole problem. 审查的是哪个 materially distinct claim、scope 是什么、原始 claim 是否被保留 / 修改 / 弱化 / 拆分 / 拒绝。不要给整个问题强行分配单一 status。
2. **Formulation and semantic correspondence / 形式化与语义对应** — what the mathematical objects represent, and their material correspondence to observables, theoretical quantities, proxies, latent quantities, controls. Do not force a state / parameter / observable trichotomy or a universal ontology. 数学对象表示什么，以及它们与 observable、理论量、proxy、latent quantity、control 的 material correspondence。不要强制 state / parameter / observable 三分法或 universal ontology。
3. **Material commitments and warrants / material 承诺与依据** — which commitments / mappings / inferences are material and what appropriate warrant each has. No closed warrant ontology: definitions, evidence, assumptions, mathematical results, experimental design, calibration, constraints — whatever fits the claim. 哪些 commitments / mappings / inferences 是 material、各自有什么 appropriate warrant。不要建立封闭 warrant ontology：warrant 可来自定义、证据、假设、数学结果、实验设计、校准、约束等，只要适合 claim。
4. **Load-bearing dependencies / 关键依赖** — which conditions the conclusion actually depends on (not a full assumption inventory); the test is whether removing or changing a condition could invalidate the claim or change its status. 当前结论真正依赖哪些条件（不要列 assumptions 大全）；检验标准：移除或改变某条件，claim 是否可能失效或改变 status。
5. **Alternatives and identification boundary / 替代方案与识别边界** — which admissible class the identification is relative to, which relevant alternatives remain unexcluded, and whether a restricted candidate set has been upgraded to unrestricted physical truth. If no specific relevant alternative exists, do not invent one. identification 相对于哪个 admissible class、哪些 relevant alternatives 尚未排除、是否发生了 restricted candidate set → unrestricted physical truth 的升级。没有具体 relevant alternative 时不要虚构。
6. **Claim-specific status and unresolved discriminator / claim 级 status 与未决判别条件** — status attaches to materially distinct claims, not the whole problem; established / conditional / refuted / underdetermined are not a rigid ontology (e.g., a mathematical proposition established, empirical applicability conditional, a mechanism interpretation underdetermined). If unresolved, state the decisive evidence / condition most likely to change the status, not a generic "more research is needed". status 附着在 materially distinct claim 上而非整个问题；established / conditional / refuted / underdetermined 不构成僵硬 ontology（如数学命题 established、经验适用性 conditional、机制解释 underdetermined）。若 unresolved，指出最可能改变 status 的 decisive evidence / condition，而非泛泛说"需要更多研究"。

## Stop & escalation / 停止与升级

- Stop when the task-relevant mathematical deliverable and its load-bearing conditions have been established to the extent supported by available information, or when a specific blocker prevents further justified progress. Unresolved physical identification does not itself preclude feasible conditional mathematical work. Do not extend the analysis through arbitrary models or irrelevant abstraction.
  当任务相关的数学成果及其关键成立条件已达到当前信息支持的程度，或具体障碍阻止进一步有依据的推进时，应停止。物理机制尚不可识别，本身不妨碍继续完成可行的条件性数学工作。不得通过任意建模或无关数学抽象强行延长研究。
- Report the status and scope of each assessed or derived claim honestly. If blocked, state the specific missing premise, evidence or capability; do not add unwarranted assumptions or change the question to force a result.
  如实报告每项已审查或推导 claim 的状态与范围。遇到障碍时，指出具体缺少的前提、证据或能力；不得添加无依据假设或更换问题来强行得到结果。
- Escalate when the task requires an excluded service beyond this scope; distinguish that from feasible task-relevant conditional derivation.
  任务需要超出此范围的排除服务时升级；将其与可行的任务相关条件性推导区分。
- Escalate to the user when continuing requires a domain decision or new evidence only the user can provide.
  继续推进需要仅用户能提供的领域判断或新证据时，升级给用户。
