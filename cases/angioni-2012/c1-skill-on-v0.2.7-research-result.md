# Angioni 2012 — Skill ON Mathematical Research

## 1. Research Source and Skill Version

- 科研证据起点：`../source-evidence.md`，原始字节 SHA-256 为 `03f247f54c0c0f1cc96ab45678f6676b1c7d540f4ed0a03a82108df420169230`。本次使用 E3、E4、M2、M4 及其限制，没有重新提取整篇 PDF，也没有补齐尚不确定的归一化。
- 论文：Angioni et al. (2012), *Off-diagonal particle and toroidal momentum transport: a survey of experimental, theoretical and modelling aspects*, DOI: 10.1088/0029-5515/52/11/114003。本报告引用的是整理证据，不表示重新认证所引实验或全部原公式。
- 被加载 Skill：`physics-to-math-research v0.2.7`；Git commit `24ce13019cb7f4630211afd12ba3c06dac244bf5`。
- 原始 Git blob SHA-256：`00d058d1a679c9da0b5fb050a7f3c3e91cc29ab6d5341408a2a7aa8aae695f4d`。以实验仓库的 `git cat-file blob <commit>:SKILL.md` 二进制 stdout 计算，匹配指定值后完整读取。长输出中截断的末段 OAC／停止条款已另行读取补全。
- **实际加载方式：显式读取冻结 Git blob，非 Codex 原生 Skill 发现／调用。** 没有使用当前 v0.2.8 工作树替代。
- **独立性限制：** 当前会话在此前发布任务中已经接触过本案例的后续 ChatGPT 评议。本轮未重新读取、搜索或引用该评议，但不能抹除已有上下文影响。因此以下是带有该污染声明的条件性数学工作，不能登记为未接触参考答案的独立 Skill ON 测试，也不能将标准秩条件或最小二乘恒等式宣称为独立发现、论文首创或 Skill 增量证据。

## 2. Physical Observation and Mathematical Question

E3指出：特定实验通过外加扭矩维持平坦零旋转，为残余应力提供约束。E4指出：忽略残余应力的两项动量输运反演存在解释风险，而且理论—实验差距不能直接全部归因于该遗漏。

物理入口是证据记录中的原式(2)：

$$
\frac{\Pi_\phi}{nmR}
=-\chi_\phi R\partial_r\Omega_\phi
+V_\phi R\Omega_\phi
+\frac{\Pi_{\rm RS}}{nmR}.
\tag{1}
$$

固定半径附近，观测目标是角速度及径向导数、密度、几何和动量通量。通量通常需要借助已知扭矩源、瞬态动量积累和边界条件重构，**不是只测旋转剖面就直接得到**。本报告把这种重构是否成立作为外部条件，不虚构已有通量数据。

研究问题为：观测何时分别确定扩散、对流和残余贡献；何时只能确定它们的总和；忽略残余项怎样影响参数和 pinch 数。数学模型的可识别性与实际装置能否实现相应控制是两层不同问题。

## 3. Minimal Mathematical Model

### 3.1 统一量纲与三项约定

固定正参考尺度 $\ell_0,\tau_0$，令 $U_0=\ell_0/\tau_0$。对第 $j$ 次观测定义

$$
\xi_j=-R_j\tau_0\partial_r\Omega_{\phi,j},\quad
\zeta_j=\frac{R_j\Omega_{\phi,j}}{U_0},\quad
\eta_j=\frac{\Pi_{\phi,j}}{n_jmR_jU_0^2},
$$
$$
a_j=\frac{\chi_{\phi,j}}{\ell_0^2/\tau_0},\quad
b_j=\frac{V_{\phi,j}}{U_0},\quad
c_j=\frac{\Pi_{{\rm RS},j}}{n_jmR_jU_0^2}.
$$

这些尺度和符号为本次明确引入，**不是论文中未核实的热速度／剪切归一化**。于是式(1)成为

$$\eta_j=a_j\xi_j+b_j\zeta_j+c_j.\tag{2}$$

$a_j>0$为所选正扩散模型的限制，$b_j,c_j$可正可负。这里识别的是式(1)约定下的**有效**系数；不能直接把 $b_j$称作单独的 Coriolis pinch。

原式(10)另列净粒子通量对流 $(\Gamma_n/n)R\Omega_\phi$，剪切相关项还可能含粘性与残余混合贡献。因此本文不把原式(10)末三项未经拆分就塞进 $c_j$。若选择分离常规粒子对流的方案，应先独立测定 $u_{p,j}=\Gamma_{n,j}/n_j$，从式(1)左侧扣除 $u_{p,j}R_j\Omega_{\phi,j}$，再按同一约定重定义有效系数。未知的常规对流与未知剪切粘性不能通过三参数拟合被自动分离。

### 3.2 信息条件与额外假设

| 信息条件 | 本文允许的结论范围 |
|---|---|
| 单次局部观测，三项均未知 | 一个总通量约束，不能直接分离三项 |
| 多个不同背景，$a_j,b_j,c_j$可各自变化 | 不能仅以样本数增加宣告可识别 |
| 同一局部背景下，$a,b,c$在观测间共享 | 下文给出精确唯一性与稳定性条件 |
| $c_j$已独立测得，而$a,b$局部共享 | 扣除$c_j$后可作两参数反演 |

共享背景近似是为了分析 E4 反演问题而引入的**额外条件**：只允许在同一半径、同一窄运行窗口中暂用 $a_j=a,b_j=b,c_j=c$。论文的物理分解不证明它；密度／温度梯度、模结构、粒子源、几何或扰动历史改变都可能使它失效。尤其共享的是归一化后的 $c$，不是在密度变化时自动共享有量纲 $\Pi_{\rm RS}$。

下文矩阵结论首先假定回归量 $\xi,\zeta$准确；随后显式处理通量误差、模型误差和回归量误差。无噪声可识别性并不意味着反演数值稳定。

## 4. Mathematical Results

### 命题1：不约束残余变化时，任意多次观测仍不足以分离

设 $N\ge1$，$\xi,\zeta,\eta\in\mathbb R^N$已知，$a>0,b\in\mathbb R$共享，但 $\mathbf c\in\mathbb R^N$任意。若存在一组相容解，则 $a,b,\mathbf c$不唯一。

**证明。** 给定相容解，任选 $u,v\in\mathbb R$，令

$$
a'=a+u>0,\qquad b'=b+v,\qquad
c'_j=c_j-u\xi_j-v\zeta_j.
$$

逐项代入得 $a'\xi_j+b'\zeta_j+c'_j=a\xi_j+b\zeta_j+c_j=\eta_j$。可选任意足够小的非零 $u$，或非零 $v$，保持扩散为正，因而存在无穷多解。证毕。

这是精确的模型等价变换，不是“可能有其他解释”的泛泛说法。若每个背景还允许不同 $a_j,b_j$，不识别性不会因未知量更多而消失。此结论相对于任意残余向量的模型类，不否定独立残余测量或有依据的闭合所能增加的信息。

### 命题2：共享残余项时的唯一性、几何条件与误差界

令

$$
X=[\boldsymbol\xi\ \boldsymbol\zeta],\quad
\boldsymbol\beta=(a,b)^\top,\quad
P=I-\frac{\mathbf1\mathbf1^\top}{N},\quad Z=PX,
$$
$$\boldsymbol\eta=X\boldsymbol\beta+c\mathbf1+\mathbf e.\tag{3}$$

所有向量取欧氏范数，矩阵取对应算子范数。

**(i) 无噪声唯一性。** 假设数据相容、$a>0$且 $c$确为共享常量。则 $(a,b,c)$唯一，当且仅当 $Z$列秩为2。等价地，

$$
\Delta=\|P\boldsymbol\xi\|^2\|P\boldsymbol\zeta\|^2
-\big((P\boldsymbol\xi)^\top P\boldsymbol\zeta\big)^2>0.
\tag{4}
$$

**证明。** $P^2=P=P^\top$且 $\ker P=\operatorname{span}\{\mathbf1\}$。若两个解相容，作差并乘 $P$，有 $Z\delta\boldsymbol\beta=0$。列秩2时 $\delta\boldsymbol\beta=0$，进而 $\delta c\mathbf1=0$，故解唯一。反之，若存在非零 $v$满足 $Zv=0$，则 $Xv=k\mathbf1$。于是 $(\boldsymbol\beta+tv,c-tk)$对所有足够小的$t$产生同一观测，且可保持$a>0$，故不唯一。式(4)是 $Z^\top Z$的行列式；该Gram矩阵半正定，行列式正当且仅当两列独立。证毕。

几何上，所有 $(\xi_j,\zeta_j)$不能落在一条直线上；仅“不相同”不够。至少需要3次观测。三次时条件具体为

$$
(\xi_2-\xi_1)(\zeta_3-\zeta_1)
-(\xi_3-\xi_1)(\zeta_2-\zeta_1)\ne0.
\tag{5}
$$

这是 $[X\ \mathbf1]$的行列式，直接由后两行减第一行得到。若已有独立的 $c_j$测量，则对 $\eta_j-c_j$反演只需 $\operatorname{rank}X=2$；不再需要未知截距所要求的非共线三点。

**(ii) 通量／模型误差。** 在$Z$列满秩时，联合最小二乘估计为

$$
\widehat{\boldsymbol\beta}=(X^\top PX)^{-1}X^\top P\boldsymbol\eta,
\qquad
\widehat c=\overline\eta-\overline{\boldsymbol x}^{\top}\widehat{\boldsymbol\beta},
\quad \overline{\boldsymbol x}=(\bar\xi,\bar\zeta)^\top.
\tag{6}
$$

**推导。** 固定$\beta$，对$c$最小化平方残差，得到$c=\bar\eta-\overline x^\top\beta$。代回目标函数得到$\|P\eta-Z\beta\|^2$。配方／正规方程给出式(6)，唯一性来自$Z^\top Z$正定。将式(3)代入，得

$$
\delta\boldsymbol\beta=Z^+P\mathbf e,
\qquad
\|\delta\boldsymbol\beta\|\le
\frac{\|P\mathbf e\|}{\sigma_{\min}(Z)},
\tag{7}
$$
$$
|\widehat c-c|\le \frac{\|\mathbf e\|}{\sqrt N}
+\|\overline{\boldsymbol x}\|\frac{\|P\mathbf e\|}{\sigma_{\min}(Z)}.
\tag{8}
$$

其中$Z^+=(Z^\top Z)^{-1}Z^\top$。取奇异值分解$Z=U\Sigma V^\top$，则$Z^+=V\Sigma^{-1}U^\top$，其算子范数为$1/\sigma_{\min}(Z)$，证明式(7)。式(8)由$\delta c=\bar e-\overline x^\top\delta\beta$及Cauchy–Schwarz不等式得到。

即使唯一，观测点接近共线时误差仍可被强烈放大。若真实系数有漂移，则

$$e_j=e_{{\rm obs},j}+\delta a_j\xi_j+\delta b_j\zeta_j+\delta c_j$$

可代入同一界，但要得到可用数值界，必须另有漂移大小的依据。此写法没有假装共享系数已获实验证明。

**(iii) 梯度等回归量也有误差。** 设测得$\widetilde X=X+E$、$\widetilde\eta=X\beta+c\mathbf1+e$，仍用相同$P$。若

$$s=\sigma_{\min}(PX)>\|PE\|,$$

则$\widetilde Z=P\widetilde X$列满秩，并且

$$
\widehat\beta-\beta=\widetilde Z^+P(e-E\beta),\qquad
\|\widehat\beta-\beta\|\le
\frac{\|Pe\|+\|PE\|\|\beta\|}{s-\|PE\|}.
\tag{9}
$$

**证明。** 对任意单位$v$，$\|\widetilde Zv\|\ge\|Zv\|-\|PEv\|\ge s-\|PE\|>0$，故满秩并得到最小奇异值下界。又$P\widetilde\eta=\widetilde Z\beta+P(e-E\beta)$，应用式(7)同样的左逆计算即得结果。证毕。这里不假设随机误差独立、零均值，因而也不宣称统计无偏；导数估计误差不能被遗漏。

### 局部扰动不自动保证测得的斜率就是输运系数

设沿实验控制路径，真实局部响应可微且为

$$F(\xi,\zeta)=a(\xi,\zeta)\xi+b(\xi,\zeta)\zeta+c(\xi,\zeta).$$

链式／乘积法则直接给出

$$
F_\xi=a+\xi a_\xi+\zeta b_\xi+c_\xi,\qquad
F_\zeta=b+\xi a_\zeta+\zeta b_\zeta+c_\zeta.
\tag{10}
$$

即使在$(0,0)$，也只能得到$F_\xi=a(0,0)+c_\xi(0,0)$和$F_\zeta=b(0,0)+c_\zeta(0,0)$。例如额外背景变量$B$满足$c(B)=c_0+dB$，而所用控制路径恰有$B=\xi$，则观测为$(a_0+d)\xi+b_0\zeta+c_0$。它完全通过仿射拟合，却不能区分$a_0$与$d$。

此处$c(\xi,\zeta)$是$c(B(\xi,\zeta))$的实验路径复合，不把论文残余应力在所有物理状态上定义成扩散项。例子说明：小扰动的极限仍可保留背景响应混杂，冻结背景须由独立物理依据支持。

## 5. Counterexample

### 同一完整旋转剖面与零总通量，既可由pinch抵消扩散，也可由残余应力抵消

取离轴局部环带$r\in[r_a,r_a+\ell_0]$，$r_a>0$，令$\rho=(r-r_a)/\ell_0\in[0,1]$；采用固定大半径$R>r_a+\ell_0$的局部几何近似，正密度与质量已知且固定，令

$$\Omega_\phi(r)=\frac{U_0}{R}e^{-\rho}.$$

按第3节定义，$\xi(\rho)=\zeta(\rho)=e^{-\rho}$。给定观测$\eta(\rho)=0$及同一端点旋转值，考虑

| 数学模型 | $a$ | $b$ | $c(\rho)$ |
|---|---:|---:|---|
| A：扩散与pinch抵消 | 1 | $-1$ | 0 |
| B：扩散与残余应力抵消 | 1 | 0 | $-e^{-\rho}$ |

对所有$\rho$，A给出$e^{-\rho}-e^{-\rho}=0$，B给出$e^{-\rho}+(-e^{-\rho})=0$。二者扩散均正，旋转、梯度、边界旋转和总通量完全相同，但对流与残余贡献不同。这里B的$c(\rho)$是预先指定的空间函数，不是定义为对任意旋转状态都正比于$\Omega$；在这一观测剖面上恰好具有相同形状。

所以“测得非零旋转剖面与零净通量，就唯一证明pinch造成该剖面”被反例否定。即使无噪声地观察连续半径，也不能排除B。两模型仅是该通量方程内的相容数学解释，没有宣称对应两个已经证实的微观机制。

若另能在同一背景下给角速度增加常量$hU_0/R$而保持梯度及两模型系数／残余空间函数不变，则A预测新通量$-h$，B预测0，因而可以区分。若允许残余项随扰动重新调整，区分能力又会失效。

还有一个针对共享常量模型的直接失效例：若所有局部观测满足$\xi_j=\zeta_j=q_j$，则$(a,b,c)=(2,-1,3)$与$(3,-2,3)$均给出$\eta_j=q_j+3$。无限增加不同$q_j$也无用，因为观测始终共线，且两套参数均有正扩散、负对流。

## 6. Omitted Residual Stress Analysis

### 6.1 遗漏项如何进入参数，而不是预先猜其方向

现在仅要求$a,b$局部共享，允许残余向量$\mathbf c$变化，准确无噪声观测满足$\eta=X\beta+\mathbf c$。若错误地用**无截距**两项模型拟合，且$X$列满秩，则

$$
\widetilde\beta-\beta=(X^\top X)^{-1}X^\top\mathbf c=X^+\mathbf c.
\tag{11}
$$

**完整推导。** 将候选参数写为$\beta+d$，目标平方误差变成$\|Xd-\mathbf c\|^2$。令$Q=X(X^\top X)^{-1}X^\top$，则$Q$为到$\operatorname{col}X$的正交投影，因而

$$
\|Xd-\mathbf c\|^2
=\|Xd-Q\mathbf c\|^2+\|(I-Q)\mathbf c\|^2.
$$

第二项不依赖$d$；第一项的唯一最小值由$Xd=Q\mathbf c$取得。左乘$(X^\top X)^{-1}X^\top$即得式(11)。证毕。这是标准最小二乘几何对当前输运问题的应用，不是新物理定律。

式(11)同时说明两个不同风险：$Q\mathbf c$污染拟合参数，而$(I-Q)\mathbf c$留在拟合残差中。若$\mathbf c\in\operatorname{col}X$，拟合残差甚至可为零但参数错误；好的拟合不自动意味着贡献分离正确。

若$X$满列秩，则

$$
\widetilde\beta=\beta\ \Longleftrightarrow\ X^\top\mathbf c=0,
\qquad
\|\widetilde\beta-\beta\|\le\frac{\|\mathbf c\|}{\sigma_{\min}(X)}.
\tag{12}
$$

这给出整体参数偏移为零的充要条件及误差界；某一个参数也可能单独无偏。若有加性误差$e$，右侧改为$X^+(\mathbf c+e)$，不能将其全归因于残余应力。若$X$不满秩，真实无遗漏模型本来就不唯一，式(11)的逆矩阵不存在。

用$\xi,\zeta$两列写出第一参数偏移为

$$
\delta a=
\frac{\|\zeta\|^2\xi^\top\mathbf c-(\xi^\top\zeta)\zeta^\top\mathbf c}
{\|\xi\|^2\|\zeta\|^2-(\xi^\top\zeta)^2}.
\tag{13}
$$

分母为正，分子没有固定符号。故不能仅凭“残余应力被遗漏”推断扩散或pinch一定向某方向偏移。

### 6.2 两组精确数值结构

全部为无量纲数学例子，不是实验数据。

1. 取$X=I_2,\beta=(2,-1)^\top$。若$\mathbf c=t(1,1)^\top$，则错误拟合精确得到$\widetilde\beta=(2+t,-1+t)^\top$。$t=1/2$和$-1/2$给出相反方向偏移，估计扩散仍为正；残余项可被两项模型完全吸收，误差残差为零。
2. 取$X$四行为$(1,0),(-1,0),(0,1),(0,-1)$，且$\mathbf c=3\mathbf1\ne0$。则$X^\top X=2I$、$X^\top\mathbf c=0$。对同一$\beta=(2,-1)^\top$，观测为$(5,1,2,4)^\top$，遗漏项拟合仍得到$(2,-1)^\top$，但留下非零常量残差。这里连非零共享残余项都不必造成参数偏差。

### 6.3 pinch数可能比系数本身更不稳定

固定几何$\kappa=R/\ell_0>0$，有效pinch数$p=-RV_\phi/\chi_\phi=-\kappa b/a$。若$a>0$且$a+\delta a\ne0$，直接通分得

$$
\widetilde p-p=-\kappa\frac{a\,\delta b-b\,\delta a}{a(a+\delta a)}.
\tag{14}
$$

若$|\delta a|\le a/2$，则

$$
|\widetilde p-p|\le2\kappa\left(\frac{|\delta b|}{a}
+\frac{|b||\delta a|}{a^2}\right).
\tag{15}
$$

证明只需对式(14)取绝对值并用$|a+\delta a|\ge a/2$。若两参数按相同比例偏移且比例非$-1$，pinch数可不变；若$a+\delta a$趋于零，该比值可发散甚至未定义。因此参数偏移为零、pinch数偏移为零及拟合残差为零是三件不同的事。没有扩散下界就没有这里所需的统一比值误差保证；错误拟合的负扩散也不能自动解读为真实反扩散机制。

## 7. Discriminating Observations or Interventions

只提出以下两项，并将可实现性留给物理验证；坐标是实测的局部$(\xi,\zeta)$，不是把外部扭矩旋钮直接等同于它们。

### 检验1：零旋转参考与两个非共线的局部剖面响应

在同一半径和可验证的局部背景内，取得三种状态$(0,0),(h,0),(0,h)$，$h\ne0$；每种状态都独立重构归一化通量。若共享三项模型适用，必有

$$
\eta_{00}=c,\qquad
a=\frac{\eta_{10}-\eta_{00}}{h},\qquad
b=\frac{\eta_{01}-\eta_{00}}{h}.
\tag{16}
$$

它增加零状态的残余锚定以及两个独立方向的信息，区分第5节中只改变$a+b$的共线解释和pinch／残余抵消解释。原单剖面没有这种独立方向；仅测$\Omega=0$而未重构通量也不能给出$c$。

实际需要验证能否分别改变局部旋转值和局部梯度，并测定密度、温度、几何、粒子源与模状态是否足够一致。$(h,0)$可涉及旋转过零处的非零局部梯度，不是整个剖面都静止；必须核对源、边界及瞬态守恒。任一控制同时改变残余项时，式(16)只给有效响应，不能解释为纯系数。

若每个通量误差绝对值不超过$\epsilon$且回归量准确，则式(16)中$a,b$误差各不超过$2\epsilon/|h|$。该设计的$\sigma_{\min}(PX)=|h|/\sqrt3$（中心化Gram矩阵特征值为$h^2,h^2/3$），所以盲目缩小$h$会放大噪声；式(10)还表明背景响应混杂未必随$h$消失。

### 检验2：增加第四点，检验共享仿射闭合的可证伪后果

在检验1之后，再取得同背景的$(h,h)$状态并重构$\eta_{11}$。共享常量模型预言

$$T=\eta_{11}-\eta_{10}-\eta_{01}+\eta_{00}=0.\tag{17}$$

证明是把$a\xi+b\zeta+c$逐点代入并抵消。这增加一个原三点恰好拟合所没有的过度识别约束。作为相容竞争模型的例子，若沿控制路径的残余项为$c_0+d\xi\zeta$而$a,b$不变，则前三点完全不变，但$T=dh^2$。因此第四点能区分这两个数学模型；这个乘积项只是判别示例，不是声称真实残余应力具有该机制。

若四个通量误差均不超过$\epsilon$，观测到$|T_{\rm obs}|>4\epsilon$即可排除准确共享仿射模型；若另容许每点$\delta$的模型误差，阈值相应为$4(\epsilon+\delta)$。坐标误差还须另计，不能直接沿用此阈值。非零$T$不能单独归因于残余项，因为$a,b$随背景变化也可产生相同结果；$T=0$更不能排除式(10)所示的线性背景混杂。

## 8. Scientific Interpretation and Limitations

| 层次 | 本次可以陈述什么 |
|---|---|
| A：原文已有依据 | 只采用source-evidence的E3、E4及两种动量分解的边界；不是本文发现残余应力 |
| B：本次额外假设 | 统一尺度、同半径局部背景、系数／残余项共享或有界漂移、通量可重构；均须另验证 |
| C：本次报告中的数学工作 | 明确写出等价参数族、中心化识别条件、回归量与输出误差界、连续剖面反例、遗漏项投影与pinch数误差、两项判别关系 |
| D：不能推出 | 装置中的具体系数、差距的单一成因、唯一微观机制、因果识别或Skill增量优势 |

所有命题是对明确模型类的有限维线性代数／微分分析应用，不宣称新定理或文献首创。不同物理闭合可以给出同一组有效参数。零旋转参考要求可靠的动量通量重构；测到零速度本身既不证明非零残余应力，也不保证局部背景不变。

本轮没有访问被禁止评议或其他答案，没有新模型会话、额外Agent、安装、gyrokinetic模拟或真实实验。工具只用于Git原字节读取、文件交付、下面的精确算术核查及利用现有KaTeX检查LaTeX语法；语法检查不替代证明。此前会话的参考答案暴露仍使“独立推导测试”身份不能成立，不能靠本轮不再读取就消除。

## 9. Research Outcome

实际完成了任意残余下的不识别证明、局部共享模型的必要充分识别条件与稳定性界、梯度误差界、两个相容剖面模型及遗漏项和pinch比值的误差推导。相对所用原文证据，本报告增加的是这些明确的条件性逆问题计算，不是新的托卡马克机制。

无法回答的仍是：现有实验是否满足共享背景、如何定量重构其通量、哪些残余贡献主导，以及候选结果相对全部文献是否新颖。最有价值的下一逻辑节点是将明确假设、证明和判别关系交给独立数学及领域审查，特别审查局部背景共享与通量重构的物理可实现性；本轮不自动执行下一阶段。

### 最小计算核查及其边界

使用已有Python标准库`fractions.Fraction`核查有限实例，无软件安装。以下是本轮运行过的核心算术方法，报告内保留，不另建脚本：

```python
from fractions import Fraction as F

def fit(X, y):
    a = sum(x*x for x, z in X)
    b = sum(x*z for x, z in X)
    d = sum(z*z for x, z in X)
    u = sum(x*t for (x, z), t in zip(X, y))
    v = sum(z*t for (x, z), t in zip(X, y))
    det = a*d-b*b
    assert det != 0
    return ((d*u-b*v)/det, (a*v-b*u)/det)

X = [(F(1), F(0)), (F(-1), F(0)),
     (F(0), F(1)), (F(0), F(-1))]
assert fit(X, list(map(F, [5, 1, 2, 4]))) == (F(2), F(-1))
```

同一次精确算术核查还得到：恒定非零残余的平衡四点例子参数误差为零；$X=I_2$、$t=\pm1/2$例子的误差各为$(t,t)$；$h=1$三点设计中心化Gram行列式为$1/3$；$a=2,b=-1,\delta a=1,\delta b=0,\kappa=1$的pinch数变化为$-1/6$；乘积项例子$h=1/2,d=3$的第四点对比为$3/4$。连续剖面反例的若干有理数代入也满足通量抵消。

这些有限实例核查不是一般证明；一般结论的依据是第4–7节的解析推导。未用采样替代证明，未将输出长度、公式或工具调用数量作为科研能力评分。
