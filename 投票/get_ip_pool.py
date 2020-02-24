import re,random,sys,time,datetime,threading
import win32api, win32con
from random import choice

import bs4
import requests
# def get_ip():
#     """获取代理IP"""
url = "http://www.xicidaili.com/nn"
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
            "Referer":"http://www.xicidaili.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
r = requests.get(url,headers=headers)
# r=requests.get(url) #不用参数加headers，网站禁止访问！
# print(r.text)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
data = soup.table.find_all("td")  #only td area
ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 创建表达式
port_compile = re.compile(r'<td>(\d+)</td>')                # 创建表达式
ip = re.findall(ip_compile,str(data))       # 获取所有IP
port = re.findall(port_compile,str(data))   # 获取所有端口
ippools=[":".join(i) for i in zip(ip,port)] #很神奇的zip函数
print(ippools)
    # return [":".join(i) for i in zip(ip,port)]
win32api.MessageBox(0, str(ippools), "消息框标题", win32con.MB_OK) #消息框无法复制
