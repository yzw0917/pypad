from flask import Flask,render_template,request,Response
import pymysql,json

conn=pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db01',
    port=3306,
    charset='utf8')
cur=conn.cursor(cursor=pymysql.cursors.DictCursor)

app = Flask(__name__)
news = 'select * from news'
user = 'select * from user'
cur.execute(news)
res = cur.fetchall()
@app.route("/")
def index():
    return render_template("login.html",u=res) #render函数会检测html语法错误,传参list  web用u.字段
    # cur.close()                        #注意有时虽然关闭了，绿箭头显示依然运行，此时测试错误的
    # conn.close()
    # # return "jj"
# print (u)
cur.close()
conn.close()
#
# #
if __name__ == "__main__":
    app.run()