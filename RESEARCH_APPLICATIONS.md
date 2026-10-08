# Research Applications & Validation / 科研应用与验证

A growing register of research problems explored with this Skill, author-confirmed publications using it, and reproducible capability evidence. This register is descriptive documentation; [SKILL.md](SKILL.md) remains the sole normative runtime source.

持续登记使用本 Skill 探索的科研问题、经作者确认使用 Skill 的论文，以及可复现的能力证据。本登记是描述性文档；[SKILL.md](SKILL.md) 仍是唯一运行时规范来源。

## What each record means / 三类记录的含义

| Type / 类型 | Meaning and boundary / 含义与边界 |
| --- | --- |
| Research application / 科研应用 | A research problem actually explored with the Skill. A `planned` candidate is only a placeholder and is not counted as actual use. / 实际使用 Skill 探索过的科研问题；`planned` 候选仅为占位，不计作实际使用。 |
| Publication / 使用 Skill 的论文 | A paper or preprint whose author explicitly confirms Skill use. Record the paper link, publication stage, Skill contribution, and a publicly shareable confirmation source and date. Background citations do not qualify. / 作者明确确认使用 Skill 的论文或预印本；记录论文链接、发表阶段、Skill 的具体贡献，以及可公开分享的确认来源和日期。背景引用不属于此类。 |
| Validation evidence / 验证证据 | A reproducible test, comparison, or independent review of a specified Skill capability, with accessible materials and bounded conclusions. / 针对某项明确 Skill 能力的可复现测试、比较或独立审查，附可访问材料与有边界的结论。 |

Use does not establish validation; publication does not establish validation. Background references, publications using the Skill, and validation evidence are recorded separately. A paper can supply validation evidence only when its actual protocol and materials support that capability claim.

使用 Skill 不等于验证 Skill，论文发表也不等于验证 Skill。背景参考文献、使用 Skill 的论文和验证证据分别记录。论文只有在实际测试方案与材料支持相应能力 claim 时，才能另作验证证据。

## Application status / 应用状态

| Status / 状态 | Definition / 定义 |
| --- | --- |
| `planned` / 计划中 | Candidate; actual Skill use has not been documented. / 候选问题，尚未记录实际 Skill 使用。 |
| `testing` / 试用中 | Actual Skill exploration is documented; work and assessment are ongoing. / 已记录实际 Skill 探索，研究与评估仍在进行。 |
| `completed` / 已完成 | The stated exploration is finished, with a linked account of its outcome and limits. / 所述探索已结束，附结果与限制的记录链接。 |
| `paused` / 暂停 | Exploration is suspended; record the reason and what would allow resumption. / 探索暂停，记录原因及恢复条件。 |

These statuses describe application progress, not scientific claim status, publication stage, or capability validation. Validation entries report their own outcome, including failures, mixed results, and limitations; absent evidence is explicitly marked `None recorded`.

这些状态描述应用进度，不代表科学 claim 状态、论文发表阶段或能力验证。验证条目单独报告结果，包括失败、混合结果与限制；没有证据时明确写 `None recorded / 暂无登记证据`。

## Application index / 应用索引

No actual-use records, author-confirmed publications, or application-specific validation evidence have been registered here yet. This does not replace the version-specific historical evidence described in the READMEs.

本表目前尚无实际使用记录、经作者确认的论文或应用专项验证证据。这不替代 README 中说明的版本专属历史证据。

| ID | Domain / 领域 | Research problem / 科研问题 | Application status / 应用状态 | Record / 记录 |
| --- | --- | --- | --- | --- |
| RA-001 | Plasma physics / 等离子体物理 | HL-3 density peaking / HL-3 密度峰化 | `planned` | [RA-001](#ra-001) |

<a id="ra-001"></a>

### RA-001 — HL-3 density peaking / HL-3 密度峰化

| Field / 字段 | Record / 记录 |
| --- | --- |
| Domain / 领域 | Plasma physics / 等离子体物理。 |
| Research problem / 科研问题 | HL-3 density peaking; candidate placeholder only. The specific question and evidence await a shareable submission. / HL-3 密度峰化；仅候选占位，具体问题与证据待可公开提交材料补充。 |
| Authors / contributors / 作者与贡献者（经确认） | Not listed; identity confirmation and permission to disclose are not recorded. / 暂不列出；尚无身份确认及披露授权记录。 |
| Skill version / Skill 版本 | Planned target: `v0.1-alpha.2`; actual version used: not recorded. / 计划目标版本：`v0.1-alpha.2`；实际使用版本：尚未记录。 |
| Application status / 应用状态 | `planned`; no actual-use record supplied. / 计划中；尚未提供实际使用记录。 |
| Background references / 背景参考文献 | None recorded; shareable sources await confirmation. / 暂无登记；待确认可公开来源。 |
| Publications using the Skill / 使用 Skill 的论文（仅经确认） | None confirmed. No Skill-assisted publication or published result is claimed. / 暂无确认；不宣称存在 Skill 辅助论文或已发表结果。 |
| Validation evidence / 验证证据 | None recorded; not validated. / 暂无登记证据；未经验证。 |

## Add or update a record / 新增或更新记录

Submit an issue or pull request as described in [CONTRIBUTING.md](CONTRIBUTING.md) / [参与贡献](CONTRIBUTING.zh-CN.md). Either language is sufficient. Use a stable ID and the eight fields above; explicitly mark unknown, absent, or undisclosed information. Link a shareable use account (question, relevant Skill output, context, date, and actual version) before changing `planned` to `testing`. Link an existing case or discussion where available; do not duplicate its full contents.

按贡献指南提交 issue 或 pull request，使用中文或英文均可。采用稳定编号及上述八个字段；对未知、缺失或不披露的信息明确标注。将 `planned` 改为 `testing` 前，链接可公开的使用记录（问题、相关 Skill 输出、环境、日期及实际版本）。如已有案例或讨论，链接它们即可，不重复全文。

List names only with confirmation and disclosure permission. For each publication, record its real title and URL or DOI if available, its stage (preprint or published), the specific Skill contribution, and the author's explicit confirmation source and date. An unconfirmed paper stays out of the publication field; include it as background only if it is relevant background literature.

姓名仅在确认且获准披露后列出。每篇论文记录真实题名、URL 或已有 DOI、阶段（预印本或已发表）、Skill 的具体贡献，以及作者明确确认的来源与日期。未确认论文不进入使用 Skill 的论文字段；仅当其确属相关背景文献时，才列入背景字段。

For validation evidence, link the tested capability, exact Skill version and preferably artifact hash, model/harness context, inputs and relevant outputs, reproducible protocol or independent-review basis, comparison condition if used, results, and limits. Identify independent reviewers and their relationship to the contributors where disclosure is permitted. Link existing evidence without changing its original conclusions or attaching it to a different artifact. Restricted materials must be marked as such; do not present them as publicly reproducible evidence.

验证证据应链接：所测能力、准确 Skill 版本及尽可能提供的文件哈希、模型与运行环境、输入和相关输出、复现方案或独立审查依据、如有比较则说明对照条件、结果与限制。在允许披露时，说明独立审查者及其与贡献者的关系。引用已有证据时保留原结论与原测试版本归属。受限材料须明确标注，不将其表述为公众可复现证据。
