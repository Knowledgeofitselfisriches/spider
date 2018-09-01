# _*_ coding:utf-8 _*_
import requests
import json
from bs4 import BeautifulSoup

url = 'https://hr.tencent.com/position.php?keywords=nginx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
resp = requests.get(url, headers=headers)

content = resp.content

soup = BeautifulSoup(content, 'lxml')

even = soup.select('tr[class="even"]')
odd = soup.select('tr[class="odd"]')

even[0:0] = odd
jb_list = []
it = {}
for item in even:
    name = item.td.a.text
    link = item.td.a['href']
    jb = item.select('td')[1].text
    nums = item.select('td')[2].text
    address = item.select('td')[3].text
    publish = item.select('td')[4].text

    it['name'] = name
    it['data_link'] = link
    it['job_category'] = jb
    it['recruit_number'] = nums
    it['address'] = address
    it['publish_time'] = publish
    jb_list.append(it)
print(type(jb_list))
with open('tx.json', 'w', encoding='utf-8') as f:
    for i in jb_list:
        ites = json.dumps(i, ensure_ascii=False) + '\n'
        f.write(ites)


class TengXunHR(object):

    def get_context(self):
        url = 'https://hr.tencent.com/position.php?keywords=nginx'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        resp = requests.get(url, headers=headers)

        content = resp.content

        return content

    def extract(self, content):
        soup = BeautifulSoup(content, 'lxml')

        even = soup.select('tr[class="even"]')
        odd = soup.select('tr[class="odd"]')
        even[0:0] = odd
        return even

    def transform(self, even):
        jb_list = []
        it = {}
        for item in even:
            name = item.td.a.text
            link = item.td.a['href']
            jb = item.select('td')[1].text
            nums = item.select('td')[2].text
            address = item.select('td')[3].text
            publish = item.select('td')[4].text

            it['name'] = name
            it['data_link'] = link
            it['job_category'] = jb
            it['recruit_number'] = nums
            it['address'] = address
            it['publish_time'] = publish
            jb_list.append(it)
        return jb_list
    def save(self, jobs):
        with open('tx.json', 'w', encoding='utf-8') as f:
            for i in jobs:
                ites = json.dumps(i, ensure_ascii=False) + '\n'
                f.write(ites)

    def __call__(self, *args, **kwargs):
        content = self.get_context()
        li = self.extract(content)
        jobs = self.transform(li)
        self.save(jobs)

if __name__ == '__main__':
    TengXunHR()()
