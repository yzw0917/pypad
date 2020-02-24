import requests

baseurl = 'http://tieba.baidu.com/f?'
params = {
  'kw' : 'python吧',
  'pn' : '50'
}
headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
# 自动对params进行编码,然后自动和url进行拼接,去发请求
res = requests.get(baseurl,params=params,headers=headers) #requests.get访问网页保存返回值
res.encoding = 'utf-8'
f=open('.\\test03.html','w',encoding="utf-8")
f.write(res.text)
#
print(res.text)
f.close()