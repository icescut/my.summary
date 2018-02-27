# BeautifulSoup
本文不仅是BeautifulSoup的使用说明，更是网络爬虫的各种应用的总结。  
基于BeautifulSoup 4版本，也叫bs4。主要用于操作html/xml字符串。  

## 开始使用
使用`pip install beautifulsoup4`来安装BeautifulSoup。  
例子：
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)
```
结果为：
```
<h1>An Interesting Title</h1>
```

1. 一般使用urllib中的urlopen来获取网页的html代码。  
2. 构造BeautifulSoup对象，该对象一般传入两个参数，第一个参数是标记语言(Markup)字符串，如html/xml；第二个参数为解释器，上例中的`html.parser`为Python内置的解释器，无需额外安装。  

### 标签名
可以使用`BeautifulSoup对象.标签名`来提取标签(tag)对象。上面使用中的`bsObj.h1`，实际下面这几种方式是等价的：
```python
bsObj.h1
bsObj.html.h1
bsObj.html.body.h1
```
可以在不影响语义的情况下选用，毕竟一个结构良好的html页面，h1是唯一的。  

## 异常处理
因为网络和网页结构都是复杂的，可能和你预想的不一致。而爬虫程序可能会执行很长时间，所以异常处理是很有必要的。  
例子：  
```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.h1
    except AttributeError as e:
        return None

    return title


title = get_title("http://pythonscraping.com/pages/page1.html")
if title is None:
    print("Title cannot be found")
else:
    print(title)
```
1. 进行网络传输的时间需要异常处理  
2. 对页面进行解释的时间也需要异常处理  

## 解析HTML
三思而后行：
1. 网页结构可能会变动，所以尽量不要用数字来匹配第几个元素，多用标签的属性。  
2. 可以参考网页的JavaScript代码。  
3. 不只限于一个网站，可以看下其他网站是否有相同数据。  

### find_all
语法：`find_all(name , attrs , recursive , text , **kwargs)`
得到所有符合条件的标签。  
* name为标签的名字  
* attrs为属性的字典  
* text参数为使用标签的内容匹配  
* recursive默认为True，表示查找所有后代节点，如果为False则只查找子节点  
* limit参数限制返回的数量，`find`方法其实等价于`find_all(...,limit=1)`  
* kwargs，可以直接通过键值的方式指定属性，比如`find_all(id="nav")`和`find_all("", {id: "nav"})`效果是一样的   

name可以是标签的集合：
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>This is h1</h1>
        <h2>This is h2</h2>
        <h3>This is h3</h3>
        <h4>This is h4</h4>
        <h5>This is h5</h5>
        <h6>This is h6</h6>
    </body>
</html>
"""
bsObj = BeautifulSoup(html, "html.parser")
titles = bsObj.find_all({'h1', 'h2', 'h3'})
for title in titles:
    print(title.get_text())
```
结果：
```
This is h1
This is h2
This is h3
```

**注意**  
`find_all`返回的是一个`ResultSet`对象，如果只有一个匹配的时候也是如此，而不是tag对象。  
相对之下，`find`返回一个tag对象或者None。  

### 通过class匹配
例子
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.find_all("span", {"class": "green"})

for name in nameList:
    print(name.get_text())
```
得到所有class属性为green的span标签。  

### get_text
通过`get_text()`方法会把你正在处理的HTML文档中所有的标签都清除，然后返回一个只包含文字的字符串。假如你正在处理一个包含许多超链接、段落和标签的大段源代码，那么.get_text()会把这些超链接、段落和标签都清除掉，只剩下一串不带标签的文字。  
```
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p>
            hello
            <span> inner1</span>
            <a href="https://www.github.com">GitHub</a>
            world
        </p>
    </body>
</html>
"""
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.p.get_text())
```
结果为：
```
            hello
             inner1
GitHub
            world
```

### 子标签
使用标签的`.children`属性即可得到它的子标签。  
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body><p>
            Hello
            <span>inner1</span>
            world
        </p><div>
            hi
            <p>inner2</p>
            world
        </div></body>
</html>
"""

bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.body.children:
    print('--------------------------\n', child)
```
结果：
```
--------------------------
 <p>
            Hello
            <span>inner1</span>
            world
        </p>
--------------------------
 <div>
            hi
            <p>inner2</p>
            world
        </div>
```

### 后代标签
使用标签的`.descendants`属性即可得到它的子标签(包括文本节点)。  
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body><p>
            Hello
            <span>inner1</span>
            world
        </p><div>
            hi
            <p>inner2</p>
            world
        </div></body>
</html>
"""

bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.body.descendants:
    print('--------------------------\n', child)
```
结果：
```
--------------------------
 <p>
            Hello
            <span>inner1</span>
            world
        </p>
--------------------------
 
            Hello
            
--------------------------
 <span>inner1</span>
--------------------------
 inner1
--------------------------
 
            world
        
--------------------------
 <div>
            hi
            <p>inner2</p>
            world
        </div>
--------------------------
 
            hi
            
--------------------------
 <p>inner2</p>
--------------------------
 inner2
--------------------------
 
            world
```

### 兄弟标签
```
from bs4 import BeautifulSoup

html = """
<html>
    <body>
    <p>1</p><p id="two">2</p><p>3</p><p>4</p><p>5</p></body>
</html>
"""

bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("p", {"id": "two"}).next_siblings:
    print('--------------------------\n', sibling)

```
结果：
```
--------------------------
 <p>3</p>
--------------------------
 <p>4</p>
--------------------------
 <p>5</p>
```

## 对象

* BeautifulSoup对象  
  
* tag对象
  代表标签  
* NavigableString对象  
  代表标签里面的文字  
* Comment对象  
  代表注释

## 参考
* [Python网络数据采集](https://www.amazon.cn/dp/B01M3VN9CW/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1519524292&sr=1-1&keywords=Python%E7%BD%91%E7%BB%9C%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86)