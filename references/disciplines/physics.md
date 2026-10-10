# Physics Adapter / 物理学适配层

Status: Experimental, optional, explicitly loaded supporting guidance.

状态：实验性、可选、需显式加载的支持指引。

## Applicability / 适用条件

Use only when physical measurement semantics, system boundaries, sources, scales, or regime assumptions can materially affect the mathematical question.

仅当物理测量语义、系统边界、源项、尺度或物理状态条件能够实质影响数学问题时使用。

## Domain-sensitive distinctions / 领域敏感区别

- Measurement vs physical quantity: When a claim concerns an unobserved physical variable, identify which calibration or observable-to-quantity relation is actually supported.
- 测量与物理量：涉及未直接观测的物理量时，确认测量与目标物理量之间受到支持的关系。

- Conservation vs system exchange: Before using conservation, distinguish local balances, internal transfer, external sources, and boundary fluxes where material.
- 守恒与系统交换：在使用守恒关系前，按实际需要区分局部平衡、内部交换、外部源项及边界通量。

- Regime and scale: Apply approximations only within their supported temporal, spatial, parameter, or physical-regime conditions.
- 状态与尺度：近似关系必须限制在有依据的时间、空间、参数或物理状态范围内。

- Physical interpretation: A mathematical fit, invariant, stability condition, or conditional solution does not independently establish its proposed physical mechanism.
- 物理解释：数学拟合、不变量、稳定性条件或条件性解本身不能证明相应物理机制。

## Non-defaults / 禁止默认化

Do not assume conservation without its relevant premises; do not force dynamical equations, equilibrium, symmetry, linear response, continuum descriptions, or any particular mathematical representation.

不得在缺少相关前提时默认守恒；不得强制采用动力学方程、平衡、对称性、线性响应、连续介质描述或特定数学表述。

Do not import any device-specific, turbulence-specific, or project-specific theory as a general physical assumption.

不得把特定装置、湍流理论或项目专用结构作为通用物理前提。

## Mathematical handoff / 数学交接

Use material domain information to formulate the actual mathematical question, establish justified premises, derive feasible checkable results, and state physical applicability boundaries.

利用重要领域信息构造实际数学问题，明确有依据的前提，完成可核查的数学工作，并说明物理适用边界。

This guidance is not a mandatory checklist. Skip irrelevant distinctions. The canonical SKILL.md prevails.

本文件不是必填检查清单；不相关项直接跳过。以 SKILL.md 为最高规范。
