# Literature Mathematical Audits / 论文数学审查档案

This archive is for completed, claim-specific mathematical reviews of journal papers and preprints, governed by the [literature audit protocol](../docs/literature-audit-protocol.md). It is separate from [Skill behavior evaluations](../evaluation-reports/README.md). These archival requirements do not change the [runtime Skill](../SKILL.md).

本目录保存对期刊论文及预印本中特定数学 claim 的真实审查记录，遵循[论文数学审查协议](../docs/literature-audit-protocol.md)，与 [Skill 自身行为评估](../evaluation-reports/README.md)分开。档案要求不改变[运行时 Skill](../SKILL.md)。

## Current status / 当前状态

Reviewed papers: **1** / 已完成限定范围独立审查：**1 篇**。

The count covers distinct papers with accepted independent, limited-scope mathematical reviews, not every result in those papers. Skill behavior evaluations remain separate and are not automatically counted as paper audits.

数量仅统计完成限定范围独立审查的不同论文，不代表整篇论文、全部热库模型或实验结论均已验证。Skill 行为评估仍独立维护，不自动计入论文审查。

### Selection & Purpose / 选文原则与审查目标

We prioritize selected cases with scientific significance, reproducibility and mathematical research value, rather than total audit count. Selection may reflect a representative physical result, an innovative method, a clear foundational mathematical question or interdisciplinary potential. Journal reputation and citation counts describe scholarly context, not mathematical correctness. “Reviewed” means a specified scope was independently checked, not that every paper conclusion was validated.

重视有科学意义、可复现且具有数学研究价值的精选案例，不追求审查总数。选文理由可包括代表性物理结果、创新方法、清楚的基础数学问题或跨学科潜力。期刊声誉和引用次数仅说明学术背景，不证明数学正确性。“已审查”指特定范围完成独立数学审查，不代表论文全部结论均获独立验证。

## Physics / 物理学

### Statistical Mechanics / 统计物理与非平衡热力学

**C. Jarzynski (1997), *Nonequilibrium Equality for Free Energy Differences*, Physical Review Letters 78, 2690–2693.**

Why selected: this study connects work statistics from finite-time nonequilibrium processes to equilibrium free-energy differences, offering a clear physical-to-mathematical case.

选文理由：该研究将有限时间非平衡过程中的功统计与平衡自由能差联系起来，提供了一个清晰的物理—数学转换案例。

- DOI：[https://doi.org/10.1103/PhysRevLett.78.2690](https://doi.org/10.1103/PhysRevLett.78.2690)
- [Formal mathematical audit / 正式数学审查报告](physics/statistical-mechanics/1997-jarzynski-nonequilibrium-free-energy.md) — Reviewed, limited scope; independent review accepted on 2026-10-12, as confirmed by the research lead. / 经科研负责人确认，限定范围独立数学审查于 2026-10-12 通过。
- Reviewed / 已审查：isolated Hamiltonian core proof, general measure-theoretic structure, two-state counterexamples and estimation boundaries. / 孤立哈密顿系统核心证明、一般测度论结构、两态反例及估计边界。
- Not reviewed / 未审查：complete reservoir dynamics, all paper derivations and actual experimental validation. / 完整热库动力学、全部论文推导和实际实验验证。
- Classification tags / 分类标签：Statistical Mechanics, Nonequilibrium Thermodynamics, Fluctuation Relations。
- Regression candidates have not undergone Skill ON/OFF testing and provide no demonstrated capability gain. / Regression candidates 尚未经过 Skill ON/OFF 检验，不构成实际能力增益证据。

Evidence / 原始证据：[script / 脚本](physics/statistical-mechanics/two-state-check.py)、[actual first-stage output / 第一阶段实际输出](physics/statistical-mechanics/two-state-check-output.txt)、[first-stage execution record / 第一阶段执行记录](physics/statistical-mechanics/execution-record.md)。

The three original evidence files retain their exact reviewed bytes. The execution record's DRAFT status, local paths and relative `audit-draft.zh-CN.md` link describe the historical first-stage directory; that historical link is not a current archive navigation link. Use the formal report link above for the renamed report. The report's retained first-stage narrative is read together with its updated review status.

三个原始证据文件保留已审查字节。执行记录中的 DRAFT 状态、本地路径及相对链接 `audit-draft.zh-CN.md` 属于第一阶段历史目录，不是当前归档导航链接；正式报告已改名，请使用上方正式报告入口。报告中保留的第一阶段叙述须结合更新后的审查状态阅读。

Only after a real audit is completed should its corresponding discipline record file be created. A paper not actually checked is a candidate, never a successful verification. Do not populate empty discipline folders. Cross-index interdisciplinary cases without duplicating records.

仅在真实论文审查完成后创建对应学科记录文件。未实际完成数学核查的文献只能标为候选，不能标为验证成功。不创建空学科目录；跨学科案例交叉索引，不复制记录。

Do not upload unauthorized full texts or copyrighted PDFs. Prefer DOI/publisher/preprint links and permitted minimal excerpts. Journal prestige does not establish mathematical validity, and publication or audit success alone does not establish incremental Skill capability.

不上传未经授权的论文全文或受版权保护的 PDF。优先使用 DOI、出版社或预印本链接及允许公开的最小摘录。期刊影响力不能判定数学成立；论文发表或审查成功本身也不构成 Skill 增量能力证据。

## Author & Community Feedback / 作者与社区反馈

Authors and researchers may voluntarily contribute explanations, corrections, proofs, public evidence, counterexamples and new questions through [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) or [Issues](https://github.com/ZWY-research/physics-to-math-research/issues). Review is claim-specific, not a paper/author pass/fail verdict. Genuine errors remain evidence-based findings; open questions and limited coverage are not automatically errors. Participation or endorsement by any author is not implied; paper-review success is separate from Skill gain.

欢迎作者与研究者通过 [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) 或 [Issues](https://github.com/ZWY-research/physics-to-math-research/issues)自愿补充解释、更正、证明、可公开证据、反例及新问题。审查针对具体命题，不评定论文或作者通过／失败；真实错误按证据记录，开放问题或有限覆盖不自动构成错误。不暗示作者已参与或认可；论文审查成功与 Skill 增益分开判断。

[Project / 项目入口](../README.md)
