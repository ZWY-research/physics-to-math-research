# Example 2 — Weighted flux to a parameter criterion / 示例二：从加权通量到参数判据

**Invocation:** “Use physics-to-math-research. Given $G=(w_1f_1+w_2f_2)/(w_1+w_2)$ with positive weights, find conditions under which decreasing component fluxes imply a decreasing total.”
**调用：**“使用 physics-to-math-research。给定正权重下的 $G=(w_1f_1+w_2f_2)/(w_1+w_2)$，求分量通量递减能够推出总量递减的条件。”

**Development:** On an interval, let $w_i>0$ and $w_i,f_i$ be continuously differentiable. Set $p=w_1/(w_1+w_2)$ and $r=\log(w_1/w_2)$. Direct differentiation gives $p'=p(1-p)r'$ and
**推进：**在某区间上设 $w_i>0$，且 $w_i,f_i$ 连续可微。令 $p=w_1/(w_1+w_2)$、$r=\log(w_1/w_2)$。直接求导得 $p'=p(1-p)r'$，以及

$$
G'=pf_1'+(1-p)f_2'+p(1-p)(f_1-f_2)r'.
$$

If throughout the interval $f_i'\le-a<0$, $|f_1-f_2|\le F$ and $|r'|\le L$, with constants $F,L\ge0$, then $0<p(1-p)\le1/4$ yields
若整个区间上 $f_i'\le-a<0$、$|f_1-f_2|\le F$、$|r'|\le L$，其中 $F,L\ge0$ 为常数，由 $0<p(1-p)\le1/4$ 得

$$
G'\le-a+\frac{FL}{4}.
$$

Consequently $FL<4a$ guarantees strict decrease, and $FL\le4a$ guarantees nonincrease. This is a sufficient criterion, not a necessary one. The coefficient $1/4$ is attained: take $f_{1,2}=-as\pm F/2$ and $(w_1,w_2)=(e^{Ls},1)$, with $F,L>0$. At $s=0$, $G'(0)=-a+FL/4$; if $FL>4a$, redistribution reverses the total slope locally even though both components decrease. No device mechanism is identified by this mathematical example.
因此 $FL<4a$ 保证严格递减，$FL\le4a$ 保证不增。这是充分判据，不是必要条件。系数 $1/4$ 可达到：取 $f_{1,2}=-as\pm F/2$、$(w_1,w_2)=(e^{Ls},1)$，其中 $F,L>0$。在 $s=0$，$G'(0)=-a+FL/4$；若 $FL>4a$，权重重分配使总量斜率在局部反向，尽管两个分量均递减。此数学示例没有识别任何装置机制。

This independent Python block checks the sharp family's derivative at zero by the quotient rule using exact rational arithmetic. The general criterion is proved above, not inferred from these two parameter choices.
以下独立 Python 代码用精确有理运算，通过商法则核对达到该界的函数族在零点的导数。一般判据由上文证明，不由这两组参数推出。

```python
from fractions import Fraction as Q

a, F = Q(1), Q(3)
for L, expected in ((Q(1), Q(-1, 4)), (Q(2), Q(1, 2))):
    # At s=0: w1=w2=1, w1'=L, w2'=0; f1=F/2, f2=-F/2.
    numerator = F / 2 - F / 2
    numerator_prime = L * F / 2 - 2 * a
    denominator, denominator_prime = Q(2), L
    derivative = (numerator_prime * denominator
                  - numerator * denominator_prime) / denominator**2
    assert derivative == -a + F * L / 4 == expected
    print(f"L={L}; G_prime_at_zero={derivative}")
```

Expected output / 预期输出：`L=1; G_prime_at_zero=-1/4`, `L=2; G_prime_at_zero=1/2`.

**Continuation invocation:** “Retain the established derivative identity and the family $f_{1,2}=-as\pm F/2$, $(w_1,w_2)=(e^{Ls},1)$. For $a,F,L>0$ and $FL>4a$, determine exactly where the total increases.” Reusing the identity gives $G=-as+(F/2)\tanh(Ls/2)$ and $G'=-a+(FL/4)\operatorname{sech}^2(Ls/2)$. Solving this explicit inequality gives the next result:
**续研调用：**“保留已建立的导数恒等式与函数族 $f_{1,2}=-as\pm F/2$、$(w_1,w_2)=(e^{Ls},1)$。在 $a,F,L>0$ 且 $FL>4a$ 时，精确确定总量递增的区间。”复用恒等式得 $G=-as+(F/2)\tanh(Ls/2)$、$G'=-a+(FL/4)\operatorname{sech}^2(Ls/2)$。解此显式不等式即可得到下一成果：

$$
G'(s)>0\quad\Longleftrightarrow\quad
|s|<\frac{2}{L}\operatorname{arcosh}\sqrt{\frac{FL}{4a}}.
$$

The continuation record can retain the derivative identity, the added family assumptions and this exact interval; the earlier sufficient bound remains valid. No complete re-audit or new physical inference is needed for this step.
续研记录可保留导数恒等式、新增函数族假设及此精确区间；原充分界仍然有效。此步骤无需完整重审，也未增加物理推断。

[Research workflows / 科研工作流](../research-workflows.md) — Mathematical Development and Research Continuation / 数学研究推进与研究续接
