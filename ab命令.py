import os
os.system("ab -n 20000 -c 10 -k http://58.63.236.212/")   #无返回值运行

# d = os.popen("ab -n 200 -c 1 -k http://58.63.236.212/")  #先运行，在返回结果，可以判断结果或者在结果中提取和查找
# print(d.read())
