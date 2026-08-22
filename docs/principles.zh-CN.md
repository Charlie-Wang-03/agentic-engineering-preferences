# 核心原则

[English](principles.md)

本文定义 Agentic Open-Source Engineering Methodology 中相对稳定、能够持续影响工程决策的原则。这些原则是强默认偏好，而不是绝对禁令。

这些原则并不都属于同一种概念类型：其中既有价值取向，也有工程默认偏好、约束、决策准则和优先采用的手段。只有当某个概念能够跨项目反复改变工程决策，并且不会随着具体工具快速过时时，才值得进入 Principle 层。

## 最高元原则：Outcomes over Dogma

项目结果优先。原则用于改善工程判断，而不是替代工程判断。

这里的“项目结果”指当前条件下项目已经明确的目的、用户、质量属性、现实约束和工程目标。当不同原则彼此冲突，或原则与这些结果冲突时，可以进行明确 trade-off，而不应机械遵循某条原则。

> **Deviation is allowed; unexplained deviation is not.**
>
> 允许偏离默认原则，但不允许无法解释的偏离。

## 概念角色

下面的分类用于澄清每条原则主要承担什么作用，不代表新增方法论层级。

| Principle | 主要角色 |
| --- | --- |
| Open by Default | 生态价值与默认取向 |
| Agent-Native, Human-Accountable | 设计默认与责任约束 |
| Portable over Model-Agnostic | 架构偏好 |
| User Sovereignty & Privacy by Default | 用户价值与安全约束 |
| Local-First When Practical | 执行偏好 / 手段 |
| Justified Dependencies | 工程决策准则 |
| Progressive Usability | 产品与文档偏好 |
| Verifiable by Default | 质量默认 |
| Reversible Change | 风险控制默认 |

## 1. Open by Default

开放优先。

优先选择符合开源生态习惯的方案，包括清晰许可证、开放格式与接口、可理解的仓库结构、互操作性以及对贡献者友好的协作方式。

这一原则主要回答项目如何与生态、用户和贡献者发生关系。具体模型、provider 或工具是否容易替换，则由 **Portable over Model-Agnostic** 更直接地处理。

Open by Default 不意味着所有内容都必须公开。私有孵化、尚未公开的研究、安全敏感信息、凭证和用户数据都可能需要受控访问。

## 2. Agent-Native, Human-Accountable

Agent 原生，人类负责。

仓库应尽可能让 AI Agent 在较少隐式上下文的情况下理解、修改、测试、验证、维护并更新文档。

优先采用明确的结构、命令、约束、验收标准、仓库不变量和机器可读指令。Agent-native 主要解决机器执行者能否可靠理解项目的问题；**Progressive Usability** 则主要解决人类用户和贡献者的 onboarding 与认知负担问题。

Agent 原生不等于“由 AI 生成”，也不意味着责任转移给 Agent。项目决策与公开结果最终仍由人承担责任。

## 3. Portable over Model-Agnostic

追求可移植，而不是绝对模型无关。

避免不必要的模型锁定、Agent 产品锁定、云平台锁定和工具链锁定；在替换确实具有潜在价值的地方，优先设计清晰、可替换的边界。

不得为了“支持一切”而把实现压缩到最低公共能力，也不得为了抽象而抽象。如果收益明确，`portable core + provider/tool-specific optimization` 是合理设计。

## 4. User Sovereignty & Privacy by Default

用户主权与默认隐私保护。

用户应尽可能对自己的数据、凭证、模型选择、Agent 选择、执行环境和项目产物保持实质控制。

应减少不必要的数据传输、权限、telemetry、凭证暴露、私人路径泄漏，以及私有材料与公开产物的混杂。

这一原则定义的是用户控制权和隐私目标；**Local-First When Practical** 只是实现这些目标的一种可能手段，而不是它们的定义。

## 5. Local-First When Practical

合理情况下本地优先。

当本地执行能够实质改善隐私、自主性、可复现性、离线能力或系统韧性，同时不会造成不合理的能力、维护或易用性成本时，应优先本地执行。

Local-first 不等于 local-only，本地运行本身也不能自动保证隐私或用户主权。当云服务明显是更优工程选择时可以采用，但相关依赖与重要数据流应保持透明。

## 6. Justified Dependencies

每个依赖都必须证明自己的价值。

评估依赖时应考虑：它解决什么问题、自行实现成本、成熟度、维护活跃度、安全暴露、安装负担、替换成本、对可移植性的影响以及长期维护成本。

不得仅为了减少依赖数量而重复实现成熟基础设施，也不得为了让项目“看起来更工程化”而加入与实际风险不匹配的工具。

## 7. Progressive Usability

渐进式用户友好。

简单任务应保持简单，同时允许高级用户在需要时逐步接触更复杂的能力。

优先提供清晰 quick start、合理默认值、较低初始认知负担、progressive disclosure，以及对新手友好的文档。这里尤其包括通过 AI Agent 进入软件开发、但缺乏传统软件工程背景的开发者。

这一原则主要面向人类使用者。Agent 所需的上下文、约束和执行规则属于 **Agent-Native, Human-Accountable**。

## 8. Verifiable by Default

默认可验证。

优先让工作结果能够被工具验证，而不是仅凭表面观感判断正确性。

在确有价值且与风险相称时，应使用 tests、lint、type checks、确定性命令、验证脚本、CI、验收标准和可复现实例。

> **Agent-generated work should be verifiable by tools, not trusted by appearance.**
>
> Agent 生成的工作应当可以由工具验证，而不是因为“看起来正确”就被信任。

Verification 回答的是：**我们凭什么知道这次修改可以接受？**

## 9. Reversible Change

修改应尽可能可逆。

优先控制 blast radius，并为失败保留清晰恢复路径。

根据需要使用版本控制、小而聚焦的 commit、可审查 diff、checkpoint、backup、dry-run、可逆 migration、破坏性操作保护以及生成产物隔离。

Reversibility 与 verification 解决不同问题：**如果修改是错的，或者条件发生变化，应该怎么办？**

## 原则如何演化

不得因为某个概念听起来正确、流行或能让清单更完整，就新增核心原则。

新增之前应先判断 proposed rule 实际属于价值、默认偏好、约束、手段、决策准则还是快速变化的 Practice。并非所有有用规则都应该进入 Principle 层。

方法论应沿以下闭环持续演化：

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Methodology`
