# Observable Audit Contract / 可观察审计要求

> 本文件只解释 [SKILL.md](../SKILL.md) 中的 OAC 条目，不新增、不修改任何规则。所有规范性表述均直接引自 SKILL.md。
> This file only explains the OAC items in [SKILL.md](../SKILL.md); it adds and changes no rules. All normative wording is quoted directly from SKILL.md.

---

## What the OAC is / OAC 是什么

> The Observable Audit Contract (OAC) is an external auditability contract for the result — not a reasoning pipeline, not a chain-of-thought protocol, not a fixed output template. When relevant, an external reviewer must be able to judge:
> OAC 是对结果的 external auditability contract——不是推理流水线，不是 chain-of-thought 协议，不是固定输出模板。当相关时，外部 reviewer 必须能够判断：

OAC 约束的是**结果**，不是内部推理过程：它规定外部审查者必须能在结果中判断什么，而不断言结果必须以什么顺序、什么格式产生。一个结果可以没有 OAC 编号、没有固定模板，但只要外部审查者无法独立判断下面六项中与当前 claim 相关的项目，该结果就不满足 OAC。

The OAC constrains the **result**, not the internal reasoning: it specifies what an external reviewer must be able to judge in the result, without prescribing the order or format in which the result is produced. A result may carry no OAC numbering and no fixed template; it still fails the OAC if an external reviewer cannot independently judge the items below that are relevant to the claim at hand.

**Claim-specific status / claim 级 status。** status 附着在 materially distinct claim 上，而不是整个问题；一个复合结论中的不同 claim 可以同时具有不同 status。SKILL.md 中给出的例子：数学命题 established、经验适用性 conditional、机制解释 underdetermined。这只是一个说明性例子，不是固定的"数学/经验/机制"三分本体论——哪条 claim 属于哪类，取决于它实际陈述了什么。

**Claim-specific status.** Status attaches to materially distinct claims, not to the whole problem; different claims inside one composite conclusion can simultaneously carry different statuses. SKILL.md's example: a mathematical proposition established, empirical applicability conditional, a mechanism interpretation underdetermined. This is an illustration, not a fixed "mathematical / empirical / mechanism" trichotomy ontology — which category a claim belongs to depends on what it actually states.

---

## OAC-1 — Claim identity / claim 身份

### What must be externally judgeable / 必须可被外部判断的

> which materially distinct claim is examined, its scope, and whether the original claim was kept, modified, weakened, split, or rejected. Do not force one status onto the whole problem.
> 审查的是哪个 materially distinct claim、scope 是什么、原始 claim 是否被保留 / 修改 / 弱化 / 拆分 / 拒绝。不要给整个问题强行分配单一 status。

### Common failure / 常见失败

把复合结论当作单一 claim，用一个 status 覆盖全部。例如把"模型内定理成立"与"物理世界成立"混在一个"结论成立"里：前者可能 established，后者可能 conditional 或 underdetermined。审查者无法判断哪个 claim 被评估时，无法复核任何一条 status。

Treating a composite conclusion as one claim and covering it with a single status. For example, merging "the theorem holds in the model" and "it holds in the physical world" into one "the conclusion holds": the former may be established while the latter is conditional or underdetermined. When the reviewer cannot tell which claim was assessed, no status can be checked.

### Minimal example / 最小例子

结论"由观察到的 proxy 现象 A*，目标现象 B 成立"至少包含三个 materially distinct claims：（i）模型内 A ⇒ B 的数学定理；（ii）A* ⇒ A 的 bridge 在 stated domain 内成立；（iii）B 在本实验中成立。三者可以分别是 established、established within stated domain、not established——把它们合在一起判一个 status 就是 OAC-1 的失败。

The conclusion "B holds because proxy phenomenon A* was observed" contains at least three materially distinct claims: (i) the mathematical theorem A ⇒ B within the model; (ii) the bridge A* ⇒ A, valid in the stated domain; (iii) B holds in this experiment. These can respectively be established, established within the stated domain, and not established — assigning them one joint status is an OAC-1 failure.

---

## OAC-2 — Formulation and semantic correspondence / 形式化与语义对应

### What must be externally judgeable / 必须可被外部判断的

> what the mathematical objects represent, and their material correspondence to observables, theoretical quantities, proxies, latent quantities, controls. Do not force a state / parameter / observable trichotomy or a universal ontology.
> 数学对象表示什么，以及它们与 observable、理论量、proxy、latent quantity、control 的 material correspondence。不要强制 state / parameter / observable 三分法或 universal ontology。

### Common failure / 常见失败

跳过对应关系本身：数学对象直接出现在结论里，但没有说明它对应测量量、理论量还是 proxy。另一极端是给每个问题套用固定三分法，把不具备 state/parameter/observable 结构的问题强行归入。两者都使外部审查者无法判断结论的语义是否忠实于原问题。

Skipping the correspondence itself: mathematical objects appear directly in the conclusion, with no statement of whether each corresponds to a measured quantity, a theoretical quantity, or a proxy. The opposite extreme is imposing a fixed trichotomy on every problem, forcing problems that lack a state/parameter/observable structure into one. Both prevent the reviewer from judging whether the conclusion's semantics is faithful to the original question.

### Minimal example / 最小例子

一个量在结论里被当作 latent quantity x 使用，但形式化里只有测量量 y。OAC-2 要求说清 y 与 x 的对应关系是什么、属于哪一类（proxy？未经验证的等同？），而不是让 x 在结论中无对应地出现，也不是把所有量都强贴 state/parameter/observable 标签。

A quantity is used in the conclusion as a latent quantity x, but the formulation contains only the measured quantity y. OAC-2 requires stating what the correspondence between y and x is and of which kind (proxy? unvalidated equivalence?), rather than letting x appear in the conclusion with no correspondence, or forcing state/parameter/observable labels onto every quantity.

---

## OAC-3 — Material commitments and warrants / material 承诺与依据

### What must be externally judgeable / 必须可被外部判断的

> which commitments / mappings / inferences are material and what appropriate warrant each has. No closed warrant ontology: definitions, evidence, assumptions, mathematical results, experimental design, calibration, constraints — whatever fits the claim.
> 哪些 commitments / mappings / inferences 是 material、各自有什么 appropriate warrant。不要建立封闭 warrant ontology：warrant 可来自定义、证据、假设、数学结果、实验设计、校准、约束等，只要适合 claim。

### Common failure / 常见失败

两个方向：material 步骤没有 warrant（静默依赖）；或者对每个步骤都索要同一种"标准" warrant，把 warrant 当成封闭清单。material 与否由 Core 2 判定——是否改变 claim 的含义、真值/status、范围、支持强度或可识别性；记号替换、等价代数变换、单位换算不属于此列。

Both directions: material steps without warrants (silent dependence), or demanding the same "standard" warrant for every step as if warrants formed a closed list. Materiality is decided by Core 2 — whether the choice changes the claim's meaning, truth/status, scope, support strength, or identifiability; notation substitutions, equivalent algebraic transforms, and unit conversions are outside it.

### Minimal example / 最小例子

"y 代表 latent 量 x"是 material 语义映射，它需要一个 appropriate warrant——例如经过验证的测量关系或定义性等价；"样本总体服从二元正态"是一个 modeling commitment，其 warrant 可以是模型检验或设计约束。两者需要的 warrant 类型不同，但都必须显式给出；而"把变量从 u 改名为 v"不构成 material，无需任何 warrant。

"y stands in for the latent quantity x" is a material semantic mapping and needs an appropriate warrant — e.g., a validated measurement relation or a definitional equivalence; "the sample population is bivariate normal" is a modeling commitment whose warrant may be a model check or a design constraint. The two need different kinds of warrant, but both must be explicit; renaming a variable from u to v is not material and needs no warrant at all.

---

## OAC-4 — Load-bearing dependencies / 关键依赖

### What must be externally judgeable / 必须可被外部判断的

> which conditions the conclusion actually depends on (not a full assumption inventory); the test is whether removing or changing a condition could invalidate the claim or change its status.
> 当前结论真正依赖哪些条件（不要列 assumptions 大全）；检验标准：移除或改变某条件，claim 是否可能失效或改变 status。

### Common failure / 常见失败

把全部假设平铺成清单，使真正承重的条件淹没其中；或者反过来，结论的关键前提完全不出现。检验标准就是条目给出的测试：移除或改变该条件，claim 是否失效或改变 status。通过这个测试的才列，通不过的不列。

Flattening every assumption into an inventory so the truly load-bearing conditions drown in it; or, conversely, the conclusion's key premises not appearing at all. The test is the one the item states: would removing or changing the condition invalidate the claim or change its status? List what passes this test; leave out what fails it.

### Minimal example / 最小例子

结论"f 在 [a,b] 上严格递增"（f 在 [a,b] 连续、在 (a,b) 上处处 f′ > 0）。load-bearing 条件只有两条：闭区间连续性、区间上处处正导数。移除后者，结论失效（例：一点处 f′ > 0 不足够）；而"f 有界""f 的图像光滑"等性质移除后结论不受影响，不属于关键依赖，不应出现在清单里。

Conclusion: "f is strictly increasing on [a,b]" (f continuous on [a,b], f′ > 0 everywhere on (a,b)). The load-bearing conditions are exactly two: continuity on the closed interval and interval-wide positivity of the derivative. Removing the latter invalidates the conclusion (positivity at one point is not enough); properties like "f is bounded" or "the graph of f is smooth" leave the conclusion untouched when removed, are not load-bearing, and do not belong in the list.

---

## OAC-5 — Alternatives and identification boundary / 替代方案与识别边界

### What must be externally judgeable / 必须可被外部判断的

> which admissible class the identification is relative to, which relevant alternatives remain unexcluded, and whether a restricted candidate set has been upgraded to unrestricted physical truth. If no specific relevant alternative exists, do not invent one.
> identification 相对于哪个 admissible class、哪些 relevant alternatives 尚未排除、是否发生了 restricted candidate set → unrestricted physical truth 的升级。没有具体 relevant alternative 时不要虚构。

### Common failure / 常见失败

主要失败是升级：在 {M1, M2} 内排除 M2 后，报告"M1 被识别为机制"，省略"within {M1, M2}"限定词。次要对偶失败是为了形式而虚构备选方案——在没有具体 relevant alternative 时编造 M3，制造虚假的 underdetermined。

The main failure is the upgrade: after ruling out M2 within {M1, M2}, reporting "M1 is identified as the mechanism" while dropping the "within {M1, M2}" qualifier. The secondary, dual failure is inventing alternatives for the sake of form — fabricating an M3 when no specific relevant alternative exists, manufacturing a spurious underdetermined.

### Minimal example / 最小例子

问题限定可接受模型类为 {M1, M2}，观测排除 M2。warranted 结论："在 {M1, M2} 内，M1 是唯一幸存候选"。升级后的结论"M1 是真实机制"需要穷尽性依据，{M1, M2} 的穷尽性必须被单独 warrant。反过来，若问题本身是 scoped 的，"可能存在未知 M3"不构成拒绝该 scoped 结论的理由——那属于虚构 alternative。

The admissible class is restricted to {M1, M2}, and the observation rules out M2. Warranted: "M1 is the unique surviving candidate within {M1, M2}". The upgraded "M1 is the true mechanism" requires an exhaustiveness basis, and the exhaustiveness of {M1, M2} must be separately warranted. Conversely, if the question is itself scoped, "an unknown M3 might exist" is not grounds to reject the scoped conclusion — that is inventing an alternative.

---

## OAC-6 — Claim-specific status and unresolved discriminator / claim 级 status 与未决判别条件

### What must be externally judgeable / 必须可被外部判断的

> status attaches to materially distinct claims, not the whole problem; established / conditional / refuted / underdetermined are not a rigid ontology (e.g., a mathematical proposition established, empirical applicability conditional, a mechanism interpretation underdetermined). If unresolved, state the decisive evidence / condition most likely to change the status, not a generic "more research is needed".
> status 附着在 materially distinct claim 上而非整个问题；established / conditional / refuted / underdetermined 不构成僵硬 ontology（如数学命题 established、经验适用性 conditional、机制解释 underdetermined）。若 unresolved，指出最可能改变 status 的 decisive evidence / condition，而非泛泛说"需要更多研究"。

### Common failure / 常见失败

两个方向：给整个问题一个笼统 status（OAC-1 的失败在此处复现为 status 层面的失败）；以及用"需要更多研究"代替决定性判别条件。"更多研究"没有指出什么证据会改变结论，因此无法被外部检验，不构成 discriminator。

Both directions: assigning one blanket status to the whole problem (the OAC-1 failure reappearing at the status level); and substituting "more research is needed" for a decisive discriminator. "More research" does not say what evidence would change the conclusion, cannot be externally checked, and is not a discriminator.

### Minimal example / 最小例子

同一个研究问题可以带出三种不同 status 的 claim，各自成立：数学命题"A ⇒ B 在模型假设 H 下成立"= established（conditional theorem）；"A 在本实验中的经验适用性"= conditional（取决于 H 与 bridge 的验证）；"B 由 A 引起"的机制解释 = underdetermined（现有证据不能区分机制解释与其它解释）。对未决项，必须给出决定性条件——例如"在本实验域内独立验证 A* ⇒ A 的严格单调 bridge"——而不是"需要更多研究"。

One research question can carry three claims with different statuses, each valid on its own: the mathematical proposition "A ⇒ B holds under model assumptions H" = established (a conditional theorem); "A's empirical applicability in this experiment" = conditional (on verification of H and the bridge); the mechanism interpretation "B is caused by A" = underdetermined (available evidence cannot distinguish it from other interpretations). For the unresolved items, a decisive condition must be named — e.g., "independent validation of a strictly monotone bridge A* ⇒ A in the present experimental domain" — not "more research is needed".
