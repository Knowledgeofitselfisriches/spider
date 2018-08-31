# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup

url = 'https://www.douyu.com/g_LOL'

resp = requests.get(url)

content = resp.content

soup = BeautifulSoup(content, 'lxml')

for h3 in soup.find_all('h3'):
    print('live_subjects', h3.text.strip())