# Cooling: two levels of research delivery / 冷却问题：双层科研表达

Teaching example only: not a reviewed paper, physical-mechanism verification or Skill ON/OFF capability result. Both accounts use the same assumptions and evidence. No empirical data were checked; the derivation is analytic and uses no external calculation software.

仅为教学实例，不计入已审查论文，不验证物理机制，也不构成 Skill ON/OFF 能力结果。两版使用相同假设与证据；未检验经验数据，仅作解析推导，未调用外部计算软件。

## A. Research Explanation / 通俗解释版

Can a simple relation describe an object cooling towards its surroundings? Suppose the surroundings stay at a constant temperature, the object's internal temperature is approximately uniform, and its cooling rate is proportional to its temperature difference from the surroundings, with a constant positive coefficient. Within this conditional model, the temperature difference decreases exponentially: its initial value is multiplied by an exponential decay factor. If the initial temperature is higher than ambient, the object approaches ambient temperature from above.

能否用简单关系描述物体向环境温度冷却？假设环境温度恒定，物体内部温度近似均匀，并采用速率正比于温差、比例系数为正常数的模型。在这个条件性模型中，温差指数衰减：初始温差乘以指数衰减因子。初始温度高于环境时，物体从上方趋近环境温度。

This does not prove the actual cooling mechanism. Changing surroundings, internal temperature gradients or a non-proportional rate may invalidate the model. An empirical fit alone would not prove the mechanism; here no empirical data were checked. The result follows analytically without external calculation software. The technical account gives the same conditional result, not stronger evidence.

这不证明真实冷却机制。环境变化、内部温度梯度或非比例速率可能使模型失效；经验拟合本身也不能证明机制。本例未检验经验数据，通过解析方法得到结果，未调用外部计算软件。专业版提供同一条件性结果，不提高证据等级。

## B. Technical Research Account / 专业科研论证版

Let $t\ge0$, $T(t)$ be the approximately uniform object temperature and $T_{\mathrm{env}}$ the constant ambient temperature. Assume $T$ is differentiable, $k>0$ is constant with units of inverse time, $T(0)=T_0$, and the proportional-rate equation holds on the interval considered:

设 $t\ge0$，$T(t)$ 为近似均匀的物体温度，$T_{\mathrm{env}}$ 为恒定环境温度。假设 $T$ 可微，$k>0$ 为量纲是时间倒数的常数，$T(0)=T_0$，并在讨论区间内满足比例速率方程：

$$
\frac{dT}{dt}=-k(T-T_{\mathrm{env}}).
$$

Define $u(t)=T(t)-T_{\mathrm{env}}$. The equation gives $u'=-ku$; hence $(e^{kt}u)'=0$ and $e^{kt}u=T_0-T_{\mathrm{env}}$. This also covers zero initial temperature difference without division by $u$. Therefore:

令 $u(t)=T(t)-T_{\mathrm{env}}$。方程给出 $u'=-ku$，因而 $(e^{kt}u)'=0$，得到 $e^{kt}u=T_0-T_{\mathrm{env}}$。这里不除以 $u$，也覆盖初始温差为零的情形。因此：

$$
T(t)=T_{\mathrm{env}}+(T_0-T_{\mathrm{env}})\exp(-kt).
$$

For $T_0>T_{\mathrm{env}}$ this is monotone cooling towards ambient; for equality it is constant. The integrating-factor identity fixes the solution for each stated initial value. Substitution and the initial condition provide an analytic reproduction check; no numerical data, parameter fit or external computation was used.

当 $T_0>T_{\mathrm{env}}$ 时，温度单调下降并趋近环境温度；两者相等时保持恒定。积分因子恒等式确定每个给定初值的解。代入方程并检查初值即可解析复核；未使用数值数据、参数拟合或外部计算。

The equation is a model assumption, not an identified physical law for every object. Nonconstant ambient temperature, appreciable spatial gradients or a different rate law can invalidate this expression. Mathematical derivation is conditional; actual mechanism and empirical applicability remain unverified. No empirical data were checked and no external calculation software was called, exactly as in the accessible account.

方程是模型假设，不是已为所有物体识别的物理规律。环境温度不恒定、显著空间梯度或不同速率关系都可能使此表达式失效。数学推导是条件性的，真实机制与经验适用性尚未验证。未检验经验数据，未调用外部计算软件，与通俗版一致。

Receipt / 回执：This file supplies two explanations of one analytic conditional result; it is not an experimental execution record. / 本文件提供同一解析条件性结果的双层解释，不是实验执行记录。
