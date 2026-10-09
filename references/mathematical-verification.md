# Mathematical verification / 数学核查

This reference explains the conditional verification guidance in [SKILL.md](../SKILL.md). It adds no runtime rules and prescribes no platform or software.
本文件解释 [SKILL.md](../SKILL.md) 的条件性核查指引，不增加运行规则，不指定平台或软件。

Use a tool when checking a particular consequential calculation could alter the answer: for example an algebraic identity, a computed bound, a counterexample, or an implemented numerical construction. A check with no plausible effect on the conclusion adds no value. Respect the existing authorization and available capabilities.
当核查某项会影响结论的具体计算可能改变答案时使用工具，例如代数恒等式、计算得到的界、反例或已实现的数值构造。不能改变结论的核查没有增益。遵守现有授权与可用能力。

Match the check to the claim. Exact algebra can check an identity under the stated domain and branch conditions. Numerical evaluation can provide a witness against a universal claim, test an implementation or illustrate model behaviour; a finite sample cannot prove a general inequality, convergence or uniqueness. An interval or certified computation supports only its specified enclosure and assumptions.
使核查与 claim 匹配。精确代数可在给定定义域与分支条件下核对恒等式。数值计算可提供否定全称命题的见证、测试实现或说明模型行为；有限抽样不能证明一般性不等式、收敛或唯一性。区间或认证计算只支持指定包围范围及其前提。

Report what was actually executed, its result and its relevant limits. Keep analytic derivation separate from computational confirmation. A tool cannot validate an unverified physical mapping merely by reproducing its mathematical consequences. If the appropriate tool is unavailable, say so and retain the justified analytic result or the specific unresolved check.
报告实际执行的核查、结果与相关限制，将解析推导与计算确认分开。工具复现数学后果不能验证尚未确证的物理映射。合适工具不可用时，如实说明，保留有依据的解析结果或具体未完成核查。
