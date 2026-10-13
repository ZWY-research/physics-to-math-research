# Research Method Sources / 研究参考与方法来源

查阅日期：2026-10-13。此记录仅登记公开资料研究与可能的组织价值，不增加 SKILL.md 规则，不证明方法已有效吸收。三项均为 **Reviewed / 已查阅**，具体方法的迁移为 **Under evaluation / 待评估**；没有 **Adopted / 已采用** 项。**Rejected / 不采用**仅表示明确否定的具体方案，目前无该项裁决。

README 的简要声明与本页一致：公开研究来源不构成合作、赞助、技术支持或认可关系。不用 Stars、知名度、形式化数量或形式证明来替代数学语义与物理适用性审查。


## OpenAI Math

- 官方仓库：[openai/math](https://github.com/openai/math)。
- 查阅 commit：`1581d4cbdd69a0faf34b2089614fe2a814316a6a`；查阅日期：2026-10-13。
- 正式许可证：**Apache-2.0**，已读取该 commit 的 LICENSE；归属保留为官方项目及其贡献者（Physlib 的社区引用信息见 README）。这是来源事实，本轮不复制其源码或大段原创文档，也不重新许可第三方材料。
- 资料状态：**Reviewed / 已查阅**。
- 方法采用状态：**Under evaluation / 待评估；Not adopted / 未采用**。

### 实际查阅范围

README（成果 family/学科分类、手稿与证明产物入口、形式化覆盖和不确定性、简化推理摘要与证明材料的区别）；history.md（修订/撤稿与保留旧版）；lean/README.md 和 ComparatorChallenges/README.md（验证配置及支持结果不等于主要定理）；CONTENTS.md 的目录头和开头示例（仅浏览组织结构，未逐篇审定）。

固定版本来源：

- [README.md](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/README.md)
- [LICENSE](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/LICENSE)
- [history.md](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/history.md)
- [lean/README.md](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/README.md)
- [CONTENTS.md](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/CONTENTS.md)
- [lean/ComparatorChallenges/README.md](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/ComparatorChallenges/README.md)

### 候选价值及 Core/OAC 关系

family 分类、产物映射、证明状态和修订追踪可帮助本项目维护可追溯档案。正式证明状态与数学/物理适用性不能混同。 与现有 Core 2 的依据、Core 4 的关键依赖及 OAC 的身份/语义/状态审计在概念上有可比较处；这是本项目的候选解释，不表示这些规则来源于该项目，也不构成新规则或已经验证的采用关系。

### 未完成事项与不可直接迁移内容

未独立复现任何选定定理；未逐篇核查其手稿或完整推理摘要，不将简化摘要当作完整证明。 形式化工程工具、证明自动化策略、庞大依赖、治理规则及公开推理材料不能不经适用性论证直接迁移为 Skill 的执行要求。没有执行新行为测试或科研增量比较。

### 未来验证要求

如未来申请采用，先由独立数学审查确定具体可迁移目标，固定一个适合本任务的证明或组织机制，区分形式命题与科学语义，再预注册相应 Regression/对照及成功标准。未经该审查与授权，不安装工具、不改 Skill、不宣称能力增强。


## Mathlib4

- 官方仓库：[leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4)。
- 查阅 commit：`105b9b1ce126e77b467aac6f6ba36b510ac57368`；查阅日期：2026-10-13。
- 正式许可证：**Apache-2.0**，已读取该 commit 的 LICENSE；归属保留为官方项目及其贡献者（Physlib 的社区引用信息见 README）。这是来源事实，本轮不复制其源码或大段原创文档，也不重新许可第三方材料。
- 资料状态：**Reviewed / 已查阅**。
- 方法采用状态：**Under evaluation / 待评估；Not adopted / 未采用**。

### 实际查阅范围

README 的数学与程序基础设施、源文件生成文档、模块构建和贡献约定入口；根目录 Mathlib/Counterexamples/Archive 等结构清单；正式 LICENSE。未运行源码、下载库或完整查阅链接中的所有指南。

固定版本来源：

- [README.md](https://github.com/leanprover-community/mathlib4/blob/105b9b1ce126e77b467aac6f6ba36b510ac57368/README.md)
- [LICENSE](https://github.com/leanprover-community/mathlib4/blob/105b9b1ce126e77b467aac6f6ba36b510ac57368/LICENSE)

### 候选价值及 Core/OAC 关系

可复用定义与引理、明确模块依赖和从源码生成文档的安排，可作为科研产物组织的候选参考。机器检查的是声明的形式命题，不能直接保证与科研语义的对应。 与现有 Core 2 的依据、Core 4 的关键依赖及 OAC 的身份/语义/状态审计在概念上有可比较处；这是本项目的候选解释，不表示这些规则来源于该项目，也不构成新规则或已经验证的采用关系。

### 未完成事项与不可直接迁移内容

未安装 Lean/Mathlib，未编译任何证明，未建立 Skill 与 Lean 的集成；尚无一般科研表现增量证据。 形式化工程工具、证明自动化策略、庞大依赖、治理规则及公开推理材料不能不经适用性论证直接迁移为 Skill 的执行要求。没有执行新行为测试或科研增量比较。

### 未来验证要求

如未来申请采用，先由独立数学审查确定具体可迁移目标，固定一个适合本任务的证明或组织机制，区分形式命题与科学语义，再预注册相应 Regression/对照及成功标准。未经该审查与授权，不安装工具、不改 Skill、不宣称能力增强。


## Physlib

- 官方仓库：[leanprover-community/physlib](https://github.com/leanprover-community/physlib)。
- 查阅 commit：`89d99e898104b7ffd93df322e0ab1ea999645116`；查阅日期：2026-10-13。
- 正式许可证：**Apache-2.0**，已读取该 commit 的 LICENSE；归属保留为官方项目及其贡献者（Physlib 的社区引用信息见 README）。这是来源事实，本轮不复制其源码或大段原创文档，也不重新许可第三方材料。
- 资料状态：**Reviewed / 已查阅**。
- 方法采用状态：**Under evaluation / 待评估；Not adopted / 未采用**。

### 实际查阅范围

README 的物理结果数字化、物理导向定义/模块文档、Physlib 与 PhyslibAlpha 审查区别；docs/ReviewGuidelines.md 的定义/引理质量、Mathlib 复用、模块范围、文档和审查组织；正式 LICENSE。

固定版本来源：

- [README.md](https://github.com/leanprover-community/physlib/blob/89d99e898104b7ffd93df322e0ab1ea999645116/README.md)
- [LICENSE](https://github.com/leanprover-community/physlib/blob/89d99e898104b7ffd93df322e0ab1ea999645116/LICENSE)
- [docs/ReviewGuidelines.md](https://github.com/leanprover-community/physlib/blob/89d99e898104b7ffd93df322e0ab1ea999645116/docs/ReviewGuidelines.md)

### 候选价值及 Core/OAC 关系

物理语义文档与分层审查状态，可帮助区分本项目的正式审查与实验记录。Lean 形式证明和经验适用性审查各有责任，不能互相替代。 与现有 Core 2 的依据、Core 4 的关键依赖及 OAC 的身份/语义/状态审计在概念上有可比较处；这是本项目的候选解释，不表示这些规则来源于该项目，也不构成新规则或已经验证的采用关系。

### 未完成事项与不可直接迁移内容

未复制治理模型，未编译证明，也未检验其流程是否提高本 Skill 的科研行为。 形式化工程工具、证明自动化策略、庞大依赖、治理规则及公开推理材料不能不经适用性论证直接迁移为 Skill 的执行要求。没有执行新行为测试或科研增量比较。

### 未来验证要求

如未来申请采用，先由独立数学审查确定具体可迁移目标，固定一个适合本任务的证明或组织机制，区分形式命题与科学语义，再预注册相应 Regression/对照及成功标准。未经该审查与授权，不安装工具、不改 Skill、不宣称能力增强。


## 网站构建依赖与许可（与科研方法来源分开）

静态全文生成使用 markdown-it **14.1.0**（MIT）处理 Markdown，使用 KaTeX **0.16.22**（MIT）在构建时输出 HTML/MathML。两者为工程依赖，**不是数学研究方法集成**。标准库没有可可靠保留表格、嵌套列表、代码和复杂 LaTeX 的完整渲染器，故采用这两个小型、固定版本库；没有大型网站框架。

[markdown-it 官方源码](https://github.com/markdown-it/markdown-it/tree/14.1.0)与[KaTeX 官方源码](https://github.com/KaTeX/KaTeX/tree/v0.16.22)。package-lock.json 固定传递依赖与 integrity。KaTeX 数学标记、CSS 和字体由本站提供，保留 Khan Academy 及贡献者 MIT 授权；markdown-it 的 MIT 授权亦保留于站内 third-party notices。本站不用第三方 CDN、正文运行时 fetch 或 GitHub iframe；没有复制三个数学项目的源码，也没有重新发布第三方论文全文。
