import pymysql

username=input("your neme:")
pwd=input("password:")

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
cur=conn.cursor()

sql='select * from user  where name="%s" and pwd="%s"'%(username,pwd)
    # sql语句防止拼接，有漏洞的
    # 这里有一个SQl注入漏洞：sql注释--会屏蔽后面的命令
    # 比如用户输入 qwqwqw" or 1=1 -- qweqweqw

print (sql)

res=cur.execute(sql)
print (res)
if res:
    print ("登陆成功")
else:
    print("登录失败")

# 及时关闭链接
cur.close()
conn.close()