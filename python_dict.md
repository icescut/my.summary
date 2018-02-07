# 字典
字典是一种由键值对组成的数据结构。正如其义，如同一本字典，可以根据字找到相应的页数，进而快速地查找。  

大纲：
* 定义字典
* 键
* 增
* 删
* 改
* 查
* 遍历字典
* 字典推导式

## 定义字典
有两种方式定义字典。  
使用`{}`定义字典时，使用`:`使用键与值，使用`,`分隔两对键值。  
使用`dict`定义字典时可以使用一个两个元素的元组的列表或名值对或`{}`定义的字典。  
```python
>>> d = {'name' : 'Alan', 'age' : 32}
>>> d
{'name': 'Alan', 'age': 32}
>>> d = dict([('name', 'Darcy'),('age', 30)])
>>> d
{'name': 'Darcy', 'age': 30}
>>> d = dict(name='Mie', age=3)
>>> d
{'name': 'Mie', 'age': 3}
>>> d = dict({'name':'Qi', 'age':60})
>>> d
{'name': 'Qi', 'age': 60}
```

### 空字典
使用`{}`或`dict()`定义空字典。  
```python
>>> d = {}
>>> d
{}
>>> d = dict()
>>> d
{}
```

## 键
字典中的键是唯一的，并且键是不可改变的，因为需要通过`hash`算法算出键对应的值的位置。  
不推荐使用浮点数作为键。因为浮点数会有精度误差。  
```python
>>> d = {}
>>> d[6.6] = 'hi'
>>> d[1.1 + 2.2]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d[1.1 + 2.2]
KeyError: 3.3000000000000003
>>> d
{6.6: 'hi'}
```

## 增
直接通过`[]`指定键值即可增加一对键值，但注意如果键存在则是修改值。  
```python
>>> d = {'name':'Alan', 'age':32}
>>> d['salary'] = 7000
>>> d
{'name': 'Alan', 'age': 32, 'salary': 7000}
>>> d['salary'] = 17000
>>> d
{'name': 'Alan', 'age': 32, 'salary': 17000}
```

`setdefault(key[, value])`  
如果键存在，则返回对应的值，不作修改；如果键不存在，则新增并赋值(第二个参数)。  
```python
>>> d.setdefault('salary', 27000)
17000
>>> d
{'name': 'Alan', 'age': 32, 'salary': 17000}
>>> d.setdefault('location', 'China')
'China'
>>> d
{'name': 'Alan', 'age': 32, 'salary': 17000, 'location': 'China'}
```

`update`  
根据参数传入的字典插入或更新当前字典。  
```python
>>> d.update({'salary': 27000, 'sex': 'male'})
>>> d
{'name': 'Alan', 'age': 32, 'salary': 27000, 'location': 'China', 'sex': 'male'}
```

## 删
使用`del`关键字删除键对应的元素。  
```python
>>> del d['sex']
>>> d
{'name': 'Alan', 'age': 32, 'salary': 27000, 'location': 'China'}
>>>
```

使用`pop(key[, value])`根据键删除元素，如果键存在，返回键值；如果键不存在返回第二个参数。  
```python
>>> d.pop('location', 'USA')
'China'
>>> d
{'name': 'Alan', 'age': 32, 'salary': 27000}
>>> d.pop('hair', 'black')
'black'
>>> d
{'name': 'Alan', 'age': 32, 'salary': 27000}
>>>
```

使用`clear`方法，原地清空字典。  
```python
>>> d2 = d
>>> d2
{'name': 'Alan', 'age': 32, 'salary': 27000}
>>> d.clear()
>>> d
{}
>>> d2
{}
```

## 改
参考**增**

## 查
使用`[]`操作。  
```python
>>> d = {'name':'Alan', 'age':32}
>>> d['name']
'Alan'
>>>
>>> d['location']
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d['location']
KeyError: 'location'
```

使用`[]`，如果键值不存在，会抛出`KeyError`。使用`get(key[, value])`返回键对应的值，如果键不存在，则返回第二个参数。  
```python
>>> d.get('name', 'unknown')
'Alan'
>>> d.get('location', 'unknown')
'unknown'
```

## 遍历字典
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

## 字典推导式
字典推导和列表推导的使用方法是类似的，中括号改成大括号。  
```python
>>> squares = {x : x ** 2 for x in range(5)}
>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
>>> squares = {x : x ** 2 for x in range(5) if x % 2 == 0}
>>> squares
{0: 0, 2: 4, 4: 16}
```
