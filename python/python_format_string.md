# 格式化字符串

大纲：
* 字符串格式化操作符`%`
* str.format

## 字符串格式化操作符`%`
字符串格式化使用字符串格式化操作符`%`来实现。在`%`在左侧放置一个格式化字符串，右侧放置希望被格式化的值。  
格式化字符串中`%`开头的值被称为转换说明符。  
实际上和经典的C语言的做法十分类似。  
```python
>>> name = 'Alan'
>>> age = 32
>>> print '%s is %d old' % (name, age)
Alan is 32 old
```
希望被格式化的值的个数及顺序必须与左边的转换说明符能够对应起来。  

### 转换类型
转换类型说明希望转换为什么类型的格式。必须能够实现转换，比如一个字符类型对应`%d`则会报错，而一个数值类型对应`%s`则没有问题，因为可转换为字符串。  
* %%	百分号标记
* %c	字符及其ASCII码
* %s	字符串
* %d	有符号整数(十进制)
* %u	无符号整数(十进制)
* %o	无符号整数(八进制)
* %x	无符号整数(十六进制)
* %X	无符号整数(十六进制大写字符)
* %e	浮点数字(科学计数法)
* %E	浮点数字(科学计数法，用E代替e)
* %f	浮点数字(用小数点符号)
* %g	浮点数字(根据值的大小采用%e或%f)
* %G	浮点数字(类似于%g)
* %p	指针(用十六进制打印值的内存地址)
* %n	存储输出字符的数量放进参数列表的下一个变量中

### 辅助符
* m.n  
m表示最小宽度，如果是`*`则表示从值元组中读出。该参数可选。  
当转换类型为实数，n表示精度，即小数点后的位数；当转换类型为字符串，n表示最大宽度，如果是`*`则表示从值元组中读出。该参数可选。  

```python
>>> name = 'Alan Liang'
>>> age = 32.5
>>> print '%s is %f old' % (name, age)
Alan Liang is 32.500000 old
>>> print '%20s is %f old' % (name, age)
          Alan Liang is 32.500000 old
>>> print '%s is %15f old' % (name, age)
Alan Liang is       32.500000 old
>>> print '%s is %.2f old' % (name, age)
Alan Liang is 32.50 old
>>> print '%s is %10.2f old' % (name, age)
Alan Liang is      32.50 old
>>> print '%.5s is %.2f old' % (name, age)
Alan  is 32.50 old
```
`m`和`n`可以同时使用，但如果只用`n`的时候，点号不能省略。  

* `-` 左对齐，默认为右对齐。  
```python
>>> print '%10s' % name
      Alan
>>> print '%-10s' % name
Alan
```

* `+` 在正数前面显示加号。  
```python
>>> print '%+f' % 12.67
+12.670000
>>> print '%+-20f end' % 12.67
+12.670000           end
```

* `0` 在前面填充0。  
```python
>>> print '%020f' % 12.67
0000000000012.670000
>>> print '%+020f' % 12.67
+000000000012.670000
>>> print '%-020f' % 12.67
12.670000
```

* ` ` 在前面填充空格。  
```python
>>> print '% 20f' % 12.67
           12.670000
```

* `#` 在八进制数前面显示零(0)，在十六进制前面显示"0x"或者"0X"（取决于用的是"x"还是"X"）。  
```python
>>> print "%d to hex is %x" %(num, num)
100 to hex is 64
>>> print "%d to hex is %#x" %(num, num)
100 to hex is 0x64
>>> print "%d to hex is %#X" %(num, num)
100 to hex is 0X64
```

* `*` 不在格式化字符串中明确写宽度或精度，而是放在右侧元组中（需要格式的值的前面）。  
```python
>>> print '%*f end' % (20, 12.67)
           12.670000 end
>>> print '%.*f end' % (2, 12.67)
12.67 end
>>> print '%*.*f end' % (20, 2, 12.67)
               12.67 end
```

### 使用字典
右侧的元组可以改为使用字典，则左侧的格式化字符串可以使用字典元素的名字。  
```python
>>> person = {'name' : 'Alan', 'age' : 32}
>>> print '%(name)s is %(age)d years old' % person
Alan is 32 years old
```

## str.format
从python 2.6开始，可以使用`str.format()`方法增强格式化输出。  
与`%`的不同之处：  
* 使用`{}`作为占位符。   
* `位置:格式`方式。  

### 基本格式化
使用`{}`占位符就可以自动将格式化对象转换为字符串。  
```python
>>> '{} {} {} {}'.format('one', 'two', 10, 5.23)
'one two 10 5.23'
>>> '{1} {0}'.format('one', 'two')
'two one'
```

### 值转换
```python
>>> class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

>>> '{0!s} {0!r}'.format(Data())
'str repr'
```

### 最小输出长度补白与对齐
`:`后面的数据表示最小**输出**长度。  
* `<`表示左对齐
* `>`表示右对齐
* `^`表示居中对齐
默认为左对齐，所以`<`可以不写。但是如果有补白则必须写，补白写在对齐之前。  
```python
>>> '{:10}|'.format('test')
'test      |'
>>> '{:>10}|'.format('test')
'      test|'
>>> '{:^10}|'.format('test')
'   test   |'
>>> '{:_<10}|'.format('test')
'test______|'
```

### 截断
使用`.`后面跟数字表示**输入**字符截断为多长。
```python
>>> '{:.5}'.format('1234567890')
'12345'
>>> '{:10.5}|'.format('1234567890')
'12345     |'
```

### 数值
使用d表示整数，使用f表示浮点数。  
```python
>>> '{:d}'.format(42)
'42'
>>> '{:f}'.format(3.141592653589793)
'3.141593'
>>> '{:06.2f}'.format(3.141592653589793)
'003.14'
```
格式化字符串中小数点后的数字对于浮点数来说则是小数点后的位数。  

使用`+`表示显示正负号，使用`-`表示负数显示负号。  
```python
>>> '{:+d}'.format(42)
'+42'
>>> '{:+d}'.format(-42)
'-42'
>>> '{:-d}'.format(42)
'42'
>>> '{:-d}'.format(-42)
'-42'
```

如果在前面再加上`=`表示控制符号显示在最前面。  
```python
>>> '{:=5d}'.format((- 23))
'-  23'
>>> '{:=+5d}'.format(23)
'+  23'
```

### 命名占位符
传入参数可以是关键字参数，则格式化字串中可以通过关键字参数的名字来获得对应的值。  
```python
>>> '{name} is {age} old'.format(name='Alan', age=32)
'Alan is 32 old'
>>> person = {'name': 'Darcy', 'age':30}
>>> '{name} is {age} old'.format(**person)
'Darcy is 30 old'
```

### 元素及对象属性
可以在格式化字符串使用列表、字典元素及对象属性方式获取参数的值。  
```python
>>> lst = [2, 4, 6, 8]
>>> '{d[1]} {d[3]}'.format(d=lst)
'4 8'
>>> '{p[name]} is {p[age]} old'.format(p=person)
'Darcy is 30 old'
>>> '{b.feather}'.format(b=Bird())
'Blue'
>>>
```
