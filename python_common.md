# python基本约定

大纲：
* 下划线


## 下划线
python对象下划线有一些约定的用法。  

### 单下划线

* 在解释器中作为上一条执行的结果。  

```python
>>> 1 + 2
3
>>> _
3
```

* 作为一个不需要用到的名称，只作占位用途。  

```python
>>> year, _, date, hours, *_ = (2018, 1, 7, 16, 4, 30)
>>> year
2018
>>> hours
16
```

* 国际化，”_“会被作为一个函数来使用。这种情况下，它通常用于实现国际化和本地化字符串之间翻译查找的函数名称。

* 名称前的单下划线，用于指定该名称属性为“私有”。以“_”开头的名称都不会被导入，除非模块或包中的“__all__”列表显式地包含了它们。

比如在`underscore.py`中定义两个属性。  
```python
attr1 = 10
_attr2 = 20

```
如果使用`from 模块名 import *`能够引用`attr1`，但无法引用`_attr2`。
```python
>>> from underscore import *
>>> attr1
10
>>> _attr2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_attr2' is not defined
```

比如在`underscore.py`中加上`__all__`定义。  
```python
attr1 = 10
_attr2 = 20
__all__ = ['attr1', '_attr2']
```
这时就可以引用`_attr2`了。
```python
>>> from underscore import *
>>> attr1
10
>>> _attr2
20
```

### 双下划线
* 名称前的双下划线用于表示类元素为"私有"，可以用于避免与子类名称冲突。  

```python  
>> class A():
	def method1(self):
		print('call method1')
	def _method2(self):
		print('call _method2')
	def __method3(self):
		print('call __method3')


>>> a = A()
>>> a.method1()
call method1
>>> a._method2()
call _method2
>>> a.__method3()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.__method3()
AttributeError: 'A' object has no attribute '__method3'
>>> dir(a)
['_A__method3', ..., '_method2', 'method1']
>>> a._A__method3()
call __method3
```
元素通过`__method3`调用双下划线开头的方法，但实际上可以通过`_类名__method3`的方式调用，所以说也并不是完全隐藏了，这要靠程序员遵守规则。  

* 名称前后的双下划线，这种用法表示python中的魔术方法。

  * 魔术方法不是私有的，可以直接调用
  * 不要自已创造名称前后有双下划线的方法，只能使用约定的这些方法。
