# Research onboarding and tools — documentation decision

Date: 2026-10-12 · Baseline origin/main: `d3d6daabe30aed324c87f68e8fb052834c3ee8e4`

## Reason / 修改原因

Make the physical-observation → general-mathematical-question entry concrete, lower the participation barrier, separate research archives, and make mathematical tool setup discoverable. This is an explicitly authorized documentation change, not a confirmed runtime-failure repair.

以具体示例说明物理观察到一般数学问题的转化，降低参与门槛，分开研究档案并提供按需工具入口。本轮是获授权的文档改进，不是已经确认的运行失败修复。

## Files and authority / 文件与权限边界

Updated both READMEs. Added evaluation-reports/README.md, its physics/plasma-and-fusion/README.md, literature-audits/README.md, docs/literature-audit-protocol.md, references/tools/index.md, references/tools/python-setup.md and this decision record. Original reports remain at their public paths.

修改两份 README；新增评估根索引与等离子体／聚变导航、论文审查档案入口与协议、工具导航与 Python 配置说明及本决策记录。原始报告保留公开路径。

Core/OAC and SKILL remain unchanged because the task changes onboarding and archival navigation, not runtime behavior. Runtime version stays 0.2-alpha.0; expected SHA-256: `6c3d4e16dd31d547083f752a316d7841d9abc55b4095669b3335dc4c25756ba0`. Physics Adapter and frozen tests are untouched. No Release or Tag.

本轮不改变运行行为，因此 Core/OAC、SKILL、物理适配层及冻结测试保持不变，运行版本仍为 0.2-alpha.0，不创建 Release／Tag。

Paper audits test specific mathematical claims; Skill evaluations test the agent's behavior under recorded conditions. Publication or successful paper review is not a treatment-gain result. Tool documents are optional on-demand references, not automatically loaded; Skill installation installs no mathematical software.

论文审查核查具体数学 claim，Skill 评估核查记录条件下的 Agent 行为，论文发表或审查成功不是增益对照结果。工具文档按需参考，不自动加载；安装 Skill 不安装数学软件。

## Verification / 验证

Checks completed before commit on 2026-10-12:

- Coordinator review found the six new README sections equivalent in English and Chinese; the Chinese entry reads continuously. Domains, profile class, formulas, nonnegativity bound, conclusion and demonstration limits agree.
- Exact rational arithmetic confirmed the zero-integral perturbation and the 2/3 nonnegativity bound; this checks the supplied teaching example, not Skill performance.
- All 126 relative links in the nine changed documents resolve. All 11 distinct HTTP links returned 200; the two existing GitHub new-post links redirect to login as expected. Official SymPy, SciPy, Pint, Lean and Python pages were read to check installation commands and paths.
- Both feedback links use 82787647@qq.com, with only the specified subject and no message body or send action.
- All historical README links and evidence prose were retained. The 27 preexisting tracked files outside the two READMEs, including runtime, adapter, tests and reports, remain byte-identical to baseline. No empty subdiscipline folder or paper-audit result was created.
- The original workspace's 1,512 existing files and Git status were checked unchanged. Diff is restricted to the nine documentation/navigation paths. Existing README CRLF endings are preserved; whitespace checks pass with CR-at-EOL recognized.
- SKILL SHA-256 is exactly `6c3d4e16dd31d547083f752a316d7841d9abc55b4095669b3335dc4c25756ba0`; version unchanged. No installations, model tests, paper audits or SkillHub operations were performed.

提交前完成中英对应、中文连贯性、示例公式、126 个相对链接与 11 个网络链接检查；邮箱仅预填指定主题。历史内容、运行文件、适配层、测试、报告及原工作区文件保持不变，变更仅涉及九个文档与导航文件，无空学科目录或虚构审查结果。

## Next logical step / 下一逻辑节点

Await voluntary real-use feedback or explicit authorization for a real, scoped paper audit. Do not automatically select a paper, create discipline records, change runtime rules or start capability tests.

等待自愿真实使用反馈或明确授权的具体论文审查，不自动选论文、创建学科记录、修改运行规则或启动能力测试。
