from flask import Flask,render_template,request
import pymysql

conn=pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db01',
    port=3306,
    charset='utf8')
cur=conn.cursor(cursor=pymysql.cursors.DictCursor)

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("login.html" )


@app.route("/chuli",methods=['POST'])    #不加参数，默认请求get.
def chuli():                             #测试显示：网址确实加了路由命令：127.0.0.1:5000/chuli
  username= request.form.get("uname")
  pwd=request.form.get("pwd")

  sql='select * from user where name = %s and pwd =%s'

  if cur.execute(sql,(username,pwd)):
      return render_template("index01.html", msg="登陆成功！")
      #这里保存cookie，在新的页面要验证
     #http://127.0.0.1:5000/templates/index01.html地址栏直接敲调不出来的
  else:
    #  return "登录失败"
      return render_template("login.html", msg="登录失败！")





# <form action="chuli"" method="POST">  这个chuli是一个动作
#     yonghuming:<input type="text" name="uname"  > key:value uname:XXX
#     mima :<input type="password" name="pwd"  >    pwd:XXXX
#     <input type="submit" value="   提   交   "> {他会组合成一个字典发送}
#
# </form>
#
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    app.run()

   # app.run(host="192.168.1.103")  #debug模式打开，修改后不用重启服务器，但是生产环境冲突了
 # 点进去run（） 查看参数说明
  #  def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):