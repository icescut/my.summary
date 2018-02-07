# 类

大纲：
* 成员
* 方法
* 属性
* 抽象类
* MRO

参考：
* [Python进阶之“属性（property）”详解](http://python.jobbole.com/80955/)
* [Python的方法解析顺序(MRO)](http://hanjianwei.com/2013/07/25/python-mro/)

## 成员
Python类中的成员有一套统一的管理方案。  

### 类成员
对象的成员可能来自于其类定义，叫做类成员。类成员可能来自类定义自身，也可能根据类定义继承来的。  

```python
>>> class Person():
	name = 'one man'

>>> print(Person.__dict__)
{'__module__': '__main__', 'name': 'one man', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
>>> print(Person.__dict__['name'])
one man
```
类的`__dict__`属性保存自己的所有成员，是一个字典，键为成员名，值为成员值。还包含了一些默认的成员。但是如果有继承，不会有父类的成员。  

```python
>>> class Programmer(Person):
	lang='Python'

>>> print(Programmer.__dict__)
{'__module__': '__main__', 'lang': 'Python', '__doc__': None}
```

既可以通过类名来引用类成员，也可以通过其实例来引用类成员（不推荐）。  
```python
>>> Person.name
'one man'
>>> a = Person()
>>> a.name
'one man'
```

### 实例成员
为每个实例自己所有的成员。  
```python
>>> class Kls():
	def __init__(self, data):
		self.data = data
	def get_data(self):
		return self.data
>>> a = Kls(5)
>>> b = Kls(10)
>>> a.get_data()
5
>>> b.get_data()
10
>>> a.data
5
>>> b.data
10
>>>
```

实例成员一般在`__init__`中可预先定义中，在类定义里面使用`self.`前缀来引用，在类外则通过实例名字来引用。  

### 私有成员
私有成员以`__`开头，只有在类内部使用，无法在类外部或子类中使用。  
```python
>>> class Kls():
	__name = 'Alan'
	def __init__(self, data):
		self.__data = data
	def get_data(self):
		return self.__data
	@classmethod
	def get_name(cls):
		return cls.__name

>>> a = Kls(888)
>>> a.get_data()
888
>>> a.get_name()
'Alan'
>>> a.__data
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.__data
AttributeError: 'Kls' object has no attribute '__data'
>>> a.__name
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.__name
AttributeError: 'Kls' object has no attribute '__name'
```
可以通过`_类名__私有成员`的方式访问私有成员，但最好不好这样。  
```python
>>> a._Kls__data
888
>>> a._Kls__name
'Alan'
```

## 方法
方法为对象可以执行的动作。  

### 实例方法
在特定实例上执行的方法，无法访问类成员。实例方法第一个参数必须是`self`，用于在调用时接收实例对象本身。    
```python
>>> class Kls():
	def __init__(self, data):
		self.data = data
	def print_data(self):
		print(self.data)

>>> a = Kls(999)
>>> a.print_data()
999
```

### 类方法
类方法是针对类层面调用的方法，类型方法只能访问类成员，不能访问实例成员。类方法需要用`@classmethod`来修饰。可以通过实例来调用类方法，但不推荐。类方法第一个参数必须是`cls`，在调用时传入类本身。  
```python
>>> class Kls():
	name = 'Kls'
	def __init__(self, data):
		self.data = data
	def print_data(self):
		print(self.data)
	@classmethod
	def print_name(cls):
		print(cls.name)

>>> a = Kls(999)
>>> Kls.print_name()
Kls
>>> a.print_name()
Kls
```

### 静态方法
静态方法与类成员及实例成员都没有关系，一般用于实现辅助功能。使用`@staticmethod`来修饰静态方法。  
```python
>>> class Kls():
	@staticmethod
	def sum(a, b):
		return a + b

>>> k = Kls()
>>> k.sum(4, 5)
9
>>> Kls.sum(5, 6)
11
```

## 属性
属性用于对内部数据进行一个封装。并且可以检测输入数据的有效性和格式化输出数据。  

### 使用装饰器
使用`@property`定义一个只读属性。  
```python
>>> class Person():
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return self._first_name + ' ' + self._last_name

>>> p = Person('Liang', 'Alan')
>>> p.full_name
'Liang Alan'
>>> p.full_name = 'Mo Darcy'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    p.full_name = 'Mo Darcy'
AttributeError: can't set attribute
```

定义写属性，则需要一个`@属性名.setter`装饰器。   
```python
>>> class Person():
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return self._first_name + ' ' + self._last_name

    @full_name.setter
    def full_name(self, full_name):
        self._first_name, self._last_name = full_name.split(' ')


>>> p = Person('Liang', 'Alan')
>>> p.full_name
'Liang Alan'
>>> p.full_name = 'Mo Darcy'
>>> p.full_name
'Mo Darcy'
```
使用`@属性名.delter`装饰器定义删除操作。  
```python
>>> class Person():
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return self._first_name + ' ' + self._last_name

    @full_name.setter
    def full_name(self, full_name):
        self._first_name, self._last_name = full_name.split(' ')

    @full_name.deleter
    def full_name(self):
        self._first_name, self._last_name = '', ''


>>> p = Person('Liang', 'Alan')
>>> p.full_name
'Liang Alan'
>>> del p.full_name

>>> p.full_name
' '
```

### 使用属性函数
使用`property`函数依次传入getter、setter、delter、docstring，从而创建一个属性。属性函数用于在遗留代码中的创建属性会比使用装饰器方便。  
```python
>>> class Person():
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_full_name(self):
        return self._first_name + ' ' + self._last_name

    def set_full_name(self, full_name):
        self._first_name, self._last_name = full_name.split(' ')

    full_name = property(get_full_name, set_full_name, None, 'full name of Person')


>>> p = Person('Liang', 'Alan')
>>> p.full_name
'Liang Alan'
>>> p.full_name = 'Mo Darcy'
>>> p.full_name
'Mo Darcy'
```

## 抽象类
python本身没有抽象类或接口的概念，如果要实现需要借助`abc`模块。  

### abc
使用`abc`模块实现抽象类及抽象方法。abc是Abstract Base Classes的缩写。  
通过`metaclass=ABCMeta`来声明类为抽象类。抽象类如果没有抽象方法是可以实例化的。  
```python
>>> from abc import *
>>> class MyABC(metaclass=ABCMeta):
	pass

>>> c = MyABC()
```

使用装饰器`@abstractmethod`来声明一个方法为抽象方法。  
```python
>>> class Animal(metaclass=ABCMeta):
	@abstractmethod
	def move(self):
		pass


>>> a = Animal()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a = Animal()
TypeError: Can't instantiate abstract class Animal with abstract methods move
>>> class Cat(Animal):
	pass

>>> c = Cat()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    c = Cat()
TypeError: Can't instantiate abstract class Cat with abstract methods move
>>> class Dog(Animal):
	def move(self):
		print('walk')


>>> d = Dog()
>>> d.move()
walk
```
如果有抽象方法没有实现，则不能实例化。  

### 注册具体类
前面是通过子类化来实现抽象类，也可以通过注册的方式来实现。  
```python
>>> class Fish():
	def move(self, speed):
		print('swin', speed)


>>> Animal.register(Fish)
<class '__main__.Fish'>
>>> issubclass(Fish, Animal)
True
>>> f = Fish()
>>> isinstance(f, Animal)
True
>>> f.move('fast')
swin fast
```

通过注册方法实现的类并不会出现在抽象类的`__subclasses__()`中。  
```python
>>> for sub_class in Animal.__subclasses__():
	print(sub_class)


<class '__main__.Cat'>
<class '__main__.Dog'>
>>>
```

### __subclasshook__
使用`__subclasshook__`能够自动将实现了抽象类相同方法的类认定为抽象类的子类。  
```python
>>> class Animal(metaclass=ABCMeta):
	@abstractmethod
	def move(self):
		pass
	@classmethod
	def __subclasshook__(cls, C):
		if cls is Animal:
			if any("move" in B.__dict__ for B in C.__mro__):
				return True
		return NotImplemented


>>> class Cat():
	def move(self):
		print('walk')


>>> issubclass(Cat, Animal)
True
>>> c = Cat()
>>> isinstance(c, Animal)
True
>>> Animal.__subclasshook__(Cat)
True
```
实际是通过`__mro__`来查找该类的方法中有没有与抽象方法同名的，如果有则认定为实现了该抽象类。  

### 抽象属性
抽象类中用`@abstractmethod`声明抽象属性，实现类中必须使用`@property`声明有实现这个属性。3.3之前使用`@abstractproperty`。  
```python
>>> class Animal(metaclass=ABCMeta):
    @property
    @abstractmethod
    def weight(self):
        return str(self._weight) + ' kilogram'


    def __init__(self, weight):
        self._weight = weight


>>> class Cat(Animal):
    def __init__(self, weight):
        super().__init__(weight)

    @property
    def weight(self):
        return str(self._weight) + ' kilogram'

>>> a = Animal()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a = Animal()
TypeError: Can't instantiate abstract class Animal with abstract methods weight
>>> c = Cat()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c = Cat()
TypeError: __init__() missing 1 required positional argument: 'weight'


>>> a = Animal(10)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a = Animal(10)
TypeError: Can't instantiate abstract class Animal with abstract methods weight
>>> c = Cat(10)
>>> c.weight
'10 kilogram'
```

另外3.3之前还有`@abstractclassmethod`和`@abstractstaticmethod`，现时都已废弃，只需在写`@classmethod`或`@staticmethod`的同时加上`@abstractmethod`即可。  
```python
>>> class A(metaclass=ABCMeta):
	@classmethod
	@abstractmethod
	def func1(cls):
		pass
	@staticmethod
	@abstractmethod
	def func2():
		pass


>>> class B(A):
	@classmethod
	def func1(cls):
		print(cls.__name__)
	@staticmethod
	def func2(name):
		print('hello' + name)


>>> b = B()
>>> B.func1()
B
>>> B.func2('Alan')
helloAlan
```

## MRO
MRO（Method Resolution Order）：方法解析顺序。  
Python语言包含了很多优秀的特性，其中多重继承就是其中之一，但是多重继承会引发很多问题，比如二义性，Python中一切皆引用，这使得他不会像C++一样使用虚基类处理基类对象重复的问题，但是如果父类存在同名函数的时候还是会产生二义性，Python中处理这种问题的方法就是MRO。  

### 经典类
经典类中的MRO使用的是深度优先搜索(DFS)。如果一个父类重复出现在路径中，取第一次出现的。如下例：    
```
D     E
|     |
B     C
|     |
+-----+
   |
   A
```
顺序为`A-->B-->D-->C-->E`。  
```python
>>> class D:
    pass
>>> class E:
    pass
>>> class B(D):
    pass
>>> class C(E):
    pass
>>> class A(B, C):
    pass
>>> pprint(inspect.getmro(A))
(
<class __main__.A at 0x0000000003AD0528>,
 <class __main__.B at 0x0000000003AC4F48>,
 <class __main__.D at 0x0000000003AC4CA8>,
 <class __main__.C at 0x0000000003AC4FA8>,
 <class __main__.E at 0x0000000003AC4D08>)
```

经典类中的MRO主要问题在于菱形继承，新式类出现后，类必然有一个object父类，导致菱形继承的问题大机率出现，所以新式类不再采用这种方法。  
```
   D
   |
+--+--+
|     |
B     C
|     |
+-----+
   |
   A
```
在python2的经典类中的MRO顺序是这样的：
```python
>>> class D:
    pass
>>> class C(D):
    pass
>>> class B(D):
    pass
>>> class A(B, C):
    pass
		>>> pprint(inspect.getmro(A))
		(<class __main__.A at 0x0000000003AC4B28>,
		 <class __main__.B at 0x0000000003AC48E8>,
		 <class __main__.D at 0x0000000003AC4A68>,
		 <class __main__.C at 0x0000000003AC4C48>)
```
过程为`A-->B-->D-->C-->D`，因为取第一次出现的D，所以为`A-->B-->D-->C`

### 新式类
Python 2.2的新式类 MRO 计算方式和经典类 MRO 的计算方式非常相似：它仍然采用从左至右的深度优先遍历，但是如果遍历中出现重复的类，只保留最后一个。
```
  object
   |
   D
   |
+--+--+
|     |
B     C
|     |
+-----+
   |
   A
```
过程为`A-->B-->D-->object-->C-->D-->object`，保留最后一次出现`A-->B-->C-->D-->object`。  
```python
>>> class D(object):
    pass
>>> class B(D):
    pass
>>>
>>> class C(D):
    pass
>>> class A(B, C):
    pass
>>> pprint(A.__mro__)
(<class '__main__.A'>,
 <class '__main__.B'>,
 <class '__main__.C'>,
 <class '__main__.D'>,
 <type 'object'>)
```
但是新式类的mro没有解决二义性的问题。  
比如下图：
```
object
   |
+--+--+
|     |
X     Y
|     |
+--+--+
   |
+--+--+
|     |
A     B
|     |
+-----+
   |
   C
```
其中A(X,Y)，B(Y,X)。
```python
>>> class X(object): pass
>>> class Y(object): pass
>>> class A(X,Y):pass
>>> class B(Y,X):pass
>>> class C(A,B):pass
```
首先进行深度遍历，结果为 [C, A, X, object, Y, object, B, Y, object, X, object]；然后，只保留重复元素的最后一个，结果为 [C, A, B, Y, X, object]。Python 2.2 在实现该方法的时候进行了调整，使其更尊重基类中类出现的顺序，其实际结果为 [C, A, B, X, Y, object]。  
对于 A 来说，其搜索顺序为[A, X, Y, object]；对于 B，其搜索顺序为 [B, Y, X, object]；对于 C，其搜索顺序为[C, A, B, X, Y, object]。我们会发现，B 和 C 中 X、Y 的搜索顺序是相反的！也就是说，当 B 被继承时，它本身的行为竟然也发生了改变，这很容易导致不易察觉的错误。

### C3
所以从python 2.3之后采用了C3算法，并禁止创建二义性的继承。  
```python
>>> class X(object): pass
>>> class Y(object): pass
>>> class A(X,Y):pass
>>> class B(Y,X):pass
>>> class C(A,B):pass
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    class C(A,B):pass
TypeError: Error when calling the metaclass bases
    Cannot create a consistent method resolution
order (MRO) for bases Y, X
```

我们把类 C 的线性化（MRO）记为 L[C] = [C1, C2,…,CN]。其中 C1 称为 L[C] 的**头**，其余元素 [C2,…,CN] 称为**尾**。如果一个类 C 继承自基类 B1、B2、……、BN，那么我们可以根据以下两步计算出 L[C]：
> L[object]
> L[C(B1,...,BN)] = [C] + merge(L(B1),...,L(BN),[B1],...,[BN])

merge的算法是：
1. 检查第一个列表的头元素（如 L[B1] 的头），记作 H。
2. 若 H 未出现在其它列表的尾部，则将其输出，并将其从所有列表中删除，然后回到步骤1；否则，取出下一个列表的头部记作 H，继续该步骤。
3. 重复上述步骤，直至列表为空或者不能再找出可以输出的元素。如果是前一种情况，则算法结束；如果是后一种情况，说明无法构建继承关系，Python 会抛出异常。

分析一下：
```
object
   |
+--+--+
|     |
B     C
|     |
+-----+
   |
   A

L[A] = [A] + merge(L[B],L[C],[B],[C])
     = [A] + merge([B, object], [C, object], [B], [C])
		 = [A] + [B] + merge([object], [C, object], [C])
		 = [A] + [B] + [C] + merge([object], [object])
		 = [A] + [B] + [C] + [object]
```
上面的情况：
```
object
   |
+--+--+
|     |
X     Y
|     |
+--+--+
   |
+--+--+
|     |
A     B
|     |
+-----+
   |
   C
L[C] = [C] + merge(L[A], L[B], [A], [B])
     = [C] + merge([A] + merge(L[X], L[Y], [X], [Y]), [B] + merge(L[Y], L[X], [Y], [X]), [A], [B])
		 = [C] + merge([A, X, Y, object], [B, Y, X, object], [A], [B])
		 = [C, A] + merge([X, Y ,object], [B, Y, X, object], [B])
		 = [C, A, B] + merge([X, Y, object], [Y, X, object])
		 这时无论X还是Y都不符合未出现在其他列表的尾部。
```
