import time
import requests
from bs4 import BeautifulSoup

for  i in range(1,116):
    url_lianjia = f'https://www.nowcoder.com/search?type=post&order=recall&query=%E5%A4%A7%E6%95%B0%E6%8D%AE&subType=2&tagId=&page={i}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    html = requests.get(url=url_lianjia, headers=headers)
    html.encoding = "utg-8"
    if html.status_code == 200:
        time.sleep(1)
        soup = BeautifulSoup(html.text, "html.parser")
        newlist=[]
        for k in soup.find_all('a',class_='js-gio'):
            '''
            for k in soup.find_all('a'):
            print(k)
            print(k['class'])#查a标签的class属性
            print(k['id'])#查a标签的id值
            print(k['href'])#查a标签的href值
            print(k.string)#查a标签的string 
            '''
            url = 'https://www.nowcoder.com/'+k['href']
            newlist.append(url)
        print(newlist)

    else:
        print("请求失败")




