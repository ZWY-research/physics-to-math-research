# Skill Evaluation Reports / Skill 行为评估档案

This archive evaluates the Skill's behavior, not the validity of a published paper. The [literature audit archive](../literature-audits/README.md) and its [protocol](../docs/literature-audit-protocol.md) are separate. Reports are evidence, not runtime rules; [SKILL.md](../SKILL.md) alone defines runtime behavior.

本目录记录 Skill 自身行为评估，不等同于对论文数学结论的审查。[论文审查档案](../literature-audits/README.md)及其[协议](../docs/literature-audit-protocol.md)独立维护。报告是证据而非运行规则；运行规范仅由 [SKILL.md](../SKILL.md) 定义。

## Existing reports / 已有报告

| Field / 领域 | Report / 报告 | Original Skill / 原始版本 | Evidence boundary / 证据边界 |
| --- | --- | --- | --- |
| Materials science / constitutive modeling（材料科学／本构建模） | [Can calibration evidence identify material response?](2026-10-09-can-calibration-evidence-identify-material-response.md) | v0.1-alpha.2 | Four-cell comparison; no material ON/OFF advantage established. / 四格对照，未建立实质性 ON/OFF 优劣。 |
| Physics / plasma and fusion（物理／等离子体与聚变） | [Can linear stability rule out sustained tokamak turbulence?](2026-10-09-can-linear-stability-rule-out-sustained-tokamak-turbulence.md) | v0.1-alpha.2 | One ON/OFF pair; internal same-model review tied. / 一组成对测试，内部同模型评价持平。 |
| Physics / plasma and fusion（物理／等离子体与聚变） | [Can ITG gradient scans distinguish turbulent states?](2026-10-09-can-itg-gradient-scans-distinguish-turbulent-states.md) | v0.1-alpha.2 | Narrow positive signal; reliable incremental value not established. / 窄幅正向信号，可靠增量价值尚未建立。 |

[Plasma and fusion navigation / 等离子体与聚变导航](physics/plasma-and-fusion/README.md). The current version's separate [v0.2-alpha.0 validation summary](../docs/v0.2-alpha.0-validation.md) does not relabel these historical reports.

[等离子体与聚变导航](physics/plasma-and-fusion/README.md)。当前版本的 [v0.2-alpha.0 验证摘要](../docs/v0.2-alpha.0-validation.md)不改变上述历史报告的版本归属。

## Classification and provenance / 分类与来源

Physics is subdivided only as actual cases arrive: plasma and fusion, condensed matter, optics and photonics, fluids and continua, for example. Do not create empty subdiscipline folders. Cross-disciplinary cases may be cross-indexed; do not duplicate or move source reports. Existing public report paths remain stable.

物理学仅随实际案例按等离子体与聚变、凝聚态、光学与光子学、流体与连续介质等细分。尚无案例时不创建空子学科目录。跨学科案例允许交叉索引，不复制或迁移原始报告，保留既有公开链接。

Formal results retain original Skill version/hash, inputs, test conditions, review method and evidence limitations. Publication, paper-audit success or a positive isolated signal is not by itself attributable Skill gain. Original reports contain the controlling details; this index does not re-score them.

正式结果保留原始 Skill 版本与哈希、输入、测试条件、评价方法和证据限制。论文发表、论文审查成功或单个正向信号本身不构成可归因的 Skill 增益。准确细节以原始报告为准，本索引不重新评分。
