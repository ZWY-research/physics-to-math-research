# Contributing

中文：[CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)

Chinese and English are first-class project languages. Issues and pull requests in either language are welcome; you do not need to provide both. Maintainers can help synchronize the other language. Material normative changes to `SKILL.md` require Chinese–English semantic-equivalence review before merge.

## Useful contributions

- Reproducible Skill failures and scientific-domain edge cases.
- Examples of excessive skepticism, premature stopping, or unsupported strengthening of a claim.
- Clearer wording and documentation.
- Regression cases derived from demonstrated failures.

The goal is better scientific-to-mathematical formulation and research reasoning. A proposed rule is not accepted merely because it sounds safer or more rigorous.

## How to participate

In the GitHub repository, open **Issues → New issue** and choose **Skill failure** or **Improvement proposal**. Blank issues are also welcome. The [failure form](.github/ISSUE_TEMPLATE/skill-failure.yml) asks for the prompt, observed output, expected behavior, and reproduction context where known. You do not need to identify a Core rule or OAC item. Use the [improvement form](.github/ISSUE_TEMPLATE/improvement.yml) for methodology, documentation, domain-support, or usability suggestions. You may also submit a pull request directly.

For a methodology change, preferably describe:

1. A concrete failure.
2. Why it matters for research.
3. The smallest proposed repair.
4. The expected regression risk.
5. A reproducible prompt and output, when possible.

A complete benchmark is not required. Typo fixes and documentation-only changes do not need methodology evidence. Share only material you may publish, omit secrets and private information, and indicate whether an example may be publicly reused for regression development.

## Sources of authority

- `SKILL.md` is the normative source for runtime behavior.
- READMEs and `references/` explain the Skill; they do not add runtime rules.
- Evaluations are evidence, not runtime instructions.
- `PROJECT_STATE.md` records maintainer development state; it is not part of runtime behavior.

The project uses the [Apache License 2.0](LICENSE).
