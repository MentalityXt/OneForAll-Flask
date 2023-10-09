# OneForAll-Flask
最新版的ARL并没有集成OneForALl,需要下载旧版本斗象开发的ARL才有集成
基于这种情况,我就想能不能在搭建一个在公网上就能访问的OneForALL,类似于ARL,也可以在公网上访问,不用在本地安装

该项目十分简单，只满足了最初的需求,只能提交单个url或者文件

# 配置api参数(很重要)

打开 flask_api.py 文件

端口配置在最下面的
app.run(host="0.0.0.0" ,port=30100, threaded=True)
将port参数改成自己想要的端口即可

最上面有两个参数
path_token = "abcdefghijklmn"
cookie_token = "admin123456"

我一直在想这么差劲的项目如何搞好安全,不能被别人访问,因为有几个接口名为index、file 等等,很容易泄露
path_token 为路径节点
可以去随机密码生成器处生成,网上有很多

设置完 path_token 之后
访问 127.0.0.1:30100/abcdefghijklmn(ip:port/path_token)

然后会出现输入token的框
这次输入cookie_token里的参数点击提交即可(这里为 admin123456)

并且如果访问不存在的节点或者没有携带正确的token,都会返回404及空页面
# -------------------------------------------------------------------


# 使用教程:

pip install -r requirements.txt

python flask_api.py

移到vps后台运行可以看这篇文章 https://blog.csdn.net/qq_34562959/article/details/130519967

OneForAll原版配置可以在setting里面改,https://github.com/shmilylty/OneForAll 作者写的很详细了

感谢原作者!

