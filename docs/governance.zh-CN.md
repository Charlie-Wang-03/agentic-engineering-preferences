# 方法论治理

[English](governance.md)

本文只负责管理方法论本身如何变化，并有意保持轻量。治理的目标是保护方法论的一致性，而不是把一个小型方法论仓库变成流程繁重的标准组织。

## 1. 规范性结构

仓库中的主要文档职责如下：

- `docs/principles.md` — 相对稳定的工程决策原则；
- `docs/decision-framework.md` — 冲突、trade-off、例外与证据处理；
- `docs/practices.md` — 可以更快演化的实现实践；
- `docs/governance.md` — 上述内容如何演化；
- `AGENT_REVIEW_PROTOCOL.md` — Agent 审查外部 Target Project 时的 canonical 执行协议；
- `AGENTS.md` — Agent 在本方法论仓库工作时的执行约束；
- `templates/PROJECT_REVIEW.md` — 审查维度与面向人类的诊断 rubric；
- 其他 `templates/` — 从方法论派生出的可复用产物；
- `README.md` — 项目定位、目标用户、边界与采用路径。

不得混淆 `AGENTS.md` 与 `AGENT_REVIEW_PROTOCOL.md`：前者约束如何修改本仓库，后者约束如何把本仓库应用于另一个目标项目。

同一规则如果出现在多个位置，应尽量保留一个 canonical normative source，其余文件使用链接或简短摘要。

## 2. 修改门槛

不同类型的修改需要不同强度的证据。

### Principle 修改

新增、删除、合并或实质重定义核心原则，需要最强的理由。提案应说明：

- 反复出现的真实工程问题；
- 为什么现有原则和决策框架无法充分处理；
- 来自真实项目或长期外部工程实践的证据；
- 与已有原则的潜在重叠；
- 对 Practices、review dimensions、templates 和 Agent instructions 的下游影响。

在私有孵化阶段，优先澄清已有原则，而不是扩张原则数量。

### Decision Framework 修改

只有真实决策暴露出歧义、trade-off 处理缺口或例外机制不合理时才修改。应始终保留其核心目的：让默认原则真正影响决策，但不变成绝对规则。

### Practice 与 Review Protocol 修改

实践层和 Agent Review Protocol 可以随着工具、访问方式与工程惯例更快演化，但仍必须解决真实问题。

除非新证据足以证明需要重新评估，Review Protocol 应持续保留以下不变量：

- evidence before judgment；
- applicability before scoring；
- 真正不相关维度可以 `N/A` 且不扣分；
- 显式处理证据不足；
- 默认只读审查；
- 区分真实缺口与合理 trade-off；
- 提供结构化输出，但不声称认证能力。

头部外部仓库和 Agent 工具是证据来源，而不是机械模仿的权威模板。

### 仓库实现修改

自动化、脚本、模板与目录结构应与本仓库真实风险和维护需求相称。

## 3. 修改传播

如果方法论已经变化，但派生产物仍然传达旧规则，这次修改就没有完成。

根据实际影响检查：

- README 摘要、一句话入口与导航；
- 配对的核心语言文档；
- `AGENT_REVIEW_PROTOCOL.md`；
- `AGENTS.md`；
- `templates/PROJECT_REVIEW*` 与其他受影响模板；
- validation rules；
- PR guidance。

Principle 修改不自动意味着评分体系必须修改；同样，Protocol 的措辞调整也不应为了“同步”而触发无关方法论修改。

不得为了制造“大范围同步修改”而更新无关文件。

## 4. 语言与文档策略

英文作为国际开源协作中的默认操作语言；简体中文是本仓库核心方法论的一等阅读路径。

默认维护中英配对的内容包括：

- `README.md` / `README.zh-CN.md`；
- Principles；
- Decision Framework；
- Practices；
- Governance；
- 当翻译确实改善采用体验时的用户向模板。

操作型文件不要求自动复制。`AGENTS.md`、`AGENT_REVIEW_PROTOCOL.md`、workflows、贡献操作细节等文件可以保持 English-first，除非中文版本确实提供实际价值。

即使 canonical Review Protocol 只保留英文，README 仍应提供可直接使用的中文一句话入口。Agent 执行审查时通常应使用用户语言输出。

配对文档应保持语义等价，但自然技术表达优先于机械直译。

## 5. 版本策略与审查可追溯性

在私有孵化阶段，`v0.x` 主要表示方法论成熟度，而不是严格 Semantic Versioning 承诺。

- 一个孵化阶段的小版本应代表一次连贯的方法论里程碑；
- 普通措辞修正或维护更新不必改变版本号；
- 只有准备正式发布的里程碑才需要 Git tag 或 GitHub Release；
- 首次公开前应进行专门 release-readiness review，而不是自动沿用当前版本号。

Agent 执行的审查在可获得时应记录方法论来源以及解析后的 commit 或 immutable ref。这样可以提供足够追溯性，而无需在孵化阶段额外建立独立 Protocol 版本系统。

## 6. 诊断评分治理

Diagnostic Score 的目的，是让用户更容易理解有证据支持的审查结果，而不是提供认证或通用项目 benchmark。

评分规则以 `AGENT_REVIEW_PROTOCOL.md` 为 canonical source。修改公式、阈值、适用性权重或分数含义时，应有证据证明当前方案会导致误导或不稳定决策。

评分体系必须继续允许：

- 对真正超出项目目标的维度标记 `N/A`；
- 证据不足时标记 `NE`；
- 显式报告 Evidence Coverage；
- 无论总分多高，严重单点 finding 仍然保持可见。

不得为了提高分数而优化方法论，也不得鼓励目标项目仅为了“提分”增加低价值工程机制。

## 7. 证据与 Decision Record

大多数方法论修改通过聚焦的 PR 说明即可。只有当选择影响广泛、难以回滚或未来很可能重新评估时，才值得保留独立 Decision Record。

不得为了证明“存在治理”而制造没有实际价值的文档。

## 8. 仓库自身也是考察对象

本仓库本身也是方法论的测试对象。如果文档宣称与实际维护行为出现偏差，应把这种不一致当成证据，并判断：

1. 仓库实现需要修改；或
2. 方法论本身过宽、成本过高或表述不清，需要修正。

Agent Review Protocol 也是一个可测试的产物。首次公开前，应在多种 Target Project 形态上进行实际测试，并在合理情况下使用多个有能力的 Agent 环境。测试重点是行为不变量，而不是要求不同模型生成完全相同的文字。

自洽性是一种诊断手段，而不是过度工程化仓库的理由。

## 9. 公开发布

从私有孵化转为公开发布之前，应专门审查：

- 方法论一致性与范围；
- README 与 onboarding；
- 一句话外部审查路径；
- Review Protocol 在代表性目标项目上的行为；
- 隐私、secrets 与 Git history；
- license 与 attribution；
- 实际承诺的语言覆盖；
- contribution 与 conduct guidance；
- validation status；
- repository settings 与 release boundary。

公开发布应当是一个明确的工程决策。
