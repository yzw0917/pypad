from flask import Flask,render_template,request,Response
from flask_script import Manager
import pymysql,json


app = Flask(__name__)
manager = Manager(app=app)

conn = pymysql.connect(
   host='127.0.0.1',
   user='root',
   password='root',
   database='db01',
   port=3306,
   charset='utf8'
)
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

@app.route("/")
def index():
   return "hello world123546545646546456"

@app.route("/admin")
def admin():
   sql="select * from user"
   cur.execute(sql)
   res=cur.fetchall()  #踩坑啊！Response大些啊！
   resp=Response(json.dumps({
      "data":res

   }))
   return resp



if __name__ == '__main__':
   manager.run()    #可以方便加参数 python manager.py runserver -p 8000  --threaded
