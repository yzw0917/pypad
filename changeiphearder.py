import urllib.request
import requests

# 查询IP  http://ip.chinaz.com/getip.aspx
url = "http://www.ip138.com/"

print("原有IP:   " + requests.get(url).text)
# 构建一个代理IP的格式
# IP
ip_data = "47.94.230.42"
# 端口
port_data = "9999"
# 固定IP格式
new_data = {
    "http": ip_data + ":" + port_data
}
# proxies=IP  resquests模块构建请求
print("代理后的IP:   " + requests.get(url, proxies=new_data).text)
# 切换回自己的IP是  当 当前代理IP失效后向代理IP提供商获取新IP的时候需要使用自己的ip
print("切换回自己的IP:   " + requests.get(url, proxies={"http": ""}).text)
