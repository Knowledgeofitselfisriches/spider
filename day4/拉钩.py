# _*_ coding:utf-8 _*_
import json

import jsonpath
import requests

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

resp = requests.get(url)

content = resp.content

content = json.loads(content, encoding='utf-8')

city = jsonpath.jsonpath(content, "$..name")

with open('city.json', 'w', encoding='utf-8') as f:
    json.dump(city, f, ensure_ascii=False)