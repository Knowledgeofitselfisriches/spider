# _*_ coding:utf-8 _*_
import json

import jsonpath
import requests

url = 'http://api.m.mtime.cn/PageSubArea/TrailerList.api'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

resp = requests.get(url, headers=headers)

content = resp.content

content = json.loads(content, encoding='utf-8')

city = jsonpath.jsonpath(content, "$..hightUrl")

with open('video.json', 'w', encoding='utf-8') as f:
    json.dump(city, f, ensure_ascii=False)