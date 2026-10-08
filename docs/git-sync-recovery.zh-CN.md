# Git 版本管理恢复与科研应用登记同步记录

日期：2026-10-08。当前状态：GitHub 认证与普通推送成功，原 OneDrive 路径已恢复 Git 管理。下文保留前期阻塞记录；最终恢复结果见末节。

## 背景与目标

将已完成的科研应用登记机制纳入 canonical 历史，再有备份地恢复 OneDrive 原路径 Git 管理能力。不修改 Skill/Core/OAC、历史 regression 或 benchmark，不启动 HL-3 测试。

## 本地与远程 Git 状态

- canonical：[ZWY-research/physics-to-math-research](https://github.com/ZWY-research/physics-to-math-research)，默认分支 `main`。
- 本轮实际查询的远程 HEAD：`dfac626b0e027387084473764f69604edb562787`，与上轮基线一致。
- 原 OneDrive 目录仍无 `.git`；不能将其当作远程 HEAD 的完整 checkout。
- 上轮临时 clone 仍存在，分支 `main`，待推送 commit 为 `29a8b99adef1a889e1d4529fdd5f9b81ea53130b`。提交前工作区干净，该 commit 是远程 HEAD 的正常后继。
- 原路径的 `docs/canonical-registry-recovery.bundle` 保存完整历史；本轮复查确认其 main 指向应用文档 commit。工程记录提交后刷新 bundle，以保存两个待推送 commit。

## 为什么选择当前方案

在独立 clone 上核验并迁移新增段落，保留 canonical 现有社区入口与原始换行格式。先确认推送成功，再逐文件备份与比较原目录；不直接覆盖整个目录，不使用 force push 或 reset --hard。

## 文件差异与合并情况

应用文档 commit 仅含 [RESEARCH_APPLICATIONS.md](../RESEARCH_APPLICATIONS.md)、[上一轮实施记录](research-applications-implementation.zh-CN.md)、两份 README 和两份 CONTRIBUTING。总计 145 行新增、无删除。远程已有的 Discussions、Casebook、贡献认可说明和 canonical 链接保留；本轮没有重新生成应用登记内容。

私有 `PROJECT_STATE.md`、`CLAUDE.md`、历史评测与 revisions、恢复 bundle 不进入公开提交。原目录的私有 AGENTS 与公开版本不同，恢复时应先保存原件，再同步公开文件。工程记录原稿也已备份；公开版本去除机器专用绝对路径，不包含凭据。

## 实际执行的 Git 操作

1. 上轮 clone canonical，核对远程 HEAD/tags 和冻结文件，按六文件 allowlist 合并并创建应用文档 commit。
2. 用户已明确授权沿用仓库级身份 `physics-to-math-research release <release@localhost>`，全局 Git 身份不变。
3. 上轮普通 push 等待凭据助手登录，被中止；远程 HEAD 未变。
4. 本轮检查 PATH、常见安装位置、用户目录与 D 盘（包含忽略文件），未找到 `gh.exe`；常见 gh 配置位置不存在，Git Credential Manager 账号列表为空。未读取或输出 token。
5. 本轮查询 `ls-remote`、检查临时 clone、bundle 和冻结原始字节；没有必要整合远程新增提交。
6. 因不能核验用户所述登录环境及写权限，未重试 push；已请求 gh.exe 路径及登录所在环境。依照用户要求停止认证相关操作。
7. 将本记录纳入单文件文档提交，使用既有授权身份；刷新本地完整历史 bundle，避免记录修改仅停留在临时文件中。

## 检查结果

- 上轮六文件 staged allowlist、差异及空白检查通过；65 个本地链接/锚点、UTF-8、双语入口一致性通过。
- 上轮 20 个公开文件及 commit blob 与审计哈希一致；本轮临时 clone 在记录更新前仍干净。
- 本轮原目录、clone commit、remote canonical 原始 `SKILL.md` SHA-256 一致：`aff41be7b14fedf078516087d11f36a80f41f565e6ca36a614187ef463ec6ce8`。两份 Core/OAC 解释文件也逐字节一致。
- 上轮原目录 145 个文件均已备份并核验；本轮没有同步覆盖原目录，历史评测与发布记录保持原样。
- 原 tag `v0.1-alpha.2` 指向 `4ee1b8761732f97d71c7c772243ad76bd3c7bbac`；本轮未修改 tag/release。
- 本地 Codex 配置已为 `gpt-6.1-sol` / `medium`，无需改写。配置文件不证明正在执行的聊天模型。

## Commit 与 GitHub 同步结果

应用文档 commit：`29a8b99adef1a889e1d4529fdd5f9b81ea53130b`，父 commit 为 `dfac626b0e027387084473764f69604edb562787`。

本记录的独立 commit 以应用文档 commit 为父提交，实际完整 hash 由 `git log -1 -- docs/git-sync-recovery.zh-CN.md` 查询并在交付报告列出；不把提交自身 hash 写入自身内容。

两个 commit 尚待同步。实际远程 HEAD 仍为上述基线；未确认 GitHub 已包含应用登记文件或 README 新入口。原目录仍未恢复正常 Git 管理，临时 clone 可正常管理 Git。

## 风险、限制与下一逻辑节点

当前环境没有可调用的已登录 gh，不能核验 GitHub 身份或写权限；这不代表远程拒绝权限。用户可能在其他 Windows 用户、WSL、远程终端或自定义路径登录，需要明确路径与环境。请勿在聊天中提供密码或 token。

下一步仅为定位已登录 CLI，核验身份及 canonical 写权限，再重新查询远程 HEAD；如有新增提交则安全整合并检查，随后普通推送两个 commit。推送成功后，备份、比较并恢复原路径 Git 元数据，使用 `.git/info/exclude` 防止私有资料误入提交。认证未解决前不改原目录的 canonical 文件，不启动科研测试。


## 最终恢复结果（2026-10-08）

### 执行环境与认证

安装后的 `gh.exe` 已在 Windows 标准安装位置存在，但 Codex 继承了安装前 PATH。仅刷新检查进程 PATH 后，`gh --version` 返回 2.102.0，`git --version` 返回 2.55.0.windows.3。当前为同一 Windows 用户环境，无 WSL 标记；无需搜索其他机器或重新生成仓库。

`gh auth status` 两次出现账号验证超时；随后已认证 API 请求成功确认账号 `ZWY-research`，canonical 默认分支为 main，具有 push/admin 权限。实际普通 push 也成功。后续文件 API 曾出现 TLS handshake timeout，因此使用 fetch 后的 Git 对象核验文件；不能把上述网络超时解释为身份失效。

Codex 用户配置仍为 GPT-6.1 Sol（`gpt-6.1-sol`）、Reasoning Effort Medium（`medium`），未改写持久配置。

### GitHub 同步及文件核验

重新 fetch 后，远程基线仍为 `dfac626b0e027387084473764f69604edb562787`，是已有提交的祖先，无须冲突整合。使用仓库级 GitHub CLI 凭据助手进行普通 fast-forward push，GitHub 接收以下既有提交：

- `29a8b99adef1a889e1d4529fdd5f9b81ea53130b`：科研应用登记机制。
- `a8597ec9ea0654a8bf0f53d9982435ad089ec079`：前期复查工程记录。

首次推送后的实际远程 HEAD 为 `a8597ec9ea0654a8bf0f53d9982435ad089ec079`；GitHub commit API 和 ls-remote 均确认该 HEAD。再次 fetch 后，全部 21 个公开文件的原始字节与该提交一致，登记表、两份 README 栏目和工程记录均已进入远程历史。

本节更新纳入单文件文档 commit，再按相同 fast-forward 要求同步；最终完整 HEAD 由 `git log -1 -- docs/git-sync-recovery.zh-CN.md` 查询并列于交付报告，避免把提交自身 hash 写入自身。

`SKILL.md` 本地与 canonical 原始字节一致，SHA-256 为 `aff41be7b14fedf078516087d11f36a80f41f565e6ca36a614187ef463ec6ce8`。Core/OAC、历史测试、benchmark、tag 和 release 未改。没有 force push 或 reset --hard。

### 原路径恢复与原文件保留

恢复前已逐文件保存全部原目录文件和 SHA-256 清单到独立临时备份。检查隐藏文件、路径和符号链接后，新增此前缺失的 `.git` 元数据及四个 canonical 文件（Discussion 模板、Welcome 草稿、community setup 和案例簿）。四份 README/贡献指南只同步已合并版本，原件在备份中保留；没有整目录覆盖或删除。

原私有 `AGENTS.md` 保持原字节，Git 明确显示 `M AGENTS.md`，不隐藏它，也不将其提交到公开仓库。其余公开文件与 canonical 一致。原科研文件、评测和 revisions 保持原样；`PROJECT_STATE.md`、`CLAUDE.md`、候选修订记录、历史评测/revisions 与恢复 bundle 通过本地 `.git/info/exclude` 排除，不进入公开提交。

原路径分支为 main，跟踪 origin/main。完成记录提交和推送后，没有未同步的登记文档或工程记录修改；唯一可见未提交文件为有意保留的私有 AGENTS。本地 bundle 刷新并核验，保存最新提交历史。恢复过程的备份位置在私有 PROJECT_STATE 中登记，不写入公开文档。

### 限制与下一逻辑节点

CLI 认证诊断及部分文件 API 存在网络超时，但身份、写权限、实际推送、远程 HEAD 和 Git 对象验证已经成功。私有 AGENTS 与 canonical 不同是保留原文件的明确结果，未来公开提交应继续使用显式路径，避免误提交它或私有资料。

本轮同步恢复任务到此停止。下一节点由维护者明确指定；不自动启动 HL-3 测试或修改科研理论。
