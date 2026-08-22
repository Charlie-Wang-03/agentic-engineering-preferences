# 实践指南

[English](practices.md)

Practices 是本方法论中变化较快的实现层，用于把相对稳定的原则与决策规则落实为具体仓库行为。

与核心原则不同，实践可以随着工具、Agent 能力、托管平台和软件工程惯例的发展而调整。

## 1. 为 Agent 提供清晰的仓库上下文

应提供明确的仓库级 Agent 指令。

优先：

- 简洁的 `AGENTS.md` 或等价仓库指令文件；
- 明确的验证命令；
- 清晰的目录职责；
- 明确的完成标准；
- 对高风险或破坏性操作进行说明；
- 尽量减少依赖未写明的本地知识。

Agent 指令应强调目标和约束，但不要无必要地规定每个实现步骤。

## 2. 中英双语文档

主要规范性文档应把英文和简体中文都作为一等版本维护。

推荐配对命名，例如：

- `README.md` / `README.zh-CN.md`；
- `docs/principles.md` / `docs/principles.zh-CN.md`。

应保持语义一致，但不要求机械直译。两种语言都应符合各自自然的技术表达。

## 3. 可验证修改

优先选择拥有清晰验证路径的修改。

根据仓库性质，可以采用：

- tests；
- lint；
- type checking；
- deterministic scripts；
- schema validation；
- 文档结构检查；
- 可复现实例；
- CI checks。

不要为了“看起来工程化”而引入维护成本高于实际风险的验证体系。

## 4. 可审查、可逆的工作方式

修改规模应保持在能够理解和恢复的范围内。

优先：

- 小而清晰，或逻辑完整的 commit；
- 非简单修改使用 feature branch；
- 使用 PR 承载需要审查的变更；
- 高风险 migration 明确 rollback path；
- 破坏性操作采用 backup 或 dry-run。

对于 Agent 生成的大规模重写，应采用比局部修改更强的审查和验证。

## 5. 依赖纪律

新增依赖前，应明确：

- 它解决什么问题；
- 为什么现有能力不足；
- 安装和维护成本；
- 安全与供应链风险；
- 替换成本；
- 对可移植性的影响。

只要依赖本身合理，优先复用成熟基础设施，而不是为了减少依赖数量进行脆弱的重复实现。

## 6. 隐私与仓库卫生

私有材料与公开材料应有意识地分离。

至少做到：

- 不提交 credentials 或 secrets；
- 避免机器专属的私人路径；
- 不把未公开或私有项目数据混入公开产物；
- 必要时说明外部数据传输；
- Agent 与自动化只获得完成任务所需的最低必要权限；
- 私有仓库转公开前审查 Git history。

## 7. 渐进式用户体验

用户 onboarding 应分层设计。

新用户应当能够快速回答：

1. 这个项目是什么？
2. 适合谁？
3. 最快且安全的尝试方式是什么？
4. 有哪些重要假设和限制？
5. 高级配置或内部实现在哪里？

不要把高级架构知识强行塞进 quick start。

## 8. 决策记录

只有值得记录的决策才使用正式 decision record。

普通修改使用清晰的 PR 或 commit 说明通常已经足够。对于高影响偏离，应记录 default、conflict、trade-off、exception、evidence、rollback considerations 和 revisit condition。

仓库提供一个轻量 decision-record 模板用于此类场景。

## 9. 公开发布准备

首次公开发布或修改 repository visibility 前，应检查：

- license 与 attribution；
- README 与 onboarding；
- 中英文一致性；
- secrets 与私有数据；
- repository history；
- dependencies；
- validation status；
- contribution 与行为规范；
- release scope 与已知限制。

公开发布是工程决策，而不只是修改一个 GitHub repository setting。

## 10. 实践如何演化

真实项目经验或工具变化足以提供依据时，应更新实践层。

不得把某个具体工具的短期使用方式直接提升为稳定原则，除非它背后代表了与该工具无关、长期存在的工程问题。
