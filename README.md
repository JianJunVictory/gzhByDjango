# 微信服务号开发
## 基于python的web框架Django开发微信公众号

### 环境
1.python 版本3.6  
2.Django 1.11.0  
3.数据库使用Django自带的sqlite3  
4.windows系统  
5.内网透传工具ngrok,使用免费版,域名是变化的，每次域名变化，需要的工程设置文件中,修改ALLOWED_HOSTS,将域名填写进步,例如：此项目中web文件夹下的settings.py中的ALLOWED_HOSTS = ['c0520119.ngrok.io']

### 开发环境搭建
1.安装python3.6，到官网下载python安装文件，自行安装，安装完成后，验证下环境路径。  
2.安装django,使用pip 命令安装。如果没有pip命令，请自行上网查询安装。pip install django  
3.创建项目,App。请到[django官网](https://docs.djangoproject.com/zh-hans/2.0/)查看django教程    

### 代码结构
├─.vscode  
├─web  //项目文件  
└─wechat  //文件公众号app  
&nbsp;&nbsp; ├─migrations  
&nbsp;&nbsp; └─wechatApi  //微信接口，例如菜单创建，删除，获取等等




