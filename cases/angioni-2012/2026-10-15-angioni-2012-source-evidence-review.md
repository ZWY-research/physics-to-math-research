# Angioni (2012) — Source Evidence 科研评议与 Skill 优化决策

- 日期：2026-10-15
- 评议对象：`experiments/angioni-2012/source-evidence.md`（阶段 A）
- 论文：Angioni et al., *Off-diagonal particle and toroidal momentum transport: a survey of experimental, theoretical and modelling aspects*, Nuclear Fusion **52**, 114003 (2012), DOI: 10.1088/0029-5515/52/11/114003
- 状态：**阶段 A 内容审查 ACCEPT WITH LIMITATIONS；Skill 科研能力 NOT TESTED；不修改 Core/OAC**

## 1. 评议范围及证据状态

此评议只审查 Codex 生成的 `source-evidence.md` 的论证结构、提取结果内部一致性以及所提出问题的数学可解性；**未直接重新读取原始 PDF 页面**，因此不重新认证原文公式与页码。原记录称 18 个 PDF 页面、已视觉核对五项数学关系；热速度、剪切归一化及部分系数定义未完全闭合。阶段 A 被明确要求不得进行完整数学推导，故未产出证明不属于失败。

## 2. 正面评价

1. E1–E5 将实验、理论、模拟、转述文献和作者解释分层，避免把综述中的引用结果误标为作者新实验（原记录 §3）。
2. M1–M5 保留了原文形式和适用条件，特别区分总粒子通量、显式粒子通量对动量的对流贡献、动量 pinch 与 residual stress（原记录 §4）。
3. C1 的问题可被压缩为一个有限维线性逆问题，具有可证明的可识别条件和遗漏项偏差表达式；比泛泛地讨论“理解机制”更可检验（原记录 §5）。
4. 主动记录公式约定和物理证据的未闭合之处，是合理的不确定性表述；但是否正确视觉核对需要直接检查 PDF 才能确认。

## 3. 必须保留的科学边界

- 零旋转及零旋转梯度时，若**独立重构出非零动量通量**，式 (2) 才能在相应模型条件下将其归于 residual stress；单独观测零旋转不充分。还需核查力矩源、边界通量及平衡/瞬态守恒。
- 式 (10) 存在显式的净粒子通量对流项，且某些剪切相关系数包含混合贡献。不得把式 (10) 不经重新定义，直接等同于三参数的“粘性 + pinch + residual stress”。
- 识别输运**贡献/有效系数**不等于唯一识别微观湍流机制；不同闭合模型可给出相同有效参数。
- 文献所述理论—实验 pinch 差距，不能直接归因于遗漏 residual stress；现有审查不判断文献新颖性。

## 4. 最小数学结果（由本次 ChatGPT 评议推导，非阶段 A Codex 成果）

在固定半径、明确归一化，并采用简化的动量输运模型时，设第 j 次观测

\[
y_j=\frac{\Pi_{\phi,j}}{n_jmR_j},\qquad
x_j=-R_j\,\partial_r\Omega_{\phi,j},\qquad
z_j=R_j\Omega_{\phi,j}.
\]

由报告提取的式 (2) 形式给出

\[
y_j=\chi_\phi x_j+V_\phi z_j+c_j,\qquad
c_j=\frac{\Pi_{\mathrm{RS},j}}{n_jmR_j}.
\]

**命题 1（条件性可识别性）。** 如果在 N 个观测之间 \(\chi_\phi,V_\phi,c\) 为共享的三个未知常量，观测及归一化准确，且 \(c_j=c\)，则无噪声数据唯一确定三个未知量，当且仅当

\[
\operatorname{rank}(A)=3,\qquad
A=[\,\mathbf x\ \mathbf z\ \mathbf 1\,].
\]

证明：\(A\theta=y\) 对 \(\theta\in\mathbb R^3\) 的解唯一，当且仅当 \(\ker A=\{0\}\)，即列满秩。若存在解且秩不足，任何非零核向量均生成不同的相容系数组。

**命题 2（遗漏项偏差）。** 设真实观测满足 \(\mathbf y=X\boldsymbol\beta+\mathbf c\)，\(X=[\mathbf x\ \mathbf z]\)，\(X^\top X\) 可逆。若使用无截距两项模型最小二乘拟合，则

\[
\widehat{\boldsymbol\beta}-\boldsymbol\beta
=(X^\top X)^{-1}X^\top\mathbf c.
\]

证明：代入 \(\widehat\beta=(X^\top X)^{-1}X^\top y\)。

故遗漏 residual stress **不必然**导致非零参数偏差：当 \(X^\top\mathbf c=0\) 时偏差为零。若 \(c_j\) 在不同背景任意变化，前述常量截距/列满秩结论不再保证可识别。存在测量误差时，条件数及误差传播也必须检查。上述结论属于一般线性代数，**不得宣称构成新的等离子体物理机制或文献首创**。

## 5. 对 Skill 的分层判定

| 候选修改或行为 | 分类 | 决策 |
| --- | --- | --- |
| 要求关键物理/数学陈述可定位到原文，且区别综述转述和作者自己的结论 | Supporting Guidance | **接受方法**；现有 OAC 可承载，暂不新增核心规则 |
| 关键数学式在解析后核对上下标、负号、归一化与适用条件 | Supporting Guidance | **接受方法**；适用于 PDF 研究，不适合加入通用 Core |
| 忽略残余项的反演不应自动宣称偏差方向；检查可识别性及竞争模型 | Regression Requirement | **保留为候选**；待实际 Skill 推导暴露失败再决定是否新增测试 |
| 为所有任务强制安装 PDF 工具或建立长期状态管理系统 | Core Rule 候选 | **拒绝**，超出通用 Skill 最小范围 |
| 把 tokamak、residual stress、特定三项输运方程写进通用 SKILL.md | Project-specific | **拒绝** |

**核心判断：本次尚无证据支持修改四条 Core Rules 或六项 OAC；也没有运行 Skill ON，不得从 PDF 阶段 A 结果推断 Skill 的增益或缺陷。**

## 6. 下一步与可证伪成功标准

下一轮在独立科研任务中调用冻结 Skill v0.2.7，输入经审查的原文证据但**不提供本评议的两个命题、证明及预期答案**，让模型自己完成一个最小数学研究节点：

- 明确观测量、共享参数与 residual stress 随实验变化的假设；
- 提出并检验可识别条件，给出秩不足反例或等价分析；
- 推导忽略 residual stress 的条件性偏差，说明何时偏差为零；
- 说明能由观测推断的是有效输运参数，还是更强的物理机制；
- 明确缺失的实验约束及最小可区分测量。

将实际回答与独立数学审查比较。若模型只复述论文而没有任何有效推导，则记录为实际科研产出不足；若产生错误秩条件、无条件偏差断言或物理因果升级，则记录具体反例并评估是否形成跨学科 Regression。**不得根据单次结果直接改写 Core。**

## 7. 当前状态

- **已冻结：** Core/OAC 与 Skill v0.2.7 基线。
- **待审：** Skill ON 真实数学研究结果及是否需要回归测试。
- **下一逻辑节点：** 用 C1 开展一次真正的数学构造和求解，不重复 PDF 环境检查。
- **发布：** 本报告为实验性评议草案，尚未写入 Canonical 仓库、提交或发布，因此不升级版本。
