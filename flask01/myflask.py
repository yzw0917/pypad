{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [15/Feb/2020 17:50:00] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [15/Feb/2020 17:50:07] \"\u001b[37mGET /002 HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,render_template  #html页面调用的程序render_template\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "#路由指向\n",
    "@app.route(\"/\")\n",
    "def index():       #这个函数名字随意，他就是路由指定根目录后执行的函数\n",
    "       #这里是处理提交到跟目录请求的处理代码的地方\n",
    "  return''' hello world '''  #实际应用中不直接返回相应，而是返回HTML模板\n",
    "                             #flask默认的页面模板都放在/templates目录下\n",
    "\n",
    "@app.route(\"/002\")   #第二个路由\n",
    "def index02():     \n",
    "    return''' <h1>第二个页面 </h1>'''\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "  app.run()\n",
    "\n",
    "#模板->html页面  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "from flask import Flask,render_template  #html页面调用的程序render_template\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index(): \n",
    "  return render_template(\"index01.html\")\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "  app.run()\n",
    "#调试模式：以app“_main_”运行  保存到myflask。py以后可以程序运行\n",
    "#至此  文件夹结构为   myflask.py 以及/templaters/html集合"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# ! calc.exe       #调用外部EXE\n",
    "# %run tuling.py    #运行py程序\n",
    "%run myflask.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,render_template  #html页面调用的程序render_template\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")  \n",
    "\n",
    "def index(): \n",
    "     #动态页面，在函数这部分定义变量，在通过入口传给页面，此时，页面可以调用了\n",
    "   s = \"我是一个字符串变量\" \n",
    "   liebiao=[\"liebiao01\",\"列表2\",\"咧biao\",\"列表4\"]\n",
    "   return render_template(\"index01.html\",str1 = s,lis1 = liebiao)  #renturn 与 s没有对齐 竟然报错了\n",
    "                              #注意传过去的参数，html要正确的接收\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "  app.run()  #debug模式打开，修改后不用重启服务器，但是生产环境冲突了"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [15/Feb/2020 19:20:20] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [15/Feb/2020 19:20:20] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,render_template  \n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")  \n",
    "\n",
    "def index(): \n",
    "     #动态页面，从页面接受数据，比如用户登录界面，将用户名和密码在提交时打包发送上来\n",
    "   return render_template(\"login.html\",) \n",
    "                           \n",
    "#  form action=\"\" method=\"POST\">   action表示表单发到哪里   post 隐式提交\n",
    "#     yonghuming:\n",
    "#     mima :\n",
    "\n",
    "# </form>    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "  app.run()  #debug模式打开，修改后不用重启服务器，但是生产环境冲突了"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
