# 模块
模块没有实际实现什么功能，能够让你按逻辑组织你的代码，并与其他模块区分。  
对于大中型项目，模块是必须不可少的。把相关代码放在同一个模块中能够让你的代码组织更合理、更易懂。  
python本身就自带了许多有用的模块，比如os、copy等。  

大纲
* 引用模块
* 自定义模块
    - 包

## 引用模块
定义一个模块`support.py`。  
```python
first_name = 'Liang'
last_name = 'Alan'

def full_name():
    return first_name + ' ' + last_name
```

在`test.py`中使用`import 模块名`的方式引用模块。  
```python
import support

print(support.last_name)
print(support.full_name())
```
结果为:
```
Alan
Liang Alan
```

如果模块名太长，可以使用`import 模块名 as 别名`的方式来缩短名字。  
```python
import support as sp

print(sp.last_name)
print(sp.full_name())
```

如果还是嫌太麻烦，可以使用`from 模块名 import 属性`的方式把需要的属性、方法引入到当前命名空间。可以引入多个属性，用逗号分开，但是和分开多行的效果是一样的。  
```python
from support import last_name, full_name

print(last_name)
print(full_name())
```
可以使用`from 模块名 import *`的方式引入所有属性，但最好不要这样，会造成命名空间污染，如果有属性刚好与当前命名空间的变量同名，会造成难以察觉的bug。  

### 搜索路径
当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

1. 程序所在的文件夹
2. 标准库的安装路径
3. 操作系统环境变量PYTHONPATH所包含的路径

## 自定义模块
一个`.py`文件就是一个模块。定义自己的模块后，放在搜索路径中就可被引入了。  

### 包
可以将多个模块放在包中，简单来说，**包就是文件夹，但该文件夹下必须存在`__init__.py`文件**。

**结构：**  
```
package_1
 |----- __init__.py
 |----- module_1.py
 |----- module_2.py
```
最简单的情况下，只需要一个空的`__init__.py`文件即可。  
`import *`这样的语句理论上是希望文件系统找出包中所有的子模块，然后导入它们。这可能会花长时间，并出现边界效应等。Python 解决方案是提供一个明确的包索引。  
这个索引由`__init__.py`定义`__all__`变量，该变量为一列表。

**例子**  
```
pack
 |----- __init__.py
 |----- support_1.py
 |----- support_2.py
test.py
```

**__init__.py**  
```python
__all__ = ['support_1', 'support_2']
```

**support_1.py**  
```python
first_name = 'Liang'
last_name = 'Alan'

def full_name():
    return first_name + ' ' + last_name
```

**support_2.py**   
```python

def say_hello():
    print('Hello')
```

**test.py**  
```python
from pack import *

print(support_1.full_name())
print(support_2.say_hello())
```

在`import *`的情况下，模块必需在`__all__`列表中，否则无法引用该模块。  

#### 包内引用
包内引用可以使用相对路径，比如`from . import brother`或`from .. import uncle`。  
