# 基础

主要内容
* 引用
* 作用域
* 关键字
* 注释
* 表达式
* 语句
* 真值
* 分支
* 循环

## 引用
python中一切都是对象。不像C++，python的对象（包括int/float/str）等都是放在堆中，而变量名是对堆中的对象的引用。  

### 不可变对象
int/float/str/bool等基本对象及元组是不可变的，所以对这些对象的赋值是断开对旧值的引用，建立对新值的引用。  
缓冲机制，对于数字和短的字符串，不频繁建立删除，会有一个缓冲池，会引用缓冲池中的对象。  
```python
>>> a = 1
>>> b = 1
>>> a is b
True
```

### 可变对象
比如列表，其元素是可以修改的，所以对列表元素的修改并不会改变引用，只会对对象进行原地修改。  
```python
>>> a = [1, 2, 3]
>>> b = a
>>> a[1] = -2
>>> b
[1, -2, 3]
```

### 参数传递
python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。  
对于不可变对象，对参数的修改都只是改变参数的引用，不会修改到外面变量的引用。  
对可变对象，因为对其元素的修改是原地进行的，会对外面变量产生影响。  

## 作用域
作用域即函数、类、模块等对象中的变量，其生命周期只存在于函数、类、模块之内，当出了函数、类、模块就无法对其进行引用。  
```python
>>> def func():
	x = 6
	print('x in func:', str(x))


>>> func()
x in func: 6
>>> x
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x
NameError: name 'x' is not defined
```

不像C++，`for`循环内不会构成作用域。循环执行完后，还是可以使用变量。  
```python
>>> for k in range(4):
	print(k, end=' ')


0 1 2 3
>>> k
3
```
python中的作用域与JavaScript类似，但又有不同。
* 一个变量名字如果只使用不修改，则会先看有无本地变量，如果没有，再看其外部作用域有没有这个变量，如果没有，再看更多层的作用域，如果类推，与JavaScript的作用域链原理类似。  

```python
>>> a = 1
>>> def func():
	print(a)


>>> func()
1
>>> def func():
	a = 2
	def func2():
		print(a)
	func2()


>>> func()
2
```

* 但如果一个变量名字在函数中进行修改，则默认是本地变量。  

```python
>>> def func():
	a += 1


>>> func()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    func()
  File "<pyshell#30>", line 2, in func
    a += 1
UnboundLocalError: local variable 'a' referenced before assignment
```

### global
将变量声明为全局的，必须写在函数体的最开头。  
```python
>>> a = 1
>>> b = 2
>>> def func():
	global a, b
	print(a, b)


>>> func()
1 2
>>> def func():
	def func2():
		global a, b
		print(a, b)
	func2()


>>> func()
1 2
```

### nonlocal
将变量声明为非本地的，即外层作用域的变量。  
```python
>>> def func():
	a = 1; b = 2
	def func2():
		nonlocal a, b
		print(a, b)
	func2()


>>> func()
1 2
```

会引用最接近的外层作用域的变量。  
```python
>>> def func():
	a = 1; b = 2
	def func2():
		a = 3; b = 4
		def func3():
			nonlocal a, b
			print(a, b)
		func3()
	func2()


>>> func()
3 4
```

如果最接近的外层作用域的变量没有该名字，会引用再外一层的作用域，如果类推。  
```python
>>> def func():
	a = 1; b = 2
	def func2():
		def func3():
			nonlocal a, b
			print(a, b)
		func3()
	func2()


>>> func()
1 2
```

但是这个外层不能是全局。  
```python
>>> def func():
	nonlocal a

SyntaxError: no binding for nonlocal 'a' found
```

### locals
`locals()`函数返回当前使用域的本地变量。  
```python
>>> a = 1
>>> import pprint as p
>>> from pprint import pprint
>>> pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'a': 1,
 'pprint': <function pprint at 0x000001947D593E18>}
>>>
>>> def func():
	a = 2
	pprint(locals())


>>> func()
{'a': 2}
```

## 关键字

### 基本

#### del
`del`删除变量对对象的引用，然后删除变量，但是并不会删除所引用的变量。对象由自动垃圾回收机制删除。  

```python
>>> a = [1, 2, 3]
>>> b = a
>>> del a
>>> b
[1, 2, 3]
>>> a
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a
NameError: name 'a' is not defined
```

#### global
将作用域中的名字声明为全局的。  
#### is
用于身份判断。  

#### nonlocal
用于

## 注释
### 行注释
一般的注释为在前面加`#`，则该行后面的内容为注释。  
如需指明源代码使用`utf-8`编码，则在代码前面使用:
```python
# -*- coding: utf-8 -*-  
```

### 大段注释
python本身没有大段注释的语法。可以使用三引号进行大段注释，另外在函数或类的最开始使用三引号书写的注释称为文档字符串(docstring)。  
当函数或类作为`help`的参数时，文档字符串对被打印出来。  

```python
>>> def func():
	"""
	A test of Docstring.
	"""
	pass

>>> help(func)
Help on function func in module __main__:

func()
    A test of Docstring.
```

## 表达式
表达式单独使用不产生什么效果。  
```python
>>> 10 + 23
33
>>> 5 - 2
3
>>> 4
4
```
单独一个常量或变量也构成一个表达式。  

## 语句
语句会产生一些效果。比如赋值语句会改变变量的值，打印语句会打印东西到屏幕。
```python
>>> a = 5
>>> print(a)
5
```

**缩进与代码块**  
python使用缩进表示代码的层次，比如`if`或`def`后面的代码。一般用4个空格来进行缩进。  
缩进的内容为代码块（或称为复合语句），即当作一条语句看待，代码块不能为空，至少有一个语句。如果实在没想好，可以使用`pass`进行占位。  
```python
>>> name = input('your name:')
your name:Alan
>>> if name == 'Alan':
	print('Hello ', name)
	print('Welcome!')
else:
	pass

Hello  Alan
Welcome!
```

## 真值
一个对象通常作为`True`，除非其有`__bool__()`方法返回`False`或者`__len__()`方法返回0。  
如下对象作为False：
* False
* None
* 0
* 0.0
* 0j
* Decimal(0)
* Fraction(0, 1)
* ''
* ()
* []
* {}
* set()
* range(0)

## 分支
分支使程序选择执行哪部分代码。  
python中的分支语句只有`if`并没有其他语句常见的`switch`语句。  
```
                   +-------------------+
                   |                   |
>>--if--condition--v-------------------^--------------<<
                   |                   |  |        |
                   +--elif--condition--+  +--else--+
```

### if
`if`为复合语句，如果其后面的条件表达式结果为`True`则执行语句块中的内容。  
```python
>>> a = 1
>>> if a == 1:
	print('a == 1')


a == 1


>>> if a == 2:
	print('a == 2')


>>>
```

### else
`else`必须和`if`一起使用，表示当`if`的条件表达式结果为`False`时执行`else`语句块中的内容。  
```python
>>> a = 1
>>> if a == 2:
	print('in if')
else:
	print('in else')


in else
```

### elif
`elif`用于当前面的条件不满足时，再判断另外一个条件。`elif`必须放在`if`之后，`else`之前。`elif`可以有多个，并且顺序是很重要的。  
```python
>>> score = 75
>>> if score > 90:
	print('class A')
elif score > 80:
	print('class B')
elif score > 70:
	print('class C')
else:
	print('class D')


class C
```

### 嵌套条件
条件语句里面的语句块可以包含其他条件语句，并且支持多层嵌套。  
```python
>>> day = 'Sunday'
>>> ill = False
>>> rain = False
>>> if day == 'weekday':
	if ill:
		print('stay at home')
	else:
		print('go to work')
else:
	if ill or rain:
		print('stay at home')
	else:
		print('go outside')


go outside
```

## 循环
循环的含义是重复执行一段代码，当某个条件满足就会跑出循环。  

### while
`while`的使用方法为，当`while`后面的条件表达式结果为`True`时，语句块中的内容执行，否则不再循环，执行后面的内容。  
```python
>>> a = 1
>>> while a < 10:
	print(a, end=' ')
	a += 1


1 2 3 4 5 6 7 8 9
```

**无限循环**  
一般使用`while True`进行无限循环。  

### for
`for`语句用于对一个可迭代对象中的所有元素按顺序执行语句块。  
```python
>>> x = ['a', 'b', 'c', 'd']
>>> for i in x:
	print(i, end=' ')


a b c d
```
如果想实现传统C语言那种for循环，那么使用`range`和`len`函数进行配合就行。  
```python
>>> for i in range(len(x)):
	print(x[i], end=' ')


a b c d
```

### break
使用`break`语句不再执行循环体中的内容，马上跳转到循环后面的第一条语句。  

```python
>>> while True:
	if a == 5:
		break
	print(a, end=' ')
	a += 1


1 2 3 4
```

### continue
使用`continue`语句不再执行循环体中的内容，马上跳转到循环的条件表达式语句。

```python
>>> a = 0
>>> while a < 10:
	a += 1
	if a % 2 == 0:
		continue
	print(a, end=' ')


1 3 5 7 9
```

### else
当`break`语句没有执行时，执行`else`语句中的内容。  
```python
>>> a = 0
>>> while a < 10:
	a += 2
	if a == 3:
		break
	print(a, end=' ')
else:
	print('no break')


2 4 6 8 10 no break
>>> a = 1
>>> while a < 10:
	a += 2
	if a == 7:
		break
	print(a, end=' ')
else:
	print('no break')


3 5
```

### 循环字典
可以直接对字典对象使用`for`循环，此时返回的值是键值。字典元素是无序的。    

```python
>>> for k in man:
	print(k)


name
age
home
```

如果只需要循环字典的值，使用`values()`方法。  
```python
>>> for v in man.values():
	print(v)


Alan
32
China
```

如果需要循环字典的键值对，使用`items()`方法。  
```python
>>> for k, v in man.items():
	print(k, v)


name Alan
age 32
home China
```
