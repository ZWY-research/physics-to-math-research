# Ott–Antonsen (2008) — Limited-scope mathematical reconstruction / 限定范围数学重建

## Paper selection, identity and significance / 选文与论文身份

Edward Ott and Thomas M. Antonsen (2008), *Low dimensional behavior of large systems of globally coupled oscillators*,
Chaos **18**, 037113. [DOI](https://doi.org/10.1063/1.2930766) ·
[作者公开全文](https://terpconnect.umd.edu/~antonsen/PublicationsTMA/Synchronization/037113_1_online.pdf)。

选择理由：该论文为复杂全局耦合振子系统的宏观行为提供重要的低维数学描述，
并为分析流形外初态的同步瞬态提供了明确起点。
本文的科学贡献来自原作者；以下新增界与反例是本案例独立研究的对象，不能归为原论文已发表结论。
Actual source: published-paper PDF, article pp. 037113-1–6, with publisher cover;
original study 2026-10-21, archival minor revisions 2026-10-22.
正文页码、公式定位、读取范围及后续原始研究均见[来源与基线](../../../cases/ott-antonsen-2008/source-and-baseline.md)。

## Review decision / 审查结论

**Independent Mathematical Reconstruction: ACCEPTED AFTER MINOR REVISIONS.**

**独立数学重建：完成小修后接受。**

本状态落实本案例终审小修的限定范围决定，并由归档时的局部数学复核支持；
不是对 Ott–Antonsen 原论文或作者的通过/失败评定，不冒称期刊同行评审或独立外部人工裁决。

| Evidence stream / 证据类别 | Status / 状态 |
|---|---|
| Specified mathematical reconstruction / 指定数学重建 | ACCEPTED AFTER MINOR REVISIONS |
| Originality / 数学原创性 | NOT ESTABLISHED |
| Empirical / Physical Validation / 经验及物理验证 | NOT ESTABLISHED |
| Skill Incremental Gain / Skill 增量优势 | NOT ESTABLISHED |

## Actual review scope / 实际审查范围

- OA 流形与混合 Poisson 核的关系，以及共同平均场下有限正混合的序参量演化。
- 固定初始幅值的严格瞬时增长率界、整个开区间的可达性。
- 满足原始频率解析条件的合法光滑正密度提升。
- 相同一阶条件 Fourier 信息、但初始增长方向不同的反例。

定义、逐步解析证明和实际算术证据的唯一完整记录：
[mathematical-result.md](../../../cases/ott-antonsen-2008/mathematical-result.md)，第2–6节。
本文件只记录正式审查结论，不复制建立第二份完整证明。

### Claim, assumptions and decisive reconstruction / 命题、条件及决定性重建

初态类 C 限于：连续极限、无外驱/噪声/时延的第一谐波 Kuramoto 模型；
Lorentzian 半宽 $\Delta>0$；$K>0$；有限核数；正固定权重和为1且不依赖频率；
每个核共享自洽平均场，实频率模小于1，并有下半频率平面有界解析延拓及足够大圆衰减。

令 $R=|z|$，固定 $z(0)=r\in(0,1)$。在该初态类内，
$$
-\Delta<\frac{\dot R(0)}r<-\Delta+K(1-r^2).
$$
该开区间中每一点都可达，两端是下确界和上确界而非本类光滑初态可取的极值。
同一初始序参量下初始增长与衰减可以共存，当且仅当
$$
K(1-r^2)>\Delta.
$$

决定性步骤为复二阶中心矩的三角不等式、两种双核构造的线性插值，
以及有理解析函数将极点状态提升为合法密度。
[数学结果第3–5节](../../../cases/ott-antonsen-2008/mathematical-result.md)
给出推导；原始编号 (1)–(12) 保留。
$\Delta=1$、$K=3/2$、$r=1/4$ 时，三个见证的 $\dot R(0)$ 分别为
$5/256$、$-19/256$、$-43/256$，初始一阶条件 Fourier 函数完全相同。

### Two completed minor revisions / 两项已完成小修

1. 加入 Engelbrecht–Mirollo (2020) 原始研究：
   [DOI](https://doi.org/10.1103/PhysRevResearch.2.023057)、
   [实际核对的作者预印本 v1](https://arxiv.org/pdf/2002.07827)。
   Poisson 测度加权混合与流形外分析已有文献基础。
   有限频率群体的非吸引结论不能直接移植为连续频率分布下宏观不吸引；
   强拓扑与附加条件下的较弱/宏观渐近行为分别记录。
2. 在[数学结果第3节](../../../cases/ott-antonsen-2008/mathematical-result.md)补全
   实部/虚部多项式向量场的局部存在唯一性。
   在每个 $|u_j|=1$ 边界上，
   $d|u_j|^2/dt=-2\Delta<0$；紧的不变闭圆盘乘积与延拓定理给出全局正时间有限维解。
   此结论不自动提供任意初态 PDE、长期物理吸引性或全局同步证明。

### Boundaries and checks not performed / 边界与未完成事项

$R=0$ 的相对增长率不定义；$r=1$、奇异原子、非 Lorentzian 频率、
频率相关混合权重、高谐波耦合和有限振子数不在本命题范围。
三个见证只是本类初态的数学构造；初始增长不等于长期有序，不否定原论文的流形上公式。
没有审查原论文的全部结果，没有建立一般初态长期同步行为，
也没有证明所有光滑初态都满足本次锐界。
未开展实验、科学模拟、全状态空间穷尽检查或现实装置验证。

## Research provenance and Skill assessment / 运行来源与 Skill 判断

实际研究版本为 **v0.2.12**，通过显式读取工作树 SKILL.md 与科研工作流说明运行，
不宣称已核实的原生自动调用。
公开可核实的版本来源：
[提交 28ac6bcb0e4f 的 SKILL.md](https://github.com/ZWY-research/physics-to-math-research/blob/28ac6bcb0e4fd502f1340c0fa040fd84bbe5d924/SKILL.md)；
Git blob SHA-256：`852bbb298d647f92e6298ae816fb8e573a613bd91ad5b5301e3c74d0156bdb52`。
研究由 Codex 执行；精确模型快照与推理设置没有独立归档元数据，不补造。
第6节保留 PowerShell/.NET Decimal 精确算术记录；归档时再次核对三个有理数，未做时间积分。

没有可信 OFF 对照；本案例不证明 Skill 增量优势。
两项文献/正则性补充是本次研究报告的小修，不自动构成可迁移 Skill failure。
本次没有发现需要修改四条 Core、六项 OAC 或十五项 Prohibited Defaults 的证据；
目前不建议新增 Regression，也未新增行为测试或运行规则。
v0.2.13 是本次归档发布版本，不是本研究实际运行版本。

## Author questions, later work and continuation / 作者问题与续研

2008原文 V（037113-5）询问流形上宏观吸引子的更一般适用性；
脚注24（037113-6）已提醒宏观行为与微观密度吸引性须区分。
原作者提出的是这些研究问题及流形方法，不是下面这项本案例建议。
2009后续研究在条件下建立宏观渐近结果；2018圆累积量、
2020加权 Poisson 混合和2022流形外瞬态描述提供相关发展，
逐项来源、条件与版本见[基线](../../../cases/ott-antonsen-2008/source-and-baseline.md)。

本案例的独立可选下一节点：初始正增长持续时间的可计算下界。
**尚未执行**；不要求读者运行模拟，本次发布不启动该节点。
[公开数学交接](../../../cases/ott-antonsen-2008/CONTINUATION.md)
保留最少定义、假设、未决问题和可直接执行的解析动作。

## Archived evidence identity / 归档证据身份

下列 SHA-256 对公开 UTF-8 Markdown 的 LF 字节计算；可独立校验完整证明和历史计算。
不含受版权保护的论文副本。

| Public artifact | SHA-256 |
|---|---|
| [source-and-baseline.md](../../../cases/ott-antonsen-2008/source-and-baseline.md) | `accb668236fa880d6a946e4dd4101e556c688d44f3095e61e6437cd369681154` |
| [mathematical-result.md](../../../cases/ott-antonsen-2008/mathematical-result.md) | `2d3cb52f88b0b6382d20b35a3855adbcefa5d6ec78cb4a36faaf1c5d8c3dbb97` |
| [CONTINUATION.md](../../../cases/ott-antonsen-2008/CONTINUATION.md) | `988cc65657ccfa2790db62ff75088415a7f364eddb9ebabe035a4d67d0ddc6b3` |

本审查基于合法公开文献和独立数学记录，不暗示原作者参与、认可、收到邀请或与本项目合作。
可通过项目 [Issues](https://github.com/ZWY-research/physics-to-math-research/issues)
和 [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) 自愿提出纠正和证据。
[审查目录](../../README.md) · [项目入口](../../../README.md)。
