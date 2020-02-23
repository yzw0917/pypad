import re
import requests
# get请求
response = requests.get(url='http://www.sxbctv.com/xwzx.htm')
# print(response.content.decode('utf-8'))  #打印解码后的返回数据
words = response.content.decode('utf-8')  #提取为文本
# print (words)
# regex_str = re.compile(r'[\u4e00-\u9fa5]+') #匹配规则
# match_str = regex_str.findall(words) #执行匹配
# for i in match_str:
#     print (i)
# # print (match_str)
# phone1=re.findall("[0-9]{11}",words)
phone1=re.findall("[\u4e00-\u9fa50-9]+",words) #所有汉字

#print("".join(phone1))
print(phone1)