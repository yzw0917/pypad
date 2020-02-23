import re
import requests
# get请求
response = requests.get(url='http://www.sxbctv.com/info/1012/55150.htm')
# print(response.content.decode('utf-8'))  #打印解码后的返回数据
words = response.content.decode('utf-8')  #提取为文本
# print (words)
# regex_str = re.compile(r'[\u4e00-\u9fa5]+') #匹配规则
# match_str = regex_str.findall(words) #执行匹配
# for i in match_str:
#     print (i)
# # print (match_str)
# phone1=re.findall("[0-9]{11}",words)
cen1=re.findall('<h2 class="article--title">(.*?)</h2>',words) #将需要的内容由.*?一次非贪婪
cen2=re.findall('<p class="vsbcontent_start">(.*?)</p>',words)
cen3=re.findall('<p>(.*)</p>',words) #取出所有
cen4=re.findall('<p class="vsbcontent_end">(.*?)</p>',words)

#print("".join(phone1))
# print(cen3,"\n")
print(cen1+cen2+cen3+cen4)