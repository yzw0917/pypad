from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)

@app.route("/")
def index():  #一条路由跟一个函数，至于函数名称，无所谓
     #动态页面，从页面接受数据，比如用户登录界面，将用户名和密码在提交时打包发送上来
   return render_template("login.html", )


@app.route("/chuli",methods=['POST'])    #不加参数，默认请求get.
def chuli():                             #测试显示：网址确实加了路由命令：127.0.0.1:5000/chuli
#接受用户的数据，必须用到request模块           但是文件结构并没有增加chuli 的文件
  username = request.form.get("uname")
  pwd=request.form.get("pwd")
#另外一种传参： url传参
#  request.args.get()


# 链接mysql数据库以后
# select * from usrs where usrname = %s and assword =%s
# 能查到数据就是登陆成功，否则登录失败
  if username=="root" and pwd == "123456":
      return "登陆成功！"
  else:
    #  return "登录失败"
      return render_template("login.html", msg="登录失败！")





# <form action="" method="POST">
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