# Fable et al. (2010)：电子粒子输运原文证据审查（阶段 A）

## 1. Source Identity

| 字段 | 核验记录 |
|---|---|
| 论文 | E. Fable, C. Angioni, O. Sauter, *The role of ion and electron electrostatic turbulence in characterizing stationary particle transport in the core of Tokamak plasmas* |
| 正式书目信息 | *Plasma Physics and Controlled Fusion* **52**, 015007 (2010)，[DOI / 出版社记录](https://doi.org/10.1088/0741-3335/52/1/015007)；出版社记录发布日期为 2009-12-01，卷年为 2010，二者不冲突 |
| 实际读取版本 | [用户指定的 EPFL 作者稿](https://infoscience.epfl.ch/server/api/core/bitstreams/8ea1f8f7-6547-4936-9208-85da5acd2bd6/content)，26 个 PDF 页面；不是期刊排版版本 |
| 版本识别 | PDF metadata title：`EF_PPCFpap2009_1stRevision.dvi`；creationDate：`D:20091004093933Z`；modDate：`D:20091015154331+02'00'`。可确认是带“1stRevision”标识的作者稿；是否等同最终 accepted manuscript **未核实** |
| 本地文件 | `experiments\fable-2010\fable-2010-epfl-author.pdf`，288771 bytes |
| SHA-256 | `8512a8ed73eae5348484fe33c93ff7d16d6ae6230bc8ef2f2bf764444e83f56c` |
| 身份核验 | PDF p.1 的标题、三位作者与出版社 DOI 记录匹配；作者稿正文未见 DOI 印字，DOI 由出版社书目关联核实，不声称从 PDF 本身读出 DOI |
| 阅读与视觉核验 | 本地文本提取用于定位；以 PyMuPDF 1.26.5 渲染原 PDF，视觉核对 p.1、3–8、10–13、20–26 的身份、关键公式、表格与全部结果图。§2–3.8 的相关正文已阅读；页码一律从 PDF 第一页计为 p.1 |
| 本地阅读附件 | `page-renders/page-NN.png` 保存页面图；`pdf-text.txt` 是可出错的定位辅助。PDF、页面图和工具目录已由本实验 `.gitignore` 排除，不提交公开仓库 |
| 日期与任务性质 | 2026-10-20（Asia/Shanghai）；定向文献取证，非正式 Skill ON 测试，非新的机制发现 |

定位约定：例如“p.13，§3.4.2，图2/p.21”表示正文在 PDF p.13，图在 PDF p.21。图1–7分别位于 p.20–26；不采用期刊版页码。

## 2. Scientific Scope

审查对象是局域、静电 gyrokinetic 模型中电子粒子通量的梯度分解、线性电子动力学和准线性谱闭合，以及无源、忽略新经典输运时的定态密度梯度。本文使用

\[
g_n=R/L_{ne},\qquad g_e=R/L_{Te},\qquad g_i=R/L_{Ti}.
\]

原文对任意物种先写 \(R/L_n=-\partial\log n/\partial\rho\)、\(R/L_T=-\partial\log T/\partial\rho\)，\(\rho=r/R\)。§3 只取主离子和电子为 bulk species，借准中性约束讨论两者一致的定态；下文通量与 pinch 均指电子。正通量取径向向外；通常 \(g_e>0\) 时，\(C_T<0\) 的热扩散贡献向内，\(C_P<0\) 的其他 pinch 向内。

物理层级须保留：

- **exact within the stated model**：§2 局域模型中的形式分解及在分母非零时的零通量关系；形式逆算子不等于求出了非线性饱和态。
- **linearized approximation**：§2.1 令非线性模耦合趋零，取复频率本征模；深俘获/近绝热 passing 的解析式比 full kinetic 计算更简化。
- **quasi-linear closure**：用线性本征函数与相移，加经验选择的相对谱权重，重建通量和 pinch。
- **numerical result**：GS2 参数扫描及少量 GYRO 非线性比较，只对所算背景提供证据。
- **empirical or interpretive statement**：§2.2 机制解释及§3.8 对既有实验趋势的解释；并非对实验数据的独立复核或机制唯一性证明。

模型与排序边界（p.2–3、6–12、18）：无粒子源、忽略 Ware 等新经典 pinch，以 \(\Gamma_{\rm turb}=0\) 求解；局域 flux-tube、ballooning 表示、shifted-circles \(s-\alpha\) 平衡、忽略磁扰动。p.3 原文写“low aspect ratio limit”，本报告保留其字面记录；数值实际取逆长宽比 \(\epsilon=0.12\)，不自行修订这一术语。研究针对芯部，典型 \(0.3\lesssim r/a\lesssim0.8\)、中半径附近；不能直接外推至边缘、高 \(\beta\) 电磁输运、强非局域剖面或所有 ETG 情形。原文未在此完整重列全部 gyrokinetic 渐近排序，不补写成已核实条件。

## 3. Evidence Map

只保留六项。以下“支持”均在上述模型与扫描条件内。

| ID / 科学主张 | 原文位置及类别 | 实际支持什么 | 缺少什么 / 不支持什么 | 对数学研究的具体价值 |
|---|---|---|---|---|
| E1：密度、电子温度梯度可在电子通量中显式分离，但系数随 bulk 湍流改变 | p.3–5，§2，式(1)–(13)；p.9–10，§3 开头。理论形式推导、test-particle 数值提取方法 | \(\Gamma_e=A'g_n+B'g_e+C'\)；\(C_T=B'/A',C_P=C'/A'\)。微量电子 packet 的梯度变化不改背景，故对 packet 梯度严格线性；改变 bulk 梯度会改系数 | 没有证明 bulk 系数为常数、定态唯一或可微；packet 的 \(B'\) 不是 bulk \(\partial\Gamma_e/\partial g_e\) 的全部 | 为“直接热扩散项”和“背景反馈项”提供有物理来源的区分；定态应作隐式问题 |
| E2：passing / trapped 的速度空间响应不同，频率、曲率和碰撞决定能量选择 | p.6–9，§2.1–2.2，式(16)–(18)。线性简化解析式与作者动力学解释 | passing 的平行 Landau 响应与 \(v_\parallel\simeq\omega_R/k_\parallel\) 相关；深俘获响应含 \((\omega_R-\bar\omega_d)^2+(\gamma+\nu)^2\) 分母及 \(E-3/2\) 温度核。碰撞还显式进入 \(\nu\omega_R+\gamma\bar\omega_d\) | “ITG 负频率与正漂移严格共振”不能由此得出；有限宽度核中的低能选择与精确共振要区分。barely trapped 未包含在简化式，定量需 full kinetic | 允许追问响应符号在何种频谱、漂移和碰撞条件下改变，而非预设电子/离子驱动大小 |
| E3：二维温度梯度扫描呈现接近混合区时定态梯度较大 | p.11–12，§3.2–3.4.1；表2/p.11、图1/p.20。自洽准线性数值结果及作者解释 | \(g_e=5,7,9,11,13\)，\(g_i=6,9,12\)，固定 \(T_e/T_i=1.5,\hat\nu=0,q=1.4,s=0.8\)。随 \(g_e/g_i\) 增大平均频率从 ITG 向 TEM 移动；\(\lvert C_T\rvert\) 在过渡附近较大，TEM 一侧明显减小；\(C_P\) 在该无碰撞扫描向 TEM 侧更负 | 图中连接线不是局部独立偏导数。\(C_T,C_P\)“主要依赖比值”只是数值近似，没有证明完全塌缩为一个变量，也无普适极值定理 | 提供可做条件响应识别的二维输入背景，而非只有一个比值；提示应检查隐式密度反馈与路径依赖 |
| E4：零总粒子通量由异号波数贡献抵消；少量非线性比较支持趋势 | p.12–13，§3.4.2–3.4.3；图2/p.21、图3/p.22。准线性谱诊断及非线性 GYRO 数值结果 | \(g_e=g_i=9\) 定态中，低波数 TEM 通量向外，中间 ITG 向内，短波电子支也可向内；\(\gamma\) 最大约在 \(k_y\rho_i=0.3\)，而 \(\gamma/\langle k_\perp^2\rangle\) 最大约在 0.15。GYRO 在固定 \(g_e=9\) 的少量点给出相符的通量符号/趋势 | 单个最不稳定模、平均频率或 ITG/TEM 标签不决定总通量。GYRO 比较未独立验证各微观贡献、全部扫描或响应偏导数；\(\zeta\) 与幅度有校准 | 使“谱权重扰动能否改变定态或响应符号”成为明确问题；反对从标签直接构造响应定律 |
| E5：碰撞性和剪切的作用取决于湍流背景 | p.8，§2.2，式(18)；p.13–15，§3.5–3.6；图4/p.23、图5/p.24。解析解释与准线性数值 | 碰撞既改变 pinch 核，也稳定 TEM、改变频率。低 \(T_e/T_i\) 的 ITG 背景下，\(C_P\) 可强烈向外、定态梯度降低；较高温度比时效应减弱。剪切扫描中低温度比的外向 \(C_P\) 可压过更强的内向热扩散，高温度比的混合背景则可随剪切增大而更尖峰 | 不是“碰撞总降低密度梯度”或“剪切总增加密度梯度”的定理。\(T_e/T_i\) 不是 \(g_e/g_i\)；保持一项不能代替保持另一项 | 明确条件参数必须进入响应问题；同标签或同平均频率仍可能有不同 \(C_T\) |
| E6：eITB 与实验解释仍受背景、谱和定量验证限制 | p.15–18，§3.7–3.8、§4；图6/p.25、图7/p.26。准线性扫描、对文献实验的引用和作者解释 | eITB 扫描用强反剪切、较大 \(g_e\)；随 \(g_i\) 增大可从 TEM 移向 ITG，较大碰撞性使过渡位置移向较小 \(g_i\)。热扩散在多数这些点占主导。跨扫描汇图把较大密度梯度与过渡附近联系起来 | 未证明 \(\omega_R^{QL}\) 是充分状态变量。作者提出需测量低/中波数湍流频率验证，并指出定量预言需非线性计算；本轮未追查实验引用的原始数据 | 界定可验证目标应是给定背景下的局部关系及其失效条件，不能宣称解释了特定装置或建立普适响应排序 |

## 4. Verified Mathematical Relations

选取八项核心关系；同项中的相邻原始编号用于补全定义。各项均已对照上述本地 PDF 页面视觉核验。公式保留作者的帽、横线和物理层级；不将简化解析式冒充 GS2 使用的 full kinetic 方程。

### M1. 非线性 gyrokinetic 入口及线性化位置

**原编号/位置：式(1)，算子定义式(2)，p.3，§2；线性极限 p.6，§2.1。**

\[
\mathbf L\widetilde{\mathbf g}+\mathbf N
=\mathbf W\widetilde{\boldsymbol\Phi}. \tag{1}
\]

其中式(2)给出

\[
L_{\mathbf k\mathbf k'}=
\left[\frac{\partial}{\partial t}
-\frac{v_\parallel}{Rq}\frac{\partial}{\partial\theta}
+i\omega_d+\widehat C\right]_{\mathbf k}I_{\mathbf k\mathbf k'},
\qquad
W_{\mathbf k\mathbf k'}=\frac{Ze}{T}
\left[\frac{\partial}{\partial t}+i\omega_*\right]_{\mathbf k}
F_0J_{0\mathbf k}I_{\mathbf k\mathbf k'}.
\]

非线性项按原文为

\[
\mathbf N=
\sum_{\mathbf k'+\mathbf k''=\mathbf k}
\left[(k_y''k_x'-k_y'k_x'')J_{0\mathbf k''}
\widetilde\Phi_{\mathbf k''}\widetilde g_{\mathbf k'}\right]
=N_{\mathbf k\mathbf k'}\widetilde g_{\mathbf k'}.
\]

这里按印刷式抄录，未另补非线性项的量纲前因子。\(\mathbf k=(k_y,k_x)\)，\(x,y\) 分别为法向、双法向坐标，\(\theta\) 为沿场线坐标，\(I\) 为单位矩阵，\(F_0\) 为 Maxwellian；\(\widetilde g\) 为非绝热 gyro-averaged 分布扰动，\(\widetilde\Phi\) 为静电势。原文关系为 \(\widetilde f_{\mathbf k}=\widetilde g_{\mathbf k}-(Ze/T)F_0J_{0\mathbf k}\widetilde\Phi_{\mathbf k}\)。\(Z\) 带物种电荷符号，电子 \(Z=-1\)；\(e\) 为基本电荷正值。\(\widehat C\) 是线性碰撞算子，不能直接等同后面的单一平均 \(\nu\)。

**适用/类别：** stated local electrostatic model 中的非线性方程；\(\mathbf D=\mathbf L+\mathbf N\)、\(\widetilde{\mathbf g}=\mathbf D^{-1}\widetilde{\mathbf P}\) 在 p.4，式(4)–(6)只是形式逆表示。线性化令 \(\|\mathbf N\|\to0\)，取 \(e^{i(\mathbf k\cdot\mathbf x-\omega t)}\)，\(\omega=\omega_R+i\gamma\)。

**可支持：** 指明平行 streaming、曲率漂移、碰撞与非线性模耦合进入电子响应的位置。**不能支持：** 仅凭形式逆证明存在唯一饱和态，或由线性极限自动确定饱和谱。

### M2. 密度、温度梯度与磁漂移的入口

**原编号/位置：式(3)，p.3，§2。**

\[
\begin{aligned}
\omega_d&=-\left(v_\parallel^2+\frac{v_\perp^2}{2}\right)
\frac{Tk_y}{v_{\rm th}^2ZeB_0R}
\left[\cos\theta+
\left(s\theta-\alpha\sin\theta+\frac{k_x}{k_y}\right)\sin\theta\right],\\
\omega_*&=\frac{Tk_y}{ZeB_0R}
\left[\frac{\partial\log n}{\partial\rho}
+\left(\frac{E}{T}-\frac32\right)
\frac{\partial\log T}{\partial\rho}\right].
\end{aligned} \tag{3}
\]

\(R\)：局域磁面几何平均大半径；\(q\)：安全因子；\(s\)：磁剪切；\(\alpha\)：Shafranov-shift 参数；\(B_0\)：原文定义的参考真空磁场；\(v_\parallel,v_\perp,E,T\) 为本物种速度、能量和温度，**此处 \(E\) 有量纲**。\(J_{0\mathbf k}\) 的自变量是 \(k_\perp\rho_Lv_\perp/v_{\rm th}\)。p.3 未独立明确本物种 \(v_{\rm th},\rho_L\) 的所有数值约定，不能自行加 \(\sqrt2\)；数值离子频率归一化见 M8。

**适用/类别：** 与 M1 相同几何和静电模型的漂移、驱动定义；不是额外的饱和闭合。passing 电子在 ITG/TEM 尺度上 \(J_0\simeq1\)，bounce-averaged trapped 电子涉及 banana orbit 平均，二者处理不同（p.3）。

**可支持：** 电子自身的 \(g_e\) 直接乘能量核 \(E/T_e-3/2\) 进入 \(\omega_{*e}\)；离子的 \(g_i\) 进入离子方程的对应驱动，并可通过耦合场改变电子看到的模。**不能支持：** 从温度核直接断言谱积分后的热扩散符号，或从离子项未显式写在电子 \(\omega_*\) 中断言离子梯度不影响电子通量。

### M3. 通量分解与系数含义

**原编号/位置：主式(11)，p.4，§2；通量定义式(10)/p.4，系数式(12)/p.5。**

\[
\Gamma_{\rm turb}=A'\frac{R}{L_n}+B'\frac{R}{L_T}+C'. \tag{11}
\]

电子版本即 \(\Gamma_e=A'g_n+B'g_e+C'\)。起点是式(10)的相关通量 \(\Gamma_{\rm turb}=\langle\widetilde n\,\widetilde v^{\,r}_{E\times B}\rangle_{\mathbf k\omega}\)，不是纯实频率或增长率。式(12)的三个定义为

\[
\begin{aligned}
A'&=\left\langle\Re\sum_{\mathbf k}
\left[\frac{ik_y\widetilde\Phi_{\mathbf k}^{*}}{B_0}
\langle J_{0\mathbf k}\widetilde\alpha_{n\mathbf k}\rangle_v\right]\right\rangle,\\
B'&=\left\langle\Re\sum_{\mathbf k}
\left[\frac{ik_y\widetilde\Phi_{\mathbf k}^{*}}{B_0}
\langle J_{0\mathbf k}\widetilde\alpha_{T\mathbf k}\rangle_v\right]\right\rangle,\\
C'&=\left\langle\Re\sum_{\mathbf k}
\left[\frac{ik_y\widetilde\Phi_{\mathbf k}^{*}}{B_0}
\langle J_{0\mathbf k}\widetilde\alpha_{P\mathbf k}\rangle_v\right]\right\rangle.
\end{aligned}
\]

\(\langle\cdot\rangle_v\) 为适当的速度空间积分，外括号为磁面平均；星号为复共轭。\(\widetilde\alpha_j=\mathbf D^{-1}\widetilde{\mathbf P}_j\) 是 p.4 的三种驱动响应，\(j=n,T,P\)；这里的 \(\alpha_j\) 与几何 \(\alpha\) 无关。\(A',B',C'\) 均乘无量纲梯度或常数，因而在该式中有粒子通量量纲；不直接把 \(A'\) 称为已按 SI 归一化的扩散率 \(D\)。

**适用/类别：** exact formal decomposition within the local model；p.4 明确局域限制，p.5 明确系数依赖梯度。**可支持：** 分离扩散、热扩散和其余 pinch 的物理入口。**不能支持：** \(A',B',C'\) 对 bulk \((g_n,g_e,g_i)\) 不变；也不能从此求得数值闭合。p.4 式(8)的相位书写疑点见§8，未擅自订正。

### M4. 定态密度梯度与自洽求根

**原编号/位置：式(13)，p.5，§2；自洽过程 p.10–11，§3.2；准线性系数式(14)/p.6，§2.1。**

\[
\left[\frac{R}{L_n}\right]_{\rm stat}
=-C_T\frac{R}{L_T}-C_P,
\qquad C_T=\frac{B'}{A'},\quad C_P=\frac{C'}{A'}. \tag{13}
\]

要求 \(A'\ne0\)、忽略粒子源与新经典项。\(C_T,C_P\) 无量纲。\(C_P\) 来源于原始驱动中的时间变化项，作者联系到极化电流，亦可从 \(\widetilde f\) 方程理解为平行与垂直动力学的相互作用；不能不加限定等同某个单独的几何常数。

式(14)补充了谱合成的实际定义：\(C_T^{QL}=(\sum_{\mathbf k}|\widetilde\Phi_{\mathbf k}(0)|^2B'_{\mathbf k})/(\sum_{\mathbf k}|\widetilde\Phi_{\mathbf k}(0)|^2A'_{\mathbf k})\)，\(C_P^{QL}\) 的分子改为 \(C'_{\mathbf k}\)。这些单模系数按 p.6 式(15)除去绝对势幅度，但仍依赖本征函数形状和电子响应。\(\widetilde\Phi_{\mathbf k}(0)\) 中的 0 指 **\(\theta=0\)**，不是初始时刻。

§3.2 的过程是扫描输入 \(g_n^{\rm in}\)，重新求线性模与系数，形成 \(g_n^{\rm out}=-C_T(g_n^{\rm in})g_e-C_P(g_n^{\rm in})\)，找到 \(g_n^{\rm out}=g_n^{\rm in}\)；之后绘图中的系数取在这个定态上。

**适用/类别：** 无源定态约束在模型内的代数后果；用 M7 权重计算系数时成为 quasi-linear closure。**可支持：** 隐式定态问题以及 tracer 固定背景下的严格线性。**不能支持：** bulk 定态显式线性、唯一性、梯度偏导数符号或大小。p.11 的稳定性斜率原文另有未推导条件，见§8，不当成已验证的数学定理。

### M5. 深俘获与近绝热 passing 电子的两个 pinch

**原编号/位置：式(16)，p.7，§2.1；机制解释 p.7–9，§2.2。**

\[
\begin{aligned}
D_0C_T={}&\sum_{\mathbf k} k_y^2
\left|\frac{e\widetilde\Phi_{\mathbf k}}{T_e}\right|^2
\left[\sqrt{\frac2\pi}f_t\int
\overline J_{0\mathbf k}^{\,2}
\frac{\widehat\gamma(E-\frac32)\sqrt E\,e^{-E}}
{(\omega_R-\overline\omega_d)^2+\widehat\gamma^2}\,dE
-\frac{1-f_t}{2}\sqrt{\frac\pi2}
\frac1{|k_\parallel v_{\rm th}^e|}\right],\\
D_0C_P={}&-\frac{eB_0R}{T_e}\sum_{\mathbf k} k_y
\left|\frac{e\widetilde\Phi_{\mathbf k}}{T_e}\right|^2
\left[\sqrt{\frac2\pi}f_t\int
\overline J_{0\mathbf k}^{\,2}
\frac{(\nu\omega_R+\gamma\overline\omega_d)\sqrt E\,e^{-E}}
{(\omega_R-\overline\omega_d)^2+\widehat\gamma^2}\,dE
+(1-f_t)\sqrt{\frac\pi2}
\frac{\omega_R}{|k_\parallel v_{\rm th}^e|}\right].
\end{aligned} \tag{16}
\]

**视觉关键点：** \(C_P\) 分子是 \(\nu\omega_R+\gamma\overline\omega_d\)，第二项用 \(\gamma\)，不是 \(\widehat\gamma\)；\(C_T\) 的 passing 项有负号和 \(1/2\)。原页积分未印上下限，此处保留 \(\int\)，不冒充原式印有 \(0,\infty\)。

\(f_t\) 是深俘获电子相对份额；\(1-f_t\) 是 passing 份额；\(\widehat\gamma=\gamma+\nu\)，\(\nu\) 为此解析近似下的有效平均碰撞性。这里 **\(E\) 已按 \(T_e\) 归一化**；横线表示对模结构平均并仅取 deeply trapped、\(v_\parallel=0\)，采用 \(\mu B=E\) 条件。原文给 \(\overline J_{0\mathbf k}=J_0(k_\perp\rho_b\sqrt{2E})\)，\(\rho_b\) 为 banana width，\(\overline\omega_d=f(s,k_y,k_x)[T_e/(eB_0R)]E\)；函数 \(f\) 未在此明确给出。每个 \(\gamma,\omega_R\) 随 \(\mathbf k\) 变；\(k_\parallel\) 为平行波数。\(e\widetilde\Phi/T_e\) 无量纲，不能把 p.7 的 \(\widehat\gamma\) 与§3 数值归一化的帽号混用。

**适用/类别：** linearized approximation，加深俘获/近绝热 passing、速度空间与模结构简化，再以谱幅度作 quasi-linear 合成；不是完整非线性定律。barely trapped 未单列，p.9 明言会影响绝对值，full kinetic 数值才适合可信定量。

**可支持：** 温度核、漂移失谐、有限增长/碰撞宽度共同决定热扩散；passing 与 trapped 需按各自扩散贡献加权。passing 单独归一化的近似 \(C_T^{(p)}\simeq-1/2\) 不等于总 \(C_T=-1/2\)。**不能支持：** 严格绝热电子贡献有限通量、任意 ITG 模有完全相同响应，或总 \(C_T\) 对 \(g_e,g_i\) 独立。

对原文共振解释的精度限制：p.8 在 \(\overline\omega_d>0\)、\(\omega_R<0\) 时说低能粒子可“resonate”。严格等式 \(\overline\omega_d=\omega_R\) 此时不能在正能量成立；式(16)可支持的是有限宽度、低能端的相对权重增强。不能把作者措辞升级成 ITG 中存在正能量精确漂移共振的证明。

### M6. 同一简化模型中的扩散归一化

**原编号/位置：式(17)，p.7，§2.1。**

\[
D_0=\sum_{\mathbf k} k_y^2
\left|\frac{e\widetilde\Phi_{\mathbf k}}{T_e}\right|^2
\left[\sqrt{\frac2\pi}f_t\int
\overline J_{0\mathbf k}^{\,2}
\frac{\widehat\gamma\sqrt E\,e^{-E}}
{(\omega_R-\overline\omega_d)^2+\widehat\gamma^2}\,dE
+(1-f_t)\sqrt{\frac\pi2}\frac1{|k_\parallel v_{\rm th}^e|}\right]. \tag{17}
\]

符号、归一化与适用条件同 M5。原文称其 diffusivity，未在该处完整给出与有量纲宏观 \(D\) 或 \(A'\) 的所有换算前因子；本报告保留 \(D_0\)，不添加 SI 单位。

**类别/可支持：** 在有效频宽 \(\widehat\gamma>0\)、非负物种份额、非零被加权模及适当有限积分等条件下，式中扩散权重非负，非退化时 \(D_0>0\)。原文据此强调扩散正而 \(C_T,C_P\) 可变号。**不能支持：** 非线性 full kinetic 的普适正定性定理、零湍流时仍严格正、任意参数下存在唯一零通量根，或两温度梯度响应的排序。

### M7. 准线性谱权重及有效垂直波数

**原编号/位置：式(19)，定义式(20)，p.10，§3.1。**

\[
|\widetilde\Phi_{\mathbf k}(0)|^2
=A_0\left(\frac{\gamma}{\langle k_\perp^2\rangle}\right)^\zeta
\Delta k_y. \tag{19}
\]

\[
\langle k_\perp^2\rangle
=k_y^2\frac{\int |\widetilde\Phi_{\mathbf k}|^2
[1+(s\theta-\alpha\sin\theta)^2]\,d\theta}
{\int |\widetilde\Phi_{\mathbf k}|^2\,d\theta}. \tag{20}
\]

\(\gamma=\gamma_{\mathbf k}\) 来自每个 \(\mathbf k=(k_y,0)\) 的最不稳定线性模，势的相对 \(\theta\) 形状取自该本征函数；\(\Delta k_y\) 是不均匀波数网格的积分权重，不能漏掉。\(\zeta=2\) 为本文选择；\(A_0\) 是整体幅度，带有使等式成立所需的归一化/量纲约定，绝对数值不由线性理论决定，在 pinch 比值与平均频率中抵消。图3的绝对幅度另作匹配，见§5。

**适用/类别：** quasi-linear saturation prescription；\(k_x=0\)，不包括完整 \(k_x\) 谱，p.10 明言这种省略没有先验充分理由。原文没有在这里给出稳定模的完整权重规则；不能自行把负增长率平方后当成有限稳定模通量。

**可支持：** 给定 full kinetic 线性谱、本征函数、单模响应后计算相对谱合成。**不能支持：** 用 \(\gamma_{\max}\) 唯一代表总通量，或宣称该权重已在全部扫描、次主导/稳定模、非线性模耦合下验证。

### M8. 平均实频率的定义与标签限制

**原编号/位置：式(21)，p.11，§3.2；符号约定表1/p.6；数值归一化 p.10、12。**

\[
\omega_R^{QL}
=\frac{\sum_{\mathbf k}|\widetilde\Phi_{\mathbf k}(0)|^2\omega_{R\mathbf k}}
{\sum_{\mathbf k}|\widetilde\Phi_{\mathbf k}(0)|^2}. \tag{21}
\]

本节数值频率按 \(v_{\rm th}^i/R\) 归一化，\(v_{\rm th}^i=\sqrt{T_i/m_i}\)，原文后续省略表示此归一化的帽号；波数横轴 \(k=k_y\rho_i\)。这避免在固定 \(T_i\) 改变 \(T_e\) 时仅由单位变化造成假频率变化。数值碰撞性是 \(\hat\nu=\nu_{ei}R/v_{\rm th}^i\)，不等同 M5 中未另给换算的有效 \(\nu\)。

**类别/可支持：** 采用 M7 幅度的谱统计量；按本文符号，单模 \(\omega_R<0\) 为离子方向/ITG，\(\omega_R>0\) 为电子方向/TEM 或 ETG。作者以 \(\omega_R^{QL}\lesssim0\)、\(\gtrsim0\) 辅助判断 ITG/TEM 主导，\(|\omega_R^{QL}|\simeq0\) 辅助判断混合。

**不能支持：** 平均接近零证明每个模频率接近零、每个波数净通量为零、两支恰等权、唯一确定整个湍流谱，或把正频率不加尺度条件地唯一认作 TEM。它不是按粒子通量权重定义，也不是直接测量的非线性频率。

## 5. Parameter Scans and Control Conditions

### 5.1 共同设置与不能悄悄固定的量

表2/p.11 与§3.3/p.11–12：\(\epsilon=0.12\)，通常 \(q=1.4\)；\(n_e=n_i=10^{19}\,{\rm m}^{-3}\)、\(T_i=1\,{\rm keV}\)、\(B_0=2\,{\rm T}\)，base case \(Z_{\rm eff}=1\)。温度比改变时 \(T_e\) 随之改变，而“改变温度比”与“改变温度归一化梯度”是不同操作。局域密度值固定不表示密度梯度固定。

特别是 \(\alpha=-q^2d\beta/d\rho\)，\(\beta=2\mu_0(n_eT_e+n_iT_i)/B_0^2\)，**每个点自洽重算**。所以“固定表中背景”的梯度响应仍包含 \(\alpha\) 的变化，不能称固定全部几何的偏导数。原文没有单独提供冻结 \(\alpha\) 的对照。

线性 GS2：静电、initial-value、局域 flux-tube，沿 \(\theta\) 每 \(2\pi\) 32 点、12 poloidal periods，\(\Delta t=0.03\,R/v_{\rm th}^i\)，\(k_x=0\)；13 个 \(k_y\rho_i\in[0.08,1.5]\)，对数网格、\(\Delta k_y\rho_i\propto k_y\rho_i\)。权重 \(\zeta=2\)。这不是完整二维非线性波数谱；initial-value 每波数取主要增长模，次主导和稳定模没有穷尽。各准线性参数点内部还要扫描 \(g_n\) 求自洽根。

| 扫描 / 定位 | 固定参数 | 独立输入变化 | 密度梯度与解释限制 |
|---|---|---|---|
| 无碰撞温度梯度，§3.4/p.12，图1/p.20 | \(q=1.4,s=0.8,T_e/T_i=1.5,\hat\nu=0\) 及共同设置 | \(g_e\in\{5,7,9,11,13\}\)，\(g_i\in\{6,9,12\}\)：二维离散组合；图例固定 \(g_e\)，横轴是 \(g_e/g_i\) | \(g_n\) 是每点自洽输出，\(\alpha\) 重算。说明论文确实分别改变过 \(g_e\)、\(g_i\)，但没有报告连续局部独立响应系数 |
| GYRO 比较，§3.4.3/p.13，图3/p.22 | base case、\(g_e=9\) | \(g_i\in\{4,9,14\}\)，对 \(g_n=3,5\) 两条固定密度梯度分别算通量 | 此处没有每点直接求零通量根；利用通量符号估计根位置，不是与图1完全相同的一组 \(g_i\) |
| 碰撞性—温度比，§3.5/p.13–14，图4/p.23 | \(g_e=g_i=9,q=1.4,s=0.8\) | \(\hat\nu\in\{0,0.02,0.1,0.3,0.8\}\)，\(T_e/T_i\in\{1.1,1.5,2.5\}\) | \(g_n\) 自洽；扫描中 \(\hat\nu\) 与温度比作为输入，不能当作沿同一实验放电自然演化的关系 |
| 剪切—温度比，§3.6/p.14–15，图5/p.24 | \(g_e=9,g_i=7,\hat\nu=0.2,q=1.4\) | 正文列 \(s\in\{0.5,0.8,1.1,1.4,1.7\}\)，\(T_e/T_i\in\{1.1,1.5,2.5\}\) | \(g_n\) 自洽；图5可见点到 \(s=1.4\)，正文列出的 1.7 未在该图清楚呈现，不能自行补数据 |
| eITB，§3.7/p.15，图6/p.25 | \(g_e=20,T_e/T_i=2.8,q=2.8,s=-1,\epsilon=0.12\) | \(g_i/g_e\in\{0.3,0.45,0.6,0.75,0.9\}\)，即 \(g_i=6,9,12,15,18\)；\(\hat\nu=0,0.02,0.04\) | 强反剪切、TCV eITB 背景专用；不能与普通正剪切扫描的响应混为一谈 |

### 5.2 比值横轴、路径斜率与独立响应

\[
x=\frac{L_{Ti}}{L_{Te}}=\frac{g_e}{g_i},
\qquad \frac{L_{Te}}{L_{Ti}}=\frac{g_i}{g_e}.
\]

图1每条同色/同符号曲线固定 \(g_e\)，沿横轴向右对应 \(g_i\) 减小；不是固定 \(g_i\) 增大 \(g_e\)。跨曲线若固定 \(x\) 比较，\(g_e\)、\(g_i\) 同比例变化，不能解释成“只改变电子温度梯度”。此外离散网格中任意固定比值未必都有成对原始点，线段不能补出新的模拟数据。

图1及 p.12 实际支持：在所算路径上，趋近 \(\omega_R^{QL}\simeq0\) 时 \(g_n^{stat}\) 通常增大；\(C_T\) 为负、在过渡附近绝对值较大，向强 TEM 方向显著减弱；\(C_P\) 在本无碰撞扫描全为负且向 TEM 侧更负，图上约从 \(-0.5\) 到 \(-1.5\) 的量级。\(g_n^{stat}\) 的峰并不要求精确位于 \(g_e/g_i=1\)。作者把固定比值时随 \(g_e\) 的整体增加主要解释为显式热扩散 \(-C_Tg_e\) 增大，并称系数主要依赖比值；这不是 \(\partial C_T/\partial g_e=0\) 或 \(\partial C_P/\partial g_e=0\) 的证明。

因此：原文**有独立输入的二维离散扫描**，并非只沿一条比值路径；但**没有给出足以严格排序局部独立偏导数的数据或定理**。读取图形最多得到有限步长、给定协议下的变化趋势，不能代替同一根分支上的局部响应。

### 5.3 谱抵消及非线性比较到底检验了什么

图2/p.21、§3.4.2：\(g_e=g_i=9\) 的自洽定态保留正、负 \(\Gamma_k\)，满足的是波数求和零通量。低波数 TEM 向外、中间 ITG 向内；短波电子方向分支也有向内相移，但受权重抑制，通量图上贡献很小。不能概括成“TEM 一概向外、ITG 一概向内”。p.10 的所谓 phase shift 实际定义为 \(\widetilde\Gamma_k=\Gamma_k/|\widetilde\Phi_k(0)|^2\)，是去幅度的通量量，不是直接等同一个相位角。

GYRO 设置（p.13）：32 toroidal modes，\(L_x=100\rho_s,L_y=135\rho_s\)，\(\Delta x/\rho_s=0.5\)，128 velocity-space grid points；本段未完整定义 \(\rho_s\) 的换算，不补写。\(g_i=9,14\) 时，\(g_n=3\) 通量略向内、\(g_n=5\) 向外，支持零点位于 3–5 之间的解释（仍隐含通量连续性）；准线性预言约为 4。\(g_i=4\) 时连 \(g_n=3\) 也向外，支持 TEM 一侧定态较低的趋势，不能仅靠一个正通量值证明零点存在或唯一。

图3标题说明 \(A_0\) 选取为匹配 square symbols 的平均值；正文说明 \(\zeta=2\) 给出最佳总体符合。故该比较含整体幅度匹配和权重选择，并非无校准的绝对通量预测。作者结论 p.17 明确限于少量非线性算例的**定性一致**，不能据此宣称已验证所有参数下的条件响应、热扩散机制唯一性或 full spectrum 闭合。

### 5.4 碰撞、剪切、温度比与 eITB 的附加限制

在§2.2，p.8，作者把式(16)中的碰撞相关 pinch 简化为式(18)：\(C_P^{(\nu)}\approx-[eB_0R/T_e](\omega_R/k_y)\nu/(\gamma+\nu)\)。该式已视觉核对，是解释性近似而非额外独立闭合。固定其余量时负 \(\omega_R\) 给出外向项；实际扫描里 \(\omega_R,\gamma\) 和谱也变化，不能仅微分显式 \(\nu\) 因子就代替整体碰撞响应。式(16)保留的 \(\gamma\bar\omega_d\) 与 \(\nu\omega_R\) 竞争，比“碰撞总破坏 pinch”更准确。

§3.5：低温度比下随碰撞增大平均频率更负，\(C_P\) 可转正、\(g_n^{stat}\) 可到负值；\(T_e/T_i=2.5\) 时扫描内定态变化很小。§3.6：高温度比混合区的剪切效应主要通过 \(C_T\)，低温度比 ITG 区则被外向 \(C_P\) 改变。这些都是特定背景结果。图7/p.26 中相近平均频率仍有 \(C_T\) 的竖向散布，不能把 \(\omega_R^{QL}\) 当作全信息坐标。

eITB：正文提到实验情境 \(g_n\sim9\sim0.45g_e\)，并说明离子温度梯度不精确；这不是把 \(g_n=9\) 固定进准线性定态求根。图6实际输出约为 2–6，不能声称复现了该情境的 \(g_n=9\)。在很多点上 \(|C_Tg_e|\gg|C_P|\)，过渡附近 \(|C_T|\approx0.3\)；但最低 \(g_i\)、无碰撞端 \(C_T\) 接近零，\(C_P\approx-0.9\)，不能把正文“沿整个扫描 \(C_P\) 可忽略”强化为每一点都有可控小误差。\(\nu\) 增大时峰向较小 \(g_i\) 移动，是该反剪切背景的数值表现。

§3.8/p.15–16 对 H-mode 碰撞趋势、L-mode 剪切趋势的讨论来自既有实验文献；本轮未核验其原始数据。作者也要求低/中 \(k_y\rho_i\) 的实测频率与代码对照，并在 p.18 指出进一步定量预言需要非线性模拟。

### 5.5 对本轮七个科学问题的取证回答

| 问题 | 原文可给出的回答 |
|---|---|
| 1. 是否研究 \(g_e,g_i\) 的独立变化？ | **是，作为二维离散输入**，§3.4 的 \(5\times3\) 设置；另有固定 \(g_e\) 改 \(g_i\) 的 GYRO 与 eITB 扫描。**局部独立偏导数及其严格比较：NOT ESTABLISHED。** |
| 2. 是否有可计算条件响应的明确通量闭合？ | 有**形式通量分解**及需线性求解器补足的**准线性计算方案**：式(11)、(14)–(21)。不是仅用 \((g_n,g_e,g_i)\) 即可代入的封闭标量函数；需本征谱、本征函数、单模相移、权重及重算协议。论文未输出完整数值数据和局部导数。 |
| 3. \(g_e\) 如何进入电子通量？ | 直接进入电子 \(\omega_*\) 的温度能量核，形成 \(B'g_e\) / \(-C_Tg_e\)；改变 bulk \(g_e\) 还会改变 TEM 驱动、频率、增长率、本征函数、谱权重、各项系数以及自洽 \(\alpha\)。 |
| 4. \(g_i\) 如何进入？ | 直接驱动离子 gyrokinetic 方程，在耦合系统中改变 ITG 与竞争分支、场和谱，再改变电子响应及 \(A',B',C'\)；本扫描也通过压力梯度改变 \(\alpha\)。单独把它压缩成平均频率变化是一种解释，非完整闭合。 |
| 5. 直接与间接如何区分？ | 式(11)电子物种的显式梯度为 \(g_n,g_e\)，没有单列 \(g_i\) 加性项；这并不排除系数对 \(g_i\) 的依赖。tracer 固定背景的 \(B'\) 可识别直接项，bulk 响应还含背景反馈。 |
| 6. ITG 区两种响应谁更大？ | 无条件的符号、绝对值或大小排序均 **NOT ESTABLISHED**；图1的路径趋势、\(\lvert C_Tg_e\rvert\) 的大值、负平均频率，均不能单独决定 \(\partial g_n^{stat}/\partial g_e\) 与 \(\partial g_n^{stat}/\partial g_i\)。 |
| 7. 严格命题还缺什么？ | 同一定态根分支、其存在/非退化/可微性；固定温度比、碰撞、几何或明确 \(\alpha\) 重算协议；完整单模响应与谱对梯度的依赖；若要求稳健物理结论，还需谱闭合不确定性或非线性验证。 |

## 6. Candidate Mathematical Problems

以下是取证后提出的研究候选，不是论文已证明的结论。本阶段不求解、不拟合新输运律、不生成未经数据支持的响应系数。

### P1. 给定控制协议时，定态密度梯度的两种条件响应何时可识别、何时可比较？

**物理证据起点：** E1 的梯度依赖系数与 tracer/bulk 区别；E2 的电子能量核；E3 的二维输入但比值作图；E4 的谱抵消。

**最小数学对象：** 将论文的同一个准线性零通量条件记为

\[
F(g_n,g_e,g_i;p)
=g_n+C_T(g_n,g_e,g_i;p)g_e+C_P(g_n,g_e,g_i;p)=0.
\]

这里只是式(13)的移项记号，不是新输运律。\(p\) 指明温度比、\(\hat\nu,q,s,\epsilon\)、幅度规则、波数集合、离子归一化与几何协议。至少区分两种协议：(a) 按论文每点重算 \(\alpha\)；(b) 固定局域 \(\alpha\) 的对照。若两种协议均研究，须分别标注，不能混成同一偏导数。

研究目标为同一根分支上的 \(\partial g_n^{stat}/\partial g_e|_{g_i,p}\) 与 \(\partial g_n^{stat}/\partial g_i|_{g_e,p}\)，并区分固定谱的 tracer 响应和重算 bulk 湍流的响应。此处不赋数值，也不把前者直接当成后者。

**待证明或反驳的具体命题：** 在明确限定的 ITG 主导、非退化定态邻域内，是否可仅由谱级的、可检验的条件保证某一条件响应的符号，或保证两响应绝对值的排序？阶段 B 应先给出可微根与控制协议条件，再检查候选排序 \(|\partial_{g_e}g_n^{stat}|\ge|\partial_{g_i}g_n^{stat}|\) 是否有额外充分条件；若没有，应在论文允许的闭合与背景内寻找反例或失效边界。该不等式只是待检验对象，**当前 NOT ESTABLISHED**，不预设正反方向。

**原论文已解决：** 物理上有来源的显式温度项、系数提取程序、数值自洽根和主要扫描趋势；电子与离子梯度进入耦合系统的途径不同。

**尚未解决：** 局部导数、隐式反馈是否放大/抵消显式项、根分支的非退化性、主导模切换处的可微性、两响应排序及适用域。ITG 标签本身不是这些性质的证明。

**需要增加：** 指定物理闭合并取得同一邻域的 \(\gamma_k,\omega_{Rk},\Phi_k(\theta),A'_k,B'_k,C'_k\) 与其梯度依赖；或先提出有物理约束的可解析谱级假设，再检查是否与 full kinetic 响应兼容。若使用有限差分数据，需固定另一梯度及全部约定，沿同一根分支重算密度与谱；图1稀疏连线不够。不能用任意指定 \(C_T,C_P\) 的玩具反例代替物理可实现性检验。

**独立数学研究价值：有条件地具备。** 仅写出隐函数定理不是足够贡献；价值在于从电子响应核和谱反馈得到可检验的符号/排序充分条件、物理反例或分支失效条件，并阐明扫描路径信息能识别到什么程度。

### P2. 谱权重不确定性下，零通量定态及响应符号能否保持？

**物理证据起点：** E4 的异号波数通量和 E3/E5 的混合区；M7 的权重选择及 \(k_x\) 省略；p.5 对次主导、稳定模的讨论。

**最小数学对象：** 论文 p.10 的谱合成写为 \(\Gamma_e^{QL}=\sum_k w_k\widetilde\Gamma_k\)，其中 \(w_k=|\widetilde\Phi_k(0)|^2\ge0\)，\(\widetilde\Gamma_k\) 是去幅度的单模通量。先固定已有线性响应，在明确定义、保留非负性的相对权重扰动类中讨论根的位置；再区分整体共同倍率和跨波数重新分配，前者不改变零通量条件。

**待证明或反驳的具体命题：** 对包含图2那类异号贡献的非退化零点，能否给出可检验的相对谱误差界，使定态根保留在给定区间；若讨论 P1 的响应符号，能否同时控制谱及其梯度导数误差？反之，仅知道 \(\omega_R^{QL}\) 的符号或数值是否足以限定根/响应？应在满足既定单模响应约束的谱中构造反例或给出额外充分条件，而非把谱任意自由化。

**原论文已解决：** 给出一个权重选择、一个谱抵消实例和少量非线性一致性证据；验证“有必要看谱”。

**尚未解决：** 相对权重误差的可容忍范围、次主导/稳定模与 \(k_x\) 扩展对根和响应的误差、平均频率作为状态压缩量的充分性。

**需要增加：** 单模通量随 \(g_n\) 的局部变化、基准根非退化条件、由非线性谱或有依据的备选闭合给出的权重误差类；研究响应时还需该类随 \(g_e,g_i\) 的变化约束。一个任意的权重球不能声称代表真实湍流不确定性。

**独立数学研究价值：具备但需物理约束。** 有机会形成零点稳定性界、误差证书或谱压缩失效的具体反例；仅作一般连续性扰动论则贡献有限。

## 7. Recommended Research Starting Point

**推荐 P1：明确控制协议与谱反馈后的定态梯度条件响应识别。**

理由是原文同时提供了电子温度核的直接入口、离子梯度通过耦合场/湍流背景影响电子通量的路径、以及可用于区分两者的 tracer 提取方法；问题有真实物理对象，又尚未被比值扫描解答。阶段 B 最初目标应是找出可定义和可比较两种响应的最小条件，并检验其符号或排序是否依赖谱；不应把“电子梯度更重要”作为目标结论。

建议以§3.4 的无碰撞、\(T_e/T_i=1.5,q=1.4,s=0.8\) 协议为首个限定背景，显式保留或明确冻结 \(\alpha\)，并选择已确认处于 ITG 主导且不跨主导模切换的局部根邻域。论文不足以保证任意指定点满足这些条件。先做条件化推导，若需数值再提出最小补充数据要求；本阶段未运行任何新 gyrokinetic 计算。P2 可作为检查 P1 结论是否依赖特定谱权重的后续支线。

## 8. Source Uncertainties

1. **版本边界。** 作者稿 metadata 标为首次修订，未与最终排版全文逐字校对；不能保证所有排版疑点在期刊版仍存在。本文全部页码与公式均绑定上述 SHA-256 的 26 页文件。
2. **稳定性条件未独立建立。** p.11，§3.2 原文确实印 \([dX^{out}/dX^{in}]_{X=X^{stat}}>1\)，\(X=R/L_n\)。已视觉确认“\(>1\)”而非文本提取误读。但未给出时间演化、边界条件或线性扰动推导；不能把它当作通常固定点迭代的收敛条件，更不能据此证明定态输运稳定性。本报告不擅改不等号，稳定性命题为 **NOT ESTABLISHED**。
3. **相位因子书写疑点。** 式(2)的驱动有 \(i\omega_*\)，但 p.4 式(8)的 \(\widetilde P_n,\widetilde P_T\) 印刷项未显式带对应的 \(i\)。未找到在这两式间说明吸收相位的约定；重建逐步代数时必须回查，不能声称已解决这一一致性问题。本报告照录关键式、不补写可能遗漏项；如阶段 B 从算子推导严格符号，须先澄清。
4. **几何与归一化。** p.3 的“low aspect ratio”用语与 \(\epsilon=0.12\) 的数值背景需分别记录；不要自行替作者改成另一极限。\(s\) 的完整公式、解析物种热速/回旋半径所有前因子、\(D_0\) 到 SI 扩散率换算、GYRO 本段 \(\rho_s\) 定义、\(\overline\omega_d\) 的几何函数，未在此次重点段落完整明确。p.7 的归一化能量与 p.3 的有量纲能量不能混用；有效 \(\nu\) 与数值 \(\hat\nu\) 不能直接等同。
5. **图号、图文差异。** §3.4.3/p.13 有将准线性/非线性对照指向图2的文字，实际对照在图3；§3.6/p.14 的部分图4引用对应实际剪切图5；§3.7/p.15 的图5(b/c/d)引用对应实际 eITB 图6。剪切正文列到 \(s=1.7\)，图5可见只到1.4。定位按节、实际图题和横轴交叉核对，不擅自补点。
6. **eITB 的定量与端点。** 实验情境 \(g_n\sim9\) 与模型输出约2–6不能混淆。最低梯度无碰撞端不支持“每点都可忽略 \(C_P\)”的强陈述。强反剪切、已知 \(g_e\)、未知离子梯度等前提不能移除。
7. **没有原始数值表。** 本轮未取得完整 GS2/GYRO 输入文件、逐模表、根扫描表或误差条；图读数均为原文给出的约数或注明为图中量级，不用于构造独立响应系数。线性主导模切换可能导致非光滑，但本文未对此作数学分析。
8. **解析近似不穷尽电子动力学。** barely trapped、强非绝热 passing、电磁效应、稳定/次主导模与完整 \(k_x\) 谱可能重要；p.9 作者已承认简化解析式绝对值有偏差。简化核中的“低能响应”不能升级为相反符号频率的精确漂移共振。
9. **模型验证强度有限。** GYRO 仅验证一组无碰撞背景下少量通量符号/趋势，且 \(A_0\)、\(\zeta\) 有匹配/选择；§3.8 是解释既有实验，未唯一辨识机制。ETG、更完整非线性定量及实验湍流频率验证仍待补充。
10. **研究结论边界。** ITG 区两种温度梯度的独立响应相对大小、普适符号、定态根唯一性、平均频率的充分性，均 **NOT ESTABLISHED**。这些不是负结论或反例，而是当前来源未提供证明或足够数据。

## 9. Status

- **阶段 A 完成：** 来源身份/版本/哈希已记录；八项核心关系及所需定义已视觉核对；六项证据、扫描控制条件、两个候选问题与一个阶段 B 推荐已整理。原文不清之处保持为未核实或 NOT ESTABLISHED。
- **没有开展阶段 B：** 未证明新数学命题、未求解新模型、未拟合响应系数、未提出新输运定律或新物理机制；未运行 GENE/GYRO/TGLF 等新计算，未以 HL-3 预期筛选证据。
- **项目边界：** 未加载正式 Skill 进行 ON 测试，未修改 `SKILL.md`、Core/OAC、README、CHANGELOG、Regression、Research Observatory 或 Angioni C1/C2 记录；未升级版本、提交、推送或修改 GitHub；未写入只读 Canonical 项目。
- **本轮文件范围：** 所有新增文件均在 `experiments\fable-2010`；PDF 与阅读附件仅本地保存并被本实验 `.gitignore` 排除。
