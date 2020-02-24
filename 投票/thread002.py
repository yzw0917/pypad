import requests
import threading


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                crawler(self.name)
            except:
                break
        print("Exiting " + self.name)


# 定义功能函数，访问固定url地址
def crawler(threadName):
    url = "http://www.baojinews.com"
    try:
        r = requests.get(url, timeout=20)
        # 打印线程名和响应码
        print(threadName, r.status_code)
    except Exception as e:
        print(threadName, "Error: ", e)


# 创建线程列表
threads = []

# 开启10个线程
for i in range(20):
    # 给每个线程命名
    tName = "Thread-" + str(i)
    thread = myThread(tName)
    thread.start()
    # 将线程添加到线程列表
    threads.append(thread)

# 等待所有线程完成
for t in threads:
    t.join()
