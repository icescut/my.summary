# Flask
Flask是一个基于Python的小型的web框架。具有一个包含基本服务的强健核心，其他功能可以通过扩展实现。  
Flask主要依赖于Werkzeug和Jinjia2。  

大纲：
* 安装
* 基本结构
* 路由和视图函数
* 渲染模板
* URL重定向与反转
* 配置

## 安装
通过`pip install flask`就可以安装Flask，当然最好是结合`virtualenv`使用。  

## 基本结构
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
```
以上便是一个完整的Flask应用。  
1. 首先使用`from flask import Flask`导入Flask。  
2. 使用`app = Flask(__name__)`创建一个应用对象。`__name__`用于初始化位置。  
3. 使用`@app.route`装饰器实现路由，路由就是URL与函数之间的映射关系，这里`hello_world`称为视图函数。函数的返回值称为响应。  
4. 使用`app.run()`启动WEB服务器。  


## 路由和视图函数
使用`@app.route`装饰器实现路由，路由就是URL与函数之间的映射关系，这里`hello_world`称为视图函数。函数的返回值称为响应。  

```python
@app.route('/')
def hello_world():
    return 'Hello World'
```

### 动态路由
URL中的值是可变的称为动态路由。   
```python
@app.route('/<name>')
def hello_world(name):
    return 'Hello %s!'  % name
```
这时访问http://127.0.0.1:5000/Alan，则在页面上显示Hello Alan!。  
1. 在URL中使用`<参数>`来指定动态传入的参数。  
2. 在视图函数中接收一个同名的参数。  
这个参数默认是字符型的，但可以限定参数类型，可以是int、float、path。path表示不受`/`限制，即可以字符串中可以包含`/`。  

```python
@app.route('/user/<int:id>')
def user(id):
    return 'Your id is %d' % id
```
这时id只能传入整型，如果是其他类型则返回Not Found。  

```python
@app.route('/<a_str>')
def str_test(a_str):
    return 'a string: %s' % a_str

@app.route('/<path:a_path>')
def path_test(a_path):
    return 'a path: %s' % a_path
```
前者能够匹配/a，但不能匹配/a/b。后者则都能匹配。  

## 渲染模板
不太可能完全自己生成html然后由视图函数返回。所以需要预先准备好html代码，但是html代码是静态的，有些东西是可变的。所以模板实际就是由静态的html代码和动态的传入参数组成，而把根据模板和传入的动态参数生成实际返回客户端的页面称为渲染。  

使用方式：  
1. 在根目录的`templates`子目录下放置模板文件。  
2. 在视图函数中通过`return render_template('模板文件',关键字参数)`返回渲染结果。  

例如：
建立`/templates/index.html`文件。  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jinjia2</title>
</head>
<body>
    {{ title }}
</body>
</html>
```
在视图函数中渲染模板。  
```python
@app.route('/tmp/')
def template_test():
    return render_template('index.html', title='Hello World!')
```
当访问/tmp/时，得到渲染的结果。  

当参数比较多时，一般使用一个字典对象保存所有参数，然后使用`**`进行解包传入。  


## URL重定向与反转
当接收到用户请求并进行处理之后，有时是需要重定向（或者说跳转）的另外一个页面，使用`redirect`函数并传入URL地址即可。  
```python
@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return 'please login first'
```
如上代码，在浏览器中输入http://127.0.0.1:5000会自动重定向到http://127.0.0.1:5000/login。  
一般不会写死URL地址，而是通过`url_for`函数从视图函数得到URL地址，这就叫做URL反转。  
```python
@app.route('/')
def index():
    return redirect(url_for('login'))   # 这里的login为视图函数名

@app.route('/login')
def login():
    return 'please login first'
```

## 配置
配置是保存在Flask对象的config属性中的。你可能会需要根据应用环境更改不同的设置，比如切换调试模式、设置密钥、或是别的设定环境的东西。  
config 实际上继承于字典，并且可以像修改字典一样修改它。  
```python
app = Flask(__name__)
app.config['DEBUG'] = True
```
给定的配置值会被推送到 Flask 对象中，所以你可以在那里读写它们:
```python
app.debug = True
```
你可以使用 dict.update() 方法来一次性更新多个键:
```python
app.config.update(
    DEBUG=True,
    SECRET_KEY='...'
)
```

### 从文件配置
从文件进行配置是最常见的方式。  
1. 从`config.py`（可以是其他名字，但使用config更好理解）导入配置。  
注意配置项的名字都要大写
confing.py:
```python
DEBUG = True
```
app.py
```python
import config

app = Flask(__name__)
# app.config['DEBUG'] = True
app.config.from_object(config)
```

2. 从环境变量中读取配置文件的路径。  
比如在项目目录中有settings\config.py：
```python
DEBUG = True
```
然后在命令行(以windows为例)设置环境变量：
```
set HELLO_SETTING=F:\Python\flask-test\hello\settings\config.py
```
app.py
```python
app = Flask(__name__)
app.config.from_envvar('HELLO_SETTING')
```
