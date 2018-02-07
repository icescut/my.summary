# 魔术方法
Python的多范式依赖于Python对象中的特殊方法(special method)。特殊方法名的前后各有两个下划线。特殊方法又被成为魔法方法(magic method)，定义了许多Python语法和表达方式。
谨记，python中一切皆对象。   

## 运算符
Python的运算符是通过调用对象的特殊方法实现的。  
```python
>>> "hello" + " world"
'hello world'
>>> "hello".__add__(" world")
'hello world'
```
在Python中，两个对象是否能进行加法运算，首先就要看相应的对象是否有__add__()方法。一旦相应的对象有__add__()方法，即使这个对象从数学上不可加，我们都可以用加法的形式，来表达obj.__add__()所定义的操作。在Python中，运算符起到简化书写的功能，但它依靠特殊方法实现。

运算符相关的魔术方法有如下几种：  
**二元运算符**  
如下为当调用对象为左操作数时，比如`a + b`相当于`a.__add__(b)`。
* `__add__(self, other)`            实现`+`
* `__sub__(self, other)`            实现`-`
* `__mul__(self, other)`            实现`*`
* `__matmul__(self, other)`         实现`@`？
* `__truediv__(self, other)`        实现`/`
* `__floordiv__(self, other)`       实现`//`
* `__mod__(self, other)`            实现`%`
* `__divmod__(self, other)`         实现`divmod()`
* `__pow__(self, other[, modulo])`  实现`**`
* `__lshift__(self, other)`         实现`<<`
* `__rshift__(self, other)`         实现`>>`
* `__and__(self, other)`            实现`&`
* `__xor__(self, other)`            实现`^`
* `__or__(self, other)`             实现`|`
当调用对象为右操作数，则魔术方法名为前面加上`r`，比如`a + b`相当于`b.__radd__(a)`，不过很少会这么用，内置类型似乎也没实现这种方式。  

## 上下文管理器
上下文管理器(context manager)用于规定某个对象的使用范围。一旦进入或者离开该使用范围，会有特殊操作被调用 (比如为对象分配或者释放内存)。它的语法形式是`with...as...`。  

```python
>>> with open('1.txt', 'w') as f:
	print(f.closed)

False
>>> print(f.closed)
True
>>> dir(f)
[...,'__enter__',...,'__exit__',...]
```

当我们使用上下文管理器的语法时，实际上要求Python在进入程序块之前调用对象的`__enter__()`方法，在结束程序块的时候调用`__exit__()`方法。

```python
>>> class A():
	def __init__(self, name):
		self.name = name
	def __enter__(self):
		self.name = 'Hello, ' + self.name
		return self
	def __exit__(self, exc_type, exc_value, trackback):
		self.name = self.name[7:]


>>> with A('Alan') as a:
	print(a.name)


Hello, Alan
>>> a.name
'Alan'
```

`__enter__()`返回一个对象。上下文管理器会使用这一对象作为`as`指的变量。  
`__exit__()`中有四个参数。当程序块中出现异常(exception)，`__exit__()`的参数中exc_type, exc_value, traceback用于描述异常。我们可以根据这三个参数进行相应的处理。如果正常运行结束，这三个参数都是None。
