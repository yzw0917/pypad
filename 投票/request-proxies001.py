from bs4 import BeautifulSoup
import requests,random,re
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
}
def get_ip():
    url = "http://www.xicidaili.com/nn"
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                "Referer":"http://www.xicidaili.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                }
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.table.find_all("td")
    ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
    ip = re.findall(ip_compile,str(data))       # 获取所有IP
    port = re.findall(port_compile,str(data))   # 获取所有端口
    return [":".join(i) for i in zip(ip,port)]  # 组合IP+端口，如：115.112.88.23:8080
ips=get_ip()
for i in ips:
    proxies = {'http':i }  #这个地方换一下ip和端口号,很多ip使用不成的
    url = 'http://tool.chinaz.com/' #访问这个网站可以返回你的IP地址 以此验证是否变换成功
    try:
        wb_data = requests.get(url,headers=header,proxies=proxies) #timeout 限定5秒相应后就退出执行
        soup = BeautifulSoup(wb_data.text,'lxml')
        print("成功:",i)
    except(requests.exceptions.ProxyError,requests.exceptions.ConnectTimeout):
        print('failed!',i)
