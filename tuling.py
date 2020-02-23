# coding=UTF-8
import urllib
import json


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


if __name__ == '__main__':
    key = '7d9bb31cd1304388a7fce2040e0482fa'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    while True:
        info = raw_input('我: ')
        request = api + info
        response = getHtml(request)
        dic_json = json.loads(response)
        print
        ('机器人: '.decode('gbk') + dic_json['text'])