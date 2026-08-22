# Agentic 开源工程方法论

> 一套面向 AI Agent 时代、用于设计、开发、验证、维护与演化开源软件的实践型方法论。

[English](README.md)

> **当前状态：v0.2 — 私有孵化。** 方法论正在真实项目工作中持续验证和修正。它是一套具有明确立场的工程方法论，而不是行业标准。

## 为什么需要这个项目

AI Agent 正在显著降低软件生成成本，真正稀缺的能力因此逐渐从“生成代码”转向工程判断：定义约束、组织仓库、验证修改、控制风险、保护用户控制权，以及判断何时应该偏离默认原则。

本仓库试图形成一套简洁的工程决策系统，用于指导人类开发者与 AI Agent 协同建设开源项目。

它应当做到：

- 足够实用，能够真正改变仓库中的工程决策；
- 足够明确，让开发者与 Coding Agent 都能够执行；
- 原则层相对稳定，同时允许实践层随着工具生态演化；
- 足够轻量，适合小团队和独立开发者；
- 允许项目根据自身情况调整，而不是规定唯一技术栈或工作流。

## 适合谁

本方法论尤其面向：

- 高度使用 Coding Agent 的独立开发者；
- 通过 AI 辅助开发进入软件工程实践的开发者；
- 会直接参与原型、代码仓库与 Coding Agent 工作流的技术型 AI 产品建设者和产品经理；
- 希望建立更清晰 Human-Agent Collaboration，但不希望引入重型流程框架的项目维护者。

本方法论假设 AI Agent 可以显著加速实现，但不能替代由人承担的工程责任与判断。

## 最高元原则

### Outcomes over Dogma

**项目结果优先。原则用于改善工程判断，而不是替代工程判断。**

当默认原则与项目明确目标、用户价值、质量、安全、性能、维护性或现实约束发生冲突时，使用：

`Default → Conflict → Trade-off → Exception → Evidence → Revisit`

> **Deviation is allowed; unexplained deviation is not.**
>
> 允许偏离默认原则，但不允许无法解释的偏离。

## 核心原则

1. **Open by Default — 开放优先**
2. **Agent-Native, Human-Accountable — Agent 原生，人类负责**
3. **Portable over Model-Agnostic — 追求可移植，而非绝对模型无关**
4. **User Sovereignty & Privacy by Default — 用户主权与默认隐私保护**
5. **Local-First When Practical — 合理情况下本地优先**
6. **Justified Dependencies — 每个依赖都必须证明自己的价值**
7. **Progressive Usability — 渐进式用户友好**
8. **Verifiable by Default — 默认可验证**
9. **Reversible Change — 修改应尽可能可逆**

这些原则并不都属于同一种概念类型，其中同时包含长期价值、工程默认偏好、约束和优先采用的手段。它们之所以属于本方法论的 Principle，是因为它们能够跨项目、持续地改变工程决策。完整说明见 [核心原则](docs/principles.zh-CN.md)。

## 方法论结构

本方法论区分三个执行层，以及一个管理方法论自身演化的治理层：

1. **Principles — 原则层**：相对稳定、能够持续影响工程决策的价值、默认偏好、约束和工程取向；
2. **Decision Framework — 决策框架**：处理原则冲突、trade-off 与合理例外；
3. **Practices — 实践层**：把方法论落实到仓库、Agent 指令、验证、贡献流程和发布流程；
4. **Governance — 治理层**：管理方法论本身如何修改，避免规则漂移和无依据膨胀。

建议从这里开始：

- [核心原则](docs/principles.zh-CN.md)
- [决策框架](docs/decision-framework.zh-CN.md)
- [实践指南](docs/practices.zh-CN.md)
- [方法论治理](docs/governance.zh-CN.md)

## 如何在项目中使用

一种轻量采用路径是：

1. 明确项目目的、主要用户、关键约束和真正重要的结果；
2. 只选择真正会影响当前项目决策的方法论默认偏好；
3. 参考 [`templates/AGENTS.md.template`](templates/AGENTS.md.template) 编写仓库级 Agent 指令；
4. 使用 [项目审查模板](templates/PROJECT_REVIEW.zh-CN.md) 暴露主要缺口，而不是把它当成认证清单；
5. 默认原则发生冲突时使用决策框架；
6. 只有高影响决策才保留持久证据；
7. 把真实项目中的失败与成功反馈给方法论。

对于需要比普通 commit 或 PR 说明更完整记录的决策，可使用轻量的 [Decision Record](templates/DECISION_RECORD.md)。

## 仓库自身也是方法论的考察对象

本仓库也必须接受自身方法论的检验，但应当与项目规模相称：它本质上主要是一个 Markdown 文档仓库，不应该为了“工程化”而建立重型基础设施。

因此，本仓库优先保持：

- [`AGENTS.md`](AGENTS.md) 中清晰的 Agent-facing instructions；
- README 与核心方法论文档的中英双语阅读路径；
- 轻量自动验证，而不是大型文档工具链；
- 聚焦、可审查、可逆的修改；
- 明确的文档职责边界；
- 尽可能少的不必要依赖与自动化。

当前验证命令：

```bash
python3 scripts/validate_repo.py
```

## 语言策略

英文作为仓库操作和国际开源协作的默认语言；README 与核心方法论文档提供完整的简体中文一等阅读路径。

并非所有操作型文件都需要机械复制为双语版本。翻译应当真正改善可访问性，而不是为了目录对称。详见 [方法论治理](docs/governance.zh-CN.md#语言与文档策略)。

## 项目边界

本项目关注的是人类开发者与 AI Agent 协同进行开源软件工程时的方法论。

它**不是**：

- 当前 AI 产品或模型的目录；
- 要求所有项目采用同一技术栈的统一规范；
- 认证标准或合规框架；
- 为证明方法论而制造的案例集合；
- 博客或内容营销仓库；
- 对成熟软件工程、安全或开源标准的替代。

具体工具相关内容属于实践层，可以随着生态快速更新。

## 方法论如何演化

本方法论来自真实工程反馈：

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Methodology`

外部优秀实践可以提供参考，但只有在确实改善本项目决策系统时才应吸收，而不是因为某种做法流行或被头部项目采用就机械复制。

仓库在孵化阶段继续保持私有。首次公开前应专门完成文档、隐私、Git 历史、治理和方法论一致性审查。

## 参与贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。私有孵化阶段应坚持证据驱动，并谨慎扩张核心原则集合。

## 许可证

本项目采用 [Apache License 2.0](LICENSE)。
