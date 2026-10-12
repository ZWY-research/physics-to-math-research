# Mathematical Tools / 数学工具导航

Select tools by the mathematical task, not a discipline label. These are optional references, read on demand, not auto-loaded runtime rules. [SKILL.md](../../SKILL.md) is unchanged. Installing the Skill does not install software; use tools only when needed by the user's task and authorized. Do not install every tool by default.

按数学任务而非学科标签选择工具。本页是按需阅读的可选参考，不自动加载、不增加运行规则。[SKILL.md](../../SKILL.md) 保持不变。安装 Skill 不会安装软件；仅在用户任务需要且已授权时使用，不要求安装全部工具。

| Mathematical task / 数学任务 | Tool / 工具 | Main limitation / 主要限制 | Official documentation and installation / 官方文档与安装入口 |
| --- | --- | --- | --- |
| Simple analytic mathematics / 简单解析数学 | Direct derivation first; no installation / 优先直接推导，无需安装 | State the necessary conditions; hand derivation can still contain errors / 需说明成立条件，手工推导仍可能出错 | No software required / 无软件依赖 |
| Symbolic computation, algebraic simplification, analytic integration / 符号计算、代数化简、解析积分 | SymPy | Results depend on symbol assumptions, domains and branch choices; expressions may remain unevaluated / 依赖符号假设、适用域与分支选择，可能无法给出闭式结果 | [SymPy installation](https://docs.sympy.org/latest/install.html) |
| Numerical integration, ordinary differential equations, optimization / 数值积分、常微分方程、优化 | SciPy | Error tolerances, conditioning and convergence matter; sampling is not proof and local optimization need not find a global optimum / 误差容限、条件数与收敛性影响结果；数值抽样不是证明，局部优化不保证全局最优 | [SciPy installation](https://scipy.org/install/) |
| Dimensions and units / 量纲和单位处理 | Pint | Compatible units do not establish a model or semantic correspondence; custom units need correct definitions / 单位相容不证实模型或语义对应，自定义单位须正确定义 | [Pint documentation](https://pint.readthedocs.io/en/stable/) · [Installation](https://pint.readthedocs.io/en/stable/getting/index.html#installation) |
| Formal proof, only when machine checking is actually needed / 仅在确需机器核查时作形式化证明 | Lean 4 | Formalization needs explicit definitions and premises; a checked theorem does not verify empirical applicability / 形式化需明确的定义和前提，通过证明核查不等于经验适用性验证 | [Lean installation](https://lean-lang.org/install/) |

For optional Python packages, see [Python setup](python-setup.md). Lean is a separate ecosystem; it is not a Python dependency. Large domain-specific software is not a default dependency.

Python 可选库的配置见 [Python 环境说明](python-setup.md)。Lean 属于独立工具体系，不是 Python 依赖。大型领域专用软件不纳入默认依赖。

Record software versions, inputs, assumptions and relevant numerical settings with actual computations. Numerical sampling does not constitute strict proof; symbolic or formal outputs do not supply missing physical evidence. See existing [mathematical verification limits](../mathematical-verification.md).

实际计算时记录软件版本、输入、前提及相关数值设置。数值抽样不构成严格证明，符号或形式化输出不能补出缺失的物理证据。参见现有[数学核查边界](../mathematical-verification.md)。
