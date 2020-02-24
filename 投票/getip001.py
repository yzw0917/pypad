import requests,PIL

# hz_url = "http://tool.lu/ip"  # 某投票网站的地址，这里不用真实的域名
# hz_url = "http://www.sxbctv.com/"
hz_url = "https://tool.lu/netcard/"
hz_r = requests.get(hz_url)
# hz_r.encoding="utf-8"
print(hz_r.raw)
# im=Image.open(hz_r.text)
# im.show()
