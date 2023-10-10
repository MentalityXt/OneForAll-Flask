# OneForAll-Flask
最新版的ARL并没有集成OneForAll,需要下载旧版本斗象开发的ARL才有集成
基于这种情况,我就想能不能在搭建一个在公网上就能访问的OneForALL,类似于ARL,也可以在公网上访问,不用在本地安装

该项目十分简单，只满足了最初的需求,只能提交单个url或者文件

# 配置api参数(很重要)

打开 flask_api.py 文件

端口配置在最下面的

app.run(host="0.0.0.0" ,port=30100, threaded=True)

将port参数改成自己想要的端口即可

------------------------------------------------------

最上面有两个参数

path_token = "abcdefghijklmn"

cookie_token = "admin123456"

我一直在想这么差劲的项目如何搞好安全,不能被别人访问,因为有几个接口名为index、file 等等,很容易泄露



path_token 为路径节点

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

# 运行截图

![1.png](https://github.com/MentalityXt/OneForAll-Flask/blob/main/images/1.png)


![2.png](https://github.com/MentalityXt/OneForAll-Flask/blob/main/images/2.png)


![3.png](https://github.com/MentalityXt/OneForAll-Flask/blob/main/images/3.png)

# 一些我发现的问题

1、没有一个好看的界面和更多的选项

2、为了安全和隐蔽性需要输入两次token，对于其他人返回只有404+空页面，但是回包的 Server:Werkzeug/2.0.3 Python/3.6.8 会显示出来，其他人会知道该端口开启了服务，并且指纹都能看到

3、对于文件管理系统，我并没有测任意文件下载方面的漏洞，我个人感觉很大概率有，但是下载的时候要验证token，只有自己会用，我就没管

4、文件管理系统没有跳转页面的功能，比如temp子文件夹，无法跳转看里面的情况，因为每个域名扫描结果是移到results文件夹里的 域名.csv 的，加上可能需要下载sqlite的数据库，我就把文件管理系统只做到了 results 文件夹，temp文件夹里更多的是跑输出的json类型的数据，属于原始数据，而 results 文件夹里的csv数据算是整理好了的

# 后面的想法

后续可能有想法将后端接口对接 goby,awvs 等扫描器，但是跑子域并不等于所有的资产都能处理完，所以需要一种fofa，hunter，同ip资产 等等能一起处理资产的工具或者方法,而fofa和hunter的api接口都需要付费，所以后续的想法就是利用arl跑完之后，在运行oneforall的接口跑完，最后全部整合放到goby里统一漏扫，算是一种集成的方法了

