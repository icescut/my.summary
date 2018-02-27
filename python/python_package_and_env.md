# python包安装与环境

大纲：
* pip
* virtualenv
* pipenv

## pip
使用pip能够方便的安装python第三方库，默认会从PyPI网站上下载。一般新版本的python都已经自带pip了。  

### 安装第三方包
使用install命令安装第三方包。比如：  
```
pip install request
```
或者下载好wheel包之后安装。  
```
pip install venv\Scripts\regex-2018.2.3-cp36-cp36m-win_amd64.whl
```
一般将wheel文件放在Scripts目录下，并且不要修改wheel文件的名字。  

直接写包名会安装最新版本的包。  
可以对包的版本进行限制。  

* 限定某个版本
```
pip install somepkg == 1.3
```

### 查看
使用show命令查看已安装包的文件。  
```
pip show --files regex

Name: regex
Version: 2018.2.3
Summary: Alternative regular expression module, to replace re.
Home-page: https://bitbucket.org/mrabarnett/mrab-regex
Author: Matthew Barnett
Author-email: regex@mrabarnett.plus.com
License: Python Software Foundation License
Location: f:\abao\work\python\myproject\venv\lib\site-packages
Requires:
Files:
  __pycache__\_regex_core.cpython-36.pyc
  __pycache__\regex.cpython-36.pyc
  __pycache__\test_regex.cpython-36.pyc
  _regex.cp36-win_amd64.pyd
  _regex_core.py
  regex-2018.2.3.dist-info\DESCRIPTION.rst
  regex-2018.2.3.dist-info\INSTALLER
  regex-2018.2.3.dist-info\METADATA
  regex-2018.2.3.dist-info\RECORD
  regex-2018.2.3.dist-info\WHEEL
  regex-2018.2.3.dist-info\metadata.json
  regex-2018.2.3.dist-info\top_level.txt
  regex.py
  test_regex.py
```

### 更新
使用install命令加上`--upgrade`参数更新现有的包。  
```
pip install --upgrade request
```

### 删除
使用uninstall命令删除已安装的包。  
```
pip uninstall request
```

### 配置国内源
首先在window的文件夹窗口输入 ：  %APPDATA%  
然后在底下新建pip文件夹，然后到pip文件夹里面去新建个pip.ini,然后再里面输入内容  
```
[global]
timeout = 6000
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
```   

## virtualenv
在开发Python应用程序的时候，所有第三方的包都会被pip安装到Python的site-packages目录下。  
如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？  
这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。  

安装virtualenv非常简单，直接在命令行执行`pip install virtualenv`即可。  

假定我们要开发一个新的项目，需要一套独立的Python运行环境。   
1. 创建目录
假设创建一个myproject目录。

2. 创建一个独立的运行环境，命令为venv。  
```
λ virtualenv --no-site-packages venv
Using base prefix 'd:\\python36'
New python executable in F:\ABao\work\Python\myproject\venv\Scripts\python.exe
Installing setuptools, pip, wheel...done.
```
参数--no-site-packages表示已经安装到系统Python环境中的所有第三方包都不会复制过来。  

3. 激活环境。
```
λ venv\Scripts\activate
(venv) λ
```
激活环境之后命令符加上了`(venv)`前缀。  

4. 安装第三方包。  
默认`pip`已经装上。  

```
(venv) λ pip install flask
```

5. 退出当前环境。  
```
(venv) λ deactivate
```
