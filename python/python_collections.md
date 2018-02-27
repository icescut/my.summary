# 容器
collections包中实现了一些python内置数据结构之外的数据结构。  

大纲：
* ChainMap
* deque

## ChainMap
ChainMap将多个字典组合成一个可更新的视图。可在ChainMap上执行字典的基本操作。  
```python
>>> food_prices = {"meat": 10, "water": 2}
>>> dress_prices = {"shirt": 30, "shoes": 25}
>>> other_prices = {"water": 3}
>>> all_prices = ChainMap(food_prices, dress_prices, other_prices)
>>> all_prices["meat"]
10
```

位于其中的字典们实际组织方式是一个**排序**的列表。读写、删除都是针对第一个找到的键值。  
```python
>>> all_prices["water"]
2
>>> all_prices["water"] += 2
>>> all_prices["water"]
4
>>> food_prices["water"]
4
```

因为其里面的字典是通过引用方式来使用，所以独立对字典的更新会返回到ChainMap上。
```python
>>> dress_prices["shoes"] = 45
>>> all_prices["shoes"]
45
```

如果创建时没有给字典，则默认至少有一个空字典。  
```python
>>> amap = ChainMap()
>>> amap
ChainMap({})
```

### maps
ChainMap的`maps`属性返回一个可更新的字典列表。
```python
>>> all_prices.maps
[{'meat': 10, 'water': 4}, {'shirt': 30, 'shoes': 45}, {'water': 3}]
```

### new_child & parents(tbc)

### 用途
常用于使用默认值，当参数不存在时使用默认参数。  
```python
import argparse
import os

from collections import ChainMap

def main():
    app_defaults = {'username':'admin', 'password':'admin'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key:value for key, value
                              in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ,
                     app_defaults)
    print(chain['username'])

if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()

```

调用`python ChainMap.py -u Alan`，结果为：
> Alan  
> Alan

这次调用command_line_arguments中有值，所有返回为`Alan`。  
调用`python ChainMap.py`，结果为：
> xxxx  
> test

这次调用，第一次调用`main`时，`command_line_arguments`中没有值，则使用`os.environ`中的值`xxxx`。第二次调用`main`时，`os.environ`的`username`也改变为`test`，所以返回`test`。  

## deque
deque是一个双向队列，比如可以用于保留最后N个元素。  
优点：  
在队列头部或尾部插入或删除元素的性能都是O(1)，可列表在**头部**插入或删除元素的性能是O(n)。  

缺点：  
相比列表，需要维护一个更大的空间。  

### 创建deque
传入一个可迭代对象以创建deque，实际会将可迭代对象从左往右不断添加到队列后面。另外有一个`maxlen`的可选参数，用于限制队列大小，如果没有，则队列是不限制大小的。  
```python
>>> d = deque([1, 2, 3], maxlen=10)
>>> d
deque([1, 2, 3], maxlen=10)
```

### 基本列表功能
deque一般情况也能当作list来使用。比如使用中括号获取元素，加法，乘法等
，但不能使用切片功能。  
```python
>>> d = deque([1, 2, 3], maxlen=10)
>>> d[0]
1
>>> d[-1]
3
>>> e = deque([4, 5, 6], maxlen=10)
>>> d + e
deque([1, 2, 3, 4, 5, 6], maxlen=10)
>>> d * 2
deque([1, 2, 3, 1, 2, 3], maxlen=10)
```

### 插入元素
* 使用`append`在队列尾部插入一个元素。
* 使用`appendleft`在队列头部插入一个元素。
* 使用`extend`在队列尾部按顺序插入一组元素。
* 使用`extendleft`在队列头部按顺序插入一组元素。
* 使用`insert`在队列任意地方插入一个元素。

```python
>>> d.append(4)
>>> d
deque([1, 2, 3, 4], maxlen=10)
>>> d.appendleft(0)
>>> d
deque([0, 1, 2, 3, 4], maxlen=10)
>>> d.extend((5,6))
>>> d
deque([0, 1, 2, 3, 4, 5, 6], maxlen=10)
>>> d.extendleft([-2,-1])
>>> d
deque([-1, -2, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
>>> d.insert(1, "a")
>>> d
deque([-1, 'a', -2, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
```

### 删除元素
* 使用`pop`在队列尾部删除一个元素并返回，如果队列为空，抛出`IndexError`。
* 使用`popleft`在队列头部删除一个元素并返回，如果队列为空，抛出`IndexError`。
* 使用`remove`在队列删除第一个出现的元素，找不到抛出`ValueError`。
* 使用`clear`清空队列。

```python
>>> d = deque([1, 2, 3, 4, 1, 2, 3], maxlen=10)
>>> d.pop()
3
>>> d
deque([1, 2, 3, 4, 1, 2], maxlen=10)
>>> d.popleft()
1
>>> d
deque([2, 3, 4, 1, 2], maxlen=10)
>>> d.remove(2)
>>> d
deque([3, 4, 1, 2], maxlen=10)
>>> d.clear()
>>> d
deque([], maxlen=10)
```

### 查找元素
使用`index(x[,start[,stop]])`查找x在队列中的第一次出现的位置，如果找不到抛出`ValueError`。  
```python
>>> d = deque([1, 2, 3, 4, 1, 2, 3], maxlen=10)
>>> d.index(2)
1
>>> d.index(2, 3)
5
```

### 其余
* 使用`count`返回一个元素在队列中出现的次数。  
* 使用`copy`深复制一个队列。  
* 使用`reverse`原地反转队列。
* 使用`rotate(n)`将尾部元素依次移到头部，如果n是负数则是将头部元素依次移到尾部。
```python
>>> d = deque([1, 2, 3, 4, 1, 2, 3], maxlen=10)
>>> d.count(2)
2
>>> d2 = d.copy()
>>> d2.clear()
>>> d
deque([1, 2, 3, 4, 1, 2, 3], maxlen=10)
>>> d.reverse()
>>> d
deque([3, 2, 1, 4, 3, 2, 1], maxlen=10)
>>> d.rotate(2)
>>> d
deque([2, 1, 3, 2, 1, 4, 3], maxlen=10)
>>> d.rotate(-1)
>>> d
deque([1, 3, 2, 1, 4, 3, 2], maxlen=10)
```

### 用途
deque有一个特性，就是当插入一个元素并且追过最大容量时，最会在相反方向删除一个元素，比如在尾部插入一个元素，那么将在删除头部第一个元素。  
这样就可以用于保留最近n个元素。一种用法是用于实现unix的`tail`，其功能为打印文件中最后n行。
```python
>>> def tail(filename, lines=10):
	with open(filename) as f:
		return deque(f, n)
```
