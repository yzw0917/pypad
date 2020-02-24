import urllib.request
import os, re, sys, time

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
loca = re.compile(r"""ion":"\D+", "ti""")
# 伪装成浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}


class Getip():
    def __init__(self, diqu):
        self.ur = {"xicidaili国内普通代理 --1线": "http://www.xicidaili.com/nt/",

                   "ip84国内普通代理 --2线": 'http://www.ip84.com/dlpn-http/',

                   'xicidaili国内高匿名代理 --1线': 'http://www.xicidaili.com/nn/',

                   'ip84国内高匿名代理 --2线': 'http://www.ip84.com/dlgn-http/',

                   'xicidaili国外高匿名代理 --1线': 'http://www.xicidaili.com/wn/',

                   'ip84国外高匿名代理 --2线': 'http://www.ip84.com/gwgn-http/',
                   'xicidaili国外普通代理 --1线': 'http://www.xicidaili.com/wt/',
                   'haodailiip国内混合代理 --3线': 'http://www.haodailiip.com/guonei/',
                   'haodailiip国外混合代理 --3线': 'http://www.haodailiip.com/guoji/',
                   }
        self.diqu = diqu

    def urlopen(self, url):
        global header
        try:
            req = urllib.request.Request(url, None, header)
            res = urllib.request.urlopen(req)

            return res
        except:
            pass

    def getip(self, ren):
        '''url = "http://proxy.ipcn.org/proxylist.html"#代理IP页面
        ip_proxy_re = re.compile(r"""\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,}""")# 直接匹配 xxx.xxx.xxx.xxx:xxxx'''

        url = self.ur[self.diqu] + str(ren)

        ip_proxy_re = re.compile(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*</td>\s*<td>\s*(\d{1,})\s*</td>\s*<[^\u4E00-\u9FA5]+>([\u4E00-\u9FA5]*\s*[\u4E00-\u9FA5]*\s*[\u4E00-\u9FA5]*)\s*<')
        #################################通用正则匹配的  格式 是  (IP,端口,地区) 地区有可能包含换行和空格
        try:
            data = self.urlopen(url).read().decode('utf-8')
        except:
            return None

        self.rel = []

        ip = ip_proxy_re.findall(data)
        ##########返回的IP 就是 正则匹配的结果(IP,端口,地区) 地区有可能包含换行和空格

        return ip


if __name__ == '__main__':
    g = Getip("xicidaili国内高匿名代理 --1线")
    import pprint

    for x in range(4):
        ips = g.getip(1)
        print('获取到ip地址一共:', len(ips))
        pprint.pprint(ips)