# Discussion category setup / Discussion 分类设置

Discussions is enabled. The authenticated GitHub GraphQL API has no category-management mutation. GitHub initially creates six default categories; the Research Problem form currently uses General so submissions can start immediately.

Discussions 已开启。当前认证 GitHub GraphQL API 没有分类管理 mutation。GitHub 初始创建六个默认分类；科学问题表单暂时使用 General，使参与者可立即提交。

## Remaining UI steps / 剩余网页步骤

1. Open [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions), click the edit icon beside **Categories**, and edit **General**, **Ideas**, and **Show and tell** using the names and descriptions below. Choose **Open-ended discussion** for all three, and save each change.

   打开 [Discussions](https://github.com/ZWY-research/physics-to-math-research/discussions)，点击 **Categories** 旁的编辑图标，将 **General**、**Ideas**、**Show and tell** 按下表编辑，三者均选择 **Open-ended discussion**，分别保存。

| Existing category / 原分类 | New name / 新名称 | Description / 描述 |
| --- | --- | --- |
| General | Research Problems | Real scientific questions, observations, claims, evidence, and formulations. / 真实科学问题、观测、claim、证据与数学表述。 |
| Ideas | Ideas & Methodology | Methodology, Skill behavior, alternative formulations, and possible improvements. / 方法、Skill 行为、竞争性 formulation 与改进思路。 |
| Show and tell | Showcase & Results | Useful applications, resolved cases, Skill experiments, and downstream results. / 有效应用、已解决案例、Skill 实验与后续结果。 |

The category names above use English for concise navigation; the descriptions and all entry links are bilingual.

上述分类名使用英文以便简洁导航；描述和所有入口链接均为双语。

2. Read the actual Research Problems category URL after saving. Rename **.github/DISCUSSION_TEMPLATE/general.yml** to match that URL's category slug, followed by **.yml**. Update the Research Problem links in both READMEs, both contribution guides, the Casebook, and the welcome draft to use the actual slug. Commit and push these adjustments. Do not guess the slug or assume renaming preserves it.

   保存后查看 Research Problems 分类的实际 URL。将 **.github/DISCUSSION_TEMPLATE/general.yml** 改名为该 URL 的实际分类 slug 加 **.yml**。同步两份 README、两份贡献指南、Casebook 和 Welcome 草稿中的科学问题链接，提交并推送。不要猜测 slug，也不要假设分类改名后 slug 保持不变。

3. After confirming no community content would be lost, remove unused **Announcements**, **Polls**, and **Q&A** through the category editor, selecting an appropriate destination if GitHub asks where to move discussions. Keep only the three requested categories. Inspect the Research Problems submission page and confirm the eight fields appear.

   确认不会丢失社区内容后，在分类编辑页删除未使用的 **Announcements**、**Polls** 和 **Q&A**；如 GitHub 要求选择讨论迁移目标，选择适当目标。仅保留三个目标分类。检查科学问题提交页是否显示八个字段。

The [welcome draft](WELCOME_DISCUSSION.md) can be posted verbatim after updating its category link. It is a draft, not a claim that a welcome thread already exists.

更新分类链接后，[Welcome 草稿](WELCOME_DISCUSSION.md) 可原样发布；它是草稿，并不表示已发布 Welcome 帖。

Official references / 官方参考：[category management](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions), [form syntax](https://docs.github.com/en/discussions/managing-discussions-for-your-community/syntax-for-discussion-category-forms).
