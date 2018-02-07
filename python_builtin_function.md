# python内置函数

大纲：
* 类型
* 反省
* 辅助功能
* 循环增加
* 函数式
* 数学函数
* 其余

## 类型

### int
返回一个整型，如果是参数是浮点型则截断所有小数位，如果是字符型，则转换为整型，如果没有参数则返回0。  
```python
>>> int(5)
5
>>> int(3.4)
3
>>> int('22.5')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int('22.5')
ValueError: invalid literal for int() with base 10: '22.5'
>>> int('22')
22
>>> int()
0
```

将二、八、十六进制字符串转换为十进制数字，可以使用第二个参数。  
```python
>>> int('010', 8)
8
>>> int('0x3b', 16)
59
>>> int('0b1101', 2)
13
>>>
```

### str
将一个对象转换为字符串。如果没有参数，则返回一个空字符串。  
```python
>>> str(45)
'45'
>>> str([1, 2, 3])
'[1, 2, 3]'
>>> str({'name': 'Alan', 'age':32})
"{'name': 'Alan', 'age': 32}"
>>> str()
''
>>>
```

### bool
返回布尔值。  
```python
>>> bool('False')
True
>>> bool('')
False
>>>
```

### list
创建一个列表。  
* 以可迭代对象作为参数。  
* 无参数则为创建空列表。

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list()
[]
```

### set
创建一个集合。  
* 以可迭代对象作为参数。  
* 无参数则为创建空集合。
```python
>>> set([1, 2, 3, 2, 3, 4])
{1, 2, 3, 4}
>>> set()
set()
>>>
```

## 反省

### hasattr
判断一个对象是否有某个属性，第一个参数为对象，第二个参数为属性的名字字符串。   
```python
>>> s = 'abc'
>>> hasattr(s, 'index')
True
>>> hasattr(s, 'nosuchattr')
False
>>>
```

### type
* `type(object)`只有一个参数，返回对象的类型。  
* `type(name, bases, dict)`三个参数，如`class`语句类似，创建一个类，`name`为类名，成为`__name__`属性；`bases`为父类，成为`__bases__`属性；`dict`为类成员，成为`__dict__`属性。  
```python
>>> a = 10
>>> type(a)
<class 'int'>
>>> A = type('A', (object,), dict(a=1,sum=lambda x, y: x + y))
>>> type(A)
<class 'type'>
>>> A.a
1
>>> A.sum(2, 3)
5
>>>
```

### vars
返回一个对象的`__dict__`，即对象的所有属性的列表。如果没有参数就所同`locals`返回的值一样。  
```python
>>> class A():
	x = 1
	y = 2
	def __init__(self, a, b):
		self.a = a
		self.b = b

>>> a = A(8, 9)
>>> vars(a)
{'a': 8, 'b': 9}
>>> a.__dict__
{'a': 8, 'b': 9}
>>>
```

### locals
以字典形式返回当前命名空间的本地变量。  
```python
>>> def func(x, y):
	a = 10
	b = 11
	print(locals())

>>> func(1, 2)
{'b': 11, 'a': 10, 'y': 2, 'x': 1}
```

### isinstance
判断一个对象是否是一个类的实例，子类也是。  
```python
>>> isinstance(a, int)
True
>>> isinstance(a, object)
True
```

### insubclass
判断一个类是否是一个类的子类（直接或间接）。  
```python
>>> class A(): pass

>>> class B(A): pass

>>> class C(B): pass

>>> issubclass(B, A)
True
>>> issubclass(C, A)
True
```

### dir
* 没有参数，返回当前作用域的对象。  
* 有参数，返回该对象的所有属性。  

```python
>>> from pprint import pprint
>>> pprint(dir())
['__annotations__',
 '__builtins__',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'pprint']
>>> pprint(dir(pprint))
['__annotations__',
 '__call__',
 '__class__',
 '__closure__',
 '__code__',
 '__defaults__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__get__',
 '__getattribute__',
 '__globals__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__kwdefaults__',
 '__le__',
 '__lt__',
 '__module__',
 '__name__',
 '__ne__',
 '__new__',
 '__qualname__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']
>>> class Shape:
	def __dir__(self):
		return ['area', 'perimeter', 'location']

>>> dir(Shape())
['area', 'location', 'perimeter']
```

## 辅助功能

### all
传入一个可迭代对象，如果所有元素都等于True或可迭代对象为空，则返回True。  
```python
>>> lst = [1, 2, 3]
>>> all(lst)
True
>>> lst = [1, 2, 0]
>>> all(lst)
False
>>> lst = []
>>> all(lst)
True
>>>
```

### any
传入一个可迭代对象，如果有一个元素等于True，则返回True。如果可迭代对象为空，返回False
```python
>>> lst = [1, 2, 3]
>>> any(lst)
True
>>> lst = [0, 0, '']
>>> any(lst)
False
>>> lst = []
>>> any(lst)
False
>>>
```

### len
返回对象的长度，一般指容器对象中元素的个数。  
```python
>>> lst = [1, 5, 7]
>>> len(lst)
3
>>>
```

如果对象有定义`__dir__`方法，则返回这个方法返回的列表。  

### help
返回帮助信息，与文档字符串相关。  

### id
返回一个对象的内存地址。  
```python
>>> a = 10
>>> id(a)
1702409568
>>> hex(id(a))
'0x6578b560'
```

## 循环增加

### enumerate
传入一个可迭代对象，返回一个enumerate对象，该对象相当于一个列表，列表中的元素为元组，元组只有两个元素，第一个元素为序号（如果不设置则从0开始），第二个元素为可迭代对象中的元素。  
```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
>>>
```


## 函数式

### map
对传入的可迭代对象依次执行传入的函数，然后返回相应的可迭代对象。  
```python
>>> it = map(lambda x: x ** 2, range(5))
>>> it
<map object at 0x0000021AB90C6278>
>>> list(it)
[0, 1, 4, 9, 16]
```

### filter
对传入的可迭代对象依次执行传入的函数，如果返回True保留，然后返回相应的可迭代对象。  
```python
>>> it = filter(lambda x: x % 2 == 0, range(10))
>>> list(it)
[0, 2, 4, 6, 8]
>>>
```

## 数学函数

### abs
返回一个数值的绝对值。  
```python
>>> abs(-34)
34
>>> abs(-3.21)
3.21
>>> abs(34.2)
34.2
```

### divmod
返回商及余数。  
```python
>>> divmod(9,2)
(4, 1)
>>> divmod(7.6, 2.3)
(3.0, 0.7000000000000002)
```
对于整数，其结果相当于`(a // b, a % b)`，对于浮点数，其结果相当于`(math.floor(a, b), a % b)`

### hex
返回一个整型的16进制，以`0x`开头，如果一个对象不是整型，则必须有一个`__index__`方法，返回一个整型。  
```python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
>>>
```

### min
返回最小值，参数可以是两个以上的可比较大小的对象或是一个可迭代对象。  
```python
>>> min(4, -2, 8, 99, 0)
-2
>>> lst = [4, -2, 8, 99, 0]
>>> min(lst)
-2
```

### max
返回最大值，参数可以是两个以上的可比较大小的对象或是一个可迭代对象。  
```python
>>> max(4, -2, 8, 99, 0)
99
>>> lst = [4, -2, 8, 99, 0]
>>> max(lst)
99
```  
