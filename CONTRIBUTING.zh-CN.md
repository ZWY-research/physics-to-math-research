# 参与贡献

English: [CONTRIBUTING.md](CONTRIBUTING.md)

中文和英文都是本项目的一等语言。欢迎使用任一语言提交 issue 或 pull request，无需同时提供双语版本；维护者可以协助同步另一种语言。对 `SKILL.md` 的实质性规范变更，合并前须完成中英文语义等价性审查。

## 欢迎哪些贡献

- 可复现的 Skill 失效案例，以及科学领域中的边界案例。
- 过度怀疑、过早停止，或无依据地强化 claim 的实例。
- 更清晰的措辞和文档。
- 从已观察到的失败中提炼出的回归案例。

目标是改善科学到数学的表述和科研推理。不会仅因为一条新规则听起来更安全或更严谨，就接受它。

## 如何参与

带一个真实科学问题到 [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions) → [Research Problems 科学问题](https://github.com/ZWY-research/physics-to-math-research/discussions/new?category=general)（目前为 General 分类）。无需 Core/OAC 术语或完整 formulation。开放的方法问题可在此讨论，可复现 failure 或具体工作使用 Issues。[Casebook](cases/README.md) 用于沉淀成熟案例；[Welcome 草稿](.github/WELCOME_DISCUSSION.md) 汇总参与方式。

实质性科研贡献可在案例记录、发布说明、贡献历史或相关文档中署名或致谢。认可应与实际贡献相匹配；不承诺论文作者资格或自动授予维护者身份。

在 GitHub 仓库中打开 **Issues → New issue**，选择 **Skill failure（Skill 失效）** 或 **Improvement proposal（改进建议）**，也欢迎使用空白 issue。[失效表单](.github/ISSUE_TEMPLATE/skill-failure.yml) 会询问提示词、实际输出、预期行为，以及已知的复现环境；无需指出是哪条 Core 规则或 OAC 项出了问题。[改进表单](.github/ISSUE_TEMPLATE/improvement.yml) 可用于方法、文档、领域支持或易用性建议，也可以直接提交 pull request。

对于方法变更，最好说明：

1. 一个具体的失败。
2. 它为什么影响科研工作。
3. 建议的最小修复。
4. 预期的回归风险。
5. 尽可能提供可复现的提示词和输出。

不要求建立完整 benchmark。仅修正错字或文档的变更无需提供方法学证据。请只分享有权公开的材料，去除密钥和私人信息，并说明案例是否可以公开用于回归开发。

## 科研应用与验证

登记实际 Skill 使用时，可提交 issue 或 pull request 更新 [RESEARCH_APPLICATIONS.md](RESEARCH_APPLICATIONS.md)。按其八字段格式填写，将背景参考文献、经作者确认的论文和验证证据分开。仅分享获准公开的材料及经确认的姓名。论文须提供作者明确确认的来源与日期；验证须说明具体能力、版本、可复现材料、结果与限制。证据缺失可以明确标注；登记应用不要求完整 benchmark。登记不改变运行规则。

## 各类文件的效力

- `SKILL.md` 是运行行为的规范性来源。
- README 和 `references/` 用于解释 Skill，不增加运行规则。
- 评测是证据，不是运行指令。
- `PROJECT_STATE.md` 记录维护者的开发状态，不属于运行行为。

本项目使用 [Apache License 2.0](LICENSE)。
