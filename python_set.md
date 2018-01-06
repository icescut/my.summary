# python集合
python中的集合就类似于数学上的集合，一个包含无序不重复元素的集。  
集合是python中内置的数据结构。  

## 创建集合
可以使用`{x, y}`创建集合或者使用`set()`函数并传入序列来创建集合。注意不能使用`{}`创建空集合，这样创建的是空字典，需使用`set()`创建空集合。  

```python
>>> a = {1, 2 ,3}
>>> a
{1, 2, 3}
>>> b = set([1, 2, 3])
>>> b
{1, 2, 3}
>>> c = set()
>>> c
set()
>>> type(c)
<class 'set'>
```

集合的元素必须是不可变的。  
```python
>>> a = {(1,2), (3,4)}
>>> a
{(1, 2), (3, 4)}
>>> b = {[1,2], [3,4]}
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    b = {[1,2], [3,4]}
TypeError: unhashable type: 'list'
```

## 集合操作
### 添加元素
使用`add`方法添加一个不可变元素到集合中，使用`update`方法添加多个不可变元素到集合中。  
```python
>>> a = {1, 2, 3}
>>> a.add(4)
>>> a
{1, 2, 3, 4}
>>> a.update((5, 6, 7))
>>> a
{1, 2, 3, 4, 5, 6, 7}
```

### 清除所有元素
使用`clear`方法清除所有元素。  
```python
>>> a = {1, 2, 3}
>>> a.clear()
>>> a
set()
```

### 复制集合
使用`copy`方法复制集合，实际是深复制。  
```python
>>> a = {1, 2, 3}
>>> b = a.copy()
>>> a.clear()
>>> b
{1, 2, 3}
```

### 差集
使用`differenct`方法求差集，或者一般使用减法。  
```python
>>> a = {1, 2, 3, 4, 5, 6}
>>> b = {2, 4, 6}
>>> a.difference(b)
{1, 3, 5}
>>> a - b
{1, 3, 5}
```

使用`differenct_update`方法求差集并用结果覆盖原集合。  
```python
>>> a.difference_update(b)
>>> a
{1, 3, 5}
```

### 删除元素
使用`discard`删除元素，如果元素不在集合中则什么都不会发生。  
```python
>>> a = {1, 2, 3, 4, 5, 6}
>>> a.discard(2)
>>> a
{1, 3, 4, 5, 6}
>>> a.discard(0)
```
也可以使用`remove`删除元素，如果元素不在集合会报`KeyError`。
```python
>>> a = {1, 2, 3, 4, 5, 6}
>>> a.remove(2)
>>> a
{1, 3, 4, 5, 6}
>>> a.remove(0)
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    a.remove(0)
KeyError: 0
```

### 并集
使用`union`求并集，一般使用`|`运算符求并集。  
```python
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> a | b
{1, 2, 3, 4, 5, 6}
```

### 交集
使用`intersection`求交集，一般使用`&`运算符求并集。  
```python
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}
>>> a.intersection(b)
{3, 4}
>>> a & b
{3, 4}
```

### 是否无交集
使用`isdisjoint`求是否有交集。  
```python
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}
>>> a.isdisjoint(b)
False
>>> c = {10}
>>> a.isdisjoint(c)
True
```

### 是否子集
使用`issubset`或`issuperset`求是否子集。  
```python
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}
>>> c = {2, 3}
>>> c.issubset(a)
True
>>> b.issubset(a)
False
```
另外可以使用`<`、`<=`、`>`、`>=`来判断，比如a是b的真子集，则`a < b`结果为`True`。  
```python
>>> a = {1, 2}
>>> b = {1, 2, 3}
>>> a < b
True
>>> a <= b
True
>>> a > b
False
```

`a.issubset(b)`相当于`a <= b`，`a.issuperset(b)`相当于`a >= b`。  

### 弹出元素
使用`pop`方法弹出任意一个元素，如果集合为空则有报错。  
```python
>>> a = {1, 2}
>>> len(a)
2
>>> a.pop()
1
>>> a.pop()
2
>>> len(a)
0
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    a.pop()
KeyError: 'pop from an empty set'
```

### 求两个集合中不重复的元素
使用`symmetric_difference`方法求两个集合中不重复的元素，一般使用运算符`^`。  
```python
>>> a = {1, 3, 5, 7, 9}
>>> b = {3, 6, 9}
>>> a.symmetric_difference(b)
{1, 5, 6, 7}
>>> a ^ b
{1, 5, 6, 7}
```

## Frozenset
Frozenset中一旦建立就不能改变其中的元素(包括不能添加元素)。  
```python
>>> f = frozenset([1, 2, 3])
>>> f.add(4)
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    f.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
```
