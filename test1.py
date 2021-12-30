import time
import requests
from bs4 import BeautifulSoup
import re

url_lianjia = f'https://www.nowcoder.com/discuss/792950'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
html = requests.get(url=url_lianjia, headers=headers)
html.encoding = "utg-8"
if html.status_code == 200:
    time.sleep(1)
    soup = BeautifulSoup(html.text, "html.parser")
    print(soup.find("span",class_="js-post-title post-title").text)
    s = soup.find("div", class_="post-topic-main").text
    for i in soup.find("ul",class_="discuss-tags-mod").findAll('a',target='_blank'):
        print(i.string)





else:
    print("请求失败")