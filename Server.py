import pymysql
from flask import Flask,render_template, url_for
import json
from flask import request
import time
import Adafruit_DHT

# 生成Flask实例
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('statistics_template.html')

# 接收前端的ajax请求
@app.route('/getData',methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        time = request.form.get("time")
        range = request.form.get("range")
    else:
        time = request.args.get("time")
        range = request.args.get("range")
    return(get_jsondata(int(range),int(time)))

# /getNowHT路由。 获取当前温湿度
@app.route('/getNowHT',methods=["GET", "POST"])
def get_now_ht():
    sensor = Adafruit_DHT.DHT22
    pin = 4 #GPIO4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity = '{0:0.1f}'.format(humidity)
    temperature = '{0:0.1f}'.format(temperature)
    # 整理成json格式
    jsonData = {}
    jsonData['temperature'] = temperature
    jsonData['humidity'] = humidity

    result = json.dumps(jsonData)
    return(result)

def conn_db(): 
    con = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'xxxxx',
        password = 'xxxx',
        db = 'your_database',
        charset = 'utf8'
    )
    return con

# 查询几分钟以内的数据，默认一小时之内的
def get_jsondata(range=1,n=20):
    con = conn_db()
    cur = con.cursor()
    result =  cur.execute("SELECT id,temperature,humidity,create_time FROM ht WHERE DATE_FORMAT(create_time,'%%i')%%%s = 0  AND   create_time >=  DATE_SUB(NOW(), INTERVAL %s MINUTE) order by create_time " %(range,n))
    u=cur.fetchall()
    con.close()
    print(u)
    
    # 整理成json格式
    jsonData = {}
    xTime = []
    yHvalues = []
    yTvalues = []
    
    for data in u:
        # xdays.append(str(data[0]))
        # xTime.append(data[3].strftime('%Y-%m-%d %H:%M:%S'))

        # 直接返回时间戳
        xTime.append(time.mktime(data[3].timetuple()))
        yHvalues.append(data[2])
        yTvalues.append(data[1])
      
    jsonData['xTime'] = xTime
    jsonData['yHvalues'] = yHvalues
    jsonData['yTvalues'] = yTvalues
    
    result = json.dumps(jsonData)
    
    return(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)



