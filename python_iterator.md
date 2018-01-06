## 可迭代对象(iterable)
可迭代对象和容器一样是一种通俗的叫法，并不是指某种具体的数据类型。  
一个对象定义了可以返回一个迭代器的`__iter__`方法，或者定义了可以支持下标索引的`__getitem__`方法，那么它就是一个可迭代对象。  
Python中经常使用`for`来对某个对象进行遍历，此时被遍历的这个对象就是可迭代对象，像常见的列表、元组都是。  

## 迭代器(iterator)
一个对象实现了如下两个协议则为迭代器：  
1. 定义了`__iter__()`方法，用于返回自身。
2. 定义了`__next__()`方法，用于访问下一个元素，当没有下一个元素的时候返回一个`StopIteration`异常。  

迭代器内部持有一个状态，该状态用于记录当前迭代所在的位置，以方便下次迭代的时候获取正确的元素。  

```python
>>> s = "hi"
>>> it = iter(s)
>>> it.__next__()
'h'
>>> next(it)
'i'
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    next(it)
StopIteration
```

对于可迭代（iterable）对象，可以通过内置的`iter()`函数来获取相应的迭代器对象。   
除了使用`__next__()`方法得到下一个元素，还可以使用内置函数`next()`。  

**修改敏感**  
迭代器对对象的修改敏感，一般不要在遍历的时候修改对象。  
```python
>>> l = [1, 2, 3, 4, 5]
>>> for i in l:
	print(i)
	l.remove(i)

1
3
5
```

**判断迭代器**   
* 使用内置函数`isinstance`判断是否迭代器。
* 可迭代对象`Iterable`和迭代器`Iterator`来自`collections`包

```python
>>> s = "hi"
>>> it = iter(s)
>>> from collections import Iterator, Iterable
>>> isinstance(s, Iterator)
False
>>> isinstance(it, Iterator)
True
>>> isinstance(s, Iterable)
True
>>> isinstance(it, Iterable)
True
```

**迭代器的限制**    
*	只能往下移动
*	不能回到开始
*	也无法复制一个迭代器，因此要再次进行迭代只能重新生成一个新的迭代器对象。

```python
>>> it = iter(range(5))
>>> for i in it:
	print(i)

0
1
2
3
4
>>> for i in it:
	print(i)

>>>
```

正因为这样，容器并没实现为简单的迭代器，而是实现为可迭代对象，使可迭代对象与迭代器分开。  
```python
>>> class ListIterable():
    def __init__(self, data):
        self.__data = data

    def __iter__(self):
        print("call itrable __iter__().")
        return ListIterator(self.__data)

>>> class ListIterator():
    def __init__(self, data):
        self.__data = data
        self.__pos = 0

    def __iter__(self):
        print("call iterator __iter__().")
        return self

    def __next__(self):
        print("call iterator __next__().")
        if self.__pos < len(self.__data):
            val = self.__data[self.__pos]
            self.__pos += 1
            return val
        else:
            raise StopIteration

>>> a = ListIterable([1,2,4,5,6])
>>> b = iter(a)
call itrable __iter__().
>>> a
<__main__.ListIterable object at 0x000001B0DD3F7BA8>
>>> b
<__main__.ListIterator object at 0x000001B0DD386198>
>>> [i for i in a]
call itrable __iter__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
[1, 2, 4, 5, 6]
>>> [i for i in a]
call itrable __iter__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
call iterator __next__().
[1, 2, 4, 5, 6]
```

## 生成器(generator)
生成器其实是一种特殊的迭代器，不过这种迭代器更加优雅。它不需要再像上面的类一样写`__iter__()`和`__next__()`方法了，只需要一个`yield`关键字。生成器一定是迭代器（反之不成立），生成器自动实现迭代器协议。  
生成器最大的好处是只有在需要的时候才产生结果，所以会节省大量的空间。  

Python有两种不同方式提供生成器：  
1. **生成器函数**：几乎与普通函数一样，但是使用`yield`语句而不是`return`语句返回结果。`yield`语句一次返回一个结果，然后**状态挂起**，下次从离开它的地方重新开始执行。生成器函数请用返回的对象即为生成器。  
2. **生成器推导式**：类似于列表推导式，但是按需返回结果，而不是一次构造所有结果。  

注意生成器只能遍历一次。  


### 生成器函数
比如返回平方数：
```python
>>> def squares(n):
	for i in range(n):
		yield i ** 2

>>> for i in squares(3):
	print(i, end="\t")


0	1	4
```
如果使用普通函数：
```python
>>> def squares(n):
	res = []
	for i in range(n):
		res.append(i ** 2)
	return res

>>> for i in squares(3):
	print(i, end="\t")


0	1	4
```
需要更多代码，也占用更多空间。

### 生成器推导式
使用列表推导式，一次产生所有结果：
```python
>>> squares = [x ** 2 for x in range(3)]
>>> squares
[0, 1, 4]
```
生成器推导式则只需将中括号替换为小括号。
```python
>>> squares = (x ** 2 for x in range(3))
>>> squares
<generator object <genexpr> at 0x00000231F40F6258>
>>> for x in squares:
	print(x, end="\t")


0	1	4
```

### range
Python 2中`range`创建列表，`xrange`创建生成器。Python 3中已经没有`xrange` ，而`range`相当于python 2中`xrange`。   
