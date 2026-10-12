# Jarzynski (1997)：从非平衡物理过程到一般指数积分恒等式

*Jarzynski (1997): From Nonequilibrium Physical Processes to a General Exponential Integral Identity*

**Reviewed — Limited-scope mathematical audit (2026-10-12)**

主分类：`Physics / Statistical Mechanics`

主题标签：`Nonequilibrium Thermodynamics, Fluctuation Relations, Mathematical Physics, Measure-preserving Transformations`

### Abstract

This draft reconstructs the isolated Hamiltonian derivation of Jarzynski's exponential work equality and separates its mathematical assumptions from the physical interpretation of reservoir coupling. The decisive step combines canonical initial weighting with a volume-preserving change of variables. A finite two-state witness illustrates why the initial distribution cannot be discarded, while a second witness distinguishes an expected finite-sample bias from a bound on every realized estimate. A limited measure-space formulation preserves the integral structure without claiming a new theorem or universal physical applicability. The accompanying standard-library Python check addresses only these prescribed discrete witnesses. Reservoir assumptions, experimental validity, and the paper's other dynamical constructions remain outside independent confirmation. The document is a draft for independent mathematical review, not a completed formal audit or evidence of Skill improvement.

## 1. Paper Identity / 论文身份

| 项目 | 记录 |
| --- | --- |
| 正式题名 | *Nonequilibrium Equality for Free Energy Differences* |
| 作者 | C. Jarzynski |
| 期刊、卷期、页、年份 | *Physical Review Letters* **78**(14), 2690–2693 (1997)；发表于 1997 年 4 月 7 日 |
| DOI | [10.1103/PhysRevLett.78.2690](https://doi.org/10.1103/PhysRevLett.78.2690) |
| PRL 出版社入口 | [APS 原始论文页面](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.78.2690) |
| 实际核查的期刊版 PDF | [UCI 提供的四页 PRL 期刊版副本](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf) |
| 对应预印本 | [cond-mat/9610209](https://arxiv.org/abs/cond-mat/9610209)，题名为 *A nonequilibrium equality for free energy differences* |
| 使用版本 | 1997 年 PRL 期刊版；预印本只用于版本身份区分，不用其公式编号 |

本轮只审查指数功平均等式、孤立哈密顿证明、热库耦合解释的条件区别、两个指定离散见证及有限的测度空间重述。不复现整篇论文、不开展物理模拟、不检索后续推广。原文链接与页码可供独立审查；仅核对元数据和指定原文定位，不以期刊声誉作为数学成立依据。出处见上述 [PRL 期刊版](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)。

## 2. Research Summary / 论文研究内容

论文研究有限时间非平衡驱动过程中所做功的统计分布，能否确定两个平衡配置之间的 Helmholtz 自由能差。PRL p.2690 Eq. (2a)、(2b) 的中心关系写为

\[
\langle e^{-\beta W}\rangle=e^{-\beta\Delta F},
\qquad \Delta F=-\beta^{-1}\log\langle e^{-\beta W}\rangle,
\qquad \beta=(k_BT)^{-1}>0.
\]

这里先对指数功取集合平均，再取对数；不是先算普通平均功再代入指数。驱动过程可以不处于平衡，右端仍指初末配置在同一参考温度下的平衡自由能差。本轮不声称原论文以实际实验验证了所有适用情况。公式编号据 [PRL p.2690](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)。

## 3. Physical Question / 原始物理问题

初始制备是在规定温度、初始外参配置下的正则平衡。随后按给定协议 \(\lambda(t)\) 在时间 \(t_s\) 内把外参从 0 切换到 1；重复过程保持协议相同，而微观初态不同，故单次功可能不同。目标是从这些非平衡过程的功分布确定平衡参考量 \(F_1-F_0\)。

必须分开三个层次：初始平衡制备、实际驱动期间的非平衡状态、定义 \(F_1\) 的终配置平衡参考状态。没有要求驱动结束时的真实分布恰好是终态正则分布。孤立证明中，正则制备之后在驱动前脱离热库；保持耦合时则要在系统与热库的完整相空间上说明制备和演化。此条件区分见 [PRL p.2691](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)。

## 4. Physical-to-Mathematical Mapping / 物理到数学的映射

| 物理概念 | 数学概念 | 映射依据与边界 |
| --- | --- | --- |
| 初始热平衡制备 | 正则概率测度 | 指定温度和 \(H_0\) 给出密度 \(Z_0^{-1}e^{-\beta H_0}\)；这是关键制备前提，不能由“发生了驱动”推出 |
| 微观状态 | 相空间点 \(z=(q,p)\) | 在本轮经典哈密顿描述中，位置和动量确定所用微观状态 |
| 外部参数切换 | 随时间变化的 Hamiltonian \(H_{\lambda(t)}\) | 外参协议规定能量函数如何随时间变化；不是任意开放系统的全局动力学假设 |
| 单次过程的功 | 轨道上的随机变量 \(W\) | 下式给出协议驱动的功；孤立情形随机性来自正则初态 |
| 重复过程的统计 | 概率期望 | 对规定初态集合及其生成的轨道取平均，不等同于任意一次有限样本平均 |
| 自由能差 | 配分函数比值的负对数 | 同一温度、同一积分约定下，\(\Delta F=-\beta^{-1}\log(Z_1/Z_0)\) |
| 孤立 Hamiltonian 演化 | 可逆、体积保持的相空间映射 | 正则且在规定时间全域存在的哈密顿流给出可逆映射；Liouville 性质提供保体积性 |

PRL p.2690 Eq. (3) 的功定义是

\[
W=\int_0^{t_s}\dot\lambda(t)
\frac{\partial H_\lambda(z(t))}{\partial\lambda}\,dt.
\]

在本轮限定的孤立、足够正则哈密顿轨道上，链式法则与哈密顿方程使

\[
\frac{d}{dt}H_{\lambda(t)}(z(t))
=\partial_z H_{\lambda(t)}\cdot\dot z(t)
+\dot\lambda\,\partial_\lambda H_\lambda
=\dot\lambda\,\partial_\lambda H_\lambda.
\]

相空间运动项为零，故积分得

\[
W=H_1(z(t_s))-H_0(z(0)).
\]

后一公式由前一公式及孤立动力学条件得到，不是任意开放子系统的普遍功定义；有热交换时，子系统能量变化还含其他贡献。原文定位见 [Eq. (3) 与 p.2691 孤立证明](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)。

## 5. Mathematical Question / 数学命题

设共同相空间为 \(\Gamma\)，采用固定的相空间体积测度 \(dz\)，\(\beta>0\)，初末可测实值能量函数为 \(H_0,H_1\)。定义

\[
Z_i=\int_\Gamma e^{-\beta H_i(z)}\,dz,
\qquad 0<Z_i<\infty,
\qquad \rho_0(z)=Z_0^{-1}e^{-\beta H_0(z)}.
\]

设规定时间的演化 \(\Phi:\Gamma\to\Gamma\) 是可逆、保体积映射，且本轮换元所需的可测性成立，定义

\[
W(z)=H_1(\Phi(z))-H_0(z).
\]

待证

\[
\mathbb E_{\rho_0}[e^{-\beta W}]=\frac{Z_1}{Z_0}.
\]

关键前提是：正则初态；给定的能量差功函数；在同一 \(\Gamma\) 上全域定义并映满该空间的保体积双射；两个配分函数正且有限。物理实现还需足够正则的哈密顿流及其在整个驱动区间的存在性。这里不默许带奇异边界、改变积分域或损失可逆性的任意演化满足条件。配分函数条件保证右端和所需指数期望有限，但不自动保证 \(\mathbb E|W|<\infty\)。

## 6. Decisive Derivation / 决定性推导

按上述明确前提，直接计算

\[
\begin{aligned}
\mathbb E_{\rho_0}[e^{-\beta W}]
&=\frac1{Z_0}\int_\Gamma
e^{-\beta H_0(z)}
e^{-\beta[H_1(\Phi(z))-H_0(z)]}\,dz\\
&=\frac1{Z_0}\int_\Gamma e^{-\beta H_1(\Phi(z))}\,dz\\
&=\frac1{Z_0}\int_\Gamma e^{-\beta H_1(y)}\,dy\\
&=\frac{Z_1}{Z_0}\\
&=e^{-\beta\Delta F}.
\end{aligned}
\]

第三步取 \(y=\Phi(z)\)：映满性保留完整积分域；保体积性保留测度，光滑情形下相应 Jacobian 的绝对值为 1。一般任意映射不能支持此换元。正则初态的权重恰好消去功指数中的 \(H_0\)，其余只剩终态 Boltzmann 积分。

与 PRL p.2691 的对应是：Eq. (6) 将平均写成终时密度 \(f(z,t_s)\) 与累积功 \(w(z,t_s)\) 的积分；Eq. (7) 结合沿轨道的密度保持和能量差，得到

\[
f(z,t)e^{-\beta w(z,t)}=Z_0^{-1}e^{-\beta H_{\lambda(t)}(z)};
\]

Eq. (8) 积分后给出 \(Z_1/Z_0\)。本节的初态换元证明与原文的 Liouville／累积功写法表达同一决定性积分结构，未要求终时真实分布重新达到平衡。定位见 [PRL Eq. (6)–(8)](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)。

**复合系统与子系统不能混同。** 原文在完整变量 \(y=(z,z')\) 上采用
\(G_\lambda=H_\lambda(z)+\mathcal H(z')+h_{\rm int}(z,z')\)，设系统和热库整体孤立并以 \(G_0\) 正则制备。按该设定，参数显式驱动 \(H_\lambda\)，功等于整体能量变化；同类证明首先得到 Eq. (9) 的 \(\langle e^{-\beta W}\rangle=Y_1/Y_0\)。不能将这一步直接写为子系统 \(Z_1/Z_0\)。原文从 Eq. (9) 到 Eq. (10) 使用弱耦合和准平衡的物理解释，并要求热库足够大；当相互作用可忽略时才直接约去热库因子。本轮不独立认证有限相互作用下的精确因子消去或误差。因此孤立证明不是所有热库耦合过程的完整适用性证明。出处：[PRL p.2691 Eq. (9)、(10)，弱耦合说明延续至 p.2692](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)。

若进一步有 \(\mathbb E|W|<\infty\)，由指数函数的凸性

\[
e^{-\beta\mathbb E W}\leq\mathbb E[e^{-\beta W}]
=e^{-\beta\Delta F},
\qquad \mathbb E[W]\geq\Delta F.
\]

这一 Jensen 推论依赖原指数恒等式及适当的功可积性，不能先删除初态、功或变换条件，再无条件套用。

## 7. Counterexamples & Failure Boundaries / 反例与失效边界

### 7.1 初始正则分布不可任意删除

在两点集合上使用计数测度及恒等映射，取

\[
H_0=(0,0),\qquad H_1=(0,\varepsilon),
\qquad \varepsilon>0,\quad\beta>0.
\]

功分别为 \(0,\varepsilon\)。初态正则概率为 \((1/2,1/2)\)，于是

\[
Z_0=2,\qquad Z_1=1+e^{-\beta\varepsilon},
\qquad \mathbb E[e^{-\beta W}]
=\frac{1+e^{-\beta\varepsilon}}2=\frac{Z_1}{Z_0}.
\]

若只把初态改成集中于零功状态的概率 \((1,0)\)，则

\[
\mathbb E[e^{-\beta W}]=1\ne\frac{Z_1}{Z_0}<1.
\]

其余能量、映射与参考配分函数不变，失去的正是正则初态权重。这是删除前提的离散见证，不反驳原论文条件内定理，也不声称实现了连续哈密顿物理实验。

### 7.2 期望偏差不等于每次样本均为上界

令 \(W_i\) 独立同分布于满足原等式的功分布，定义

\[
A_N=\frac1N\sum_{i=1}^N e^{-\beta W_i},
\qquad \widehat{\Delta F}_N=-\beta^{-1}\log A_N.
\]

在相关期望存在时（例如 \(\mathbb E|\log A_N|<\infty\)，且指数期望有限），\(\mathbb E A_N=e^{-\beta\Delta F}\)。\(-\log\) 的凸性给出

\[
\mathbb E[\widehat{\Delta F}_N]
\geq-\beta^{-1}\log\mathbb E A_N=\Delta F.
\]

这并不推出逐样本的 \(\widehat{\Delta F}_N\geq\Delta F\)。上述正则两态分布中，对任意有限正整数 \(N\)，所有样本功均为零的事件有概率 \(2^{-N}>0\)，在该事件上

\[
\widehat{\Delta F}_N=0<
-\beta^{-1}\log\left(\frac{1+e^{-\beta\varepsilon}}2\right)=\Delta F.
\]

这是对“有限样本每次都给上界”的误读的反例，不宣称发现原论文错误。原文讨论稀有低功事件对指数平均估计的影响，见 [PRL p.2692](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)；本轮不建立通用有限样本收敛理论。

### 7.3 指定数值见证的边界

固定 \(\beta=1,\varepsilon=\ln4\)，得

\[
Z_0=2,\quad Z_1=\frac54,\quad Z_1/Z_0=\frac58,
\quad\Delta F=\ln\frac85>0.
\]

正则指数平均为 \(5/8\)，非正则零功初态的指数平均为 1；全零功样本估计为 0；平均功 \(\ln4/2\geq\ln(8/5)\)。[脚本](two-state-check.py)使用有理数和带容差的浮点检查，[实际输出](two-state-check-output.txt)及[执行记录](execution-record.md)单独保存。它仅核查这些指定见证，不是一般定理的机器证明。

## 8. General Mathematical Formulation / 一般数学问题

设 \((X,\mu)\) 为测度空间，\(\Phi:X\to X\) 为可测、具有可测逆映射的保测度双射，即 \(\mu(\Phi^{-1}A)=\mu(A)\) 对每个可测集合 \(A\) 成立。设 \(H_0,H_1\) 为可测实值函数，\(\beta>0\)，且

\[
0<Z_i=\int_Xe^{-\beta H_i}\,d\mu<\infty.
\]

定义

\[
dP_0=Z_0^{-1}e^{-\beta H_0}\,d\mu,
\qquad W(x)=H_1(\Phi(x))-H_0(x).
\]

则

\[
\begin{aligned}
\mathbb E_{P_0}[e^{-\beta W}]
&=Z_0^{-1}\int_X e^{-\beta H_1\circ\Phi}\,d\mu\\
&=Z_0^{-1}\int_Xe^{-\beta H_1}\,d\mu
=Z_1/Z_0.
\end{aligned}
\]

第二步使用推前测度 \(\Phi_*\mu=\mu\)，因而非负可测函数的积分不变；配分函数条件保证结果有限。这里保留任务指定的双射假设，不另行研究假设的最弱化。

这是给定积分结构的一般测度论表述，无需预先指定装置；不是原创数学定理，也不意味着每种物理动力学均存在满足条件的映射。它保留指数权重、初态规范化、能量差函数、保测度变换及配分函数比。它不再提供温度的物理意义、Hamiltonian 的动力学实现、真实功测量、热库耦合与弱耦合近似的语义。把结构迁移到另一场景时仍要核查这些映射，不能把抽象层次提高本身当作科研价值证明。

## 9. Objective Assessment / 客观审查结论

| 层面 | 当前状态及范围 |
| --- | --- |
| 数学层面 | 在第 5 节规定的孤立哈密顿条件下，中心等式的决定性积分步骤已复现；经独立数学审查，在报告列明的假设下，孤立哈密顿系统的决定性数学证明成立。本结论不代表整篇论文、所有热库模型或实验结果已经验证。 |
| 物理层面 | 热库耦合解释需要额外物理条件；本轮未独立确认所有实际系统满足这些条件 |
| 数值层面 | 指定两态见证的运行结果见执行记录；离散检查不能代替一般证明或物理实验 |
| 正式审查状态 | 已完成限定范围数学审查；未审查部分保留原有声明。 |

尚未审查：Nosé–Hoover 部分的完整推导、Metropolis 或其他更新机制、全部累积量结果、实际实验或大规模数值验证、后续文献的广泛推广。本轮不宣称全面验证了整篇论文或发现原论文错误。

## 10. Skill Implications / 对 Skill 的启示

以下仅为待验证的 Regression candidates，未修改任何既有输入、判据或运行规范：

1. **初始正则分布的关键作用。** 保护的行为：明确概率平均的制备分布，保留指数权重消去的前提，不把一个特定正则等式外推至任意初态。
2. **精确期望恒等式与有限样本估计的区别。** 保护的行为：区分集合等式、估计量期望偏差与单次样本值，不把 Jensen 的期望界误报为逐样本保证。
3. **复合系统结果与子系统解释的区别。** 保护的行为：明确计算使用的相空间、能量与配分函数，并识别把 \(Y_1/Y_0\) 解释为子系统自由能差时新增的物理条件。

`Candidate regression only — no demonstrated Skill failure or capability gain.`

三个 Regression candidates 尚未经过 Skill ON/OFF 运行检验，不构成实际能力改进证据。

本轮没有实际 ON/OFF 模型输出，不能判定 Skill 存在失败或能力增益，也不能据此修改 Core/OAC。

独立审查人可检查：第 4 节功定义与能量差的条件；第 6 节换元及 PRL Eq. (6)–(10)；第 7 节正则／非正则与有限样本反例；第 8 节可测性、保测度和积分前提。原文定位见[期刊版 PDF](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)，文件路径为本目录内 [two-state-check.py](two-state-check.py)、[two-state-check-output.txt](two-state-check-output.txt)及 [execution-record.md](execution-record.md)。

Review status: Reviewed — Limited scope; independent mathematical review accepted on 2026-10-12.
