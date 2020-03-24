import Adafruit_DHT
import pymysql
import time
import datetime
site = "卧室" # 传感器安装位置

# m分钟采集一次. 最大频率为1分钟一次
def record_by_minute(m=1):
    sensor = Adafruit_DHT.DHT22
    pin = 4 #GPIO4
    
    con = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'xxxx',
        password = 'xxxx',
        db = 'your_database',
        charset = 'utf8'
    )
    
    while True:
        while True:
            now=datetime.datetime.now()
            if now.minute % m == 0:
                break
			# 过50秒进行一次判断
            time.sleep(50)
            
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            cur = con.cursor()
            print(datetime.datetime.now())
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            cur.execute("insert into ht(create_time,site,temperature,humidity) value(now(),'%s','%s','%s')" %(site,temperature,humidity))
            con.commit()
            cur.close()
            # 采集一次后等待一段时间再判断，不能少于60s；少于60会出现同一分钟多次记录
            time.sleep(60)
        else:
            print('Failed to get data from Adafruit_DHT22!')
            time.sleep(5)
        
    con.close()
              
record_by_minute(5) 

