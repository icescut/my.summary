# flask sqlalchemy
sqlalchemy是flask中最常用的ORM框架。  

## 安装
使用`pip install flask-sqlalchemy`安装。  

## 连接数据库
1. 配置数据库连接
连接语句的格式：
```
dialect+driver://username:password@host:port/database
```
其中driver是你安装的数据驱动。    
config.py  
```python
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
```
SQLALCHEMY_DATABASE_URI这个名字是固定的。  
app.py
```python
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)
```

2. 导入并初始化SQLAlchemy对象。  
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
```
3. 使用`db.create_all()`执行连接，如果正常启动服务器，则为成功。  
可能会返回如下Warning，不影响。  
```
D:\Python36\lib\site-packages\pymysql\cursors.py:165: Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 481")
```

## 创建表映射
```python
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
```
1. 类名对象表名，但是第一个字母要大写，继承自`db.Model`。  
2. 类属性对象表中的列，使用`db.Column`方法定义，第一个参数为类型，后面使用关键字参数定义附加属性。  
    类型：  
    * Integer   Int  
    * String    Char/Varchar  
    * Text      Text  
    附加属性：  
    * primary_key   主键  
    * autoincrement 自动增加  
    * nullable      是否可以为空，默认为可以  
3. 通过执行`db.create_all()`可以在数据库中真正建立表。  

## 增删改查
增删改查都是通过`db.session`对象来进行的。  
因为事务，需要执行`db.session.commit()`才会真正执行。  

### 增加
1. 创建模型对象。  
2. `db.session.add(模型对象)`
3. `db.session.commit()`
```python
    article = Article(title='aaa', content='bbb')
    db.session.add(article)
    db.session.commit()
```
执行后
```
MySQL [db_demo1]> select * from article;
+----+-------+---------+
| id | title | content |
+----+-------+---------+
|  1 | aaa   | bbb     |
+----+-------+---------+
1 row in set (0.00 sec)
```

### 查询
使用模型对象的query属性。  
