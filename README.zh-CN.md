# Agentic 开源工程方法论

> 一套面向 AI Agent 时代、用于设计、开发、验证、维护与演化开源软件的实践型方法论。

[English](README.md)

> **当前状态：v0.1 — 私有孵化。** 方法论仍在真实项目工作中持续验证，目前不应被视为行业标准或已经完成的正式规范。

## 为什么需要这个项目

AI Agent 正在显著降低软件生成成本，但这并不会消除工程判断的重要性。相反，当生成速度越来越快时，清晰约束、验证能力、可审查性、隐私边界和可维护的项目结构会变得更加重要。

本仓库试图形成一套具有明确立场、但允许根据项目实际情况调整的工程决策系统，用于指导人类开发者与 AI Agent 协同建设开源项目。

它应当做到：

- 足够实用，能够影响真实仓库中的工程决策；
- 足够可执行，能够逐步转化为 `AGENTS.md`、模板、检查和自动化；
- 原则层保持稳定，同时允许实践层随着工具快速演化；
- 开放且可复用，但不假设一种工作流适用于所有项目。

## 最高元原则

### Outcomes over Dogma

**项目结果优先。原则用于改善工程判断，而不是替代工程判断。**

当默认原则与用户价值、项目质量、安全、性能、维护性或其他原则冲突时，使用：

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

完整说明与适用边界见 [核心原则](docs/principles.zh-CN.md)。

## 方法论结构

本方法论区分三个变化速度不同的层次：

1. **Principles — 原则层**：回答什么价值和工程属性应当优先；
2. **Decision Framework — 决策框架**：回答原则冲突、trade-off 和合理例外应当如何处理；
3. **Practices — 实践层**：回答如何在仓库、Agent 指令、验证、贡献流程和发布流程中实际执行。

建议从这里开始：

- [核心原则](docs/principles.zh-CN.md)
- [决策框架](docs/decision-framework.zh-CN.md)
- [实践指南](docs/practices.zh-CN.md)

## 如何在项目中使用

一种轻量采用路径是：

1. 阅读核心原则；
2. 选择真正会影响当前项目决策的默认偏好；
3. 参考 [`templates/AGENTS.md.template`](templates/AGENTS.md.template) 编写仓库级 Agent 指令；
4. 默认原则发生冲突时使用决策框架；
5. 只有高影响决策才保留更持久的证据；
6. 把真实项目中的失败与成功重新反馈给方法论。

对于需要比普通 commit 或 PR 说明更完整记录的决策，仓库提供了一个轻量的 [Decision Record 模板](templates/DECISION_RECORD.md)。

## 仓库自身作为 Reference Implementation

这个仓库应尽可能实践自己描述的方法论，包括：

- 使用 [`AGENTS.md`](AGENTS.md) 提供清晰的 Agent-facing instructions；
- 将英文与简体中文都作为一等文档维护；
- 提供轻量自动化验证；
- 保持修改聚焦且可逆；
- 明确贡献规则；
- 避免不必要依赖。

当前仓库验证命令：

```bash
python3 scripts/validate_repo.py
```

## 项目边界

本项目关注的是人类开发者与 AI Agent 协同进行开源软件工程时的工程方法论。

它**不是**：

- 当前 AI 产品或模型的目录；
- 要求所有项目使用相同技术栈的统一规范；
- 为证明方法论而制造的案例集合；
- 博客或内容营销仓库；
- 对成熟软件工程、安全或开源规范的替代。

具体工具相关内容属于实践层，可以随着生态快速更新。

## 私有孵化与演化

仓库当前有意保持私有，在首次公开发布之前持续验证方法论。

方法论应沿以下闭环演化：

`Principles → Projects → Decisions → Failures / Successes → Lessons → Revised Principles`

只有在文档、隐私、Git 历史、仓库治理和方法论一致性经过审查后，才应进行首次公开发布。

## 参与贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。在私有孵化阶段，应坚持证据驱动，并谨慎扩张核心原则集合。

## 许可证

本项目采用 [Apache License 2.0](LICENSE)。
