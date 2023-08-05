# 日志记录

## 简介
日志记录模块是一个简单的日志输出工具，它可以将不同等级（INFO、WARNING、ERROR、DEBUG、CRITICAL）的日志输出到控制台。该模块还支持彩色输出，以提高在支持彩色显示的控制台上的可读性。

## 使用方法
要使用日志记录模块，请在您的Python脚本或模块中导入它，如下所示：

```
pip install logPPP
```

```python
import logPPP
```

## 常量

### `__version__`
- 类型：字符串
- 描述：日志记录模块的版本号。

### `IS_COLOR`
- 类型：布尔值
- 描述：一个标志，用于指示是否启用彩色输出。当设置为`True`时，日志消息将以彩色显示。可以更改此标志以控制彩色输出的行为。

### `LEVEL`
- 类型：`Level` 枚举
- 描述：最低日志等级，只有等级大于等于`LEVEL`的日志消息才会被打印。可能的日志等级包括`INFO`、`WARNING`、`ERROR`、`DEBUG`和`CRITICAL`。

## 日志等级

### `info(*args, sep=' ', end='\n', file=None, is_color=None)`
- 描述：以INFO日志等级记录一条消息。
- 参数：
  - `*args`：要记录的消息或多个消息。
  - `sep`：多个消息参数之间的分隔符（默认为一个空格）。
  - `end`：消息结尾的字符（默认为换行符）。
  - `file`：将日志写入的文件对象（默认为控制台）。
  - `is_color`：一个标志，用于覆盖全局的`IS_COLOR`设置以启用或禁用彩色输出。如果设置为`True`，将启用彩色，如果设置为`False`，将禁用彩色。如果设置为`None`（默认值），则将使用全局的`IS_COLOR`设置。

### `warning(*args, sep=' ', end='\n', file=None, is_color=None)`
- 描述：以WARNING日志等级记录一条消息。
- 参数：与`info()`相同。

### `error(*args, sep=' ', end='\n', file=None, is_color=None)`
- 描述：以ERROR日志等级记录一条消息。
- 参数：与`info()`相同。

### `debug(*args, sep=' ', end='\n', file=None, is_color=None)`
- 描述：以DEBUG日志等级记录一条消息。
- 参数：与`info()`相同。

### `critical(*args, sep=' ', end='\n', file=None, is_color=None)`
- 描述：以CRITICAL日志等级记录一条消息。
- 参数：与`info()`相同。

## 示例

```python
import logPPP

logPPP.LEVEL = logPPP.Level.DEBUG
logPPP.IS_COLOR = True

logPPP.info("info", 'test', is_color=True)
logPPP.warning("warning")
logPPP.error("error")
logPPP.debug("debug")
logPPP.critical("critical")
logPPP.critical("critical", is_color=False)
```

在这个示例中，日志等级被设置为INFO，因此只有INFO、WARNING、ERROR和CRITICAL等级的日志消息会被显示出来。根据`IS_COLOR`标志，日志消息会以彩色或非彩色显示。如果`IS_COLOR`设置为`True`，日志消息将以彩色显示，否则将以非彩色显示。
