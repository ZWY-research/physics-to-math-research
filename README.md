# physics-to-math-research

中文说明：[README.zh-CN.md](README.zh-CN.md)

**Version:** 0.1-alpha.2 (frozen artifact)

**Alpha status:** Open to research use and feedback. Alpha users are invited to report real failure cases; validation remains limited.

> Documentation is explanatory. [SKILL.md](SKILL.md) is the single normative source for this version; where this README differs from it, `SKILL.md` prevails.

## What this Skill does

`physics-to-math-research` turns a scientific or physics problem into a checked mathematical formulation and audits the integrity of the resulting claim, with diagnostic derivation where needed:

- audits whether a problem is correctly formulated as a mathematical problem;
- checks whether material modeling commitments, semantic mappings, and inferential steps carry appropriate explicit warrants;
- checks whether mathematical conclusions have been over-upgraded into stronger physical, causal, or mechanistic conclusions;
- performs diagnostic derivation only as far as needed to test whether a formulation can support the target claim and to expose its load-bearing structure.

## Why it exists

Scientific work often fails at the boundary between a phenomenon and its mathematical formulation: a correlation is reported as causation, a proxy is treated as the latent quantity it stands in for, a model-class result is reported as an unrestricted statement about the physical system, and a mathematical theorem is reported as an empirical finding.

This Skill is designed to reduce specific scientific formulation and claim-integrity failures of this kind.

## When to use it

- You need to formulate a scientific or physics problem as a mathematical problem, or audit an existing formulation.
- A claim's modeling commitments, semantic mappings, inferential steps, or status need auditing.
- Limited derivation is needed to test whether a formulation supports a target claim.

## When not to use it

- Tasks outside its scope: full theorem proving, literature review, experiment design, simulation, statistical methodology, paper writing.
- There is no scientific problem to formulate and no claim to audit.

## Core idea

The Skill is built on four fixed core rules — problem provisionality, material commitment accountability, relative identifiability, and dependency audit — plus an Observable Audit Contract (OAC) that makes results externally auditable.

High-level summaries and worked explanations live in:

- [references/core-principles.md](references/core-principles.md) — the four Core rules, bilingual.
- [references/observable-audit-contract.md](references/observable-audit-contract.md) — the OAC items, bilingual.

The OAC is not a reasoning pipeline, a chain-of-thought protocol, or an output template: it is a contract about what an external reviewer must be able to judge in the result.

## Typical input

A short scientific problem statement together with a target claim and the evidence or premises the claim is supposed to rest on. For example: *"y is measured and x is latent; y correlates strongly with x in calibration; does y1 > y2 imply x1 > x2 in the present experiment?"*

## Typical output

A claim-by-claim assessment: what each materially distinct claim states and means, which commitments and warrants it depends on, what is established, conditional, or underdetermined, and what decisive evidence or condition would change the status.

## Installation

Copy or link the skill directory into a skill library. Recommended structure:

```text
Multi_Skills/
└── physics-to-math-research/
    ├── SKILL.md
    ├── README.md
    ├── README.zh-CN.md
    └── references/
        ├── core-principles.md
        └── observable-audit-contract.md
```

For Claude Code, the skill directory can be placed in — or linked into — the user-level skill directory. The layout above is a recommendation, not a platform requirement; it does not assume Windows, OneDrive, Claude Code, or any particular model provider.

## Usage

Activate the Skill explicitly and provide the problem statement and the target claim, together with the evidence or premises in hand. The Skill does not prescribe a fixed pipeline; it applies its rules to whatever the problem actually requires and returns a claim-level status assessment. Exact runtime behavior is defined by `SKILL.md`.

## Contributing

Issues and pull requests in Chinese or English are welcome; you do not need to provide both. See [CONTRIBUTING.md](CONTRIBUTING.md). On GitHub, choose **Issues → New issue** to use the [Skill failure](.github/ISSUE_TEMPLATE/skill-failure.yml) or [improvement](.github/ISSUE_TEMPLATE/improvement.yml) form, or open a blank issue.

Licensed under [Apache License 2.0](LICENSE). Version changes are listed in [CHANGELOG.md](CHANGELOG.md).

## Validation status

**v0.1-alpha.1 — initial targeted validation only.**

Completed so far:

- architecture freeze (four Core rules, OAC, scope boundaries);
- an implementation audit;
- an initial targeted behavior regression batch (A–E pairs) covering: measurement/semantic bridge, relative identifiability, local/global dependency, mathematical vs empirical status, and model-class commitment;
- the A–E pairs passed this first-round targeted regression in one tested environment (Claude Code harness, DeepSeek API, deepseek-v4-pro).

These are initial single-run targeted tests, not repeated-run reliability estimates. Current evidence does not establish:

- correctness across models, harnesses, or providers;
- broad cross-domain validation;
- repeated-run stability;
- Chinese–English behavioral equivalence.

## Limitations

This Skill does not guarantee that scientific conclusions are correct. It is not:

- a tool for automatically proving a user's theory;
- a tool for automatically selecting the most complex mathematics;
- a tool for automatically confirming a physical mechanism;
- a replacement for domain experts;
- a universal autonomous research agent.

It audits formulation and claim integrity; it cannot supply the domain knowledge, warrants, or experimental evidence a claim may require.

## Project structure

```text
physics-to-math-research/
├── SKILL.md                             # frozen runtime specification (normative)
├── README.md                            # this file
├── README.zh-CN.md                      # Chinese equivalent
└── references/
    ├── core-principles.md               # explanation of the four Core rules
    └── observable-audit-contract.md     # explanation of the OAC items
```
