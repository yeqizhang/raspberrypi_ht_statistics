# 简介
网络上有很多实时显示树莓派测量的温湿度的例子，但作者没有找到采集数据并能够展示历史数据的现有轮子，于是就自己摸索弄了一个，现在开源出来供大家参考使用，如果有好的修改，欢迎 pr ~
## 概览

* [程序环境](#程序环境)
* [运行指南](#运行指南)
* [可能存在的问题及修改建议](#可能存在的问题及修改建议)

## 程序环境

1. 树莓派（我的是 2B ）

2. DHT22 温湿度传感器（其它传感器比如DHT11需要修改一部分代码。推荐使用 DHT22 ，比 DHT11 精度高）

3. python 3.5+ 、 mysql

4. 导入相关库，例如： Adafruit_DHT 、 pymysql 、 flask 、 json 等。

## 运行指南

上述环境准备工作完成后，将本项目代码下载解压到树莓派中。

#### 数据采集

1. 新建数据库，运行 sql/ht.sql 建立“温湿度采集表”

有需要的话可以使用 test 文件下的 TestConnect.py 、 TestSelect.py 测试数据表是否创建成功。

`python3 TestConnect.py`

![](https://raw.githubusercontent.com/yeqizhang/raspberrypi_ht_statistics/master/images/table.png)

2. 第1步没有问题后，将 HtDataRecord.py 中的数据库配置修改成你自己的， 在树莓派 GPIO4 上插好传感器后，运行

`python3 HtDataRecord.py`

如果打印出温湿度，数据库也插入成功，继续进行下面的数据展示。

#### 页面展示

修改 Server.py 中的数据库连接配置，并运行

`python3 Server.py`

在浏览器输入: *http://树莓派ip:5000* 统计图能够展示，则表示部署成功。

![](https://github.com/yeqizhang/raspberrypi_ht_statistics/raw/master/images/page.png)

#### 开机启动

`vi /etc/rc.local`

参考 *config/rc.local* 的配置。

## 可能存在的问题及修改建议

* 由于作者住在广州，温度最低是 5 摄氏度左右，不会有什么问题，未测试 0 度以下是否存在 bug 。

* 采集频率目前设置为 5 分钟测量 1 次，你也可以设置成 1 分钟采集 1 次；如果设置其它采集频率例如 2 分钟、 3 分钟等，查询及展示那块需要修改。

* 目前的查询策略是，查 1 天的数据支持查 5 分钟、10 分钟的颗粒精细度；7天之内则以30分钟为颗粒度； 30 天以内则为 60 分钟。更多的时间由于目前作者采集的数据不太好测试，暂未开发。查询的时间范围以及精细度由前端传入后台。

* 需要外网访问建议安装 ZeroTier 。


