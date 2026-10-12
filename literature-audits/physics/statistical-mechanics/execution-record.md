# Execution Record / 工程执行记录

Status: DRAFT — Pending independent mathematical review
Date: 2026-10-12 (Asia/Shanghai)

## 基准与限定范围

- 基准 Git commit：`c48f20dfc23a23c2df683d124c073a5a2ae32458`（本轮 fetch 的最新 origin/main）。
- 草稿分支：`review/jarzynski-1997-draft`，独立 worktree；未推送、不创建 PR／Release／Tag。
- Skill 版本：`0.2.1`；SKILL.md SHA-256：`ab6cb6cf6a42678ab2f25332d94608b73f96bb526372b73495bf6aaa8cbc7f8f`，运行文件、Core/OAC、物理适配层及全部原有文件未修改。
- 论文：C. Jarzynski, *Nonequilibrium Equality for Free Energy Differences*, Physical Review Letters 78(14), 2690–2693 (1997)。[DOI](https://doi.org/10.1103/PhysRevLett.78.2690)；[APS 元数据页面](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.78.2690)。
- 仅创建本目录指定四个 UTF-8 文件。README、CHANGELOG、项目版本和正式论文登记保持原样。原工作区 1655 个既有文件及 Git status 已核对未变；基准 36 个跟踪文件逐字节保留。

## 原文定位与来源核验

实际使用 [UCI 提供的 PRL 期刊版副本](https://www.physics.uci.edu/~tritz/BP/Jarz97.pdf)，HTTP 200，141186 字节，四页，页码 2690–2693；下载字节 SHA-256：`7089061ac79e650536aae6cd15b437a4f9d6669a66cd99b4149b69abb2003b1c`。APS 页面确认题名、作者、年份、卷期、起始页与 DOI；页尾确认结束页。期刊版与出版社原站 PDF 的逐字节等价未另行认证，镜像身份与排版已核对，未绕过登录。

| PRL 原文定位 | 实际核查范围 |
| --- | --- |
| p.2690 Eq. (2a)、(2b) | 指数功期望与自由能差，不是普通平均功 |
| p.2690 Eq. (3) | 参数驱动功的轨道积分定义 |
| p.2691 Eq. (6)–(8) | 累积功、Liouville 密度保持及孤立系统配分函数比证明 |
| p.2691 Eq. (9)、(10)，文字延续至 p.2692 | 复合系统 Y1/Y0 与子系统自由能解释的区别；原文弱耦合条件 |
| p.2692 指定讨论段 | 稀有低功事件影响指数平均估计，仅核查原文定位，未建立收敛理论 |

[arXiv 预印本](https://arxiv.org/abs/cond-mat/9610209)只核对身份；不使用其公式编号替代 PRL 编号。不展开新文献检索。

采用已有 Poppler 对期刊版第 1、2 页渲染并进行视觉核对，结合全文提取文本核对 p.2692 的相关说明。渲染器报告缺少 Symbol／ArialUnicode 显示字体，但已生成可读页面；核心公式与编号可辨，未据渲染警告改变原文。论文 PDF 和页面图仅作仓库外临时核验，不在此草稿或提交中附入论文全文／图片。

## 唯一一次 Python 执行

- Python 版本：`3.14.7`；实际解释器：`D:\Dev\Miniconda3\python.exe`。
- 脚本：`two-state-check.py`；SHA-256：`31b0b646e0593be0b56b92afcb384d37c7e1c039afe1a0d9a5c4de3b9700e489`。
- 执行 argv（无 shell 拼接）：`["D:\\Dev\\Miniconda3\\python.exe", "-X", "utf8", "D:\\OneDrive\\Multi_Skills\\physics-to-math-research\\revisions\\jarzynski-1997-review\\worktree\\revisions\\literature-audit-drafts\\jarzynski-1997\\two-state-check.py"]`。
- 工作目录：`D:\OneDrive\Multi_Skills\physics-to-math-research\revisions\jarzynski-1997-review\worktree\revisions\literature-audit-drafts\jarzynski-1997`。
- 开始：`2026-10-12T17:41:41.646059+08:00`；结束：`2026-10-12T17:41:41.737835+08:00`。
- 执行次数：**1**；返回码：**0**；状态：**PASS**。
- 输出：`two-state-check-output.txt`；SHA-256：`bb4ba12671051f4589db17f410df7a7b44b8255e03ef51e31449813109b4194b`。stdout／stderr 区块为实际捕获字节；区块外标头记录命令、时间和状态，不是模拟输出。
- stdout／stderr 长度：516／61 字节。stderr 实际含解释器启动诊断 `Failed to find real location of D:\Dev\Miniconda3\python.exe`，已原样保留；进程返回码仍为 0，全部见证断言实际完成。
- 只使用标准库 fractions、math、sys、traceback；固定参数 beta=1、epsilon=ln4，Fraction 精确值与浮点 rel_tol=abs_tol=1e-12。有限样本见证采用 N=1 的固定零功值，无随机抽样、网络、依赖安装或物理模拟。

实际断言包括 Z0=2、Z1=5/4、比值与正则指数平均=5/8、非正则指数平均=1且不同于5/8、自由能差=ln(8/5)>0、零功样本估计=0<自由能差及平均功=epsilon/2不小于自由能差。详细数值以原始输出为准。

## 证明与计算的范围区别

审查草稿在明确正则初态、能量差功、同域保体积双射及有限配分函数条件下复现孤立系统的积分证明，并重述为有限的一般测度空间命题。这是可供审查的手工数学推导，不是通过有限数值抽样证明一般定理。Python **PASS** 只反映指定两态见证的断言状态，不认证任意 Hamiltonian 流、热库物理或整篇论文。

一般化保留正则指数权重、能量差、保测度换元与规范化积分结构，未保留温度、测量功、热库和相互作用的物理实现；不声称原创定理或适配任意实际动力学。

未审查：Nosé–Hoover 完整推导、Metropolis／其他更新机制、全部累积量结果、实际实验、大规模数值验证及后续广泛推广。热库条件的实际满足性、有限耦合误差及镜像与出版社 PDF 的字节等价仍未独立认证。

没有 ON/OFF 模型输出、研究子代理或额外模型调用；候选 regression 不表示已发现 Skill failure 或 capability gain。未修改原有测试、数学判据或规范。

## 下一阶段独立核查文件索引

1. [audit-draft.zh-CN.md](audit-draft.zh-CN.md)：十节中文草稿、126 词英文 Abstract、公式定位与明确的 DRAFT 状态。
2. [two-state-check.py](two-state-check.py)：固定参数离散见证，标准库断言。
3. [two-state-check-output.txt](two-state-check-output.txt)：一次真实执行的 stdout／stderr、返回码及状态。
4. [execution-record.md](execution-record.md)：本记录、来源与环境、范围及未决事项。

## Next action / 唯一下一步

等待科研负责人的独立数学验收；不自动正式归档、登记论文、推送、升级版本或启动 Skill 测试。

Review status: Pending independent mathematical review
