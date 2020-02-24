from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/tijiao',methods=["POST"])
def tijiao():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
