# racoon
Racoon是一个渗透工具，它由web浏览器作人机界面，flask提供api接口并调度后台任务，通过sqlalchemy操作数据库，目前已实现目标网站http状态码检测等功能。


## require
``` sh
yum install epel-release -y
yum install python36 -y
pip3 install sqlalchemy requests
```

## deploy
``` sh
cp /usr/bin/python3.* /usr/bin/python3
./run
```






