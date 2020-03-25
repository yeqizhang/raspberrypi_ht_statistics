import pymysql

def conn_db(): 
    con = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'xxxx',
        password = 'xxxx',
        db = 'xxx',
        charset = 'utf8'
    )
    return con

# 查询几分钟以内的数据，默认一小时之内的。  
def get_data(n=60):
    con = conn_db()
    cur = con.cursor()
    result =  cur.execute("SELECT id,temperature,humidity,create_time FROM ht  WHERE create_time >=  DATE_SUB(NOW(), INTERVAL '%s' MINUTE) order by create_time " %(n))
    data=cur.fetchall()
    con.close()
    print(data)

get_data(30);    
