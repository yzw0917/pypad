#
import re,time
from typing import List
from urllib.request import Request, urlopen
import gzip, zlib


firefox_headers = {'User-Agent': " Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0 ",
                   "Accept-Encoding": "gzip, deflate"}
# 网站获取数据Api
for i in range (1,3):
    url = 'http://t.weather.sojson.com/api/weather/city/101250105'
    # 构建请求
    request = Request(url, headers=firefox_headers)
    html = urlopen(request)
    # 获取数据以utf-8的编码方式
    # data2 = html.read().decode('utf-8')
    data2 = zlib.decompress(html.read(), 16 + zlib.MAX_WBITS).decode('utf-8')
    data1 = str(data2)
    # data3 =dict(html.read().decode('utf-8'))
    # data3 =dict (str(data2))
    # 将｛｝[]符号都转化为，
    # data3=re.sub(r""[])
    data3 = data2.replace(r'}', ',').replace(r'{', ',').replace(r']', ',').replace(r':', ',')
    print (data1)
    time.sleep(30)
