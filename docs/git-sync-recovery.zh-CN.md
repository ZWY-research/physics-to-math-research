# Git 版本管理恢复与科研应用登记同步记录

日期：2026-10-08。状态：应用文档 commit 已完成；本轮复查仍被 GitHub CLI 登录环境缺失阻塞。本记录已准备为独立文档提交，尚未同步到 GitHub。

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
