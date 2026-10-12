# Literature Audit Protocol / 论文数学审查协议

This protocol specifies public archival records for completed paper audits. It is not a new runtime rule, a mandatory reasoning pipeline, or authority to audit papers automatically. [SKILL.md](../SKILL.md) remains the sole runtime specification. This update performs no literature audit.

本协议规定已完成论文审查的公开档案内容，不是新增运行规则、强制推理流水线或自动审查论文的授权。[SKILL.md](../SKILL.md) 仍是唯一运行时规范。本轮不开展文献审查。

## Scope / 范围

Choose the mathematical claim that actually needs review; a full rederivation of every part of the paper is not required. Record what was and was not checked. Journal impact or reputation is not a mathematical warrant. Separate mathematical validity from empirical or physical validation.

选择实际需要审查的数学 claim，不要求完整重做每篇论文。记录已经核查与未核查的范围，不能凭期刊影响力或声誉判定数学成立。数学有效性与经验、物理验证分别记录。

## Required contents of a formal record / 正式记录必备内容

1. **Paper identity / 论文身份。** Title, authors, year, journal (or preprint status), DOI/original link and the exact version consulted. / 题名、作者、年份、期刊（或预印本状态）、DOI／原始链接及实际使用的版本。
2. **Target mathematical claim / 目标数学 claim。** State the specific proposition, equation, bound or inference actually under review, with its source location and scope. / 写明实际待审的命题、方程、界或推断，以及来源位置和审查范围。
3. **Dependencies / 推导依赖。** Definitions, premises, applicable domain and load-bearing derivation conditions. Distinguish supplied facts from reviewer assumptions. / 定义、前提、适用域及关键成立条件；区分原文事实与审查者假设。
4. **Decisive reproduction / 决定性步骤复现。** Whether the decisive mathematical step can be reproduced; preserve a checkable derivation, script or output if actually produced. If not, state the missing premise, data or capability rather than implying success. / 能否复现决定性的数学步骤；如已完成，保留可核查推导、脚本或输出；如未完成，写明缺少的前提、数据或能力，不暗示成功。
5. **Failure and boundary cases / 反例与边界。** Relevant counterexamples, singularities, degeneracies or boundary conditions and which conclusions they affect. Explicitly say when a relevant check was not performed; no exhaustive case search is required. / 相关反例、奇异性、退化情形或边界条件，以及其影响的结论；未检查时明确说明，不要求穷尽所有情形。
6. **Separate result states / 分离结果状态。** State mathematical validity and physical/empirical validation separately, at claim level, including unresolved issues and evidence limits. A reproduced identity does not establish a real mechanism. / 按 claim 分别说明数学有效性与物理／经验验证状态、未决问题和证据限制；恒等式复现不证实真实机制。
7. **Skill failure assessment / Skill failure 判断。** Whether a generalizable Skill failure actually occurred, with the used Skill version/hash, model/environment and observable failure evidence if applicable. Paper errors or reviewer corrections are not automatically Skill failures; “not assessed” is allowed. / 是否出现可一般化的 Skill failure；如相关，记录所用版本与哈希、模型环境及可观察失败证据。论文错误或审查者纠正不自动构成 Skill 失败，允许记为“未评估”。
8. **Regression recommendation / 回归建议。** Whether to recommend a new regression and why: identify the demonstrated behavior it would protect, or explain why none is justified. Recommendation is not authorization to alter frozen tests or runtime. / 是否建议新增 regression，以及理由；说明要保护的已观察行为，或解释为何不建议。建议不等于修改冻结测试或运行规范的授权。

## Registration and evidence / 登记与证据

A candidate whose mathematical steps have not actually been checked must be labelled **candidate**, never **verified**. Create discipline record files only after a real audit is completed; a completed audit may still find invalidity, conditional validity or an unresolved blocker. Preserve these outcomes honestly rather than equating completion with success.

未实际核查数学步骤的文献必须标为**候选**，不能标为**验证成功**。仅在真实审查完成后创建学科记录文件；已完成审查也可发现无效、条件性成立或未决障碍，如实记录，不把完成等同于成功。

Keep reproducible evidence where sharing is authorized. Link to originals; do not upload unauthorized paper full texts or copyrighted PDFs. Record any public reproduction limits. Formal paper audits belong in [literature-audits](../literature-audits/README.md); comparisons of Skill behavior belong in [evaluation-reports](../evaluation-reports/README.md), with cross-links when relevant. A successful audit or published paper does not, by itself, prove Skill gain.

仅公开获授权且可复现的证据，链接原文，不上传未经授权的论文全文或受版权保护的 PDF，并说明公开复现限制。正式论文审查归入 [literature-audits](../literature-audits/README.md)，Skill 行为对照归入 [evaluation-reports](../evaluation-reports/README.md)，必要时交叉链接。论文审查成功或论文发表本身不证明 Skill 增益。
