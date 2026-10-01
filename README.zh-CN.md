# Agentic Engineering Preferences

一份公开、持续演化的个人工程参考，记录我在与 AI Agent 协作开发软件项目时通常采用的工程偏好、决策规则与项目约定。

[English](README.md)

> **这是个人参考，不是通用标准。内容表达默认偏好，而不是强制规则。具体项目的本地上下文始终优先。**

## 为什么存在这个仓库

我长期使用 ChatGPT、Claude Code、Codex 等 Coding Agent 参与软件项目开发。不同项目中会反复出现相似的工程问题：需要多强的验证、什么时候值得加入 CI、什么时候应该引入依赖、什么时候发布 Release、有何操作必须获得明确批准，以及 Agent 在开始工作前应该掌握多少项目上下文。

这个仓库用于降低这些重复决策和重复沟通的成本。它记录我通常采用的默认倾向，让具备能力的 Agent 可以把它作为二级上下文，而不必在每次对话中重新推断我的工程偏好。

## 这是什么

仓库主要包含：

- **[工程偏好](docs/preferences.md)** — 相对稳定的工程倾向；
- **[决策规则](docs/decision-rules.md)** — 面对反复出现的工程选择时，我通常如何判断；
- **[项目约定](docs/project-conventions.md)** — 决定采用某种做法后，我通常如何组织和维护项目；
- **[真实项目中的采用](docs/used-in-practice.md)** — 选取公开、可核验的实例，展示这些偏好和决策规则已经如何被实际采用，但不据此宣称它们导致了更好的工程结果；
- **[AGENTS.md 模板](templates/AGENTS.md.template)** — 为具体项目编写 Agent 本地指令的轻量起点。

这个仓库有意保持鲜明的个人工程取向，因为它描述的是我的工作偏好，而不是行业共识。

## 这不是什么

它不是行业标准、通用软件工程方法论、合规或认证框架、项目评分系统、强制项目模板，也不是对具体项目目标和约束进行实际理解的替代品。

## Agent 应如何使用

当 Agent 参与我的项目时，应：

1. 先检查项目真实状态；
2. 优先读取目标仓库自己的本地指令；
3. 理解项目目标、约束、用户与成熟度；
4. 仅把本仓库作为可复用的二级偏好上下文；
5. 只应用对当前项目确实有意义的偏好；
6. 当本仓库与项目本地证据或指令冲突时，以后者为准；
7. 未经明确授权，不执行破坏性或高影响操作。

目标是减少重复解释，而不是用规则替代工程判断。

## 当前核心倾向

当前重点包括：

- 项目结果优先于跨项目惯例；
- 可验证结果优先于“看起来正确”；
- 可审查、可回退的修改优先于不必要的大 blast radius；
- 明确项目上下文优先于隐式本地知识；
- 每个依赖都应证明其维护成本合理；
- 隐私、权限与公开/私有边界应被有意识地管理；
- 仅在确有价值时追求 portability 或 local execution。

完整说明见 [工程偏好](docs/preferences.md)。

## 仓库状态

这个仓库是一份持续演化的个人参考。只有当某条内容确实能够减少未来的重复工程判断或重复 Agent 沟通时，才值得进入核心。

在当前定位之前，本仓库承载的是 **Agentic Engineering Review**：一套 evidence-first 项目 Review 系统。旧设计已由历史 [v0.4 Release](https://github.com/Charlie-Wang-03/agentic-engineering-preferences/releases/tag/v0.4) 保存。当前仓库不再把评分或 Review Protocol 作为主要产品方向。

## 验证

运行：

    python3 scripts/validate_repo.py

## 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

采用 [Apache License 2.0](LICENSE)。
