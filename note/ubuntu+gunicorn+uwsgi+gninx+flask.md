1. [ubuntu 部署Flask（阿里云)](https://zhuanlan.zhihu.com/p/28204251)
2. [部署Flask(阿里云+gunicorn)](https://www.cnblogs.com/homeworknotes/p/11219902.html)
3. [nginx+uwsgi, nginx+gunicorn区别和部署](https://www.jianshu.com/p/be2b587a900e)
4. [uWSGI vs Gunicorn](https://zhuanlan.zhihu.com/p/50857407)
5. [gunicorn flask](https://zhuanlan.zhihu.com/p/88422780)





# **阿里云服务器超级详细配置（FLASK+UWSGI+NGINX）**

 

## **一准备工作：**

 

我们先到阿里云官网注册和登录以及实名认证,然后可以在官网上购买收费的云服务器或者领取一个月免费的云服务器。

官网：https://www.aliyun.com/

阿里云：https://free.aliyun.com/

 

我们这次安装的是Ubuntu 18.04 64位 阿里云目前最新版的系统。

![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422171616419-1426674749.jpg)

------

输入root密码 记住哦~这个就是登录服务器的密码

![img](data:image/jpeg;base64,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)

服务器地址，第一个(￣▽￣)"复制一下~

![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422171636733-1310270030.jpg)

![img]()

配置安全组，主要设置容许你的网页访问的端口。。。go on~

![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422171653648-88696654.jpg)

![img]()

端口范围和授权对象必须要写哦，0.0.0.0/0就是对所有人公开~

![img]()

 ![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422171715679-812444765.jpg)

OK，下面我们进入我们的服务器，当然如果你的不是阿里云的服务器也可以，你的服务器装好系统之后可以从这一步开始：

![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422171741459-1108046471.jpg)

下载putty，SSH啥的 你自己随意，我觉得这个顺手一点吧。黑色的地方填写服务器地址 其他不变。然后OPEN！

 

**![img]()**

 

## 二、进入ubunru终端界面并创建虚拟环境：

   输入密码进来之后：

   **![img]()![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422171856648-2108534583.jpg)**

   **第一个命令，更新服务器列表  O(∩_∩)O**

###    1.apt-get update   

   

###    2.这个mysql需要就装。 

​     如果你用的sqlite,这个可以不装，以后需要再装也行，但是还是要说一下：

​    apt-get install mysql-server  

​    apt-get install libmysqlclient-dev   

​     装完之后可以用命令查看安装的包和软件：

​     dpkg -s mysql-server

​     ![img]()![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422171912239-1849702853.png)

 

###    3.如果你安装了mysql，就顺便把redis也安装一下，redis是什么，后面有说明的，想了解的可以去看看。

​     apt-get install redis-server   redis的安装（缓存数据库）

  

 

###    4. 安装 virtualenv （虚拟环境）：

​     安装一下 pip 

​     **apt install python-pip**

​     

​     **再安装** pip install virtualenv

 

​    pip3 install virtualenvwrapper （虚拟环境管理工具） (如果是python3 切换下)

 

   至此虚拟环境就安装好了 O(∩_∩)O 恭喜你完成了很多人要爬很多坑的一步。

### **这里应该有分割线--------------------------------------------------------------------------------------**

 

接下来我们看下 virtualenvwrapper.sh 的位置，为什么要看呢，因为我们的服务器怕找不到虚拟环境所需要的文件， 

​     使用命令 ：which virtualenvwrapper.sh  然后添加以下代码

​     **![img]()![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422172028648-1008582795.png)**

​     编辑~/.bashrc文件,内容如下:（vim ~/.bashrc  修改文件用 i 命令，改完之后 ，输入:wq 保存退出）

​       （ 每一个用户在进入home目录后，其中都会有一个隐藏文件.bashrc 

按ctrl+h可以显示隐藏文件，该文件保存该用户角色下的环境变量，所以直接打开终端时，运行的命令都是从 这 个.bashrc中去寻找）

如果一切顺利的话  那么在创建可能会提示 【/usr/bin/python: No module named virtualenvwrapper】

这样的提示，没关系，那是因为：

我这个用的3.5版本安装的这个环境，系统的2.7版本是没有的。解决：

先查看python3 的位置：

which python3

然后在刚刚的 .bashrc 文件中修改 ：

export WORKON_HOME=$HOME/.virtualenvs/ 

export PROJECT_HOME=$HOME/workspace/ 

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

source /usr/local/bin/virtualenvwrapper.sh

![img]()![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422172045499-1543948575.png)

最后千万一定要加上这条命令，马上执行：

**source ~/.bashrc**

 

------

这个时候 虚拟环境已经配置好了

这个时候便是创建虚拟环境。

创建py3_flask的虚拟环境：

mkvirtualenv -p python3 py3_flask

进入虚拟环境：

**workon py3_flask**

这个时候 会有变化哦,是不是root前面已经有（py3_flask）了，代表我们已经进入这个虚拟环境了

(py3_flask) root@*******:

使用 pip list就可以查看当前虚拟环境安装了哪些包了。

 

附上虚拟环境操作命令：

 

mkvirtualenv env1：创建运行环境 env1

workon env1: 工作在 env1 环境 或 从其它环境切换到 env1 环境

deactivate: 退出终端环境

其它的：

rmvirtualenv ENV：删除运行环境ENV

mkproject mic：创建mic项目和运行环境mic

mktmpenv：创建临时运行环境

lsvirtualenv: 列出可用的运行环境

lssitepackages: 列出当前环境安装了的包

 

 

创建的环境是独立的，互不干扰，无需sudo权限即可使用 pip 来进行包的管理。

 

 

 

------

## **三、安装uwsgi:**

再升级下我们的 pip  （如果提示 PIP 需要升级 可以这样：pip3 install --upgrade pip 升级PIP）**
**

安装也很简单，进入到虚拟环境安装，查看虚拟环境 ：workon

我的就提示py3_flask

workon py3_flask 进入：

查看当前的路径 和虚拟环境 是不一样的 比如pwd 命令显示的路径并没有 虚拟路径在内，尤其注意。

那要怎么查看虚拟环境 包安装的位置呢？很简单，我们只要看下我们知道的其中一个包的位置就可以了

比如 python3 

输入： which python3

/root/.virtualenvs/py3_flask/bin/python

你看 就得到了当前的虚拟环境/root/.virtualenvs/py3_flask

uwsgi 的安装 就是pip3 uwsgi

如果觉得慢可以选择安装源，比如这样：

**pip3 install -i https://pypi.douban.com/simple uwsgi**

使用的 豆瓣的源 速度会快很多哦。

OK，安装好了 uwsgi 那么下一步就要安装 FLASK

## **四、安装FLASK**

一样的安装方法：用pip install flask

哦 ~ 失败，呵呵 那就**pip3 install flask** ：）

呵呵 刚刚和你开个玩笑，让你明白现在的环境是pip3说了算 - -!

其实很快就装好了 对不对，

OK下面 我们用Flask 来测试下我们的网页：

你要用 vim工具 修改下 app.py的一些小参数

app(host='0.0.0.0'，port=5000 , debug='True')

![img]()![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422172254508-702503269.png)

这个界面是不是很熟悉

 如果你是云服务器的话 就这样改就可以，端口你随意，我干了。

然后保存退出 vim ，好了第一次运行我们的网站：

python3 app.py

浏览器打开 输入网址:5000

不要忘记加端口哦。

是不是看到网页了。OK，

## **五、安装 nginx：**

sudo apt-get install nginx

**![img]()![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422172309627-1791471637.png)**

下载ngnix 也是在虚拟环境。

安装ngnix的方法也很简单

很快就安装好了

如果出问题了，？@！

那好吧，升级下 sudo apt-get updata

在安装就可以了。

安装好了之后就是最重要的配置了。

## **六、配置uwsgi和nginx:**

需要拷入你的项目到文件夹下：

一般推荐使用工具，比如【winscp】，把项目文件放好，一般放在HOME目录。

 

![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422172321328-838256855.png)

 

说一下配置文件的位置：

nginx的在etc文件夹下的nginx文件夹里：

uwsgi的 需要自己创建ini文件 放在虚拟目录就可以了，位置随便。

![img](https://img2020.cnblogs.com/blog/2016399/202004/2016399-20200422172331988-1016040829.png)

------

 

 

[uwsgi]

chmod-socket = 666         

socket =127.0.0.1:5000     #和nginx配置的端口号

\#http=0.0.0.0:5000       #单独启动uwsgi时使用

chdir=/home/51job/51_flask  #项目路径

wsgi-file=app.py         #项目启动文件

home = /root/.virtualenvs/py3_flask/   #这个是项目的虚拟路径

callable=app         

processes=4         

threads=2

master=True

pidfile=uwsgi.pid

daemonize=uswgi.log

\-------------------------------------------

如果只想测试下 uwsgi 是否成功，

那么改成这样：

[uwsgi]

\#chmod-socket = 666

\#socket =127.0.0.1:5000

http=0.0.0.0:5000

chdir=/home/51job/51_flask       #你的项目目录

wsgi-file=app.py             #你的启动文件 

home = /root/.virtualenvs/py3_flask/  #这就是你的虚拟目录，还记的开始的时候说的怎么得到虚拟目录吗？

callable=app

processes=4

threads=2

master=True

pidfile=uwsgi.pid

daemonize=uswgi.log

就可以了在uwsgi上访问了，注意浏览器的端口:5000哦

------

OK，下面就是ngnix的配置，so easy！！！

哎 说简单 其实我可是趴了俩天的坑啊 -，-

events {

​    worker_connections 768;

​    \# multi_accept on;

}

http {

server {

​                listen     80;         #监听端口，就是网站端口啦

​                server_name   XXX.XXX.XXX.XXX  #你的服务器地址,也可以是你的域名

​                charset     utf-8;

​                location /static {

​                            alias  /home/51job/51_flask/static;

​                               \#这个是你项目的JS文件地址，是不是很熟悉static

​                }

​                \#location /upload {

​                   \#alias  /var/www/datavis/taihesite/upload;

​                \#}

​                location / {

​                   uwsgi_pass  127.0.0.1:5000;#这个是与你对接的uwsg的地址端口

​                   include   /etc/nginx/uwsgi_params;

​                }

}

​    \##

​    \# Basic Settings

​    \##

 

**复制下面这段代码到相应位置就可以了，注意覆盖哦，需要修改的地方 我都做了标记了，如果复制下来 请把注释去掉哦**

 

 

## 七、启动服务器：

uwsgi uwsgi.ini

service nginx start

这样就启动了。。。

顺便说下停止服务器的方法：

sudo pkill -f uwsgi -9 停止uwsgi 最有效的办法 都不需要输入pid 去 KILL

service nginx stop    停止 nginx

 

那就一其说一下吧：

service nginx restart   重启Nginx服务

service nginx status   Nginx服务的状态

service nginx reload 在Nginx服务启动的状态下，重新加载nginx.conf这个配置文件

sudo nginx -t     检查nginx 配置是否正确

 

 

**至此终于完成了所有的配置 ，你的服务器应该已经可以访问了，假如，还不能启动，那肯定都是小问题，无非就是版本不匹配啥的，**

**对于这样的问题 最好的办法就是 sudo atp-get update**

 

**下面说一下其他的一些问题的解决办法：**

 

1、uwsgi uwsgi.ini

 

   此时如果提示端口已经被占用，则可以尝试换个端口或者使用kill命令杀死占用该端口的进程。

  使用：

   ps -aux | grep uwsgi

会列出和uwsgi相关的进程，然后使用:kill -9 [PID] 杀死进程。

 

2、卸载包或则软件：

   在终端中找到你需要卸载的软件的名称，列表是按照首字母排序。用这个命令：

   dpkg -s    包的名字检查 ,是否安装了某个软件

   dpkg -l 列出所有安装的软件

比如卸载：

  sudo apt-get --purge remove uwsgi

 

3、安装文件 这个就不说了吧，算了还是提一下：

   sudo apt-install xxx 安装软件 （最高权限安装 sudo 表示 “superuser do”，前提你是超级管理员）

   sudo apt-get是用来安装linux下的各种工具包的。

 

4、为什么要安装两个数据库（mysql，redis）？

​    本身的持久化，会可能丢失数据，因为本身的持久化，不是实时的，是数据先在百内存，再定时的保存到硬盘来达到持久化，当然，这个定时的时间相度隔，是可以配置的。

这个配置的时问间，如果太短，那么使用redis的效率就低，如果长了，那么可能丢失的数据就会多，所以，要根据自己的答业务来取得一个均衡。保存到数据库的，可以理解为比较保险，redis出现问题，还可以从数据库中恢复内过来

从两者的擅长角度来看，数据库擅长的容是存储和检索redis相当于内存数据库，擅长的地方是读结合两个的擅长点来使用，才是王道。

 

5、指定安装包的版本比如：

   sudo pip install flask==0.10.1

 

6、查看当前工作路径只需要一个命令即可：pwd ，啥意思不就是 password缩写吗，hhhhh。好记吧。

 

7、一下杂项：

   •查看目录内容 ls

   • 切换目录 cd

   • 创建和删除操作 touch , mkdir , rm

​     ls 命令:

   • ls 是英文单词 list 的简写，其功能为列出目录的内容，是用户最常用的命令之一，类似于 DOS 下的 dir 命令

​    ls 常用选项

 

   参数  含义

   -a  显示指定目录下所有子目录与文件，包括隐藏文件

   -l  以列表方式显示文件的详细信息

   -h  配合 -l 以人性化的方式显示文件大小

   Ls  的相关选项

   -a 显示所有（包括隐藏）

   -l 以列表形式显示每个文件的详细信息

8、还有什么呢？我想想：

   vim 编辑器推出的方式

   先是 选择文件 进行编辑  vim ~/ 加文件名

   进去之后 按 i 插入的意思 进行编辑

   编辑结束 按 冒号 ： 然后输入 WQ 意思 就是 写入 推出。

   还有俩种方法 ：

​     1：在最后输入命令时，直接输入"x"，也是一样的，即X=wq。

​     2：最快捷的方法：按了ESC后，直接按shift+zz，或者切换到大写模式按ZZ，就可以保存退出了，即是按2下大         写的Z。

 

9、查看命令：cat 可以查看文件内容：如：cat /usr/local/con.cfg

   source命令也称为“点命令”,也就是一个点符号(.)。source命令通常用于重新执行刚修改的初始化文件,使之立即    生效,而不必注销并重新登录

 

10、加入有人告诉你，遇到问题 只要 rmdir, 那是在坑你哦~

   删除目录：rmdir 可使用rmdir命令删除一个目录。必须离开目录，并且目录必须为空目录，不然提示删除失败。

   删除文件：rm（推荐使用）加上 i 询问是否删除 -f 是强制删除  -r递归删除目录下的所有内容

   sudo rm /文件路径  

 

11、设置python版本的优先级，我觉得很重要吗，前面也说过了：

设置python3 优先级

首先使python3.6优先级较高：

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

最后修改为默认：

sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150

 

根据自己的版本修改哦。

 

12、这个有点不一样：

   为Python 3安装pip：

 

   sudo apt install python3-pip

 

13、安装开发工具

 

我们还将安装用于构建Python模块所需的开发工具，以供Python 3运行：

 

sudo apt install build-essential python3-dev python3-setuptools

 

假设我们想要安装一个名为scrapy的包，我们可以通过发出以下命令来实现：

 

pip install scrapy

 

scrapy是用于抓取网站并提取结构化数据的Python库

 

卸载程序包运行：

 

pip uninstall scrapy

 

从PyPI搜索软件包：

 

$pip search "search_query"

 

列出已安装的软件包：

 

$pip list

 

要列出过期的软件包：

 

$pip list --outdated

 

ps -aux |grep uwsgi 列出uwsgi 运行目录

 

14、查看版本和日志：

 

查看日志，命令: tali -f catalina.out

 

查看版本 ：java -version

 

15、端口占用和文件查找的问题：

查看运行文件及目录

which python  

 

查看文件安装及目录

whereis python

 

查看端口占用

lsof -i :8000

 

杀死端口占用程序

sudo kill -9 pid

 

杀死所有有nginx有关的进程

sudo killall -9 nginx

 

查询与nginx有关的进程

ps aux | grep nginx

 

 

 