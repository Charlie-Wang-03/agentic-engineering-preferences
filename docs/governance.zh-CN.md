# 方法论治理

[English](governance.md)

本文只负责管理方法论本身如何变化，并有意保持轻量。治理的目标是保护方法论的一致性，而不是把一个小型方法论仓库变成流程繁重的标准组织。

## 1. 规范性结构

仓库中的主要文档职责如下：

- `docs/principles.md` — 相对稳定的工程决策原则；
- `docs/decision-framework.md` — 冲突、trade-off、例外与证据处理；
- `docs/practices.md` — 可以更快演化的实现实践；
- `docs/governance.md` — 上述内容如何演化；
- `AGENTS.md` — Agent 在本仓库工作时的执行约束；
- `templates/` — 从方法论派生出的可复用产物；
- `README.md` — 项目定位、目标用户、边界与采用路径。

同一规则如果出现在多个位置，应尽量保留一个 canonical normative source，其余文件使用链接或简短摘要。

## 2. 修改门槛

不同类型的修改需要不同强度的证据。

### Principle 修改

新增、删除、合并或实质重定义核心原则，需要最强的理由。提案应说明：

- 反复出现的真实工程问题；
- 为什么现有原则和决策框架无法充分处理；
- 来自真实项目或长期外部工程实践的证据；
- 与已有原则的潜在重叠；
- 对 Practices、templates 和 Agent instructions 的下游影响。

在私有孵化阶段，优先澄清已有原则，而不是扩张原则数量。

### Decision Framework 修改

只有真实决策暴露出歧义、trade-off 处理缺口或例外机制不合理时才修改。应始终保留其核心目的：让默认原则真正影响决策，但不变成绝对规则。

### Practice 修改

实践层可以随着工具和工程惯例更快演化，但仍应解决真实问题。头部外部仓库是证据来源，而不是机械模仿的权威模板。

### 仓库实现修改

自动化、脚本、模板与目录结构应与本仓库真实风险和维护需求相称。

## 3. 修改传播

如果方法论已经变化，但派生产物仍然传达旧规则，这次修改就没有完成。

根据实际影响检查：

- README 摘要与导航；
- 配对的核心语言文档；
- `AGENTS.md`；
- templates；
- validation rules；
- PR guidance。

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

操作型文件不要求自动复制。`AGENTS.md`、workflows、贡献操作细节等文件可以保持 English-first，除非中文版本确实提供实际价值。

配对文档应保持语义等价，但自然技术表达优先于机械直译。

## 5. 版本策略

在私有孵化阶段，`v0.x` 主要表示方法论成熟度，而不是严格 Semantic Versioning 承诺。

- 一个孵化阶段的小版本应代表一次连贯的方法论里程碑；
- 普通措辞修正或维护更新不必改变版本号；
- 只有准备正式发布的里程碑才需要 Git tag 或 GitHub Release；
- 首次公开前应进行专门 release-readiness review，而不是自动沿用当前版本号。

## 6. 证据与 Decision Record

大多数方法论修改通过聚焦的 PR 说明即可。只有当选择影响广泛、难以回滚或未来很可能重新评估时，才值得保留独立 Decision Record。

不得为了证明“存在治理”而制造没有实际价值的文档。

## 7. 仓库自身也是考察对象

本仓库本身也是方法论的测试对象。如果文档宣称与实际维护行为出现偏差，应把这种不一致当成证据，并判断：

1. 仓库实现需要修改；或
2. 方法论本身过宽、成本过高或表述不清，需要修正。

自洽性是一种诊断手段，而不是过度工程化仓库的理由。

## 8. 公开发布

从私有孵化转为公开发布之前，应专门审查：

- 方法论一致性与范围；
- README 与 onboarding；
- 隐私、secrets 与 Git history；
- license 与 attribution；
- 实际承诺的语言覆盖；
- contribution 与 conduct guidance；
- validation status；
- repository settings 与 release boundary。

公开发布应当是一个明确的工程决策。
