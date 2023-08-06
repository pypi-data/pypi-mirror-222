# DocsBot 使用说明

DocsBot 是一个命令行工具，提供了方便的方式来管理和查询你的资料库。

## 命令和参数

以下是 DocsBot 支持的命令及其参数：

### `addbase`

这个命令用于添加一个新的资料库。

```bash
$ docsbot addbase <dir>
```
`<dir>`: 要添加的资料库的目录路径。

### `listbase`
这个命令用于列出所有已添加的资料库。

```bash
$ docsbot listbase
```

### `deletebase`
这个命令用于删除一个已添加的资料库。

```bash
$ docsbot deletebase <baseid>
```
`<baseid>`: 要删除的资料库的ID。

### `query`
这个命令用于查询一个资料库。

```bash
docsbot query <baseid> <query>
```
<baseid>: 要查询的资料库的ID。
<query>: 查询字符串。

注意：在所有命令中，<baseid>都应该替换为真实的资料库ID，<dir>应该替换为真实的目录路径，<query>应该替换为你的查询字符串。