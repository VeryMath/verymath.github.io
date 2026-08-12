# VeryMath 首页贡献者姓名双语显示设计

日期：2026-08-12
状态：待书面审阅

## 目标

VeryMath 首页已经使用统一的中英文切换。贡献者卡片也应遵循同一语言状态：英文页面只显示英文姓名，中文页面只显示中文姓名。GitHub 头像、账号、主页链接、卡片身份和排列位置不随语言切换改变。

## 方案选择

采用数据层双语字段，并由 Liquid 同时生成英文与中文节点：

- `name_en`：英文姓名，统一采用“名 + 姓”顺序；
- `name_zh`：中文姓名；
- `initial_en`：英文模式下头像失败或无头像时的缩写；
- `initial_zh`：中文模式下头像失败或无头像时的姓氏文字；
- `github`：已确认的 GitHub 登录名，没有可用账号时为 `null`；
- `evidence`：公开贡献、身份或角色来源。

页面继续使用既有 `.lang-en`、`.lang-zh` 和 `data-vm-lang` 机制，不新增姓名专用 JavaScript 字典。这样数据文件仍是唯一身份来源，服务端生成的 HTML 在 JavaScript 不可用时也保留默认英文姓名。

未采用以下方案：

1. 在同一卡片中始终显示 `English / 中文`：不符合“中英文区分”，也会增加移动端拥挤。
2. 在 JavaScript 中维护账号到姓名的翻译字典：会让身份数据分散在两个文件，并增加无脚本页面的不一致风险。

## 姓名映射

英文姓名统一采用“名 + 姓”顺序。老师的中文名采用其个人主页公开写法“王祥丰”：<https://xfwang87.github.io/>。

| English | 中文 | GitHub |
| --- | --- | --- |
| Conan Xu | 徐柯楠 | `ConanXu-math` |
| Dong Yuan | 袁东 | `dyuan311` |
| Yun Hua | 华贇 | `hyyh28` |
| Mengyuan Xing | 邢梦圆 | `IsRivulet` |
| Miao Dong | 董淼 | 无可用映射 |
| Zhixin Zheng | 郑智心 | 无可用映射 |
| Quan Sun | 孙权 | 无可用映射 |
| Siyu Zhang | 张司雨 | `rain37233-del` |
| Haoru Tang | 汤皓如 | `tang0805-em` |
| Xiangfeng Wang | 王祥丰 | `xfwang87` |
| Xiaowen Zhang | 张笑玟 | 无可用映射 |
| Yihong Wei | 尉毅宏 | `Imccark` |
| Yunfeng Lu | 陆云峰 | 无可用映射 |
| Zhuojie Tu | 涂卓杰 | `Tu-ZJ` |
| Shuangxi Li | 李爽夕 | `ricercar77` |
| Boxian Jiang | 蒋博先 | `Joseph20060208` |

卡片保持当前稳定顺序。切换语言只改变可见姓名与备用缩写，不重新排序，避免卡片在用户操作时跳动。

## 页面渲染

每张卡片的姓名节点包含两个语言子节点：

```html
<span class="vm-contributor-name">
  <span class="lang-en">English name</span>
  <span class="lang-zh">中文姓名</span>
</span>
```

备用头像文字采用相同结构。英文模式显示两到三个拉丁字母缩写，中文模式显示一个姓氏汉字。GitHub 头像成功加载后继续覆盖备用文字；头像加载失败时，当前语言对应的备用文字保持可见。

GitHub 账号行始终显示同一 `@github`，链接地址不随语言改变。指导老师与其他参与者使用相同卡片样式，不置顶、不添加排行榜或贡献次数。

贡献者区域说明同步涵盖指导支持：

- English: `We thank everyone who has contributed tools, workflows, research infrastructure, and guidance to VeryMath.`
- 中文：`感谢所有为 VeryMath 的工具、工作流、科研基础设施与指导支持作出贡献的参与者。`

## 数据迁移

将现有 `_data/contributors.json` 中的 `name`、`initial` 分别迁移为双语字段。`github` 和 `evidence` 原样保留，记录数量保持 16，GitHub 关联数量保持 11。

页面模板不再读取旧的 `name` 或 `initial` 字段。测试应拒绝混用旧字段，防止未来新增记录只提供一种语言。

## 验证

自动测试覆盖：

1. 16 条记录均具有完整双语字段，英文名与中文名分别不重复；
2. 英文姓名全部采用已批准映射，中文姓名全部采用已批准映射；
3. 11 个 GitHub 账号、头像 URL 和主页链接保持不变；
4. 默认英文模式只显示英文姓名与英文备用缩写；
5. 切换中文后只显示中文姓名与中文备用文字；
6. 头像成功、加载失败和延迟加载三种状态均不泄露错误语言的备用文字；
7. 桌面与手机视口均保持现有卡片数、列数要求和无横向溢出；
8. 页面不新增贡献者 GitHub API 请求、排名或贡献计数。

浏览器验证生成英文和中文两种桌面、手机预览。人工检查长姓名 `Xiangfeng Wang`、`Xiaowen Zhang` 以及中文姓名均不截断。

## 变更范围

预计修改：

- `_data/contributors.json`；
- `index.md` 中贡献者说明和卡片 Liquid 模板；
- `tests/test_contributors.py`；
- `tests/verify_contributors_browser.cjs`；
- 相关测试说明与既有贡献者设计记录。

不修改其他首页模块，不改变 GitHub 账号映射，不合并或发布网站。
