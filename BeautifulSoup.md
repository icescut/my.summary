# BeautifulSoup
本文不仅是BeautifulSoup的使用说明，更是网络爬虫的各种应用的总结。  
基于BeautifulSoup 4版本，也叫bs4。主要用于操作html/xml字符串。  

三思而后行：
1. 网页结构可能会变动，所以尽量不要用数字来匹配第几个元素，多用标签的属性。  
2. 可以参考网页的JavaScript代码。  
3. 不只限于一个网站，可以看下其他网站是否有相同数据。 

大纲：
* 开始使用  
* 对象的种类  
* 遍历  
* 搜索  
* 修改  
* 异常  

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

## 对象

* BeautifulSoup对象  
  BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作Tag对象,它支持遍历文档树和搜索文档树中描述的大部分的方法.  
  因为BeautifulSoup对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name属性是很方便的,所以 BeautifulSoup对象包含了一个值为 “[document]” 的特殊属性.name。

* Tag对象
  代表标签。每个Tag都有自己的名字，通过`.name`获取。Tag的属性的操作方法与字典相同，可以添加和修改。    
  ```python
  from bs4 import BeautifulSoup

  html = """
  <b class="red">hello</b>
  """

  bsObj = BeautifulSoup(html, "html.parser")

  print(bsObj.b.name)
  print(bsObj.b["class"])
  bsObj.b["class"] = ["green", "bold"]
  bsObj.b["id"] = "test"
  print(bsObj.b)
  ```
  结果:
  ```
  b
  ['red']
  <b class="green bold" id="test">hello</b>
  ```
  因为class是多值属性，所有修改时可以使用字符串列表。  
  
* NavigableString对象  
  NavigableString对象用来包装Tag中的字符串。  
  ```python
  from bs4 import BeautifulSoup

  html = """
  <b class="red">hello</b>
  """

  bsObj = BeautifulSoup(html, "html.parser")

  print(bsObj.b.string)
  bsObj.b.string.replace_with("hi")

  print(bsObj.b)
  ```
  结果：
  ```
  hello
  <b class="red">hi</b>
  ```
  可以使用`.replace_with`方法替换字符串。  
* Comment对象  
  代表注释。Comment对象是一个特殊类型的NavigableString对象。  

## 遍历文档

### 标签名
可以使用`BeautifulSoup对象.标签名`来提取标签(tag)对象，提取的是第一次出现的标签，实际下面这几种方式是等价的：
```python
bsObj.h1
bsObj.html.h1
bsObj.html.body.h1
```
可以在不影响语义的情况下选用，毕竟一个结构良好的html页面，h1是唯一的。  
实际上`bsObj.h1`等价于`bsObj.find("h1")`，`bsObj.html.h1`等价于`bsObj.find("html").find("h1")`。  
### 子节点
使用标签的`.contents`属性可以得到**列表形式**的子节点。  
使用标签的`.children`属性即可得到**迭代器形式**的子节点。  
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p>Hello<span>inner1</span>world</p>
        <div>hi<p>inner2</p>world</div>
        </body>
</html>
"""

bsObj = BeautifulSoup(html, "html.parser")

print(bsObj.body.contents)
print(bsObj.body.children)
for child in bsObj.body.children:
    if child.name != None:
        print('--------------------------\n', child.name)
```
结果：
```
['\n', <p>Hello<span>inner1</span>world</p>, '\n', <div>hi<p>inner2</p>world</div>, '\n']
<list_iterator object at 0x000001EB15A1EBE0>
--------------------------
 p
--------------------------
 div
```
注意标签之间的空白也会被当作一个子节点，但是这个节点毫无用处，可以通过节点的name为None来进行过滤。  

### 后代节点
使用标签的`.descendants`属性即可得到它的后代节点(包括文本节点)。  
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p>
            Hello
            <span>inner1</span>
            world
        </p>
        <div>
            hi
            <p>inner2</p>
            world
        </div>
    </body>
</html>

"""

bsObj = BeautifulSoup(html, "html.parser")

for descendant in bsObj.body.descendants:
    if descendant.name != None:
        print('--------------------------\n', descendant.name)

```
结果：
```
--------------------------
 p                        
--------------------------
 span                     
--------------------------
 div                      
--------------------------
 p                        
```

### .string
如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点。  
如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同。  
如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None。  
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p id="t1">hello</p>
        <p id="t2"><span>hi</span></p>
        <p id="t3"><span>good</span>night</p>
    </body>
</html>
"""

bsObj = BeautifulSoup(html, "html.parser")

print(bsObj.find(id="t1").string)
print(bsObj.find(id="t2").string)
print(bsObj.find(id="t3").string)
```
结果：
```
hello
hi
None
```

### .strings 和 stripped_strings

### 兄弟节点
* next_siblings，当前节点后面有所有兄弟节点  
* previous_siblings，当前节点前面有所有兄弟节点  
* previous_sibling，当前节点紧挨着前面的兄弟节点  
* next_sibling，当前节点紧挨着后面的兄弟节点  
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p id="one">1</p>
        <p id="two">2</p>
        <p id="three">3</p>
        <p id="four">4</p>
        <p id="fifth">5</p>
    </body>
</html>
"""

bsObj = BeautifulSoup(html, "html.parser")

print('siblings after id two:')
for sibling in bsObj.find("p", {"id": "two"}).next_siblings:
    if sibling.name != None:
        print(sibling)

print('---------------------------')
print('siblings before id four:')
for sibling in bsObj.find("p", {"id": "four"}).previous_siblings:
    if sibling.name != None:
        print(sibling)

print('---------------------------')
print('sibling before id three:')
print(bsObj.find("p", {"id": "three"}).previous_sibling)

print('---------------------------')
print('sibling after id three:')
print(bsObj.find("p", {"id": "three"}).next_sibling)
```
结果：
```
siblings after id two:
<p id="three">3</p>
<p id="four">4</p>
<p id="fifth">5</p>
---------------------------
siblings before id four:
<p id="three">3</p>
<p id="two">2</p>
<p id="one">1</p>
---------------------------
sibling before id three:


---------------------------
sibling after id three:

```
注意无用的空白节点，导致previous_sibling和next_sibling没有按预期那样。一种思路是如果取上一节点有值，并且节点的name为None则继续取上一节点，直到节点的name不为None则为真正的上一节点。  

### 父节点
* parent，当前节点的直接父节点  
* parents，当前节点的所有祖先节点，直到html和document节点  
```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p>
            Hello
            <span id="inner1">inner1</span>
            world
        </p>
    </body>
</html>
"""

bsObj = BeautifulSoup(html, "html.parser")

print("span's parent:")
print(bsObj.span.parent.name)
print("----------------------")
print("span's parents:")
for parent in bsObj.span.parents:
    print(parent.name)
```
结果：
```
span's parent:
p
----------------------
span's parents:
p
body
html
[document]
```

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

### 正则表达式


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

## 参考
* [Python网络数据采集](https://www.amazon.cn/dp/B01M3VN9CW/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1519524292&sr=1-1&keywords=Python%E7%BD%91%E7%BB%9C%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86)