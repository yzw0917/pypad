
#
# def init_route(app):
#     @app.route('/')
#     def hello_world():
#         return 'Hello World!  Hello World! '
#
#     @app.route('/121/')
#     def  e1():
#         return  'luyoufenzhi'
from flask import Blueprint

blue=Blueprint('blue',__name__)

@blue.route('/')
def index ():
    return '蓝图的路由器插件'


@blue.route('/121/')
def  e1():
 return  'luyoufenzhi'