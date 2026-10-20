# Fable et al. (2010) — Mathematical Review / 数学审查记录

## Overall Decision / 总体结论

**ACCEPT WITH LIMITATIONS — 附限制接受。**

本记录转录项目负责人提供的、已经完成的 ChatGPT 数学内容审查结论；归档发布没有重新评议或重新证明研究结果。
This record preserves the completed ChatGPT mathematical-content review supplied by the project owner. Publication did not repeat the scientific review or proofs.

审查对象：[完整 Stage B 报告](skill-on-p1-v0.2.9/research-result.md)；物理依据：[Stage A 原文证据](source-evidence.md)及[原论文 DOI](https://doi.org/10.1088/0741-3335/52/1/015007)。
The decision applies to the stated conditional mathematics, not to full-paper validation or the paper's authors.

## Accepted mathematical results / 接受的数学结果

以下在报告声明的数学条件下接受。 / Accepted under the mathematical conditions stated in the report.

A. 有限正谱权重下，加权通量导数的协方差分解。 / Covariance decomposition of weighted-flux derivatives for a finite positive-weight spectrum.

B. 定态非退化根上，两种温度梯度的局部条件响应公式。 / Local conditional responses to electron and ion temperature gradients on a nondegenerate stationary root.

C. 固定 alpha 与按压力梯度重算 alpha 两种控制协议的局部响应差异。 / Local response differences between fixed-alpha and pressure-gradient-recomputed-alpha protocols.

D. 基于单模变化和相对谱重分配预算的符号与响应排序充分条件。 / Sufficient sign and ordering conditions based on budgets for single-mode changes and relative spectral redistribution.

E. 正负波数通量相消下的谱重分配恒等式及相反排序条件。 / The spectral-redistribution identity for cancelling signed wavenumber fluxes and sufficient conditions for the opposite ordering.

F. 保持正谱权重、零总通量及恒定负平均频率的三波数数学反例。 / A three-wavenumber mathematical counterexample retaining positive weights, zero total flux and a constant negative mean frequency.

G. 根位置误差小不自动保证条件响应导数误差小。 / Small root-position errors do not automatically imply small conditional-response derivative errors.

## Essential limitations / 关键限制

1. 结论属于指定有限谱合成模型及其正则性条件。 / Results concern the specified finite spectral-synthesis model under its stated regularity conditions.
2. 主要响应排序条件是充分条件，不是必要条件。 / The principal ordering criteria are sufficient, not necessary.
3. 三波数反例证明谱合成结构本身不足以固定排序，但未证明该反例可由真实 gyrokinetic 本征问题同时实现。 / The counterexample shows structural insufficiency for ordering; joint realizability by a genuine gyrokinetic eigenproblem has not been established.
4. ITG 主导或负平均模频率不能单独确定两种独立响应的排序。 / ITG dominance or a negative mean mode frequency alone cannot determine the ordering of the two independent responses.
5. Fable 原论文缺少完整逐模梯度导数，无法判断实际 ITG 点是否满足所推导的充分条件。 / The paper does not provide complete mode-resolved gradient derivatives, so applicability of the ordering criteria at actual ITG points is unknown.
6. 未运行新的 GS2、GYRO、GENE 或 TGLF 模拟。 / No new GS2, GYRO, GENE or TGLF simulations were run.
7. 未重新分析 HL-3 实验数据，未证明任何具体装置中的物理机制。 / HL-3 experimental data were not reanalysed; no device-specific physical mechanism has been established.
8. 本次研究显式读取冻结 Skill v0.2.9 的 Git blob，非原生 Skill 调用。 / The study explicitly loaded the frozen v0.2.9 Git blob, rather than invoking the Skill natively.
9. 没有可信 Skill OFF 对照，不能证明相对基线模型的增量优势。 / No credible Skill OFF control exists; incremental advantage over a baseline model is NOT ESTABLISHED.
10. 本审查是 ChatGPT 对数学内容的限定范围评议，不代表论文作者认可、期刊同行评审或完整独立物理验证。 / This is a limited-scope ChatGPT mathematical-content review, not author endorsement, journal peer review or complete independent physical validation.

## Scientific significance / 科学意义

电子温度梯度进入电子动力学的显式项，但定态密度梯度总响应还受单模系数、谱权重及密度反馈影响。离子温度梯度即使没有同样的显式电子通量项，也可能经谱变化产生更大的条件响应。两种情形均有数学充分条件；实际哪种发生，须由物理谱计算及其导数判定。

The electron temperature gradient has an explicit entry in electron dynamics, while the total stationary-density response also depends on modal coefficients, spectral weights and density feedback. The ion temperature gradient can yield a larger conditional response through spectral changes despite lacking the same explicit electron-flux term. Mathematical sufficient conditions exist for both cases; physical spectra and their derivatives must determine which applies.

**Actual gyrokinetic response ordering: NOT ESTABLISHED.**
**Incremental Skill capability gain: NOT ESTABLISHED.**

不宣称已经解释 HL-3 的响应、发现新的 ITG 机制或证明电子梯度实际主导。
No explanation of HL-3 responses, new ITG mechanism or actual electron-gradient dominance is claimed.

## Author-identified limitations and next analyses / 作者提出的局限与后续研究

以下按已归档[阶段 A 证据](source-evidence.md) E6、§5.4 记录作者稿的原文定位；本次未重新开展论文研究。页码均为 26 页 1stRevision 作者稿，不混用期刊分页。
The following faithfully summarizes author-identified directions using the archived Stage A evidence; this release did not conduct a new paper review.

- 作者在 §3.8、PDF p.16 提出将低/中波数的实测湍流频率与代码预测比较，以检验实验依赖是否来自相应湍流背景；这本身不能决定两种独立梯度响应的排序。 / Section 3.8, PDF p.16 proposes comparing measured low/intermediate-wavenumber turbulent frequencies with code predictions to test the inferred turbulence-regime explanation, not to establish response ordering by frequency alone.
- 作者在 §4、PDF p.18 指出，更定量的预言需要非线性模拟；p.17–18 也保留与具体实验及重要 ETG 情形进一步比较的需要。 / Section 4, PDF pp.17–18 retains further comparison with specific experiments and important ETG cases; p.18 states that more quantitative predictions require nonlinear simulations.

这些建议没有明确要求未来必须使用某个指定软件。原文在 §3 使用 GS2，并在 §3.4.3 用 GYRO 做有限比较，是既有工作记录，不等于作者要求未来重复使用同一工具。
No specific future software requirement is established by these passages. The paper's use of GS2 and its limited GYRO comparison are historical methods, not a mandate for future tool choice.

## Optional physical validation methods / 可选物理验证方法

以下来自本次独立数学研究的 [Stage B §8](skill-on-p1-v0.2.9/research-result.md)，不是原论文作者的工具推荐，也不是要求读者执行的任务。
The following are optional proposals of the independent mathematical study, not author-attributed recommendations or user obligations.

| 独立建议 / Independent proposal | 可判别内容 / Discriminator | 实际状态 / Execution |
|---|---|---|
| GS2 局域本征谱与梯度导数 / Local eigenspectra and gradient derivatives | 区分直接项、单模变化、谱重分配、密度反馈与 alpha 协议，判断真实谱是否满足排序充分条件 / Separate response contributions and test sufficient criteria under the stated controls | 未运行 / Not run |
| GYRO 非线性响应对照 / Nonlinear response comparison | 判断准线性响应排序是否在非线性饱和及完整波数重分配后保持 / Check whether ordering survives nonlinear saturation and spectral redistribution | 未运行 / Not run |

实际响应排序、三波数反例的真实本征谱可实现性仍未确立；上述建议不能自动证明任一具体装置机制。数学交付已完成其条件性范围，无需等待物理验证。未安装相关工具、未运行新模拟，也未进行实验或 HL-3 数据重分析。
Actual ordering and eigenproblem realizability remain unestablished. Conditional mathematical delivery does not require completion of physical validation; no installation, new simulation, experiment or HL-3 reanalysis occurred.
