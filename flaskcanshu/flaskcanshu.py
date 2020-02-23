from flask import Flask

app = Flask(__name__)


@app.route('/<string:name02>')
def ppoe(name02):
    print(name02)
    return '<h1>Hello World! %s</h1>'%name02



if __name__ == '__main__':
    app.run()
