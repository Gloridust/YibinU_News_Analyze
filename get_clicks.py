import requests

url = "https://www.yibinu.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid=62031&owner=1397404744&clicktype=wbnews"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
res = requests.get(url=url, headers=header)
print(res.text)