# Published Research Case 01 — 来源与基线

研究日期：2026-10-21（Asia/Shanghai）。本轮仅处理 Ott–Antonsen (2008) 的一个数学节点：OA 流形外的初始同步增长率。

## 1. 研究版本与运行来源

原始研究于2026-10-21完成；本公开副本于2026-10-22完成两项限定小修并随 v0.2.13 归档。
研究实际使用 physics-to-math-research **v0.2.12**，通过显式读取开发工作树中的完整
SKILL.md 及三项科研能力说明运行；不据此声称经过独立验证的原生 Skill 调用。

可复核来源：[v0.2.12 的 SKILL.md](https://github.com/ZWY-research/physics-to-math-research/blob/28ac6bcb0e4fd502f1340c0fa040fd84bbe5d924/SKILL.md)，
提交 `28ac6bcb0e4fd502f1340c0fa040fd84bbe5d924`；该 Git blob 的 SHA-256 为
`852bbb298d647f92e6298ae816fb8e573a613bd91ad5b5301e3c74d0156bdb52`。
原始研究由 Codex 执行；精确模型快照、推理配置未在独立可核验的执行元数据中归档，故不补造。
原始算术核查为 PowerShell/.NET Decimal，代码和实际输出保存在
[完整数学结果](mathematical-result.md) 第6节。
没有可信 Skill OFF 对照，不据此认定 Skill 增量优势。

公开副本保留数学内容、历史研究版本和计算证据，去除环境管理信息。
归档只补充 Engelbrecht–Mirollo (2020) 的直接相关文献及有限核系统的正则性说明；
主要定理、公式编号、反例和有理数结果不变。
本次未运行科学模拟或实验，不公开论文 PDF 或完整原文复制品。
本次正式范围和结论见[限定范围数学审查](../../literature-audits/physics/nonlinear-dynamics/2008-ott-antonsen-low-dimensional-behavior.md)。

## 2. 完整原始来源和阅读范围

Ott, E. and Antonsen, T. M. (2008).
Low dimensional behavior of large systems of globally coupled oscillators.
Chaos 18, 037113. [DOI](https://doi.org/10.1063/1.2930766)。
[作者公开完整 PDF](https://terpconnect.umd.edu/~antonsen/PublicationsTMA/Synchronization/037113_1_online.pdf)。

已获取并通读全文的文本提取，包括正文、结论、参考文献及脚注24。
PDF 共7页：封面1页，文章6页。以下使用印刷页码 037113-1 至 037113-6；
它们分别是 PDF 第2至第7页。DOI 跳转抓取失败，但作者 PDF 全文可读；
未将摘要代替全文。原 PDF 未另存本地，后续可用此完整链接重取。
未对作者的模拟或引用论文做复现实验。

## 3. 作者问题与结果定位

原始科学问题：大量全局耦合相位振子的集体同步及其瞬态能否用少量宏观量描述？
外驱动模型呈现近似二维宏观行为，是本文的重要动机。
有限 N 为 N 维相位 ODE；连续极限为频率—相位密度的输运方程。

| 原文位置 | 已有结果或问题 |
|---|---|
| 037113-1，(1)–(3)；037113-2，(4)–(5) | Kuramoto、外驱动、群体耦合；连续性方程和复序参量 |
| 037113-2，(6)；037113-3，(7)–(9) | Fourier 系数取同一函数的幂，得到 Poisson 核族及其不变性 |
| 037113-3，(10)–(11) | 解析延拓与 Lorentzian 留数闭合，得到流形上精确幅值 ODE 及显式演化 |
| 037113-4，(12)、(14)、(15) | 其他有理频率密度、外驱动、多群体的闭合描述 |
| 037113-5，(19)–(21) | 固定时延产生延迟微分方程；仍需历史函数，非有限维 ODE |
| 037113-5，V；037113-6，脚注24 | 一般初态的宏观吸引性尚待研究；不声称密度强收敛至该流形 |

关键区分：不变流形本身仍是无限维的；适当频率分布使序参量闭合。
2008年的流形不变性不是任意初态的有限时间闭合证明。
所用条件包括连续极限、第一谐波平均场耦合、特定 Fourier 幂关系，
以及下半频率平面无奇点和适当衰减；Lorentzian 半宽须正。
以上内容的出处均为[2008年原文](https://terpconnect.umd.edu/~antonsen/PublicationsTMA/Synchronization/037113_1_online.pdf)。
本轮不使用原文 (11) 的排版式进行计算；数学文件直接从输运方程和 (6) 独立推导。

## 4. 针对本节点的后续知识核对

仅核对与吸引性、流形外瞬态和混合核直接相关的四项原始研究：

1. Ott and Antonsen (2009), Long time evolution of phase oscillator systems,
   Chaos 19, 023117, DOI 10.1063/1.3136851。
   [作者全文](https://user.eng.umd.edu/~antonsen/PublicationsTMA/Synchronization/023117_1_online.pdf)。
   核对 III 末尾的 (32) 及 IV（印刷023117-5）：在正频率宽度和解析/衰减条件下，
   非 OA 部分的宏观贡献渐近消失。这是后续结果，不归给2008年；
   也不保证从相同初始序参量出发，两种描述在有限时间重合。

2. Tyulkina, Goldobin, Klimenko and Pikovsky (2018),
   Dynamics of noisy oscillator populations beyond the Ott-Antonsen ansatz,
   Physical Review Letters 120, 264101, DOI 10.1103/PhysRevLett.120.264101。
   [作者预印本全文](https://arxiv.org/pdf/1804.05326)（v2，PDF第2–3页，(4)、(13)–(14)）。
   已有全矩层级及二阶圆累积量 κ₂=Z₂−Z₁²。
   本轮的闭合误差恒等式是该已有结构的无噪声特例，不是新方法；
   本轮不用其弱噪声二累积量截断，也不假设 κ₃=0。

3. Cestnik and Pikovsky (2022),
   Exact finite-dimensional reduction for a population of noisy oscillators and its link
   to Ott–Antonsen and Watanabe–Strogatz theories,
   Chaos 32, 113126, DOI 10.1063/5.0106171。
   [作者预印本全文](https://arxiv.org/html/2207.02302v2)。
   定向核对 II.2、IV.2、VIII.2.1–2：流形外初态需要额外信息；
   正 Poisson 核混合和共同平均场下的多核演化已经存在。
   一般初态的“三个复变量”仍携带一个由初态确定的常函数，不能解释为
   仅凭 Z₁(0) 的普遍闭合。未复现全文的数值例子。

4. Engelbrecht, J. R. and Mirollo, R. (2020), Is the Ott-Antonsen manifold attracting?,
   Physical Review Research 2, 023057。
   [DOI](https://doi.org/10.1103/PhysRevResearch.2.023057)；
   [作者原始预印本](https://arxiv.org/pdf/2002.07827)（实际核对 v1，2020-02-18；
   II.C，PDF第5–6页；III，PDF第12–15页；IV，PDF第15页）。
   论文以 Poisson 测度的加权混合系统研究流形外动力学。
   有限数量频率群体的连续模型中，双 Poisson 核的双曲距离不变量阻碍向流形内部吸引；
   该模型不同于有限个单振子的系统，也不同于本例的连续 Lorentzian 频率分布。
   连续频率情形必须区分强拓扑中的非吸引与附加条件下宏观序参量/较弱拓扑的渐近行为；
   不能将前一种非吸引结论移植为后一种宏观不吸引结论。
   因此，混合核及流形外研究已有直接文献基础；本例固定初始幅值的锐界、
   可达性与具体同一阶信息反例仍记为本轮独立推导，未经证实的数学原创性不作声明。

另做了“Kuramoto/OA + second moment/transient growth/Poisson mixture/initial growth/sharp bound”
的定向检索；无关结果未作为依据，未进行大规模综述。
这足以确认数学工具已有来源，但不足以排除本轮锐界和具体反例也早已存在。
故成果地位是“本轮独立完成的条件性推导”，不声称首次发现或数学原创性。
