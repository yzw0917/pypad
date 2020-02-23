import re,os
import requests
from docx import Document

response = requests.get(url='http://www.sxbctv.com/moban2017/list.jsp?a50823t=111&a50823p=1&a50823c=10&urltype=tree.TreeTempUrl&wbtreeid=1012')

words = response.content.decode('utf-8')  #提取为文本

ymid=re.findall('class="list--title"><a href="/info/1012/(.*).htm" rel',words) #取出所有


#print("".join(phone1))
# print(cen3,"\n")
# print(ymid)
# f = open("news.txt", "a")
f=Document()
for i in ymid:
    response = requests.get(url='http://www.sxbctv.com/info/1012/{num}.htm'.format(num=i))
    words = response.content.decode('utf-8')
    cen1 = re.findall('<h2 class="article--title">(.*?)</h2>', words)  # 将需要的内容由.*?一次非贪婪
    cen2 = re.findall('<p class="vsbcontent_start">(.*?)</p>', words)
    cen3 = re.findall('<p>(.*)</p>', words)  # 取出所有
    cen4 = re.findall('<p class="vsbcontent_end">(.*?)</p>', words)
    s01=("第%s"%(i)+"条新闻：\n"+str(cen1) +"\n"+ str(cen2)+"\n" + str(cen3)+"\n" +str(cen4)+"\n")
    # f = open("news.txt", "a")
    # f.write(s01)
    f.add_paragraph(s01)
f.save("d:\\pythontest\\news01.docx")

# os.system("D:\\Notepad++\\notepad++.exe  news.txt")
os.system("d:\\pythontest\\news01.docx")