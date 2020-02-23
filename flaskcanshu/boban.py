from flask import Flask,render_template,redirect,session

app = Flask(__name__,template_folder="views")


# @app.route('/')
# def ppoe():
#      htm=open("views/main.html").read()
#      return htm


@app.route('/')
def ppoe():
     return  render_template("main.html")

@app.route('/bd')
def bd():
    return  redirect("http://www.baidu.com/")  #重定向：代码号302


if __name__ == '__main__':
    app.run(debug=True)