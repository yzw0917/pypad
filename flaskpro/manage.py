from flask import Flask
from flask_script import Manager
# import app.views   # app文件夹下的views.py 包特征 __init__.py  循环导入报错

from app import create_app

app = create_app()

manager = Manager(app=app)




if __name__ == '__main__':
    manager.run()
