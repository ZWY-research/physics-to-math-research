# Angioni C1/C2 — Conditional Mathematical Review / 条件性数学审查

- Record date / 归档日期：2026-10-20
- Release / 发布：v0.2.9 — Research results and review records update
- Authority / 来源：本记录转录项目负责人在 ChatGPT 中完成并授权归档的数学内容评议决策；归档执行者未重新开展数学研究，也未修改已审查命题。 / This records the project owner's authorized decisions from mathematical-content discussion in ChatGPT; publication does not constitute a new mathematical adjudication.
- Scope / 范围：未重新分析原始实验数据，未重新核验 PDF，不是期刊同行评审，也不冒称完全独立的外部审稿。 / No raw experimental reanalysis or PDF revalidation; not journal peer review or fully independent external refereeing.

## C1 — Conditional mathematical review: ACCEPT WITH LIMITATIONS

接受任意残余项下的不识别性证明、共享参数模型的秩充要条件、条件性测量误差界、竞争解释反例，以及遗漏项参数偏差和 pinch 数误差分析。

Accepted: non-identifiability with arbitrary residual terms; rank conditions for shared-parameter models; conditional measurement-error bounds; competing-explanation counterexamples; omitted-term parameter bias and pinch-number error analysis.

**无约束估计限定。** C1 解析最小二乘公式属于无约束估计。真实模型中扩散参数为正，不保证无约束估计也为正。若要求估计值严格为正，需要另行讨论约束优化；不能直接将原公式称为受约束估计。本限定补充于此，原研究报告公式及主要结论未改写。

**Unconstrained-estimation limitation.** The analytic least-squares formulas are unconstrained estimates. Positivity of the true diffusion parameter does not ensure positivity of its unconstrained estimate. Requiring a strictly positive estimated diffusion parameter needs a separate constrained-optimization treatment; the published formulas must not be described as constrained estimates.

**参考答案暴露限定。** C1 的 Codex 会话此前曾接触 ChatGPT 参考评议，不能作为未受参考答案影响的独立能力测试。 / The C1 Codex session had prior exposure to a ChatGPT reference review and is not a reference-unexposed independent capability test.

## C2 — Conditional mathematical review: ACCEPT

接受零通量约化的守恒条件、连续残差存在性结果、指定区间及状态分支上的唯一性条件、根扰动界和局部唯一性证明、三根／无解／切触根／多分支反例、状态反馈总导数分析，以及非单调关联不推出自洽多解的反证。

Accepted: conservation conditions for zero-flux reduction; existence results for continuous residuals; uniqueness conditions on a specified interval and state branch; root-perturbation bounds and local uniqueness proofs; three-root, no-root, tangency and multiple-state-branch counterexamples; total derivatives with state feedback; and the counterexample to inferring self-consistent multiplicity from a non-monotone association.

**物理适用性限定。** C2 是明确建模假设下的条件性数学分析，不证明真实托卡马克具有多个密度梯度平衡，不证明相关微观湍流机制。“稳定性界”仅指代数根对残差扰动的界，不是动力学稳定性结论。人为闭合不是已验证的 ITG/TEM 模型，没有运行 GENE 或 TGLF。

**Physical limitation.** C2 is conditional on explicit modeling assumptions. It establishes neither multiple density-gradient equilibria in an actual tokamak nor a microscopic turbulent mechanism. Its stability bounds concern algebraic-root perturbations, not dynamical stability. Artificial closures are not validated ITG/TEM models; no GENE or TGLF simulation was run.

## Shared conclusions / 共同结论

- 两项研究都产生了实际可核查的数学结果，均使用冻结 Skill 文本，但加载方式是显式 Git blob 读取，非原生 Skill 调用。 / Both studies contain checkable mathematical results and explicitly read frozen Skill Git blobs rather than using native Skill invocation.
- 没有可信的 Skill OFF 对照；Skill incremental gain：**NOT ESTABLISHED**。 / No credible Skill OFF control; incremental Skill capability gain is not established.
- 没有发现必须修改 Core/OAC 的通用推理失败；本次也没有新科研 Agent 测试。 / No general reasoning failure requiring Core/OAC revision was identified; no new scientific-agent test was run for this release.
- 科研成果不等同于新数学定理或新物理机制；有效参数识别也不等于唯一微观机制识别。 / These results do not establish new mathematical theorems or new physical mechanisms; effective-parameter identification does not uniquely identify a microscopic mechanism.
- Angioni 保留 Research in Progress 分类，完整物理闭合与装置验证尚未完成；Reviewed Papers 仍为 **1**。 / Angioni remains Research in Progress pending physical closure and device validation; Reviewed Papers remains 1.
- **工程检查 PASS 与数学审查 ACCEPT 是不同判断。** 构建、链接、公式渲染检查仅验证发布完整性，不重新作出科研审查决策。 / Engineering PASS and mathematical ACCEPT are distinct: build, link and formula-rendering checks verify publication integrity, not scientific adjudication.

## Provenance and preservation / 来源与保留

| Artifact / 材料 | Frozen Skill / 冻结版本 | Original raw report SHA-256 / 本次输入原始字节 |
|---|---|---|
| [C1 complete report](c1-skill-on-v0.2.7-research-result.md) | v0.2.7; commit 24ce13019cb7f4630211afd12ba3c06dac244bf5 | 93ac948d596db71080ae0e20f45f4f7d8d91f72d79080a539d94e3a60bfa9728 |
| [C2 complete report](c2-skill-on-v0.2.8-research-result.md) | v0.2.8; commit 9c59ad6f8bf63f1502b1c7a9d93121cefbcb839b | 2ee5a08d5c2657f2ada20842dcd6f0e99dcfecff1cf640eba472a3a517385442 |

Frozen Skill raw Git-blob SHA-256 / 冻结 Skill 原始 blob 哈希：

- C1 v0.2.7：00d058d1a679c9da0b5fb050a7f3c3e91cc29ab6d5341408a2a7aa8aae695f4d
- C2 v0.2.8：82f603987087d5dcef36b47937212826220ece3863ad85361b106057142d7662

Original report locations relative to the experiment workspace / 原实验文件相对位置：

- C1: experiments/angioni-2012/skill-on-v0.2.7/research-result.md
- C2: experiments/angioni-2012/skill-on-c2-v0.2.8/research-result.md

原实验报告保持不变。C1 为完整复制；其正文中的原相对证据标识 ../source-evidence.md 对应本目录的 [source-evidence.md](source-evidence.md)。C2 仅在公开副本替换本地绝对路径并增加公开归档说明，不改变数学公式、主要结论或原有历史叙述。本文所列原始字节哈希与公开副本的 LF 归一化哈希区分记录；报告正文中的 03f247… 为原研究使用的历史源证据哈希，不是脱敏后公开证据文件的新认证。

Original experimental reports remain unchanged. C1 is copied in full. C2 only redacts local absolute paths and adds a publication note; its mathematics and historical assertions are retained. Original raw-byte hashes and LF-normalized public-copy hashes have different roles. The reports' historical source-evidence hash is not a new certification of the sanitized public copy.

LF-normalized UTF-8 public report SHA-256 / 公开报告 LF 归一化哈希：

- C1: 93ac948d596db71080ae0e20f45f4f7d8d91f72d79080a539d94e3a60bfa9728
- C2: 8b48567dd5a4ea5c28cccf3141d0b275e4cd428bef3314494990f95d1dd3deca

[Stage A source evidence / 原文证据](source-evidence.md) 与 [initial ChatGPT review / 初步评议](2026-10-15-angioni-2012-source-evidence-review.md) 保持原样和历史贡献归属；原 ChatGPT 评议中的结果不追溯改记为阶段 A 或 Skill ON 成果。 / Historical Stage A and initial-review records retain their original contents and attribution.

v0.2.9 Skill artifact SHA-256 (LF Git content) / 仅版本元数据与标题变更后的 Skill 哈希：0fc3c572951edbc8357aa2779edba33cb21dc2697b6022a2ec32b8ff800342c2。除此之外的运行文字与 v0.2.8 一致；四条 Core、六项 OAC 不变。
