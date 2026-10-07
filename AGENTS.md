# Agent guidance — physics-to-math-research

Use the repository files as the source of project context; do not assume access to prior conversations.

Before changing runtime behavior, read `SKILL.md` and the relevant contribution guide. Read only the explanatory references needed for the task.

## Authority and improvement

- `SKILL.md` is the sole normative source for runtime behavior.
- READMEs and `references/` are explanatory; they do not add runtime rules.
- Evaluation results are evidence, not runtime instructions. Preserve their version-specific provenance.
- Prefer failure-driven improvement: use the Skill, compare results, identify concrete failures, and make the smallest sufficient repair.
- Do not add methodology rules merely because they sound safer or more rigorous. Runtime changes need a demonstrated reason or an explicitly authorized design change.
- Follow the scope in `SKILL.md`; do not silently expand the project into a universal research agent or a complete theorem-proving, statistical, causal, simulation, or experiment-design framework.
- For runtime revisions, explain the motivating failure or capability, the smallest repair, and regression risk; record the version and artifact hash.

## Languages and participation

Chinese and English are first-class project languages. Contributions may use either language; contributors need not supply both. Maintainers may help synchronize translations. Material normative changes to `SKILL.md` require Chinese–English semantic-equivalence review before merge.

中文和英文都是本项目的一等语言。贡献可使用任一语言，无需同时提供双语版本；维护者可协助同步翻译。对 `SKILL.md` 的实质性规范变更，合并前须完成中英文语义等价性审查。

See [CONTRIBUTING.md](CONTRIBUTING.md) or [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md) for reporting failures and proposing changes.
