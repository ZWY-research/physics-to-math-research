# Fable 2010 Stage B：定态电子密度梯度的条件响应

## 1. Source and Skill Version

**结果摘要。** 本次推导两种温度梯度响应的谱级分解，证明一个带明确余量的符号/大小保证命题，并构造平均频率始终相同、响应排序却不同的三波数反例。命题对 Fable 实际本征谱的适用性尚未核实；证明没有被升级为实际等离子体响应定律。

| 项目 | 实际使用材料与读取方式 |
|---|---|
| Skill | physics-to-math-research **v0.2.9**；Canonical commit **21c2719942c556469c54aabf96f4b4e4d5fdc32d** |
| Git blob | SKILL.md 对象 **c32e3d152c3da396a32d9e67f036f5155a227b40**；22287 bytes |
| Skill SHA-256 | **0fc3c572951edbc8357aa2779edba33cb21dc2697b6022a2ec32b8ff800342c2** |
| 实际加载 | 从 Canonical 执行下面的 git show，完整读取历史对象；以 Python subprocess.check_output 接收同一对象原始 bytes，hashlib.sha256 计算哈希，未经过 PowerShell 文本重编码 |
| 版本隔离 | 未使用当前工作树 SKILL.md 替代历史版本。初次 Git 读取触发 ownership 检查后，只加命令级 safe.directory，未修改全局配置或 Canonical |
| 辅助协议 | 同一 commit 的 references/mathematical-verification.md、references/research-deliverables.md，以 git show 读取；它们仅作解释，SKILL.md 为运行规范 |
| 论文 | E. Fable, C. Angioni, O. Sauter (2010), PPCF 52, 015007，[DOI](https://doi.org/10.1088/0741-3335/52/1/015007)；Stage A 已核验的 EPFL 26 页首次修订作者稿 |
| PDF SHA-256 | **8512a8ed73eae5348484fe33c93ff7d16d6ae6230bc8ef2f2bf764444e83f56c** |
| 证据报告 | [source-evidence.md](../source-evidence.md)，本轮初始 SHA-256：**bade53f0441838094a9bb8b37afdd759930c94121b0ccf4fe317f86e54e36452** |
| 本轮复核 | 重看已有原 PDF 渲染 p.5、10、11，核对式(11)–(14)、(19)–(21)、系数依赖和压力协议；其余依据沿用 Stage A 的定位及不确定性 |
| 工具 | 现有 Python 3.13.15 / SymPy 1.14.0 作精确代数检查；Git/PowerShell 读取、哈希和文件核查。未安装软件或运行新 gyrokinetic 模拟 |
| 日期与输出 | 2026-10-20，Asia/Shanghai；本轮仅创建此 research-result.md |

实际历史读取命令：

~~~powershell
git -c safe.directory="$CANONICAL_REPO" -C "$CANONICAL_REPO" show 21c2719942c556469c54aabf96f4b4e4d5fdc32d:SKILL.md
~~~

两个辅助文件的 SHA-256 依次为 edd7771ba829b32e643dec1421b13bd67ae0bb952d73f50febbe3d68902914d1、e6b3f33d9edba924354e58f3db0a61ba809dc276395e32966da29199e6682285。本轮没有读取其他论文的既往数学评议。

下文 **[A]** 是论文已有物理/数值依据，**[B]** 是本次附加分析假设，**[C]** 是已完成的数学推导/证明，**[D]** 是实际物理未决项。同一结果的数学成立与物理适用可有不同状态。

## 2. Physical Problem and Control Protocol

### 2.1 目标与物理范围

用 \(g_n=R/L_{ne},g_e=R/L_{Te},g_i=R/L_{Ti}\)，证明中简记
\[
u=g_n,\qquad x=g_e,\qquad y=g_i.
\]
\(n_e,n_i\) 仍指物理密度。目标是在同一零通量根分支 \(u=h(x,y)\) 上研究
\[
s_e=\left.\partial_xh\right|_{y,p},\qquad
s_i=\left.\partial_yh\right|_{x,p}. \tag{B1}
\]
这是相同无量纲梯度增量下的响应。比较符号、比较绝对值、比较弹性 \(xs_e,ys_i\) 是不同命题；本文讨论前两种，不把它们混用。

**[A]** 原文 p.4–5，§2，式(11)–(13)给出局域通量分解与无源定态；p.5 明确 bulk 系数随梯度变化，只有固定背景的 passive species 严格线性。p.9–10 微量电子 packet 提取的是给定背景的系数，不直接等于改变 bulk 梯度的总导数。

范围保持芯部、局域、静电、两 bulk 物种、忽略粒子源与新经典 pinch。本报告研究准线性闭合的条件响应，不证明全非线性 gyrokinetic 解、径向输运时间稳定性或装置中的机制唯一性。

### 2.2 两个不能混淆的控制协议

首选§3.4背景：\(T_e/T_i=1.5,\hat\nu=0,q=1.4,s=0.8,\epsilon=0.12\)。固定局域 \(n_e=n_i,T_i,T_e,B_0,R\)、物种参数、波数网格及归一化。改变局域温度梯度不同时改变局域温度值；准中性下两 bulk 密度梯度同为 \(u\)。

- **F：固定 \(\alpha\)**，独立改变 \(u,x,y\)，冻结局域几何。它是分离几何反馈的对照，不声称是原文实际扫描或任意全局 MHD 平衡。
- **P：论文压力协议**，每点重算 \(\alpha=-q^2d\beta/d\rho\)。几何反馈必须同时进入三个梯度方向，包括密度方向。

**[C，基于 A 的代数]** 令 \(\beta_e=2\mu_0n_eT_e/B_0^2,\beta_i=2\mu_0n_iT_i/B_0^2\)。固定上述局域值与 \(q\)，则
\[
\begin{aligned}
\alpha(u,x,y)&=q^2[(\beta_e+\beta_i)u+\beta_e x+\beta_i y],\\
\alpha_u&=q^2(\beta_e+\beta_i),\quad
\alpha_x=q^2\beta_e,\quad \alpha_y=q^2\beta_i .
\end{aligned} \tag{B2}
\]
因为 \(\partial_\rho(n_eT_e)=-n_eT_e(u+x)\)，离子项同理，故符号为正。这是原文定义的局域推论，不是新增输运闭合。若温度值、密度值、\(q\) 或单位也改变，需重新求这些导数。

图1横轴 \(L_{Ti}/L_{Te}=x/y\)：固定 \(x\) 的曲线向右意味着 \(y\) 减小；固定比值跨曲线则两种梯度同时变化。两者均不能直接替代(B1)。

## 3. Minimal Mathematical Formulation

### 3.1 原有谱合成的改记号

**[A]** 从原文式(14)–(15)、p.10 单模通量定义和式(19)出发，在固定有限波数集合 \(\mathcal K\) 上记
\[
\begin{aligned}
w_k&=|\widetilde\Phi_k(0)|^2
=A_0(\gamma_k/K_k)^2\Delta k_y,\quad K_k=\langle k_\perp^2\rangle_k,\\
\varphi_k&=a_ku+b_kx+c_k,\quad (a_k,b_k,c_k)=(A'_k,B'_k,C'_k),\\
\Gamma_e^{QL}&=\sum_{k\in\mathcal K}w_k\varphi_k .
\end{aligned} \tag{B3}
\]
这里 0 指 \(\theta=0\)；\(K_k\) 已经是平方波数平均。指数2是论文选用的 \(\zeta\)，不是线性理论证明的饱和定律。\(a_k,b_k,c_k,w_k\) 都可依赖 \((u,x,y,\alpha;p)\)。没有增加 \(y\) 的独立加性输运系数；这些系数与通量均为取实后的实数量。

\(b_kx\) 是电子温度梯度的显式入口；离子梯度通过耦合离子响应、模频率/增长率、场和本征函数进入系数与权重。几何另按协议变化。真实动力学中这些变化不必独立。

**[B]** 为使用对数权重和普通导数，先限定固定有限活跃谱：\(w_k>0,\gamma_k>0,K_k>0\)，相关函数在邻域内为 \(C^1\)。它对应可平滑追踪的本征支，远离初值代码选支突变；论文没有证明这个条件。原文13个固定波数适合有限和；连续谱推广需另检查交换积分与求导，本轮不作推广。

定义
\[
W=\sum_kw_k>0,\quad \mu_k=w_k/W,\quad
\langle v\rangle_\mu=\sum_k\mu_kv_k,\quad
G=\Gamma_e^{QL}/W=\langle\varphi\rangle_\mu . \tag{B4}
\]
令 \(\mathcal A=\langle a\rangle_\mu,\mathcal B=\langle b\rangle_\mu,\mathcal C=\langle c\rangle_\mu\)，则
\[
G=\mathcal A u+\mathcal Bx+\mathcal C,\quad
F=G/\mathcal A=u+C_Tx+C_P,\quad
C_T=\mathcal B/\mathcal A,\quad C_P=\mathcal C/\mathcal A. \tag{B5}
\]
写 \(F\) 要求 \(\mathcal A\ne0\)。原文整体 \(A'=W\mathcal A\)，并非两者数值相等。只要 \(W>0\)，\(G=0\) 与原零通量等价；先用 \(G\) 求导，避免把比值误当成常系数。

### 3.2 承重假设的地位

**[B]** 根分支还需基准零点、非退化性或括根区间；这些不是 ITG 标签的推论。主命题只要求总 \(\mathcal A>0\)，不假设每个 \(a_k>0\)。Stage A M6 的简化解析扩散正性是动机，不能替 full kinetic 数值证明全部假设。

单模归一化采用论文的 \(\theta=0\) 势幅度约定。换按波数变化的归一化会重新分配“单模系数变化”和“权重变化”的数值，总导数不变。这些是给定约定后的可计算分项，不自动成为独立物理因果机制。

## 4. Conditional Response Derivation

### 4.1 五种贡献的求导分解

对 \(z\in\{u,x,y\}\)，定义其他梯度与 \(p\) 固定时的导数：
\[
\mathscr D_z^F=\partial_z|_\alpha,\qquad
\mathscr D_z^P=\partial_z|_\alpha+\alpha_z\partial_\alpha . \tag{B6}
\]
这是对通量函数的偏导，还没有沿定态根求全导。记
\[
\begin{aligned}
\ell_{kz}&=\mathscr D_z\log w_k,\\
\chi_{kz}&=u\mathscr D_z a_k+x\mathscr D_z b_k+\mathscr D_z c_k,\\
\mathcal R_z&=\langle\chi_z\rangle_\mu,\quad
\mathcal S_z=\operatorname{Cov}_\mu(\varphi,\ell_z),\quad
\mathcal U_z=\mathcal R_z+\mathcal S_z .
\end{aligned} \tag{B7}
\]
\(\mathcal R_z\) 是单模系数变化，\(\mathcal S_z\) 是相对谱重分配；几何分别通过系数与权重的导数进入。

商法则给
\[
\mathscr D_z\mu_k=\mu_k(\ell_{kz}-\langle\ell_z\rangle_\mu). \tag{B8}
\]
再以
\(\mathscr D_z\varphi_k=\mathbf1_{z=u}a_k+\mathbf1_{z=x}b_k+\chi_{kz}\)
代入有限和的乘法则，得到 **[C]**
\[
\boxed{G_u=\mathcal A+\mathcal U_u=:H,\quad
G_x=\mathcal B+\mathcal U_x,\quad G_y=\mathcal U_y.} \tag{B9}
\]
(B8)–(B9)在邻域内成立，不仅在根处。根处 \(\langle\varphi\rangle_\mu=0\)，故
\(\mathcal S_z=\langle\varphi\ell_z\rangle_\mu\)；总通量零不意味着它为零。

固定网格、\(\zeta=2\) 时，
\[
\ell_{kz}=\mathscr D_z\log A_0+
2\left(\frac{\mathscr D_z\gamma_k}{\gamma_k}
-\frac{\mathscr D_zK_k}{K_k}\right). \tag{B10}
\]
移动网格还会有 \(\mathscr D_z\log\Delta k_y\)，本协议没有。共同的 \(A_0\) 项在协方差中抵消；\(K_k\) 的变化包括几何与本征函数形状变化，不能只看增长率。

### 4.2 条件响应、存在性与分母

**[C]** 若 \(G(u_0,x_0,y_0)=0,G\in C^1,H_0\ne0\)，则隐函数定理保证该点附近唯一的局部 \(C^1\) 根图 \(u=h(x,y)\)，不保证其他位置没有根。这里采用该定理是为处理已由论文提出的自洽零点，而非默认添加平衡方程。

对 \(G(h(x,y),x,y)=0\) 求导得
\[
\boxed{
s_e=-\frac{\mathcal B+\mathcal R_x+\mathcal S_x}
{\mathcal A+\mathcal R_u+\mathcal S_u},\qquad
s_i=-\frac{\mathcal R_y+\mathcal S_y}
{\mathcal A+\mathcal R_u+\mathcal S_u}.} \tag{B11}
\]
所有量取在同一个根、同一控制协议上。\(\mathcal B\) 是显式电子温度驱动，\(\mathcal R,\mathcal S\) 保留背景响应，分母是定态密度反馈。离子分子没有显式 \(\mathcal B\)，并不意味着它小。固定 tracer 背景的响应不能代替整个分子或分母。

由(B5)，根处 \(G_z=\mathcal A F_z\)，交叉得到
\[
\begin{aligned}
s_e&=-\frac{C_T+x\mathscr D_xC_T+\mathscr D_xC_P}
{1+x\mathscr D_uC_T+\mathscr D_uC_P},\\
s_i&=-\frac{x\mathscr D_yC_T+\mathscr D_yC_P}
{1+x\mathscr D_uC_T+\mathscr D_uC_P}.
\end{aligned} \tag{B12}
\]
其中系数导数必须重算 bulk 背景。比较同一根上的绝对值时，共同非零分母抵消；但参数变化会移动根并改变分子，不能说密度反馈对实际排序永远无作用。

沿扫描路径只能得到
\[
dh/dt=s_e\,dx/dt+s_i\,dy/dt. \tag{B13}
\]
例如固定 \(x\)，用 \(r=x/y\) 作横轴，则 \(dh/dr=-x s_i/r^2\)，不是 \(s_e\)。固定比值而改变 \(x\) 则为 \(s_e+s_i/r\)；一个路径斜率一般不能识别两个偏导数。

### 4.3 重算 \(\alpha\) 与冻结 \(\alpha\) 的精确差异

在两个协议共享的基准点，记
\(H_F=G_u|_\alpha,N_{eF}=G_x|_\alpha,N_{iF}=G_y|_\alpha,Z=G_\alpha\)。
则
\[
H_P=H_F+\alpha_u Z,\qquad
s_j^P=-\frac{N_{jF}+\alpha_j Z}{H_F+\alpha_u Z},
\quad j=e,i, \tag{B14}
\]
其中 \(\alpha_e=\alpha_x,\alpha_i=\alpha_y\)。两分母非零时，通分得
\[
\boxed{s_j^P-s_j^F
=-\frac{Z(\alpha_j+\alpha_u s_j^F)}{H_F+\alpha_u Z}.} \tag{B15}
\]
几何同时改分子和分母；密度方向的 \(\alpha_u Z\) 不能遗漏。这只比较共享点的局部响应，不声称离开该点两协议的根仍相同。

## 5. Main Mathematical Proposition and Proof

### 5.1 谱级预算界

定义
\[
\begin{aligned}
\sigma_\mu(v)^2&=\langle(v-\langle v\rangle_\mu)^2\rangle_\mu,\\
r_z&=\langle|\chi_z|\rangle_\mu,\qquad
\varepsilon_z=r_z+\sigma_\mu(\varphi)\sigma_\mu(\ell_z).
\end{aligned} \tag{B16}
\]
这些不是新输运系数，而是对现有反馈项的保守控制量；需要逐模梯度变化才能计算。真实模型中系数变化与谱变化可以相关，证明不要求独立。

**[C]**
\[
|\mathcal U_z|\le\varepsilon_z. \tag{B17}
\]
**证明。** 三角不等式给 \(|\mathcal R_z|\le r_z\)；对中心化有限向量使用带权 Cauchy–Schwarz，
\[
|\mathcal S_z|
=|\langle(\varphi-\langle\varphi\rangle_\mu)
(\ell_z-\langle\ell_z\rangle_\mu)\rangle_\mu|
\le\sigma_\mu(\varphi)\sigma_\mu(\ell_z).
\]
相加即得。总通量为零只消掉均值，不消掉 \(\sigma_\mu(\varphi)\)。证毕。

### 5.2 主命题：根、符号与响应大小的余量保证

**[B，前提]** 在所选协议下取 \(I=[u_-,u_+]\) 及控制量开邻域 \(V\ni(x_0,y_0)\)。假定：

1. 有限活跃谱及其 \(C^1\) 条件在包含 \(I\times V\) 的开集成立。
2. 存在 \(\mathcal A_{\min}>0,0\le\rho<1\)，柱内有
   \[
   \mathcal A\ge\mathcal A_{\min},\qquad
   \varepsilon_u\le\rho\mathcal A. \tag{B18}
   \]
3. 基准控制下严格括根：
   \[
   G(u_-,x_0,y_0)<0<G(u_+,x_0,y_0). \tag{B19}
   \]

尤其(B18)不是 ITG 标签的推论。

**[C，结论]** 缩小 \(V\) 后，每个控制点在 \(I\) 内恰有一个根，形成 \(C^1\) 分支。令根处直接热扩散强度 \(\tau=-\mathcal B\)：

(i) 若 \(\tau>\varepsilon_x\)，则 \(s_e>0\)，并有
\[
\frac{\tau-\varepsilon_x}{\mathcal A+\varepsilon_u}
\le s_e\le
\frac{\tau+\varepsilon_x}{\mathcal A-\varepsilon_u},
\qquad
|s_i|\le\frac{\varepsilon_y}{\mathcal A-\varepsilon_u}. \tag{B20}
\]

(ii) 若更强地
\[
\boxed{\tau>\varepsilon_x+\varepsilon_y,} \tag{B21}
\]
则 \(s_e>|s_i|\)。

(iii) 严格括根、非退化及排序余量在足够小的 \(C^1\) 谱数据扰动下保持。仅控制谱值不控制谱导数，不能保证响应排序。

**完整证明。**

由(B17)–(B18)，
\[
H=G_u\ge\mathcal A-|\mathcal U_u|
\ge(1-\rho)\mathcal A_{\min}>0. \tag{B22}
\]
因此对每个固定 \((x,y)\)，函数 \(G\) 随 \(u\) 严格递增。由端点连续性和(B19)的严格符号，缩小 \(V\) 后端点符号仍成立。介值定理给至少一个根，严格递增给至多一个根。每个根处(B22)保证非退化，隐函数定理给局部 \(C^1\) 根图；图在重叠部分因根唯一而一致，故构成所述分支。唯一性只在 \(I\) 内，不是全局断言。

在根上，(B11)为
\[
s_e=(\tau-\mathcal U_x)/H,\qquad s_i=-\mathcal U_y/H.
\]
由 \(|\mathcal U_x|\le\varepsilon_x<\tau\) 与 \(H>0\)，电子响应严格为正。再用
\(\mathcal A-\varepsilon_u\le H\le\mathcal A+\varepsilon_u\)
及两分子的界，得到(B20)。

若(B21)成立，则
\[
\tau-\mathcal U_x\ge\tau-\varepsilon_x
>\varepsilon_y\ge|\mathcal U_y|.
\]
除以同一个正 \(H\) 就得到 \(s_e>|s_i|\)。由于使用共同分母，不需额外比较两个松分母界。

最后，在较小的闭邻域内，有限个正权重离零有界；小的 \(C^1\) 扰动使 \(G,G_z,\mathcal A,\mathcal B,\varepsilon_z\) 连续变化。严格括根与(B22)有正余量；若(B21)在基准根严格成立，根的连续性使它在更小根邻域也有正余量。因此足够小的上述扰动仍保留端点符号、根的非退化及排序，重复前面证明即可。只控制 \(C^0\) 谱值不能控制 \(G_z\)，该步骤便不成立；§6–7给出明确见证。证毕。

**物理对应与强度。** (B16)将可变项分成单模响应变化和相对谱变化；(B21)是直接热扩散超过两种反馈预算的保守充分条件，不是必要条件。它没有假定真实 ITG 满足这些界，界失效也不证明反向排序。研究成果超出“只要非退化就可用隐函数定理”：它给出了可从谱诊断构造的响应余量与根存在/局部唯一检查。

**[D]** 论文没有输出所需逐模导数；因此尚不能据此判断 Fable 的任何实际 ITG 点是否满足(B21)。

### 5.3 异号通量的谱重分配命题及相反排序的充分条件

固定零通量点，令 \(\mathcal O=\{k:\varphi_k>0\}\)、
\(\mathcal I=\{k:\varphi_k<0\}\)，假定存在非零异号贡献。则
\[
P=\sum_{\mathcal O}\mu_k\varphi_k
=\sum_{\mathcal I}\mu_k(-\varphi_k)>0.
\]
定义各组按**通量贡献**加权的相对权重导数：
\[
L_z^+=P^{-1}\sum_{\mathcal O}\mu_k\varphi_k\ell_{kz},\qquad
L_z^-=P^{-1}\sum_{\mathcal I}\mu_k(-\varphi_k)\ell_{kz}.
\]
**[C]**
\[
\boxed{\mathcal S_z=P(L_z^+-L_z^-).} \tag{B23}
\]
**证明。** 根处协方差均值修正为零，拆分
\(\sum_k\mu_k\varphi_k\ell_{kz}\)，正组给 \(PL_z^+\)，负组给
\(-PL_z^-\)，零组无贡献。证毕。

在 \(H>0,\mathcal R_y=0\) 时，若外向组的平均相对权重增速高于内向组，
\(L_y^+>L_y^-\)，则 \(s_i<0\)；反之为正。若 \(\mathcal R_y\ne0\)，应判断
\(\mathcal R_y+P(L_y^+-L_y^-)\) 的符号。

同一结构也能保证**离子响应绝对值较大**，无需预设电子占优。具体地，若 \(\tau=-\mathcal B>0,H\ne0\)，且
\[
P|L_y^+-L_y^-|-r_y>\tau+\varepsilon_x, \tag{B24}
\]
则 \(|s_i|>|s_e|\)。

**证明。** 反三角不等式与(B23)给
\[
|\mathcal U_y|\ge|\mathcal S_y|-|\mathcal R_y|
\ge P|L_y^+-L_y^-|-r_y,
\]
而 \(|\mathcal B+\mathcal U_x|\le\tau+\varepsilon_x\)。由(B24)比较两个分子的绝对值，再除以共同 \(|H|>0\) 即得。证毕。

(B21)与(B24)是不同谱响应情形的充分条件；原文没有足够导数数据验证其中任何一个。它们把比较问题落到真实可测算的响应预算与异号通量组的权重变化上，不把通量方向与 ITG/TEM 名称等同。

## 6. Counterexample and Failure Conditions

### 6.1 明确的三波数见证

**[B，允许类与限制]** 以下是遵守原通量分解、正谱权重和零通量结构的简化谱合成模型，用于攻击无附加条件的结构性排序推断。**没有证明它是实际 gyrokinetic 本征问题的解；它不是 Fable 数据拟合、ITG/TEM 新机制或新增物理输运闭合。** 在真实本征谱可实现子类内能否实现此行为仍是未决问题。

取三个不同波数，设
\[
a=(1,1,1),\quad b=(-1/2,-1/2,-1/2),\quad
c=(-3,-2,1),\quad \omega_R=(-3,-2,-1). \tag{B25}
\]
三个频率全为负。基准 \(x_0=y_0=4\)，任意实 \(\kappa_e,\kappa_i\)，令
\[
t=\tanh[\kappa_e(x-4)+\kappa_i(y-4)],\qquad
w=(1+t,\ 2-2t,\ 1+t). \tag{B26}
\]
\(-1<t<1\) 保证权重严格正，\(W=4\)。单模系数不变，非平凡反馈只来自相对谱重分配。直接计算
\[
\begin{aligned}
\mathcal A&=1,\quad \mathcal B=-1/2,\quad
\mathcal C=-3/2+t/2,\\
G&=u-x/2-3/2+t/2,\qquad
h(x,y)=x/2+3/2-t/2 .
\end{aligned} \tag{B27}
\]
\(H=1\)，根唯一且光滑；基准根为 \(7/2>0\)。基准单模通量
\(\varphi=(-3/2,-1/2,5/2)\)，加权贡献为
\((-3/2,-1,5/2)\)，严格相消而各自非零。并且
\[
\omega_R^{QL}
=\frac{-3(1+t)-2(2-2t)-(1+t)}4=-2 \tag{B28}
\]
对整个邻域恒成立。\(C_T=-1/2,C_P=-3/2+t/2<0\) 也始终成立。不存在靠零点退化、权重负值或反转直接热扩散系数制造结果的问题。

直接求导：
\[
\begin{aligned}
s_e&=1/2-(\kappa_e/2)\operatorname{sech}^2[\kappa_e(x-4)+\kappa_i(y-4)],\\
s_i&=-(\kappa_i/2)\operatorname{sech}^2[\kappa_e(x-4)+\kappa_i(y-4)] .
\end{aligned} \tag{B29}
\]

| 基准 \((\kappa_e,\kappa_i)\) | \(s_e\) | \(s_i\) | 结论 |
|---|---:|---:|---|
| \((0,0)\) | \(1/2\) | \(0\) | 固定谱时只有直接电子响应 |
| \((0,-4)\) | \(1/2\) | \(2\) | 两者都为正，离子响应仍可更大 |
| \((0,4)\) | \(1/2\) | \(-2\) | 离子响应可反号且绝对值更大 |
| \((2,0)\) | \(-1/2\) | \(0\) | 内向 \(C_T\) 不保证 bulk 电子梯度响应为正 |

四个见证有同一基准权重、单模系数、频率、根和通量贡献；平均频率函数也完全相同。仅权重对梯度的变化不同。因此在明确声明的谱合成类中，基准谱值及一个平均频率函数不能识别条件响应。它不是已找到实际 ITG 物理反例的声明。

也可保留式(19)的权重代数：选三个固定波数及正 \(K_k,\Delta k_y\)，令 \(A_0=1\)，取
\[
\gamma_k=K_k\sqrt{w_k/\Delta k_y}>0 .
\]
则 \(w_k=(\gamma_k/K_k)^2\Delta k_y\) 精确成立。**这只证明权重规则本身不排除见证，不证明这些增长率、频率与响应系数能同时由 gyrokinetic 方程产生。**

### 6.2 对充分条件的压力测试

这里 \(\mathcal R_z=0,\mathcal U_u=0\)，基准
\(\mathcal S_x=\kappa_e/2,\mathcal S_y=\kappa_i/2\)。
在 \((0,-4)\) 时 \(\tau=1/2,|\mathcal U_y|=2\)，任何合法
\(\varepsilon_y\) 均至少为2，故(B21)不能成立；在 \((2,0)\) 时
\(\mathcal U_x=1>\tau\)，正电子响应的充分条件也不能成立。反例攻击的是省略谱反馈的无条件推断，没有推翻主命题。


充分条件不是空条件：在同一数学见证类取 \(\kappa_e=\kappa_i=1/8\)，基准处有
\(\sigma_\mu(\varphi)=3/2\)、\(\sigma_\mu(\ell_z)=|\kappa_z|\)，且 \(r_z=0\)。
所以 \(\varepsilon_x=\varepsilon_y=3/16,\varepsilon_u=0\)，
\(\tau-(\varepsilon_x+\varepsilon_y)=1/8>0\)，实际
\(s_e=7/16,s_i=-1/16\)，符合主命题；严格余量保证其在足够小邻域继续成立。这只验证条件命题在含非零谱反馈的数学模型中有内容，不验证真实本征谱满足条件。

### 6.3 推导与解释的失效边界

1. **根缺失或根分支混淆。** 未有基准零点/括根不能使用响应公式；局部非退化不保证全局唯一，跨根比较不是同一条件响应。
2. **\(H=0\) 或接近零。** 分母退化须另分析；可能有折叠、分裂或特殊光滑结构，不能自动断言其中任一种。接近零使误差放大；总扩散正不排除密度反馈抵消。
3. **本征支或选模规则非光滑。** 最不稳定支交换、主导本征函数突变、简并及接近稳定阈值可能破坏 \(C^1\)。仅有频率平滑过零、ITG/TEM 标签改变，本身并不必然使导数失效。
4. **零权重与活跃集变化。** \(w_k=0\) 时对数形式失效；可回到原始有限和检查可微性，不能直接延续本报告的 score 公式。
5. **控制协议或谱范围改变。** 改 \(\hat\nu,T_e/T_i\)、加入 \(k_x\)、次主导/稳定模或改变局域值，必须重新说明偏导条件。
6. **静态条件被误作时间稳定性。** \(H>0\) 是本报告单调性与条件数条件，不是输运 PDE 稳定性证明。Stage A 记录的原文 p.11 的 \(dX^{out}/dX^{in}>1\) 缺少推导，本轮不依靠或擅改它。

## 7. Spectral Feedback and Mechanism Limits

### 7.1 零通量并不消除谱反馈

**[A]** §3.4.2、图2提供异号波数贡献相消的实际例子。**[C]** (B23)说明相消只约束通量值，不约束两组相对权重的变化；即使单模系数冻结，\(\mathcal S_z\) 仍可改变排序。

共同正倍率不同：把所有 \(w_k\) 乘同一 \(C(u,x,y)>0\)，有
\(\Gamma\mapsto C\Gamma\)，根不变，根处通量偏导共同乘 \(C\)，响应不变。对数权重增加同一 \(\mathscr D_z\log C\) 也不改协方差。故共同 \(A_0\) 不是判别数据，相对谱及其梯度导数才是。

还可严格区分根位置稳健与响应稳健。若原根区间内 \(G_u\ge m>0\)，另一闭合
\(\widetilde G=G+\delta G\) 在同一区间有根 \(\tilde h\)，且
\(\sup|\delta G|\le\eta\)，则
\[
|\tilde h-h|\le\eta/m. \tag{B30}
\]
**证明。** \(G(h)=0,\ |G(\tilde h)|=|\delta G(\tilde h)|\le\eta\)，再由中值定理及导数下界即得。此界没有保证扰动根存在；存在是已声明前提。

它也不控制根的导数：把(B26)的 \(t\) 换为
\(\epsilon\tanh[(y-4)/\epsilon^2]\)，\(0<\epsilon<1\)。各权重与固定谱 \(t=0\) 相差 \(O(\epsilon)\)，根也只差 \(O(\epsilon)\)，但基准 \(s_i=-1/(2\epsilon)\)。正权重、恒定负平均频率与零通量结构仍保留。故“通量或定态很接近”不能代替响应导数验证。这仍是数学见证类中的谱扰动，不是新物理闭合。

### 7.2 动力学项的物理意义与证据限制

**[A]** Stage A M2/M5，即原文式(3)、(16)，给出电子温度驱动的 \(E/T_e-3/2\) 能量核，俘获响应的
\((\omega_R-\bar\omega_d)^2+(\gamma+\nu)^2\) 分母，及 \(C_P\) 分子中的
\(\nu\omega_R+\gamma\bar\omega_d\)；passing 响应与平行 Landau 动力学有关。改变梯度可能改变失谐、宽度、模结构和能量选择，故 \(\mathcal R_x,\mathcal R_y\) 不应先验为零。

这些核提供可能的符号变化途径，却没有约束单模导数一定小于直接驱动。能量核可正可负，\(\omega_R,\gamma\) 与本征函数对梯度的导数也未给出。由 ITG 负频率或 \(C_T<0\) 直接推出(B21)，缺少中间证据；由此断言(B24)也同样没有根据。

Stage A 关于深俘获近似、barely trapped、相位印刷疑点和归一化的限制仍在。本轮从已核验的通量合成层证明结论，没有将有疑点的算子相位推导用作严格符号依据。

### 7.3 一个平均频率为什么通常不够？

\(\omega_R^{QL}=\langle\omega_R\rangle_\mu\) 只保留一个谱矩。即便有其导数，
\[
\mathscr D_z\omega_R^{QL}
=\langle\mathscr D_z\omega_R\rangle_\mu+
\operatorname{Cov}_\mu(\omega_R,\ell_z),
\]
也不同于决定通量响应的
\(\operatorname{Cov}_\mu(\varphi,\ell_z)\)，还缺单模通量系数变化。§6的平均频率及其所有梯度导数都相同，响应却不同。

所以“平均频率不足”的严格结论相对于已声明的谱合成类成立；它没有证明真实 gyrokinetic 可实现类一定包含该反例，也没有否定在额外受约束的本征谱子类中平均频率可能有判别力。所需额外约束不能自行假定。

## 8. Discriminating Numerical Tests

只设计两个计算，不实际运行。目标是判定(B9)、(B16)、(B23)中的缺失项。

### 测试一：GS2 局域谱导数与几何协议对照

先在§3.4背景计算确认一个 ITG 主导、存在可连续追踪本征支的基准零点，不能仅凭图上标签认为这些前提已满足。

1. 括定密度根并检查局部通量斜率。在共享基准点固定 \(\alpha\)，取中心及 \(u,x,y\) 三方向正负扰动七点，再加 \(\alpha\) 正负扰动两点，一个步长层级共九个 bulk 线性谱背景。
2. 每点保存相同网格上的 \(\gamma_k,\omega_{Rk},\widetilde\Phi_k(\theta)/\widetilde\Phi_k(0),K_k\)。用 \((1,0),(0,1),(0,0)\) 三种微量电子 packet 梯度提取相同归一化下的 \(a_k,b_k,c_k\)，并统一 packet 与 bulk 浓度的换算。packet 提取保持该点 bulk 不变；不同 bulk 点之间的差分才是系数背景导数。
3. 估计 \(\mathcal R_z,\mathcal S_z,H,\tau,\varepsilon_z\) 及通量正负组的 \(L_z^\pm\)，不只输出 \(C_T,C_P\)。用(B2)、(B14)重建压力协议导数，判断几何项是否改变符号、排序或条件数。
4. 对决定结论的导数缩半步长并跟踪本征支；余量与误差同量级时不认证排序。选择最有判别力的温度梯度方向重算扰动后的密度根，检查隐式预测与根位移一致性。

**判别力：** 可区分直接驱动、单模变化、相对谱变化、几何和密度反馈；检验(B21)或(B24)，或直接估计(B11)。有限差分本身不证明全邻域 \(C^1\) 或区间上的界，若要严格认证还需相应误差/覆盖依据。九点是已知基准根后的谱导数 stencil，不包括预先找根和必要收敛检查的成本。

### 测试二：针对一个关键背景的非线性 GYRO 核查

若测试一预言明确排序，或排序主要依赖敏感的 \(\mathcal S_z\)，只选一个最有判别力的背景。采用同物种、单位与控制协议，以实际计算出的非线性零通量状态为中心，取中心及 \(u,x,y\) 正负扰动共七个背景。

保存饱和后平均粒子通量、\(k_x,k_y\) 分辨的通量与势谱，以及足以区分信号的平均误差；估计
\[
s_e^{NL}\simeq-\frac{\partial_x\langle\Gamma_e^{NL}\rangle}
{\partial_u\langle\Gamma_e^{NL}\rangle},\qquad
s_i^{NL}\simeq-\frac{\partial_y\langle\Gamma_e^{NL}\rangle}
{\partial_u\langle\Gamma_e^{NL}\rangle}.
\]
仍需非退化和局部正则；分母近零、误差过大或饱和状态切换时不报排序。每点固定或重算 \(\alpha\) 的规则必须一致。

**判别力：** 判断准线性排序是否在完整 \(k_x\) 重分配与非线性饱和后保持；不一致时查看差异来自哪些波数。仅增加平均频率不能完成这个检验。七点不包括建立基准和必要分辨率/统计收敛检查；这不是无成本的现成数据。趋势相符也不证明微观机制唯一。

## 9. Research Outcome

### 9.1 四类结果的最终状态

| 类别 | 具体成果或依据 | 状态与限制 |
|---|---|---|
| A：论文已有 | 梯度依赖通量分解、tracer 提取、谱权重、异号谱抵消、二维梯度扫描、有限非线性对照 | 非本次新发现；保留作者稿与 Stage A 的适用范围 |
| B：本次附加 | 有限活跃谱 \(C^1\)、明确几何协议、总扩散正、括根和反馈余量、响应预算 | 可检验但尚未对实际本征谱验证，不能作为既定物理事实 |
| C：已完成证明 | 响应分解(B9)–(B12)、几何差(B15)、谱预算界与根/符号/排序命题、正负通量组公式及相反排序条件、三波数反例、根位置误差界 | 在各自前提与见证类内成立；超出仅重述隐函数定理 |
| D：实际物理未决 | 具体 ITG 点的响应符号/数值/排序、反例本征谱可实现性、充分条件实际是否满足、非线性排序是否保持 | **NOT ESTABLISHED**；关键缺口是逐模梯度导数、密度反馈和几何导数 |

跨学科解释：电子温度梯度确有直接入口，但改变它也会重组湍流；离子梯度能通过湍流变化影响电子通量。定态来自总通量零，所以不同波数如何相消以及如何重新分配，不能被一个标签代替。本次得到可计算的条件门槛，并证明不同谱反馈情形可支持不同排序；没有确定真实等离子体中的哪一种情形成立。

### 9.2 实际精确代数核查

Python/SymPy 经标准输入执行，未创建检查脚本或安装工具。实际结果：

- 对三个任意正权重的归一化加权和，符号求导减去“平均单模导数 + 协方差”精确化简为0。
- (B15)减去直接通分的几何响应差精确化简为0；(B2)三个偏导与公式一致。
- 反例的根残差为0，\(W=4,\omega_R^{QL}=-2,G_u=1\)，基准根 \(7/2\)，模贡献 \((-3/2,-1,5/2)\)；四组响应均精确为§6的有理数。

可复现的反例检查代码：

~~~python
import sympy as s
u, x, y, ke, ki = s.symbols("u x y ke ki", real=True)
t = s.tanh(ke*(x-4) + ki*(y-4))
w = s.Matrix([1+t, 2-2*t, 1+t])
phi = s.Matrix([u-x/2-3, u-x/2-2, u-x/2+1])
omega = s.Matrix([-3, -2, -1])
G = s.simplify(w.dot(phi)/sum(w))
h = x/2 + s.Rational(3, 2) - t/2
assert s.simplify(G.subs(u, h)) == 0
assert s.simplify(w.dot(omega)/sum(w)) == -2
assert s.diff(G, u) == 1
for pair in [(0, 0), (0, -4), (0, 4), (2, 0)]:
    values = {x: 4, y: 4, ke: pair[0], ki: pair[1]}
    print(pair, [s.diff(h, z).subs(values) for z in (x, y)])
~~~

代数核查辅助检查恒等式与见证；§5的完整解析证明不由数值抽样替代。工具没有验证未证的 gyrokinetic 物理映射。

### 9.3 交付与停止点

本轮仅创建：

experiments\fable-2010\skill-on-p1-v0.2.9\research-result.md

未修改 Canonical、正式 SKILL.md、Core/OAC、README、CHANGELOG、Regression、Research Observatory、PDF、source-evidence.md 或 Angioni 记录；未提交、推送、升级版本或发布网站。数学任务已完成到现有证据支持的条件结果；实际物理排序保留为未决，不据此修改 Skill 或自行开展模拟。
