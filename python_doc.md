# python文档相关
## docstring
docstring(文档字符串)是一个函数或类的说明，函数或类定义时写在最前面的第一个字符串则按规定成为文档字符串。  
可以通过`help`函数或`__doc__`方法获得一个函数或类的文档字符串。  
```python
>>> def sum(a, b):
	"""sub two numbers"""
	return a + b

>>> help(sum)
Help on function sum in module __main__:

sum(a, b)
    sub two numbers

>>> class A():
	"""just a test class"""

	
>>> help(A)
Help on class A in module __main__:

class A(builtins.object)
 |  just a test class
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> print(A.__doc__)
just a test class
>>> print(sum.__doc__)
sub two numbers
```

文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。 强烈建议 你在你的函数中使用文档字符串时遵循这个惯例。  
```python
>>> print(int.__doc__)
int(x=0) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> 
```

## pydoc
pydoc能够根据模块中的文档字符串生成文档。  

示例如何书写符合pydoc规则的python文件，主要是模块、类、方法的文档字符串，额外还可以以`__`开头写一个约定的元数据，如`__author__`、`__version__`。  
```python
#!/usr/bin/python
"""Show off features of [pydoc] module
This is a silly module to
demonstrate docstrings
"""
__author__ =  'Alan'
__version__=  '1.0'
__nonsense__ = 'nonsense'
class MyClass:
    """Demonstrate class docstrings"""
    def __init__ (self, spam=1, eggs=2):
        """Set default attribute values only
        Keyword arguments:
        spam ― a processed meat product
        eggs ― a fine breakfast for lumberjacks
        """
        self.spam = spam
        self.eggs = eggs

```
切换到当前文件所有目录，执行`python -m pydoc mymod`。
```python
F:\ABao\work\Python\files\test>python -m pydoc mymod
Help on module mymod:

NAME
    mymod

DESCRIPTION
    Show off features of [pydoc] module
    This is a silly module to
    demonstrate docstrings

CLASSES
    builtins.object
        MyClass

    class MyClass(builtins.object)
     |  Demonstrate class docstrings
     |
     |  Methods defined here:
     |
     |  __init__(self, spam=1, eggs=2)
     |      Set default attribute values only
     |      Keyword arguments:
     |      spam ― a processed meat product
     |      eggs ― a fine breakfast for lumberjacks
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

DATA
    __nonsense__ = 'nonsense'

VERSION
    1.0

AUTHOR
    Alan

FILE
    f:\abao\work\python\files\test\mymod.py
```

对于如下有继承关系的代码。
```python
from mymod import MyClass
class MyClass2(MyClass):
    """Child class"""
    def foo(self):
        pass
```

执行`python -m pydoc mymod2.MyClass2`
```python
Help on class MyClass2 in mymod2:

mymod2.MyClass2 = class MyClass2(mymod.MyClass)
 |  Child class
 |
 |  Method resolution order:
 |      MyClass2
 |      mymod.MyClass
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  foo(self)
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from mymod.MyClass:
 |
 |  __init__(self, spam=1, eggs=2)
 |      Set default attribute values only
 |      Keyword arguments:
 |      spam ― a processed meat product
 |      eggs ― a fine breakfast for lumberjacks
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from mymod.MyClass:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

```
能够正确打印继承关系。

### 服务器模式
启动一个本地web服务器，通过网页方式查看文档帮助。
```python
python -m pydoc -p 1234
```
使用`-p`选项，后跟端口号。这时在浏览器中输入`localhost:1234`便可以访问服务器，包括当前目录下的模块和内置模块和自带模块和安装到site-packages的第三方库。  

### HTML生成器模式
生成静态的HTML文档。 
```python
python -m pydoc -w mymod mymod.html
```
使用`-w`参数，后跟文件名及要生成的html文件名。

## doctest
doctest在python自带的包中，用于根据文档字符串中的交互式代码对函数、方法进行简单测试。  

### TDD步骤
1. 编写doctest
2. 执行doctest，观察失败
3. 编写使之通过的代码
4. 如果还有失败，检查失败原因
5. 如果是不合理的失败，不应编写太挑剔的doctest
6. 如果是失败，修正代码，返回步骤2

### 编写doctest
```python
'''
Module showing how doctests can be included with source code
Each '>>>' line is run as if in a python shell, and counts as a test.
The next line, if not '>>>' is the expected output of the previous line.
If anything doesn't match exactly (including trailing spaces), the test fails.
'''
 
def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
```
注意函数`multiply`中有两个交互式执行和结果。  
```python
F:\ABao\work\Python\files\test>python -m doctest unnecessary_math.py

F:\ABao\work\Python\files\test>python -m doctest -v unnecessary_math.py
Trying:
    multiply(4, 3)
Expecting:
    12
ok
Trying:
    multiply('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    unnecessary_math
1 items passed all tests:
   2 tests in unnecessary_math.multiply
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```
