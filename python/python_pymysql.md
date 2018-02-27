# pymysql
pymsql是Python中操作MySQL的模块，其使用方法和MySQLdb几乎相同。但目前pymysql支持python3.x而后者不支持3.x版本。  

## 安装配置
1. 安装pymysql。  
使用`pip install pymysql`安装pymysql模块。  
安装完成后在IDLE中使用`import pymysql`，如果没有报错则表示安装成功。  

2. 准备mysql。
创建表
```mysql
CREATE TABLE product(
	id int NOT NULL AUTO_INCREMENT,
    name varchar(80) NOT NULL,
    price DECIMAL(9, 2) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
```

插入数据。  