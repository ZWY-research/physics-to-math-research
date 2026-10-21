# Research workflows / 科研工作流

Supporting methods and worked examples for the three capabilities in [SKILL.md](../SKILL.md). Read the section relevant to the task and follow its example link only when needed; this reference adds no runtime rules or mandatory sequence. Examples are idealized mathematical research, not experimental reports.
本文件为 [SKILL.md](../SKILL.md) 的三种能力提供方法与完整示例。按任务读取相关部分，需要完整示例时再打开对应链接；不增加运行规则或强制顺序。示例是理想化数学研究，不是实验报告。

## Research Discovery / 研究问题发现

Start with the feature that needs explanation: a trend, scale, balance or discrepancy in the stated phenomenon. Turn it into a question with distinguishable mathematical answers, such as whether a decay rate follows from the proposed exchange law. Use observations and constraints to motivate the formulation; distinguish what they establish from an exploratory closure. Prefer a question for which the available premises allow useful progress now.
从现象中待解释的趋势、尺度、平衡或差异出发，将其转为答案能够相互区分的数学问题，例如给定交换规律是否推出特定衰减率。用观察和约束支撑问题构造，区分它们已经确定的内容与探索性闭合假设。优先选择当前前提允许取得有用进展的问题。

The useful handoff is a defined question plus a first result: an invariant, scaling relation, bound or solvable conditional model with a derivation. If a missing premise blocks that result, identify it specifically and complete any supported partial construction. [Example 1](examples/research-discovery-heat-exchange.md) demonstrates this from a qualitative heat-exchange setting.
有用交付是定义清楚的问题及首项成果，例如附推导的不变量、尺度关系、界或可解条件模型。若缺少某个前提阻断结果，具体指出该前提，并完成当前支持的部分构造。[示例一](examples/research-discovery-heat-exchange.md)展示从定性热交换情境开展研究。

## Mathematical Development / 数学研究推进

Choose the method for the next scientific consequence. Factoring or a change of variables may expose a conserved quantity; differentiating a normalized mixture may separate component response from redistribution; a parameter inequality may turn an expression into a usable monotonicity criterion. Carry the chosen method to its conclusion instead of listing every applicable technique. [Example 2](examples/mathematical-development-weighted-flux.md) derives such a criterion and shows when it can fail.
根据下一项科学后果选方法。因式分解或变量替换可揭示守恒量；对归一化混合量求导可分离分量响应与权重重分配；参数不等式可将表达式推进为可用的单调性判据。将选定方法实际推进到结论，而非罗列所有适用技术。[示例二](examples/mathematical-development-weighted-flux.md)推导这种判据，并展示其失效条件。

An analytic statement with its conditions, an explicit counterexample, or a reproducible computational construction is a useful outcome. For a numerical construction, the input, algorithm settings and relevant residual or error estimate explain what was obtained. Conjectures suggested by computation remain candidates for proof.
附条件的解析命题、显式反例或可复现计算构造都是有用成果。对于数值构造，输入、算法设置及相关残差或误差估计说明实际获得了什么。计算启发的猜想仍待证明。

## Research Continuation / 研究续接

Read the relevant existing result and its assumptions, not the entire project archive. Locate the next obstacle: a sufficient condition may need sharpening, a local statement may need extension, or a construction may lack an error bound. Reuse established intermediate results and examine only dependencies affected by the new step. An unsupported inherited assertion can be retained as a clearly conditional premise while supported mathematics proceeds.
读取相关已有结果及其假设，无需重读全部项目档案。定位下一障碍，例如充分条件需要收紧、局部结论需要推广、构造缺少误差界。复用已建立的中间结果，只检查新步骤影响的依赖。依据不足的继承主张可以作为明确的条件前提保留，同时继续有依据的数学工作。

The handoff is the added result and a compact continuation note: which earlier result it uses, what assumptions changed, what was computed and which mathematical question remains. An existing authorized research note can hold the increment beside the earlier result. A dialogue-only task can leave the same information in the response. [Example 2](examples/mathematical-development-weighted-flux.md) also supports Research Continuation, from a sufficient bound to an exact sign interval.
交付新增成果与简短续研记录：使用了哪项旧结果、哪些假设改变、实际计算了什么、还剩哪个数学问题。已有且获授权的研究记录可在旧结果旁保存本轮增量；纯对话任务可在回答中保留相同信息。[示例二](examples/mathematical-development-weighted-flux.md)也用于 Research Continuation，包含从充分界续接到精确符号区间的推进。

### Copyable continuation handoff / 可复制的研究交接

The following note reuses the completed weighted-flux research. It is an example to copy into an authorized research note or a response, not a required template.
以下记录复用已完成的加权通量研究，可复制到获授权的研究笔记或回答中，不是强制模板。

> - **已建立结果及支持状态：**加权通量导数恒等式、充分界 $G'\le-a+FL/4$（$FL<4a$ 时严格递减，$FL\le4a$ 时不增），以及指定指数权重族的精确递增区间，均有条件性解析证明；独立 Python 代码精确核对 $s=0$ 处两组导数，不构成经验验证。
> - **关键成立条件：**区间上 $w_i>0$，$w_i,f_i$ 连续可微；充分界另需 $f_i'\le-a<0$、$|f_1-f_2|\le F$、$|r'|\le L$，其中 $r=\log(w_1/w_2)$、$F,L\ge0$ 为常数。精确区间另限于 $f_{1,2}=-as\pm F/2$、$(w_1,w_2)=(e^{Ls},1)$，且 $a,F,L>0$、$FL>4a$。
> - **结果来源：**v0.2.12 [加权通量示例](examples/mathematical-development-weighted-flux.md)的推导、续研结果与独立 Python 核对代码；原始推导来自提交 `d259a40bacce9d7a3ba7d79af8091ee4bdacc47b`，现按原文迁移。未建立装置机制或物理适用性。
> - **下一数学问题：**研究一般可微正权重比函数下，加权通量导数的符号条件。
> - **下一项可直接执行的数学操作：**先保留 $f_{1,2}=-as\pm F/2$，将指数权重比推广为可微函数 $\rho(s)=w_1/w_2>0$；在已有导数恒等式中代入 $p=\rho/(1+\rho)$、$r'=\rho'/\rho$，整理 $G'>0$、$G'=0$、$G'<0$ 对 $\rho,\rho'$ 的条件，再代回 $\rho=e^{Ls}$ 核对原精确区间。

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

## Design sources / 设计来源

The organization adapts [Anthropic's progressive disclosure](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), [Superpowers' composable task skills](https://github.com/obra/superpowers#whats-inside), and [Scientific Agent Skills' package/workflow pairing](https://github.com/K-Dense-AI/scientific-agent-skills). These are design influences, not runtime dependencies or imported instructions. No external skill text or code is bundled here.
组织方式借鉴 [Anthropic 的按需加载](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)、[Superpowers 的可组合任务能力](https://github.com/obra/superpowers#whats-inside)及 [Scientific Agent Skills 的软件与工作流结合](https://github.com/K-Dense-AI/scientific-agent-skills)。它们是设计参考，不是运行依赖或引入的指令；本文件没有打包外部 Skill 的文本或代码。
