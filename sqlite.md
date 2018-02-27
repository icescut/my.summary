# SQLite
SQLite是一个开源的自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。  

**优点**  
* 不需要一个单独的服务器进程或操作的系统（无服务器的）。  
* SQLite 不需要配置，这意味着不需要安装或管理。  
* 一个完整的 SQLite 数据库是存储在一个单一的跨平台的磁盘文件。  
* SQLite是非常小的，是轻量级的，完全配置时小于400KiB，省略可选功能配置时小于250KiB。
* SQLite 是自给自足的，这意味着不需要任何外部的依赖。  
* SQLite 事务是完全兼容 ACID 的，允许从多个进程或线程安全访问。  

大纲：
* 安装  

## 安装
1. 从[SQLite Download Page](http://sqlite.org/download.html)下载对应的版本。  
2. 解压到某个目录。  
3. 将该目录添加到Path。  
4. 在命令行下输出`sqlite3`，如果进行SQLite命令行，则成功安装。  

## 数据库
SQLite中的数据库就是一个单一的文件。  

### 创建数据库
直接在命令行中输入
```
sqlite3 dbname.db
```
则会在当前目录中建立一个数据库，当建表时才会实际生成文件。  

## 表
* DML语句有SELECT、UPDATE、INSERT、DELETE等。  
* DDL语句有CREATE、ALTER、DROP、GRANT、REVOKE等。  
* DCL语句有COMMIT、SAVEPOINT、ROLLBACK等。  

### 创建表
SQLite的CREATE TABLE语句用于在任何给定的数据库创建一个新表。  
语法：  
```
CREATE TABLE database_name.table_name(
   column1 datatype  PRIMARY KEY(one or more columns),
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
);
```

例如：
```
sqlite> CREATE TABLE person(
   ...> id      INT PRIMARY KEY NOT NULL,
   ...> name    TEXT            NOT NULL,
   ...> age     INT             NOT NULL,
   ...> address CHAR(50),
   ...> salary  REAL
   ...> );
```
使用`.schema`命令可以查看建表语句。  

### 删除表
SQLite的DROP TABLE语句用来删除表定义及其所有相关数据、索引、触发器、约束和该表的权限规范。  
语法：  
```
DROP TABLE [IF EXISTS] database_name.table_name;
```

例如：
```
DROP TABLE IF EXISTS person;
```
最好加上`IF EXISTS`语句防止表不存在时报错。  

### INSERT
INSERT语句往表中插入一行或多行数据。有两种语法。  

1. 直接插入数据。  
语法：
```
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);
```

例如：
```
sqlite> INSERT INTO person (ID,NAME,AGE,ADDRESS,SALARY)
   ...> VALUES (1, 'Paul', 32, 'California', 20000.00 );
sqlite> SELECT * FROM person;
id          name        age         address     salary
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
```

SQLite并有支持MySQL的`INSERT INTO table VALUE (value1,...), (value2,...), ...`一次插入多条记录的语法，这种语法也不是标准的SQL语法。 

如果按定义的顺序设置VALUES，可以省略列名。  
```
INSERT INTO person VALUES (7, 'James', 24, 'Houston', 10000.00 );
sqlite> SELECT * FROM person WHERE id = 7;
id          name        age         address     salary
----------  ----------  ----------  ----------  ----------
7           James       24          Houston     10000.0
```

如果省略可以为空的列，则默认会给NULL。  
```
sqlite> INSERT INTO person(id,name,age) VALUES(8, 'Tom', 40);
sqlite> SELECT * FROM person WHERE address is NULL;
id          name        age         address     salary
----------  ----------  ----------  ----------  ----------
8           Tom         40
```

2. 从其他表选择数据进行插入。  
语法：
```
INSERT INTO first_table_name [(column1, column2, ... columnN)] 
   SELECT column1, column2, ...columnN 
   FROM second_table_name
   [WHERE condition];
```

例如：
```
sqlite> INSERT INTO person_2
   ...>         SELECT * FROM person
   ...>         WHERE age > 30;
sqlite> SELECT * FROM person_2;
id          name        age         address     salary
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
8           Tom         40
```

### SELECT
SQLite的SELECT语句用于从SQLite数据库表中获取数据，以结果表的形式返回数据。这些结果表也被称为结果集。  
语法：  
```
SELECT column1, column2, columnN FROM table_name;
SELECT * FROM table_name;
```

例如：
```
sqlite> SELECT * FROM person;
id          name        age         address     salary
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
8           Tom         40
sqlite> SELECT name, address FROM person;
name        address
----------  ----------
Paul        California
Allen       Texas
Teddy       Norway
Mark        Rich-Mond
David       Texas
Kim         South-Hall
James       Houston
Tom
```

## 点命令
点命令以点号开始，并且不以分号结束。用于执行SQLite的管理及辅助功能。  

### .databases
列出数据库及对应的文件。  
```
sqlite> .databases
main: F:\ABao\work\sqlite-test\test.db
```
因为可以通过`ATTACH`附加数据库，所以可能列出不止一个。  

### .show
列出命令提示符的设置。  
```
sqlite> .show
        echo: off
         eqp: off
     explain: auto
     headers: off
        mode: list
   nullvalue: ""
      output: stdout
colseparator: "|"
rowseparator: "\n"
       stats: off
       width:
    filename: test.db
```

### .schema
显示表的创建语句。  
```
sqlite> .schema person
CREATE TABLE person(
id INT PRIMARY KEY NOT NULL,
name TEXT NOT NULL,
age INT NOT NULL,
address CHAR(50),
salary REAL
);
```

### .tables
列出当前数据库中的表，可以使用通配符，类似`LIKE`语句。  
```
sqlite> .tables
person
sqlite> .tables p%
person
```

### 格式化
如果不设置格式化。查询出来的结果是这样的。  
```
sqlite> SELECT * FROM person;
1|Paul|32|California|20000.0
```
使用`|`分隔，并且没有列标题。  

**.header**  
使用`.header on`打开列标题显示。  
```
sqlite> .header on
sqlite> SELECT * FROM person;
id|name|age|address|salary
1|Paul|32|California|20000.0
```

**.mode**  
使用`.mode 输出模式`设置显示的模式。选项有：   
* csv 逗号分隔的值  
```
sqlite> .mode csv
sqlite> SELECT * FROM person;
id,name,age,address,salary
1,Paul,32,California,20000.0
```
* column 左对齐的列  
```
sqlite> .mode column
sqlite> SELECT * FROM person;
id          name        age         address     salary
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
```
* html HTML的<table>代码  
```
sqlite> .mode html
sqlite> SELECT * FROM person;
<TR><TH>id</TH>
<TH>name</TH>
<TH>age</TH>
<TH>address</TH>
<TH>salary</TH>
</TR>
<TR><TD>1</TD>
<TD>Paul</TD>
<TD>32</TD>
<TD>California</TD>
<TD>20000.0</TD>
</TR>
```
* insert TABLE 表的SQL插入（insert）语句  
```
sqlite> .mode insert
sqlite> SELECT * FROM person;
INSERT INTO "table"(id,name,age,address,salary) VALUES(1,'Paul',32,'California',20000.0);
```
* line 每行一个值  
```
sqlite> .mode line
sqlite> SELECT * FROM person;
     id = 1
   name = Paul
    age = 32
address = California
 salary = 20000.0
```
* list 由.separator字符串分隔的值  
* tabs 由Tab分隔的值  
```
sqlite> .mode tabs
sqlite> SELECT * FROM person;
id      name    age     address salary
1       Paul    32      California      20000.0
```
* tcl TCL列表元素  
```
sqlite> .mode tcl
sqlite> SELECT * FROM person;
"id" "name" "age" "address" "salary"
"1" "Paul" "32" "California" "20000.0"
```

一般都是开启`.mode column`，如果需要查看一个记录的详情可以使用`.mode line`，其余使用较少。  

**.timer**  
使用`.timer on`开启时间监控，在执行完操作后在最后面显示使用的时间。  
```
sqlite> .timer on
sqlite> SELECT * FROM person;
id          name        age         address     salary
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
Run Time: real 0.003 user 0.000000 sys 0.000000
```
选择性开启。  

**.width**  
有时输出会截断，使用`.width 第一列,第二列,...`设置显示列的宽度。  

### .quit
退出SQLite命令行。  

## 运算符
运算符是一个保留字或字符，主要用于SQLite语句的WHERE子句中执行操作，如比较和算术运算。  
运算符用于指定SQLite语句中的条件，并在语句中连接多个条件。  

### 算术运算符
SQLite中的算术运算符只能作用于数值。  
* `+` 加法
* `-` 减法
* `*` 乘法
* `/` 除法
* `%` 取模

```
sqlite> .mode line
sqlite> select 1.2 + 3.4;
1.2 + 3.4 = 4.6
sqlite> select 1.2 - 3.4;
1.2 - 3.4 = -2.2
sqlite> select 1.2 * 3.4;
1.2 * 3.4 = 4.08
sqlite> select 1.2 / 3.4;
1.2 / 3.4 = 0.352941176470588
sqlite> select 8 % 3;
8 % 3 = 2
```

### 比较运算符
* `==` 是否相等  
* `=` 是否相等  

## 约定
### sqlite_master
sqlite_master表记录当前数据库的元数据。  

使用查询已建立的表：  
```
sqlite>  SELECT tbl_name FROM sqlite_master WHERE type = 'table';
tbl_name
----------
person
person_2
```





