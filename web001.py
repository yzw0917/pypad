# coding:utf-8

import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

page = urllib.urlopen('http://www.baojinews.com')
contents = page.read()
print(contents)
# soup = BeautifulSoup(contents, "html.parser")
# print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
# for tag in soup.find_all('div', class_='info'):
#     # print tag
#     m_name = tag.find('span', class_='title').get_text()
#     m_rating_score = float(tag.find('span', class_='rating_num').get_text())
#     m_people = tag.find('div', class_="star")
#     m_span = m_people.findAll('span')
#     m_peoplecount = m_span[3].contents[0]
#     m_url = tag.find('a').get('href')
#     print(m_name + "        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)
