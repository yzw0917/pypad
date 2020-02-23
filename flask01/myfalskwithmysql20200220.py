from flask import Flask,render_template,request
import pymysql

conn=pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db01',
    port=3306,
    charset='utf8')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

app = Flask(__name__)

@app.route("/")
def index():
    sql1 = 'select * from news '
    cur.execute(sql1)
    u= cur.fetchall()
    return render_template("login.html",u=u)


@app.route("/chuli",methods=['POST'])    #不加参数，默认请求get.
def chuli():                             #测试显示：网址确实加了路由命令：127.0.0.1:5000/chuli
  username= request.form.get("uname")
  pwd=request.form.get("pwd")
  sql='select * from user where name = %s and pwd =%s'

  if cur.execute(sql,(username,pwd)):
      return render_template("index01.html",msg="登陆成功！")
  else:
      sql1 = 'select * from news '
      cur.execute(sql1)
      u = cur.fetchall()
      return render_template('login.html',msg="登录失败！",u=u)
#
# cur.close()  #打开项目 和打开文件 运行环境不同，可能文件找不到
# conn.close() #这里关闭连接会导致路由里面失效
    
if __name__ == "__main__":
    app.run()