import math
import time
scale=10
print("执行开始")
t=time.process_time()
for i in range(scale+1):
    a,b='**'*i,'..'*(scale-i)
    c=(i/scale)*100
    π=4*(4*math.atan(1/5)-math.atan(1/239))
    print("%{:3}[{}->{}]".format(a,b,c))
    time.sleep(0.1)
print(π)
print("{:.2f}s".format(t))
print("执行结束")
