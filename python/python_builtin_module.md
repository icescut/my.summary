# python内置模块

大纲：
* pprint
* copy

## pprint
pprint模块能够比print打印得更加好看。实际上print只是在一行中打印。  

### PrettyPrinter类
PrettyPrinter是一个类，创建类时设定打印的喜好设置，然后使用`pprint`方法进行打印。  
```python
>>> import pprint
>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> stuff.insert(0, stuff[:])
>>> pp = pprint.PrettyPrinter(indent=8)
>>> pp.pprint(stuff)
[       ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
        'spam',
        'eggs',
        'lumberjack',
        'knights',
        'ni']
>>> pp = pprint.PrettyPrinter(width=50, compact=True)
>>> pp.pprint(stuff)
[['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
 'spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot', ('fresh fruit',))))))))
>>> pp = pprint.PrettyPrinter(depth=4)
>>> pp.pprint(tup)
('spam', ('eggs', ('lumberjack', ('knights', (...)))))
```

* indent 缩进位数
* width 一行最大长度
* depth 最大层数，超出则用`...`表示
* compact 压缩，默认是不压缩，即遇到逗号会断行

### pprint与pformat函数
`pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False)`
实际上省去上创建PrettyPrinter的麻烦，但不可重用设定的格式。  

pformat的使用方式与pprint一样，只是pformat是返回一个字符串而不是打印出来。  

## copy
python的赋值语句并不会复制对象，只是将名字指向对象。  
对于容器这些可变对象，使用copy模块来复制一份新的内存是很有用的。  

### copy函数
使用`copy`函数进行浅复制。   
一般的赋值并不会开辟新的内存，只是指向同一块内存。  
```python
>>> x = [1, 2, 3]
>>> y = x
>>> id(x)
2426214238280
>>> id(y)
2426214238280
>>> x[0] = -1
>>> x
[-1, 2, 3]
>>> y
[-1, 2, 3]
```
使用`copy`函数则会新开一块内存。  
```python
>>> x = [1, 2, 3]
>>> from copy import copy, deepcopy
>>> y = copy(x)
>>> id(x)
2426214029640
>>> id(y)
2426214238408
>>> x[0] = -1
>>> x
[-1, 2, 3]
>>> y
[1, 2, 3]
```
但是对于对象中的元素、属性复制的仍然是引用，不会新开内存。  
```python
>>> x = [1, [2, 3, 4], 5, 6]
>>> y = copy(x)
>>> x[1][1] = -3
>>> x
[1, [2, -3, 4], 5, 6]
>>> y
[1, [2, -3, 4], 5, 6]
```
如同下图，x和y实际是共享其中的子列表`[2, 3, 4]`：
```
x                  y
[1]               [1]
[lst] --> [2] <-- [lst]
          [3]
          [4]
[5]               [5]
[6]               [6]
```

### deepcopy函数
`deepcopy`即为深复制。对于对象其中的元素或函数也会拷贝一份，不会发生上面的浅复制的情况。  

```python
>>> x = [1, [2, 3, 4], 5, 6]
>>> y = deepcopy(x)
>>> x[1][1] = -3
>>> x
[1, [2, -3, 4], 5, 6]
>>> y
[1, [2, 3, 4], 5, 6]
>>>
```
