# short_chn_yn
短文本中文字面肯定否定识别。

逻辑异常简单，目的异常简单。

### 1.目的

中文是由字组成的，日常交流中最常见的很短的字面肯定和否定，例如“嗯，是的”，“不是啊”，这种肯定和否定不需要太复杂语义识别。

### 2.逻辑

Yes-or-No=Not(Xor(yes,no))。

例如，“不是啊“，“不”表示False，“是”表示True，“啊”是无意义词，忽略，则Not(Xor(True,False))=False=No，故表示否定。

对于更复杂的情况，“难道不是吗”，进行递归，Not(Xor(Not(Xor(False, False)), True))=True=Yes，表示肯定。

这样做的问题是：

1. 有的词有语义性，例如“嗯”，很难说清楚它表示肯定还是语气词。
2. 中文表达的顺序性，例如“是不”，表示的是疑问，而根据代码，会识别为否定。

### 3.使用

```python
from prettyprinter import pprint 
import short_chn_yn as yn
if __name__=="__main__":
    #实例化对象
    y1=yn.yn()
    s = "嗯是"
    #输入
    result = y1.y_n(s)
    pprint(result)
```

其中的`simple_dict.txt`含有：`pos, neg, others, filter`四个内容，分别表示：肯定、否定、无意义词和特殊处理词(解决问题2)，用户可自行修改。

`yn(dictionary)`，构造函数，可以用符合标准的字典，空缺使用默认字典。

`y_n(s, thre)`，输出判断，其中`s`为输入字符串，`thre`为阈值，因为语速是大部分人都是一定的，所以1~2s 说出的词的个数也是固定的，默认为6。

`y_n()`输出为字符串：

```
    Positive: 肯定

​    Negtive: 否定

​    Nonsense: 无意义

​    Incognizance: 不识别

​    too long: 字符串长度超过thre
```



### 4.协议

3 Clause BSD

