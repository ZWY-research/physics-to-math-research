# Research workflows / 科研工作流

Supporting methods and worked examples for the three capabilities in [SKILL.md](../SKILL.md). Read the section relevant to the task; this reference adds no runtime rules or mandatory sequence. Examples are idealized mathematical research, not experimental reports.
本文件为 [SKILL.md](../SKILL.md) 的三种能力提供方法与完整示例。按任务读取相关部分；不增加运行规则或强制顺序。示例是理想化数学研究，不是实验报告。

## Research Discovery / 研究问题发现

Start with the feature that needs explanation: a trend, scale, balance or discrepancy in the stated phenomenon. Turn it into a question with distinguishable mathematical answers, such as whether a decay rate follows from the proposed exchange law. Use observations and constraints to motivate the formulation; distinguish what they establish from an exploratory closure. Prefer a question for which the available premises allow useful progress now.
从现象中待解释的趋势、尺度、平衡或差异出发，将其转为答案能够相互区分的数学问题，例如给定交换规律是否推出特定衰减率。用观察和约束支撑问题构造，区分它们已经确定的内容与探索性闭合假设。优先选择当前前提允许取得有用进展的问题。

The useful handoff is a defined question plus a first result: an invariant, scaling relation, bound or solvable conditional model with a derivation. If a missing premise blocks that result, identify it specifically and complete any supported partial construction. Example 1 demonstrates this from a qualitative heat-exchange setting.
有用交付是定义清楚的问题及首项成果，例如附推导的不变量、尺度关系、界或可解条件模型。若缺少某个前提阻断结果，具体指出该前提，并完成当前支持的部分构造。示例一展示从定性热交换情境开展研究。

## Mathematical Development / 数学研究推进

Choose the method for the next scientific consequence. Factoring or a change of variables may expose a conserved quantity; differentiating a normalized mixture may separate component response from redistribution; a parameter inequality may turn an expression into a usable monotonicity criterion. Carry the chosen method to its conclusion instead of listing every applicable technique. Example 2 derives such a criterion and shows when it can fail.
根据下一项科学后果选方法。因式分解或变量替换可揭示守恒量；对归一化混合量求导可分离分量响应与权重重分配；参数不等式可将表达式推进为可用的单调性判据。将选定方法实际推进到结论，而非罗列所有适用技术。示例二推导这种判据，并展示其失效条件。

An analytic statement with its conditions, an explicit counterexample, or a reproducible computational construction is a useful outcome. For a numerical construction, the input, algorithm settings and relevant residual or error estimate explain what was obtained. Conjectures suggested by computation remain candidates for proof.
附条件的解析命题、显式反例或可复现计算构造都是有用成果。对于数值构造，输入、算法设置及相关残差或误差估计说明实际获得了什么。计算启发的猜想仍待证明。

## Research Continuation / 研究续接

Read the relevant existing result and its assumptions, not the entire project archive. Locate the next obstacle: a sufficient condition may need sharpening, a local statement may need extension, or a construction may lack an error bound. Reuse established intermediate results and examine only dependencies affected by the new step. An unsupported inherited assertion can be retained as a clearly conditional premise while supported mathematics proceeds.
读取相关已有结果及其假设，无需重读全部项目档案。定位下一障碍，例如充分条件需要收紧、局部结论需要推广、构造缺少误差界。复用已建立的中间结果，只检查新步骤影响的依赖。依据不足的继承主张可以作为明确的条件前提保留，同时继续有依据的数学工作。

The handoff is the added result and a compact continuation note: which earlier result it uses, what assumptions changed, what was computed and which mathematical question remains. An existing authorized research note can hold the increment beside the earlier result. A dialogue-only task can leave the same information in the response. Example 2 includes a continuation from a sufficient bound to an exact sign interval.
交付新增成果与简短续研记录：使用了哪项旧结果、哪些假设改变、实际计算了什么、还剩哪个数学问题。已有且获授权的研究记录可在旧结果旁保存本轮增量；纯对话任务可在回答中保留相同信息。示例二包含从充分界续接到精确符号区间的推进。

## Computation matched to the task / 按任务选择计算

These are options, not dependencies to install. A short availability check of the intended interpreter and package avoids mistaking an unavailable environment for a completed calculation. Existing authorized tools can both develop a construction and check a result; the mathematical question determines their role.
以下是可选工具，不是待安装的依赖。简短检查拟用解释器及软件包的可用性，可避免将不可执行的环境误记为已完成计算。已授权的现有工具既可推进构造，也可核查结果；具体作用由数学问题决定。

| Mathematical task / 数学任务 | Existing tool option / 现有工具选项 | Useful output / 有用产出 |
|---|---|---|
| Exact coefficient or rational arithmetic / 精确系数或有理运算 | Python standard library, `fractions.Fraction` / Python 标准库 | Exact coefficients, witnesses or reproducible constructions / 精确系数、见证或可复现构造 |
| Symbolic derivatives, factorization or equation solving / 符号求导、分解或解方程 | [SymPy](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html) | Simplified relation with domain and branch conditions / 附定义域与分支条件的化简关系 |
| Numerical roots, quadrature or matrix computations / 数值求根、积分或矩阵运算 | [SciPy](https://docs.scipy.org/doc/scipy/tutorial/index.html), NumPy | Candidate root, integral or spectral quantity with relevant residual/error / 附相关残差或误差的候选根、积分或谱量 |

For example, computing the zero of a derived scalar expression is a mathematical construction; launching a device simulation to establish a transport mechanism is a different task. The existing simulation and empirical-validation boundary in SKILL.md still applies. One-off code can accompany a result; recurring operations alone may justify a maintained script.
例如，计算推导所得标量表达式的零点属于数学构造；启动装置模拟以确立输运机制属于另一任务。SKILL.md 既有的模拟与经验验证边界仍适用。一次性代码可随结果记录；只有反复使用的操作才可能值得维护为脚本。

## Example 1 — Heat exchange to a decay law / 示例一：从热交换到衰减规律

**Invocation:** “Use physics-to-math-research. Two bodies exchange heat while insulated from the outside; their temperature difference decreases. Discover a useful mathematical question and obtain a first conditional result.”
**调用：**“使用 physics-to-math-research。两个物体与外界隔热、彼此交换热量，温差逐渐缩小。提出一个有用的数学问题并取得首项条件性结果。”

**Question and exploratory premise:** What determines the relaxation time and common limiting temperature? Let constant heat capacities be $C_1,C_2>0$. Conservation motivates $C_1\dot T_1=-q$, $C_2\dot T_2=q$. To model heat transfer tending to zero with the temperature difference, explore the linear closure $q=k(T_1-T_2)$, $k>0$ constant. The qualitative observation alone does not establish this closure.
**问题与探索前提：**弛豫时间和共同极限温度由什么决定？设恒定热容 $C_1,C_2>0$。能量守恒支持 $C_1\dot T_1=-q$、$C_2\dot T_2=q$。为描述温差趋零时热流趋零，探索线性闭合 $q=k(T_1-T_2)$，其中 $k>0$ 恒定；定性观察本身并未确立该闭合。

**First result:** Adding the balances gives constant $C_1T_1+C_2T_2$. Subtracting the temperature equations gives $\dot\Delta=-\lambda\Delta$, where $\Delta=T_1-T_2$ and $\lambda=k(1/C_1+1/C_2)>0$. Thus
**首项成果：**相加得 $C_1T_1+C_2T_2$ 守恒；温度方程相减得 $\dot\Delta=-\lambda\Delta$，其中 $\Delta=T_1-T_2$、$\lambda=k(1/C_1+1/C_2)>0$。因此

$$
\Delta(t)=\Delta(0)e^{-\lambda t},\qquad
\overline T=\frac{C_1T_1(0)+C_2T_2(0)}{C_1+C_2},\qquad
T_1=\overline T+\frac{C_2\Delta(t)}{C_1+C_2},\quad
T_2=\overline T-\frac{C_1\Delta(t)}{C_1+C_2}.
$$

Both temperatures tend to $\overline T$, with relaxation time $1/\lambda$. These are consequences of the conditional model. The following standalone Python block checks the solution coefficients exactly for illustrative parameters $C_1=2,C_2=3,k=6/5,T_1(0)=4,T_2(0)=1$; these values are not measurements. Coefficients $b_1,b_2$ multiply $e^{-\lambda t}$, so checking them checks the differential equations for every $t$, rather than sampling a trajectory.
两温度以弛豫时间 $1/\lambda$ 趋于 $\overline T$。这些是条件模型的后果。以下独立 Python 代码用示意参数 $C_1=2,C_2=3,k=6/5,T_1(0)=4,T_2(0)=1$ 精确核对解的系数；参数不是测量值。$b_1,b_2$ 是 $e^{-\lambda t}$ 的系数，因此核对系数是在所有 $t$ 上核对微分方程，而非抽样轨迹。

```python
from fractions import Fraction as Q

C1, C2, k = Q(2), Q(3), Q(6, 5)
T10, T20 = Q(4), Q(1)
rate = k * (1 / C1 + 1 / C2)
mean = (C1 * T10 + C2 * T20) / (C1 + C2)
b1 = C2 * (T10 - T20) / (C1 + C2)
b2 = -C1 * (T10 - T20) / (C1 + C2)
assert (mean + b1, mean + b2) == (T10, T20)
assert C1 * b1 + C2 * b2 == 0
assert -C1 * rate * b1 == -k * (b1 - b2)
assert -C2 * rate * b2 == k * (b1 - b2)
print(f"decay_rate={rate}; limiting_temperature={mean}")
```

Expected output / 预期输出：`decay_rate=1; limiting_temperature=11/5`.

## Example 2 — Weighted flux to a parameter criterion / 示例二：从加权通量到参数判据

**Invocation:** “Use physics-to-math-research. Given $G=(w_1f_1+w_2f_2)/(w_1+w_2)$ with positive weights, find conditions under which decreasing component fluxes imply a decreasing total.”
**调用：**“使用 physics-to-math-research。给定正权重下的 $G=(w_1f_1+w_2f_2)/(w_1+w_2)$，求分量通量递减能够推出总量递减的条件。”

**Development:** On an interval, let $w_i>0$ and $w_i,f_i$ be continuously differentiable. Set $p=w_1/(w_1+w_2)$ and $r=\log(w_1/w_2)$. Direct differentiation gives $p'=p(1-p)r'$ and
**推进：**在某区间上设 $w_i>0$，且 $w_i,f_i$ 连续可微。令 $p=w_1/(w_1+w_2)$、$r=\log(w_1/w_2)$。直接求导得 $p'=p(1-p)r'$，以及

$$
G'=pf_1'+(1-p)f_2'+p(1-p)(f_1-f_2)r'.
$$

If throughout the interval $f_i'\le-a<0$, $|f_1-f_2|\le F$ and $|r'|\le L$, with constants $F,L\ge0$, then $0<p(1-p)\le1/4$ yields
若整个区间上 $f_i'\le-a<0$、$|f_1-f_2|\le F$、$|r'|\le L$，其中 $F,L\ge0$ 为常数，由 $0<p(1-p)\le1/4$ 得

$$
G'\le-a+\frac{FL}{4}.
$$

Consequently $FL<4a$ guarantees strict decrease, and $FL\le4a$ guarantees nonincrease. This is a sufficient criterion, not a necessary one. The coefficient $1/4$ is attained: take $f_{1,2}=-as\pm F/2$ and $(w_1,w_2)=(e^{Ls},1)$, with $F,L>0$. At $s=0$, $G'(0)=-a+FL/4$; if $FL>4a$, redistribution reverses the total slope locally even though both components decrease. No device mechanism is identified by this mathematical example.
因此 $FL<4a$ 保证严格递减，$FL\le4a$ 保证不增。这是充分判据，不是必要条件。系数 $1/4$ 可达到：取 $f_{1,2}=-as\pm F/2$、$(w_1,w_2)=(e^{Ls},1)$，其中 $F,L>0$。在 $s=0$，$G'(0)=-a+FL/4$；若 $FL>4a$，权重重分配使总量斜率在局部反向，尽管两个分量均递减。此数学示例没有识别任何装置机制。

This independent Python block checks the sharp family's derivative at zero by the quotient rule using exact rational arithmetic. The general criterion is proved above, not inferred from these two parameter choices.
以下独立 Python 代码用精确有理运算，通过商法则核对达到该界的函数族在零点的导数。一般判据由上文证明，不由这两组参数推出。

```python
from fractions import Fraction as Q

a, F = Q(1), Q(3)
for L, expected in ((Q(1), Q(-1, 4)), (Q(2), Q(1, 2))):
    # At s=0: w1=w2=1, w1'=L, w2'=0; f1=F/2, f2=-F/2.
    numerator = F / 2 - F / 2
    numerator_prime = L * F / 2 - 2 * a
    denominator, denominator_prime = Q(2), L
    derivative = (numerator_prime * denominator
                  - numerator * denominator_prime) / denominator**2
    assert derivative == -a + F * L / 4 == expected
    print(f"L={L}; G_prime_at_zero={derivative}")
```

Expected output / 预期输出：`L=1; G_prime_at_zero=-1/4`, `L=2; G_prime_at_zero=1/2`.

**Continuation invocation:** “Retain the established derivative identity and the family $f_{1,2}=-as\pm F/2$, $(w_1,w_2)=(e^{Ls},1)$. For $a,F,L>0$ and $FL>4a$, determine exactly where the total increases.” Reusing the identity gives $G=-as+(F/2)\tanh(Ls/2)$ and $G'=-a+(FL/4)\operatorname{sech}^2(Ls/2)$. Solving this explicit inequality gives the next result:
**续研调用：**“保留已建立的导数恒等式与函数族 $f_{1,2}=-as\pm F/2$、$(w_1,w_2)=(e^{Ls},1)$。在 $a,F,L>0$ 且 $FL>4a$ 时，精确确定总量递增的区间。”复用恒等式得 $G=-as+(F/2)\tanh(Ls/2)$、$G'=-a+(FL/4)\operatorname{sech}^2(Ls/2)$。解此显式不等式即可得到下一成果：

$$
G'(s)>0\quad\Longleftrightarrow\quad
|s|<\frac{2}{L}\operatorname{arcosh}\sqrt{\frac{FL}{4a}}.
$$

The continuation record can retain the derivative identity, the added family assumptions and this exact interval; the earlier sufficient bound remains valid. No complete re-audit or new physical inference is needed for this step.
续研记录可保留导数恒等式、新增函数族假设及此精确区间；原充分界仍然有效。此步骤无需完整重审，也未增加物理推断。

## Design sources / 设计来源

The organization adapts [Anthropic's progressive disclosure](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), [Superpowers' composable task skills](https://github.com/obra/superpowers#whats-inside), and [Scientific Agent Skills' package/workflow pairing](https://github.com/K-Dense-AI/scientific-agent-skills). These are design influences, not runtime dependencies or imported instructions. No external skill text or code is bundled here.
组织方式借鉴 [Anthropic 的按需加载](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)、[Superpowers 的可组合任务能力](https://github.com/obra/superpowers#whats-inside)及 [Scientific Agent Skills 的软件与工作流结合](https://github.com/K-Dense-AI/scientific-agent-skills)。它们是设计参考，不是运行依赖或引入的指令；本文件没有打包外部 Skill 的文本或代码。
