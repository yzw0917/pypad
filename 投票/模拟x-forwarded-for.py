#模拟x-forwarded-for
#requests.get(url)不构造头信息，服务器能返回python的request信息
# @app.route('/getInfo')def hello_world():
#    if(str(request.headers.get('User-Agent')).startswith('python')):
#    return "小子，使用爬虫是吧？滚你的"
#    else:
#    return "这里假装有很多数据"
import threading
import requests,random
url = 'http://www.baojinews.com'
cookies = {'_ga': 'GA1.2.1078940745.1527045185'}
def zuhe():
    byte01=random.randint(1,254)
    byte02=random.randint(1,254)
    byte03=random.randint(1,254)
    byte04=random.randint(1,254)
    return (str(byte01)+'.'+str(byte02)+'.'+str(byte03)+'.'+str(byte04))

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting " + self.name)
        for t in range(100):
            try:
                crawler(self.name)
            except:
                break
        print("Exiting " + self.name)

def crawler(threadName):
    url = "http://192.168.1.1"
    try:
        ip = zuhe()
        headers = {'CLIENT-IP': ip, 'X-Forwarded-For': ip, 'content-type': 'application/json'}
        r = requests.get(url, headers=headers, cookies=cookies, timeout=20)
        # r = requests.get(url, timeout=20)
        # 打印线程名和响应码
        print(ip,headers)
        print(threadName, r.status_code)
    except Exception as e:
        print(threadName, "Error: ", e)

threads = []

# 开启10个线程
for i in range(200):
    # 给每个线程命名
    tName = "Thread-" + str(i)
    thread = myThread(tName)
    thread.start()
    # 将线程添加到线程列表
    threads.append(thread)

# 等待所有线程完成
for t in threads:
    t.join()

