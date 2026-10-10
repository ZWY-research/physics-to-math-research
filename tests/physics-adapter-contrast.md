# Physics Adapter — Experimental Contrast Cases

Status: Specified, not executed.

These fixtures test optional physics-domain guidance, not independent proof of adapter benefit. Provide only Input to the evaluated model.

## P+ — Closed-system balance

Input:

在有界光滑区域 Ω 内，已知

∂tρ + ∇·J = 0

且边界满足 J·n = 0。

在足以使用积分与散度定理的正则性条件下，求总量 M(t)=∫Ωρ 的变化规律，并给出依据。

Acceptance:

必须完成 dM/dt=0 的推导，说明其依赖局部连续性方程、零边界通量及必要正则性。不能仅建议积分求解。

## P− — Open-system countercase

Input:

仍有 ∂tρ + ∇·J = 0，但现在边界总外向通量 F(t)=∫∂Ω J·n dS > 0。

能否继续断言总量 M(t) 守恒？

Acceptance:

必须得到 dM/dt=−F(t)<0，不能无依据假设系统封闭，也不能把局部连续性方程直接升级为全局总量守恒。

## P0 — Irrelevant-domain guidance

Input:

已测得同一仪器的两个信号 y1>y2，假设 y=h(x)，但未知 h 的单调性。能否断言潜在量 x1>x2？

Acceptance:

不能直接推断潜在量顺序；可用 h(x)=x 和 h(x)=−x 作为相反的相容见证。不得无关地引入守恒定律、平衡方程或动力学模型。

## Evaluation boundary

All cases are currently unexecuted. Mathematical equivalence is allowed. Compare Core-only and Core-plus-physics guidance under matched conditions before claiming improvement.
