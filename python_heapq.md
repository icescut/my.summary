# 堆算法

大纲：
* 函数
* 用途

heapq 模块提供了堆算法，或者称为优先队列算法。  
堆是二叉树的一种，任一父节点都小于或等于其子节点。即`heap[k] <= heap[2*k + 1]`并且`heap[k] <= heap[2*k + 2]`。堆中最小的元素位于`heap[0]`。  
注意heapq本身提供了算法，而没有实现数据结构，数据结构是用户提供的一个可迭代对象。  
heap的优点是在不断插入元素的同时又能高效地保持有序性。  

## 函数

**建堆**  
语法：`heapq.heapify(x)`，把列表原地转换为堆，只需要线性的时间：`O(len(x))`。  

```python
>>> heap = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> heapq.heapify(heap)
>>> heap
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
```

**弹出堆顶元素**  
语法：`heapq.heappop(heap)`，弹出堆顶元素，即最小的元素。实际可以通过建堆后连续弹出堆顶元素实现下面的`nsmallest`函数。  

```python
>>> heapq.heappop(heap)
-4
>>> heapq.heappop(heap)
1
>>> heapq.heappop(heap)
2
>>> heap
[2, 7, 8, 23, 42, 37, 18, 23]
```

**插入元素并整理堆**  
语法：`heapq.heappush(heap, item)`，插入元素，并且会整理heap，使其保持堆的特点。  

```python
>>> heap = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> heapq.heapify(heap)
>>> heap
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
>>> heapq.heappush(heap, 5)
>>> heap
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8, 5]
>>> heapq.heappush(heap, 0)
>>> heap
[-4, 2, 0, 23, 7, 1, 18, 23, 42, 37, 8, 5, 2]
```

**merge**  
语法：`heapq.merge(*iterable, key=None, reverse=False)`，合并n个已经有序的可迭代对象，返回一个合并后的生成器对象，可顺序返回元素。
```python
>>> a = [1, 5, 8, 13]
>>> b = [2, 5, 9, 20]
>>> c = [-1, 6, 7, 14]
>>> d = heapq.merge(a, b, c)
>>> d
<generator object merge at 0x0000022FE6C4A2B0>
>>> list(d)
[-1, 1, 2, 5, 5, 6, 7, 8, 9, 13, 14, 20]
```

**返回最大n个元素**  
语法：`heapq.nlargest(n, itrable, key=None)`，返回itrable中的前n个最大的元素，itrable无需有序。可选key参数可以为复杂结构提供自己的比较方式。  
```python
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> heapq.nlargest(3, nums)
[42, 37, 23]
>>> nums
[1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
```

**返回最小n个元素**  
语法：`heapq.nsmallest(n, itrable)`，返回itrable中的前n个最小的元素，itrable无需有序。  
```python
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> heapq.nsmallest(3, nums)
[-4, 1, 2]
>>> nums
[1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

>>> portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
>>> cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
>>> expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
>>> cheap
[{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
>>> import pprint
>>> pprint.pprint(cheap)
[{'name': 'YHOO', 'price': 16.35, 'shares': 45},
 {'name': 'FB', 'price': 21.09, 'shares': 200},
 {'name': 'HPQ', 'price': 31.75, 'shares': 35}]
>>> pprint.pprint(expensive)
[{'name': 'AAPL', 'price': 543.22, 'shares': 50},
 {'name': 'ACME', 'price': 115.65, 'shares': 75},
 {'name': 'IBM', 'price': 91.1, 'shares': 100}]
```

**heappushpop**  
语法：`heapq.heappushpop(heap, item)`，先把item加入到堆中，然后再pop，比`heappush()`再`heappop()`要快得多。  

**heapreplace**  
语法：`heapq.heapreplace(heap, item)`，先pop，然后再把item加入到堆中，比`heappop()`再`heappush()`要快得多。  

## 用途
1. 当要查找的元素个数相对比较小的时候，函数`nlargest()`和`nsmallest()`是很合适的。   
如果你仅仅想查找唯一的最小或最大（N=1）的元素的话，那么使用`min()`和`max()`函数会更快些。 类似的，如果 N 的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点 （ `sorted(items)[:N]`或者是`sorted(items)[-N:]`）。 需要在正确场合使用函数`nlargest()`和`nsmallest()`才能发挥它们的优势 （如果 N 快接近集合大小了，那么使用排序操作会更好些）。

2. 实现堆排序。  
通过`heapify`或者`heappush`建堆后，不断通过`heappop`弹出最小元素。  

```python
>>> def heapsort(iterable):
	h = []
	for value in iterable:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]

>>> heapsort([1, 3, 5, 7, 9, 2, 4])
[1, 2, 3, 4, 5, 7, 9]
```
