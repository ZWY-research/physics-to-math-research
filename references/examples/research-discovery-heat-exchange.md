# Example 1 — Heat exchange to a decay law / 示例一：从热交换到衰减规律

**Invocation:** “Use physics-to-math-research. Two bodies exchange heat while insulated from the outside; their temperature difference decreases. Discover a useful mathematical question and obtain a first conditional result.”
**调用：**“使用 physics-to-math-research。两个物体与外界隔热、彼此交换热量，温差逐渐缩小。提出一个有用的数学问题并取得首项条件性结果。”

**Question and exploratory premise:** What determines the relaxation time and common limiting temperature? Let constant heat capacities be $C_1,C_2>0$. Conservation motivates $C_1\dot T_1=-q$, $C_2\dot T_2=q$. To model heat transfer tending to zero with the temperature difference, explore the linear closure $q=k(T_1-T_2)$, $k>0$ constant. The qualitative observation alone does not establish this closure.
**问题与探索前提：**弛豫时间和共同极限温度由什么决定？设恒定热容 $C_1,C_2>0$。能量守恒支持 $C_1\dot T_1=-q$、$C_2\dot T_2=q$。为描述温差趋零时热流趋零，探索线性闭合 $q=k(T_1-T_2)$，其中 $k>0$ 恒定；定性观察本身并未确立该闭合。

**First result:** Adding the balances gives constant $C_1T_1+C_2T_2$. Subtracting the temperature equations gives $\dot\Delta=-\lambda\Delta$, where $\Delta=T_1-T_2$ and $\lambda=k(1/C_1+1/C_2)>0$. Thus
**首项成果：**相加得 $C_1T_1+C_2T_2$ 守恒；温度方程相减得 $\dot\Delta=-\lambda\Delta$，其中 $\Delta=T_1-T_2$、$\lambda=k(1/C_1+1/C_2)>0$。因此

$$
\Delta(t)=\Delta(0)e^{-\lambda t},\qquad
\overline T=\frac{C_1T_1(0)+C_2T_2(0)}{C_1+C_2},\qquad
T_1=\overline T+\frac{C_2\Delta(t)}{C_1+C_2},\quad
T_2=\overline T-\frac{C_1\Delta(t)}{C_1+C_2}.
$$

Both temperatures tend to $\overline T$, with relaxation time $1/\lambda$. These are consequences of the conditional model. The following standalone Python block checks the solution coefficients exactly for illustrative parameters $C_1=2,C_2=3,k=6/5,T_1(0)=4,T_2(0)=1$; these values are not measurements. Coefficients $b_1,b_2$ multiply $e^{-\lambda t}$, so checking them checks the differential equations for every $t$, rather than sampling a trajectory.
两温度以弛豫时间 $1/\lambda$ 趋于 $\overline T$。这些是条件模型的后果。以下独立 Python 代码用示意参数 $C_1=2,C_2=3,k=6/5,T_1(0)=4,T_2(0)=1$ 精确核对解的系数；参数不是测量值。$b_1,b_2$ 是 $e^{-\lambda t}$ 的系数，因此核对系数是在所有 $t$ 上核对微分方程，而非抽样轨迹。

```python
from fractions import Fraction as Q

C1, C2, k = Q(2), Q(3), Q(6, 5)
T10, T20 = Q(4), Q(1)
rate = k * (1 / C1 + 1 / C2)
mean = (C1 * T10 + C2 * T20) / (C1 + C2)
b1 = C2 * (T10 - T20) / (C1 + C2)
b2 = -C1 * (T10 - T20) / (C1 + C2)
assert (mean + b1, mean + b2) == (T10, T20)
assert C1 * b1 + C2 * b2 == 0
assert -C1 * rate * b1 == -k * (b1 - b2)
assert -C2 * rate * b2 == k * (b1 - b2)
print(f"decay_rate={rate}; limiting_temperature={mean}")
```

Expected output / 预期输出：`decay_rate=1; limiting_temperature=11/5`.

[Research workflows / 科研工作流](../research-workflows.md) — Research Discovery / 研究问题发现
