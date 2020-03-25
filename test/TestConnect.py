import pymysql
 
con = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'xxxx',
    password = 'xxxx',
    db = 'xxxxx',
    charset = 'utf8'
)
cur = con.cursor()
cur.execute("show tables")
data=cur.fetchall()
print(data)
