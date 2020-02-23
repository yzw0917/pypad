import pymysql

#建立链接：
conn=pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db01',
    port=3306,
    charset='utf8'
)
# 建立游标
cur=conn.cursor(cursor=pymysql.cursors.DictCursor) #注意DictCursor大小写

sql='select * from news '

res=cur.execute(sql)
dict01=cur.fetchall()
for items in dict01:
    print(items)

# 及时关闭链接
cur.close()
conn.close()