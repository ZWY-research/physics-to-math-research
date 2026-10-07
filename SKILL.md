---
name: physics-to-math-research
description: Use when the user asks to turn a scientific or physics problem into a mathematical problem, audit the integrity of such a formulation or claim (material commitments, semantic mappings, warrants, claim status), or run diagnostic derivation far enough to test whether a formulation supports a target claim. Not for theorem proving, literature review, experiment design, or general scientific reasoning. 当用户要求把科学或物理问题构造成数学问题、审查该 formulation 或 claim 的完整性（material 承诺、语义映射、warrant、claim status）、或做诊断性推导以检验 formulation 能否支持目标 claim 时使用。不用于定理证明、文献综述、实验设计或一般科学推理。
metadata:
  version: "0.1-alpha.2"
---

# physics-to-math-research — v0.1-alpha

## Purpose & Scope / 目的与范围

Scientific-to-mathematical formulation and claim-integrity audit, with purpose-bounded diagnostic derivation.
科学问题到数学问题的构造与 claim 完整性审查，并允许具有诊断目的的有限数学推导。

The skill audits whether a problem is correctly formulated mathematically, whether material commitments / semantic mappings / inferential steps have warrants, and whether conclusions have been over-upgraded (e.g., mathematical → physical / causal). Derivation serves only to test a formulation and judge claim status, never to solve the full problem.
本 Skill 审查问题是否被正确数学化、material 承诺 / 语义映射 / 推理步骤是否有依据，以及结论是否被过度升级（如数学结论 → 物理 / 因果结论）。推导只用于检验 formulation 与判断 claim status，不用于解决完整问题。

Not a theorem prover, symbolic algebra system, causal discovery system, statistical methodology framework, literature review workflow, simulation framework, experiment optimizer, universal scientific ontology, publication-writing system, or autonomous research agent.
不是 theorem prover、symbolic algebra system、causal discovery system、statistical methodology framework、literature review workflow、simulation framework、experiment optimization、universal scientific ontology、publication-writing system，也不是 autonomous research agent。

## When to use / 何时使用

- The user asks to formulate a scientific / physics problem mathematically, or to audit an existing formulation. 用户要求把科学 / 物理问题构造成数学问题，或审查已有 formulation。
- A claim's commitments, mappings, inferential steps, or status need auditing. 需要审计 claim 的建模承诺、语义映射、推理步骤或 status。
- Limited derivation is needed to test whether a formulation supports the target claim. 需要通过有限推导检验 formulation 能否支持目标 claim。

## When not to use / 何时不用

- The task is in one of the excluded categories above. 任务属于上述排除类别。
- No scientific problem to formulate and no claim to audit. 没有需要形式化的科学问题，也没有需要审计的 claim。

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

### Diagnostic derivation / 诊断性推导

Real mathematical derivation is allowed, but only as far as needed to test whether the formulation can support the target claim, expose its load-bearing structure, and determine the relevant claim status. Do not define "bounded" by a fixed line or token count.
允许真正进行数学推导，但只推导到足以检验 formulation 能否支持目标 claim、暴露其关键依赖结构、并确定相关 claim status 的程度。不要用固定行数或 token 数定义 "bounded"。

### Mathematical structure / 数学结构

"Minimal sufficient mathematical structure" is not a Core rule. Avoid mathematical commitments that neither support the target claim nor discriminate among relevant formulations; competing formulations compatible with the evidence may be kept.
"Minimal sufficient mathematical structure" 不是 Core 规则。避免引入既不支持目标 claim、也不能区分 relevant formulations 的数学承诺；可保留与证据兼容的 competing formulations。

### Counterexamples / 反例

No exhaustive counterexample search. Only when relevant, look for adversarial witnesses / counterexamples / alternative explanations that could change the claim status, are domain-compatible, and have diagnostic value — to determine what the conclusion depends on, not to manufacture skepticism.
不要穷尽式搜索反例。只在相关时寻找能改变 claim status 的、与问题域相容的、具有诊断价值的 adversarial witness / counterexample / alternative explanation——目的是确定结论真正依赖什么，不是制造无限怀疑。

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

- Stop deriving once the formulation's support for the target claim and its load-bearing structure are clear, unless the stated task remains incomplete because a claim-relevant step that is warranted by the available information and feasible within the current formulation or diagnostic scope is still needed. Complete the smallest such step to an operational level before stopping: specify what is to be estimated, tested, compared, propagated, or derived, and how that step would be carried out at the level supported by the available information. Do not merely name a needed analysis. Do not continue merely to make the analysis more complete or to solve the full problem.  
  当 formulation 对目标 claim 的支持程度与 load-bearing structure 已清楚时停止推导；但如果由于仍缺少一个与 claim 相关、由现有信息支持、且在当前 formulation 或诊断范围内可行的步骤，使得用户所提出的任务尚未完成，则应在停止前把其中最小的必要步骤推进到可操作层级：明确需要估计、检验、比较、传播或推导什么，并在现有信息所支持的程度上说明该步骤如何实施。不得仅仅指出“还需要某项分析”而停止。不得仅为了使分析更加完整而继续，也不得继续求解完整问题。
- Report the status of each assessed claim honestly (e.g., refuted or underdetermined). Determining claim status is not by itself a stopping condition when the preceding rule requires a bounded continuation. Otherwise, do not add unwarranted assumptions or change the claim to force further progress or reach a preset conclusion (Core 2); stop and state the missing evidence or condition.  
  如实报告每项已审查 claim 的 status（如 refuted / underdetermined）。当上一条要求进行有界继续时，仅完成 claim status 的判定本身并不构成停止条件。除此之外，不得为了强行继续推进或得到预设结论而添加无 warrant 的假设或更换 claim（Core 2）；此时应停止并指出缺失的证据或条件。
- Escalate when the task leaves this skill's scope (full theorem proving, literature review, experiment design, writing): state that it is out of scope and point to the appropriate workflow. 任务超出范围（完整定理证明、文献综述、实验设计、写作等）时升级：说明超出范围并指向相应流程。
- Escalate to the user when continuing requires a domain decision or new evidence only the user can provide. 继续推进需要用户提供领域判断或新证据时，升级给用户。
