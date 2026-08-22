# 实践指南

[English](practices.md)

Practices 是本方法论中变化较快的实现层，用于把相对稳定的原则与决策规则落实为具体仓库行为。

与核心原则不同，实践可以随着工具、Agent 能力、托管平台和软件工程惯例的发展而调整。

## 1. 为 Agent 提供清晰的仓库上下文

应提供明确的仓库级 Agent 指令。

优先：

- 简洁的根目录 `AGENTS.md` 或等价仓库指令文件；
- 明确的验证命令；
- 清晰的目录职责与仓库不变量；
- 明确的完成标准；
- 对高风险或破坏性操作进行说明；
- 尽量减少依赖未写明的本地知识。

Agent 指令应强调目标、约束、不变量和验证路径，但不要无必要地规定每个实现步骤。

对于较大的仓库，如果某个子系统确实拥有不同命令、约束或不变量，可以增加 scoped / nested Agent instructions；不得因为存在这种机制就给每个目录机械添加指令文件。

## 2. 明确文档职责

不同文档应承担不同职责，不要把一个文件写成包办一切的万能说明书。

一种合理默认是：

- `README.md` — 项目发现、目标用户、边界与采用路径；
- `docs/principles*` — 相对稳定的工程原则；
- `docs/decision-framework*` — 冲突、trade-off 与例外处理；
- `docs/practices*` — 可以更快演化的落地实践；
- `docs/governance*` — 方法论自身如何修改；
- `AGENTS.md` — 当前仓库的 Agent 执行约束；
- `CONTRIBUTING.md` — 贡献流程与要求；
- `templates/` — 从方法论派生出的可复用产物。

避免在多个文件中重复维护同一套规范性文本，应通过链接指向 canonical document。

## 3. 语言与翻译

只有在确实改善可访问性时才维护双语文档，不要求仓库中的每个文件都存在中英两个版本。

对于本方法论仓库，默认维护中英配对的内容包括：

- README；
- 经常由人阅读的核心方法论文档；
- 翻译具有实际使用价值的用户向模板。

`AGENTS.md`、workflow 配置、贡献操作细节等操作型文件可以保持 English-first，除非翻译确实改善使用体验。

配对文档应保持语义一致，但不要求机械直译。

## 4. 可验证修改

优先选择拥有清晰验证路径的修改。

根据仓库性质，可以采用：

- tests；
- lint；
- type checking；
- deterministic scripts；
- schema validation；
- 文档结构或链接检查；
- 可复现实例；
- CI checks。

验证强度应与仓库规模和风险相称。不要引入维护成本高于实际风险的验证体系。

## 5. 可审查、可逆的工作方式

修改规模应保持在能够理解和恢复的范围内。

优先：

- 小而清晰，或逻辑完整的 commit；
- 非简单修改使用 feature branch；
- 使用 PR 承载需要审查的变更；
- 高风险 migration 明确 rollback path；
- 破坏性操作采用 backup 或 dry-run。

对于 Agent 生成的大规模重写，应采用比局部修改更强的审查和验证。

## 6. 依赖纪律

新增依赖前，应明确：

- 它解决什么问题；
- 为什么现有能力不足；
- 安装和维护成本；
- 安全与供应链风险；
- 替换成本；
- 对可移植性的影响。

只要依赖本身合理，应优先复用成熟基础设施，而不是脆弱地重复实现。对于以 Markdown 为主的文档仓库，除非更强自动化解决了真实问题，否则应特别克制工具链规模。

## 7. 隐私与仓库卫生

私有材料与公开材料应有意识地分离。

至少做到：

- 不提交 credentials 或 secrets；
- 避免机器专属的私人路径；
- 不把未公开或私有项目数据混入公开产物；
- 必要时说明外部数据传输；
- Agent 与自动化只获得完成任务所需的最低必要权限；
- 私有仓库转公开前审查 Git history。

## 8. 渐进式用户体验

用户 onboarding 应分层设计。

新用户应当能够快速回答：

1. 这个项目是什么？
2. 适合谁？
3. 最小且有价值的采用或尝试方式是什么？
4. 有哪些重要假设和限制？
5. 高级或内部细节在哪里？

不要把高级架构或方法论的所有概念强行塞进初始采用路径。

## 9. 项目审查

使用轻量项目审查来暴露关键工程决策缺口，而不是先增加更多流程。

审查应覆盖项目目的、用户、Agent 上下文、隐私边界、依赖、验证、可逆性、可移植性和 onboarding。它是诊断工具，不是认证评分表。

见 [`templates/PROJECT_REVIEW.zh-CN.md`](../templates/PROJECT_REVIEW.zh-CN.md)。

## 10. 决策记录

只有值得记录的决策才使用正式 decision record。

普通修改使用清晰的 PR 或 commit 说明通常已经足够。对于高影响偏离，应记录 default、conflict、trade-off、exception、evidence、rollback considerations 和 revisit condition。

见 [`templates/DECISION_RECORD.md`](../templates/DECISION_RECORD.md)。

## 11. 公开发布准备

首次公开发布或修改 repository visibility 前，应检查：

- license 与 attribution；
- README 与 onboarding；
- 项目真正承诺维护的语言覆盖；
- secrets 与私有数据；
- repository history；
- dependencies；
- validation status；
- contribution 与行为规范；
- release scope 与已知限制。

公开发布是工程决策，而不只是修改一个 GitHub repository setting。

## 12. 实践如何演化

真实项目经验或工具变化足以提供依据时，应更新实践层。

外部优秀仓库可以提供机制和示例，但应选择性吸收。不得因为某个头部项目使用了某种流程、目录、工具或约定，就机械复制。

不得把某个具体工具的短期使用方式直接提升为稳定原则，除非它背后代表了与该工具无关、长期存在的工程问题。
