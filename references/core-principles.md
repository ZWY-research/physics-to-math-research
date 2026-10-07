# Core Principles / 核心原则

> 本文件只解释 [SKILL.md](../SKILL.md) 中已冻结的四条 Core 规则，不新增、不修改任何规则。所有规范性表述（normative wording）均直接引自 SKILL.md。
> This file only explains the four frozen Core rules in [SKILL.md](../SKILL.md); it adds and changes no rules. All normative wording is quoted directly from SKILL.md.

---

## Core 1 — Problem provisionality / 问题暂定性

### Rule / 规则

> Treat the initial problem statement, target claim, and interpretation of its quantities as provisional — not as correct premises — until checked for material mis-specification.
>
> 初始问题、目标 claim 及其 quantity 的解释，在检查是否存在会实质改变结论的问题错设（material mis-specification）之前，只能作为暂定表述，不能直接视为正确前提。

### What failure it prevents / 防止什么错误

把错设的问题当成前提（taking a mis-specified problem as a premise）。典型形态：claim 涉及的 quantity 与研究真正关心的问题不一致；claim 比现有证据所能支持的范围说得更多；某个解释在未经检查之前就被默认固定下来。错设一旦被带入推导，后续每一步都会继承它，最后得到的结论可能形式上严格、但与真正的问题无关。

Taking a mis-specified problem as a premise. Typical forms: the quantity in the claim is not what the research question is really about; the claim says more than the available evidence can support; an interpretation is silently fixed before it has been checked. Once a mis-specification enters the derivation, every later step inherits it — the final result can be formally rigorous yet unrelated to the actual question.

### What it does not require / 它不要求什么

检查的对象是 **material** 层面的错设——即会实质改变结论的错设；规则本身只设了这一道门槛。它不要求重做全部工作，也不要求把每个措辞差异都当作疑点对待。

The check is for **material** mis-specification — one that could materially change the conclusion; the rule sets only this threshold. It does not demand redoing everything, nor treating every difference of wording as suspect.

### Minimal example / 最小例子

某研究要判断哪种机制解释某个响应，但 claim 中出现的 quantity 是 latent 且未测量，现有证据只涉及一个 proxy。在发现这个测量缺口之前就把问题当作 well-posed，正是 Core 1 针对的失败：问题本身（关于 latent quantity 的结论）与证据能支持的问题（关于 proxy 的结论）不是同一个问题。

A study asks which mechanism explains a response, but the quantity appearing in the claim is latent and unmeasured, and the available evidence concerns only a proxy. Treating the question as well-posed before noticing this measurement gap is exactly the failure Core 1 targets: the question as posed (a conclusion about the latent quantity) and the question the evidence can support (a conclusion about the proxy) are not the same question.

---

## Core 2 — Material commitment accountability / 实质性承诺问责

### Rule / 规则

> Every material claim-relevant modeling commitment, semantic mapping, or inferential step requires an appropriate explicit warrant. Material = a choice that changes what the claim means, its truth/status, its scope, its support strength, or its identifiability. Notation substitutions, equivalent algebraic transforms, and unit conversions are not material and create no audit burden.
>
> 每一个 material 的、与 claim 相关的 modeling commitment、语义映射或推断步骤，都需要适当的显式 warrant。Material = 会改变 claim 的含义、真值/status、范围、支持强度或可识别性的选择。记号替换、等价代数变换与单位换算不构成 material，不产生审计负担。

### What failure it prevents / 防止什么错误

把建模选择、含义指派或推断步骤当作"显然成立"而静默使用（silently treating a modeling choice, a meaning assignment, or an inferential step as obviously valid）。典型形态：把 proxy 当作它所指代的 latent 量（"y 与 x 一起变化，所以 y 可以替代 x"）；把相关性当作因果性；在需要 validated measurement relation 的地方只给出一个"常用假设"。这类步骤决定了 claim 的含义和强度，缺 warrant 时，结论就建立在未说明、未检查的承诺之上。

Silently treating a modeling choice, a meaning assignment, or an inferential step as obviously valid. Typical forms: treating a proxy as the latent quantity it stands in for ("y co-varies with x, so y can stand in for x"); treating correlation as causation; supplying a "commonly assumed" relation where a validated measurement relation is needed. These steps determine what the claim means and how strong it is; without warrants, the conclusion rests on unstated, unchecked commitments.

### What it does not require / 它不要求什么

规则自带豁免项：记号替换、等价代数变换、单位换算不构成 material，不产生审计负担。需要 warrant 的是会改变含义、真值/status、范围、支持强度或可识别性的选择——不是推导中的每一步运算。

The rule carries its own carve-out: notation substitutions, equivalent algebraic transforms, and unit conversions are not material and create no audit burden. Warrants are required for choices that change meaning, truth/status, scope, support strength, or identifiability — not for every algebraic step.

### Minimal example / 最小例子

x 是 latent 量，y 是测量量。"y 代表 x"这一步是 material 的语义映射：它决定了结论究竟是关于 x 还是关于 y。它需要一个显式 warrant——例如一个经过验证的测量关系（validated measurement relation），并明确其方向和适用范围。没有这个 warrant，从 y 的观察推出的任何关于 x 的结论都不被支持；而单位换算（如把结果从 eV 换成 J）则不需要任何 warrant。

x is latent and y is measured. The step "y stands in for x" is a material semantic mapping: it determines whether the conclusion is about x or about y. It needs an explicit warrant — for example a validated measurement relation, with its direction and domain of validity stated. Without that warrant, no conclusion about x drawn from observations of y is supported; by contrast, a unit conversion (e.g., eV to J) requires no warrant at all.

---

## Core 3 — Relative identifiability / 相对可识别性

### Rule / 规则

> Do not select among stated admissible alternatives when available evidence cannot distinguish alternatives that imply materially different answers to the target claim. Any identification claim is relative to the stated admissible class, unless that class is warranted as exhaustive for the stated claim and scope. This does not license unlimited skepticism: a claim explicitly defined as class-relative is fully valid relative to its class; silence outside the class is not a defect, and rejecting it on that ground alone is over-skepticism.
>
> 当现有证据无法区分会给目标 claim 带来 materially different 答案的备选方案时，不得从中做出选择。任何识别性 claim 都相对于 stated admissible class，除非有适当依据表明该 class 对当前 claim 和 scope 已经足够穷尽。这不授予无限怀疑权：明确定义为 class-relative 的 claim 相对于其 class 完全成立；class 外的沉默不是缺陷，仅以此为由拒绝它就是过度怀疑。

### What failure it prevents / 防止什么错误

在证据不能区分的时候做出选择（selecting among alternatives when the evidence cannot distinguish them）。典型形态：只排除了 M2 之后就把 M1 宣布为"被识别出的机制"；把 "within {M1, M2} 内的唯一幸存候选"升级为"无限制陈述下的真机制"；在缺少穷尽性依据（exhaustiveness warrant）时使用绝对识别语言。这类升级把受限候选集上的结论，静默改写为关于物理系统的无限制结论。

Selecting among alternatives when the evidence cannot distinguish them. Typical forms: declaring M1 "the identified mechanism" after only ruling out M2; upgrading "the unique surviving candidate within {M1, M2}" into "the true mechanism, without restriction"; using absolute-identification language when no exhaustiveness warrant exists. Such upgrades silently rewrite a restricted-candidate-set result into an unrestricted statement about the physical system.

### What it does not require / 它不要求什么

规则自带反虚无条款（anti-nihilism）：明确为 class-relative 的 claim 相对于其 class 完全成立；class 外的沉默不是缺陷。对 scoped 问题，不得以"还可能存在未知的 M3"为由拒绝——那属于过度怀疑。穷尽性 warrant 只在 claim 本身越过 class 边界时才被要求。

The rule carries its own anti-nihilism clause: a claim explicitly defined as class-relative is fully valid relative to its class; silence outside the class is not a defect. For a scoped question, "some unknown M3 might exist" is not grounds for rejection — that is over-skepticism. An exhaustiveness warrant is required only when the claim itself crosses the class boundary.

### Minimal example / 最小例子

一个问题把可接受模型类限定为 {M1, M2}，实验排除 M2。warranted 的结论是："在 {M1, M2} 内，M1 是唯一幸存候选"——这是有效的 class-relative 识别，成立。不被 warrant 的结论是："M1 是（唯一）物理机制"——除非有适当依据表明 {M1, M2} 对当前 claim 和 scope 已经穷尽。前者是 scoped 结论，后者是越过 class 边界的升级。

A question restricts the admissible class to {M1, M2}, and the experiment rules out M2. The warranted conclusion is "M1 is the unique surviving candidate within {M1, M2}" — a valid class-relative identification, and it holds. The unwarranted conclusion is "M1 is the (unique) physical mechanism" — unless there is an appropriate basis for {M1, M2} being exhaustive for the claim and scope at hand. The former is a scoped conclusion; the latter is an upgrade across the class boundary.

---

## Core 4 — Dependency audit / 依赖审计

### Rule / 规则

> Audit the load-bearing prerequisites of the inference, mathematical operation, or interpretive step actually used — not a fixed rigor checklist. Examples: a derivative requires differentiability (not smoothness or compactness); an inverse requires existence, uniqueness, and conditioning; an invariance claim requires the class of allowed transformations to be specified. Do not mechanically check compactness, topology, smoothness, or bifurcation for every problem.
>
> 审计实际使用的推断、数学操作或解释步骤的 load-bearing 前提——而不是固定的严谨性清单。例如：导数要求可微性（不是光滑性或紧性）；逆要求存在性、唯一性与条件数；不变性 claim 要求指定所允许的变换类。不要对每个问题机械检查紧性、拓扑、光滑性或分岔。

### What failure it prevents / 防止什么错误

在前提不成立的地方应用定理或操作（applying a theorem or operation whose prerequisites do not hold in the case at hand）。典型形态：由某一点的 f'(x₀) > 0 推出 f 全局递增；把条件数很差的系统当作可逆系统使用；在未指定允许变换类的情况下声称"不变"。这类失败不需要夸张的数学框架——它们往往只是一个关键前提被跳过。

Applying a theorem or operation whose prerequisites do not hold in the case at hand. Typical forms: concluding that f is globally increasing from f'(x₀) > 0 at a single point; treating a poorly conditioned system as invertible; claiming invariance without specifying the class of allowed transformations. These failures do not need elaborate mathematical machinery — they are usually a single skipped prerequisite.

### What it does not require / 它不要求什么

规则明确排除了固定的严谨性清单（fixed rigor checklist）：不要对每个问题机械检查紧性、拓扑、光滑性或分岔。审计对象是实际用到的那个推断或操作的前提——只审计 load-bearing 的那部分，不是全部可想到的数学性质。

The rule explicitly excludes a fixed rigor checklist: do not mechanically check compactness, topology, smoothness, or bifurcation for every problem. The audit targets the prerequisites of the inference or operation actually used — only the load-bearing part, not every mathematical property one can think of.

### Minimal example / 最小例子

结论："f 在 [a,b] 上严格递增。"Load-bearing 前提是：f 在 [a,b] 连续，且在 (a,b) 上处处 f′ > 0（后者是充分的，不是必要的——例如 x³）。单独一点 f′(x₀) > 0 不足够：x + 2x²sin(1/x²) 一类函数可以在 f′(0) = 1 的同时在 0 的任意邻域内振荡下降。而"f 在 (a,b) 上光滑"或"f 的图像紧致"之类性质与结论无关，不属于 load-bearing 前提，不产生审计负担。

Conclusion: "f is strictly increasing on [a,b]." The load-bearing prerequisites are: f is continuous on [a,b], and f′ > 0 everywhere on (a,b) (the latter is sufficient, not necessary — e.g., x³). Positivity at a single point f′(x₀) > 0 is not enough: functions of the form x + 2x²sin(1/x²) can have f′(0) = 1 while oscillating downward in every neighborhood of 0. Properties such as "f is smooth on (a,b)" or "the graph of f is compact" are irrelevant to the conclusion, are not load-bearing, and create no audit burden.
