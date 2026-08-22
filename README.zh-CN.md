# Agentic 开源工程方法论

> 一套面向 AI Agent 时代、用于设计、开发、验证、维护与演化开源软件的实践型方法论。

[English](README.md)

> **当前状态：v0.3 — 私有孵化。** 方法论正在真实项目工作中持续验证和修正。它是一套具有明确立场的工程方法论，而不是行业标准。

## 用一句话让 AI Agent 审查你的项目

如果你的 AI Agent 能够访问本方法论仓库和目标项目，可以直接发送：

> **请使用 `https://github.com/Charlie-Wang-03/Agentic-Open-Source-Engineering-Methodology` 中的 Agentic Open-Source Engineering Methodology 审查 `<TARGET_PROJECT>`。先读取并遵循 `AGENT_REVIEW_PROTOCOL.md`；基于实际项目证据判断哪些方法论维度真正适用，给出结构化诊断评分与有证据支持的发现；除非我明确要求，否则不要修改目标项目。**

`<TARGET_PROJECT>` 可以是 Agent 当前打开的本地 workspace、本地项目目录、GitHub 仓库、其他远程仓库，或者 Agent 实际能够读取的其他项目来源。

目标项目**不要求必须开源，也不要求使用 Git**。本方法论的核心定位仍然是 Agentic Open-Source Engineering，但外部审查协议会根据项目实际目标选择适用维度：真正不相关的维度标记为 `N/A`，而不是视为缺陷。

审查默认 evidence-first 且只读。canonical、工具无关的执行协议见 [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md)。

如果 Agent 无法访问方法论或目标项目的重要部分，应明确报告限制，而不是假装已经完成完整审查。

## 为什么需要这个项目

AI Agent 正在显著降低软件生成成本，真正稀缺的能力因此逐渐从“生成代码”转向工程判断：定义约束、组织项目、验证修改、控制风险、保护用户控制权，以及判断何时应该偏离默认原则。

本仓库主要面向人类开发者与 AI Agent 协同建设开源项目，形成一套简洁工程决策系统；同时提供可移植的外部项目审查协议，在确有适用性的情况下也可检查更广泛类型的项目。

它应当做到：

- 足够实用，能够真正改变工程决策；
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

并非每条原则或每个审查维度都对所有目标项目有实质意义。必须先根据项目真实目的与约束判断适用性，再讨论是否存在缺口。

## 方法论结构

本方法论区分三个执行层，以及一个管理方法论自身演化的治理层：

1. **Principles — 原则层**：相对稳定、能够持续影响工程决策的价值、默认偏好、约束和工程取向；
2. **Decision Framework — 决策框架**：处理原则冲突、trade-off 与合理例外；
3. **Practices — 实践层**：把方法论落实到仓库、Agent 指令、验证、贡献流程和发布流程；
4. **Governance — 治理层**：管理方法论本身如何修改，避免规则漂移和无依据膨胀。

外部 Agent Review Protocol 是建立在这些规范源之上的执行接口，并不构成新的 Principle 层。

建议从这里开始：

- [Agent Review Protocol](AGENT_REVIEW_PROTOCOL.md) — 让 Agent 实际审查另一个项目；
- [核心原则](docs/principles.zh-CN.md) — 相对稳定的工程默认；
- [决策框架](docs/decision-framework.zh-CN.md) — trade-off 与合理例外；
- [实践指南](docs/practices.zh-CN.md) — 落地实践；
- [方法论治理](docs/governance.zh-CN.md) — 方法论自身如何演化。

## 两种使用方式

### 1. 外部审查 — 默认方式

让方法论保持在目标项目之外，只在真正有价值的节点调用，例如：

- 一个项目开始进入认真开发阶段；
- 重大架构或依赖决策；
- 大规模重构；
- 准备公开发布；
- 重要 Release；
- 事故、失败或明显工程问题之后。

Agent Review Protocol 会输出适用性自适应的评分表、Evidence Coverage、高价值缺口、已接受 trade-off、待补证据、主动 defer 的问题和有优先级的下一步行动。

正常情况下，审查不会在目标项目中留下任何方法论专属文件。

### 2. 选择性落地 — 确有价值时

如果外部审查发现反复出现的项目特定需求，只把真正有价值的结论转化为目标项目自己的工程产物。

例如：

- 如果 Coding Agent 缺乏明确上下文，可以参考 [`templates/AGENTS.md.template`](templates/AGENTS.md.template)；
- 如果某个高影响决策值得长期保留理由，可以使用 [Decision Record](templates/DECISION_RECORD.md)；
- 因为项目本身需要而增加 tests、validation、documentation 或 safeguards，而不是为了证明“符合方法论”。

不得把九条原则或整套方法论文件机械复制到每个项目。

## 诊断评分

外部审查协议提供结构化评分，但不把方法论变成认证体系。

对于每个可能适用的审查维度：

- 先判断 `Material`、`Relevant` 或 `N/A`；
- 证据充分的维度给出 `0–4` 分和置信度；
- 适用但证据不足的维度标记为 `NE`，而不是猜分；
- `N/A` 不扣分；
- 只有加权 Evidence Coverage 达到至少 70% 时，才给出 `/100` 的 Diagnostic Score。

分数只是对已检查状态的摘要，不能代替具体 finding，也不能抵消严重单点问题；不同类型项目之间不应机械横向比较总分。

详见 [项目审查](templates/PROJECT_REVIEW.zh-CN.md) 与 [Agent Review Protocol](AGENT_REVIEW_PROTOCOL.md)。

## 仓库自身也是方法论的考察对象

本仓库也必须接受自身方法论的检验，但应当与项目规模相称：它本质上主要是一个 Markdown 文档仓库，不应该为了“工程化”而建立重型基础设施。

因此，本仓库优先保持：

- 明确区分 [`AGENTS.md`](AGENTS.md)（约束 Agent 如何维护本仓库）与 [`AGENT_REVIEW_PROTOCOL.md`](AGENT_REVIEW_PROTOCOL.md)（约束 Agent 如何审查外部目标项目）；
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

Agent Review Protocol 保持单一英文 canonical operational file；审查结果通常应使用用户的语言输出。并非所有操作型文件都需要机械复制为双语版本。翻译应当真正改善可访问性，而不是为了目录对称。详见 [方法论治理](docs/governance.zh-CN.md#语言与文档策略)。

## 项目边界

本项目核心关注人类开发者与 AI Agent 协同进行开源软件工程时的方法论。外部审查协议也可以检查私有、本地、内部或非 Git 项目，但只应用真正与目标项目相关的维度。

它**不是**：

- 当前 AI 产品或模型的目录；
- 要求所有项目采用同一技术栈的统一规范；
- 认证标准或合规框架；
- 安全审计的替代品；
- 为证明方法论而制造的案例集合；
- 博客或内容营销仓库；
- 对成熟软件工程、安全或开源标准的替代。

具体工具相关内容属于实践层，可以随着生态快速更新。

## 方法论如何演化

本方法论来自真实工程反馈：

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Methodology`

外部优秀实践可以提供参考，但只有在确实改善本项目决策系统时才应吸收，而不是因为某种做法流行或被头部项目采用就机械复制。

仓库在孵化阶段继续保持私有。首次公开前应专门完成文档、隐私、Git 历史、治理、方法论一致性以及跨 Agent Review Protocol 行为测试。

## 参与贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。私有孵化阶段应坚持证据驱动，并谨慎扩张核心原则集合。

## 许可证

本项目采用 [Apache License 2.0](LICENSE)。
