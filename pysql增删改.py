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
cur=conn.cursor(cursor=pymysql.cursors.DictCursor) #注意DictCursor大小写

sql='insert into  user (name,pwd) values(%s,%s)'
    # sql语句防止拼接，有漏洞的
    # 这里有一个SQl注入漏洞：sql注释--会屏蔽后面的命令
    # 比如用户输入 qwqwqw" or 1=1 -- qweqweqw
    # 给字符川传参  vs  字符串拼接
print (sql)

res=cur.execute(sql,[username,pwd])  #pysql帮我们解决SQl注入问题 这里可用[数组] (元祖) {字典}
conn.commit() #数据变动提交之前只存在缓存中
print (res)

if res:
    print ("改动成功")
else:
    print("改动失败")


cur.execute('select * from user') #cur相当与光标指向记录
print(cur.fetchall())

# 及时关闭链接
cur.close()
conn.close()