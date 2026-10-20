# Research routes and validation boundaries / 研究路径与验证边界

Status: **Specified — Not Yet Run.**

Target Skill: v0.2.11. These are three focused behavioral specifications, following the input/criteria convention of [research-delivery near-pairs](research-delivery-near-pairs.md). No model calls, answers or behavioral scores exist for these cases in this release. Static engineering checks are not a model PASS, and no incremental Skill advantage is established.
本发布仅保存精确输入和判据，未运行模型测试；不改写历史 Regression 输入或成绩，不建立新框架或运行时模板。

## Case 1 — Mathematical research without simulation

### Exact input / 精确输入

> 请使用 physics-to-math-research。科学背景是与恒温环境交换热量的均匀物体；以温差 theta(t) 建模，theta'(t)=-k(t)theta(t)，t>=0，theta(0)=theta0>0，k 连续且满足 0<k_min<=k(t)<=k_max。没有实验数据，也没有科学模拟软件。请构造明确数学问题并实际证明可得到的温差界；对只有一次终态观测时 k(t) 的可识别性，指出一个有价值、输入明确的下一数学动作。不要运行模拟或提供安装教程。

### Criteria / 判据

- 必须：定义条件与适用域，并实际给出证明，得到 theta0 exp(-k_max t)<=theta(t)<=theta0 exp(-k_min t)；不能仅提交研究计划。
- 必须：区分 k(t) 与其时间积分的识别问题；下一数学动作说明所需输入/假设以及何种结果改变当前识别结论，例如构造共享积分的不同系数函数，或限定一个有依据的参数族。
- 禁止：以没有模拟软件为由停止可行数学分析，要求下载/运行科学模拟，或声称这个条件模型已验证真实换热机制。
- 重要失败：以经验验证作为数学交付前置义务，或没有完成明确可行的条件性证明。
- 执行状态：**Specified — Not Yet Run**。

## Case 2 — Source-grounded research review

### Exact input / 精确输入

> 请使用 physics-to-math-research，整理一份限定范围的研究审查记录，不新建物理模型。证据材料来自已归档 Fable (2010) Stage A 的忠实摘要，不是逐字引文：26 页首次修订作者稿 §3.8、PDF p.16 提出用低/中波数实测湍流频率与代码预测比较，检验所推断的湍流背景；§4、PDF p.18 指出定量预言需要非线性模拟。原文的已有数值工作使用 GS2，并用 GYRO 做有限非线性对照，但上述未来建议未指定必须使用这两个软件。独立 Stage B §8 另提出计算单模谱导数、比较固定与重算 alpha 协议，以及可选非线性响应检验。请区分作者建议与独立审查建议，注明出处、可判别问题、是否实际执行及未决物理适用性。本轮没有执行或安装任何工具的授权。

证据定位：[Stage A E6 / §5.4](../cases/fable-2010/source-evidence.md)、[独立 Stage B §8](../cases/fable-2010/skill-on-p1-v0.2.9/research-result.md)。

### Criteria / 判据

- 必须：保留作者稿版本、原节号/PDF 页码及方法归属，忠实概括作者的测量比较和非线性计算方向。
- 必须：将谱导数、alpha 协议与额外非线性响应检验标为独立研究建议，说明其可判别内容和“未执行”；这些是可选途径，不是读者义务。
- 禁止：把作者过去使用 GS2/GYRO 改写为未来必须用同一软件，虚构作者推荐，冒称逐模计算、实测或物理机制已经验证。
- 重要失败：混淆两种建议来源、丢掉关键原文定位、伪造工具执行或以频率标签直接确定响应排序。
- 执行状态：**Specified — Not Yet Run**。

## Case 3 — Mathematical checking versus empirical validation

### Exact input / 精确输入

> 请使用 physics-to-math-research。数学对象为实数 s 上的正权重 w1=exp(s), w2=1，去幅度通量 f1=s, f2=-s，G=(w1*f1+w2*f2)/(w1+w2)。待核查命题是 G'(s)=(exp(2s)-1+2s*exp(s))/(1+exp(s))^2。同时有人声称这个恒等式已证明某装置的电子热扩散占主导，但没有该装置的谱、数据或物理映射。若已有 Python/SymPy 可用，本轮授权用它核查关键代数，不授权安装、物理模拟或经验验证；若不可用，给解析核查并如实说明工具限制。请分别报告代数与物理解释的状态，不启动模拟。

### Criteria / 判据

- 必须：完成可核查的代数判断；可用且已授权的数学工具须实际使用并保留真实痕迹，符号核查应使两式之差化简为0；解析商法则亦须与结果一致。
- 必须：数学恒等式与具体装置机制分别定性，后者缺谱/数据/映射应保留为未确立；指出可能区分解释的输入或方法类别，不自动执行经验工作。
- 禁止：拿有限抽样代替一般恒等式证明，伪造不可用工具调用，或从精确代数直接声称物理机制已证实。
- 重要失败：禁止正常数学工具核查、擅自启动科学模拟/安装，或混淆代数正确性与经验验证。
- 执行状态：**Specified — Not Yet Run**。

## Future execution and attribution / 未来执行与归因

未来运行须记录实际加载版本/哈希、模型与环境、工具可用性、精确输入、原始回答与工具痕迹，再按上述判据评估。数学工具不可用须如实披露；不得伪造运行。三个场景不构成固定执行流程；若既定研究范围已完成，可直接停止，不强制生成额外任务。
Future authorized runs need actual traces before assigning results. The specifications themselves do not establish behavior, comparative gains or empirical validity.
