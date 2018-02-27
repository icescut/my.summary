# Jinjia2
模板仅仅是文本文件。它可以生成任何基于文本的格式（HTML、XML、CSV、LaTex 等等）。 它并没有特定的扩展名，.html或.xml都是可以的。  
模板包含变量或表达式，这两者在模板求值的时候会被替换为值。模板中 还有标签，控制模板的逻辑。  

基本使用：
1. 定义模板。
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}
</body>
</html>
```
2. 在Flask的视图函数中调用`render_template`并传入参数。  
```python
@app.route('/')
def hello():
    context = {
        "navigation" : [
            {
                "caption": "GitHub",
                "href": "https://github.com/"
            },
            {
                "caption": "Leetcode",
                "href": "https://leetcode.com/"
            },
            {
                "caption": "flask",
                "href": "http://flask.pocoo.org/"
            }
        ],
        "a_variable" : "hello"
    }
    return render_template('hello.html', **context)
```

## 语法
* 表达式，`{{ expression }}`   
* 语句，`{% statement %}`   
* 注释，`{# ... #}`

## 变量访问
使用{{ object.attr}}或{{ object["attr"]}}的方式设置对象的属性或字典的键值是类似的，只是调用`getattr(object, 'attr')`和`object.__getitem__('attr')`的顺序不同而且。  

```html
    <h1>水果</h1>
    <ul>
        <li>苹果：{{ fruit.apple }}</li>
        <li>香蕉：{{ fruit["banana"] }}</li>
        <li>橙子：{{ fruit.orange }}</li>
    </ul>
    <h1>人</h1>
    <ul>
        <li>姓名：{{ person.name}}</li>
        <li>年龄：{{ person["age"] }}</li>
    </ul>
```

```python
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/')
def hello():
    fruit = {
        "apple" : 6,
        "banana" : 2.5,
        "orange" : 5
    }
    p = Person('Alan', 32)

    return render_template('index2.html', fruit=fruit, person=p)
```
