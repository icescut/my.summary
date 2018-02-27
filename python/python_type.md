# 类型

大纲：
* int
* float

## int
int表示整型数字，python能够自动判断数字是否为整型（无小数点）。  

```python
>>> a = 18
>>> print(a, type(a))
18 <class 'int'>
```
### 十六进制
使用`0x`开头的数字为十六进制数字。  
```python
>>> a = 0X5C
>>> print(a)  # 5 * 16 + 12
92
```

### 八进制
使用`0o`开头的数字为十六进制数字。  
```python
>>> a = 0o36
>>> print(a)  # 3 * 8 + 6
30
```

### 二进制
使用`0b`开头的数字为十六进制数字。  
```python
>>> a = 0b10101   # 16 + 4 + 1
>>> print(a)
21
```

## float
带小数点的数字自动识别为float类型。因为float类型是使用
