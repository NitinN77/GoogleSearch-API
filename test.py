# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=data+science&btnG='
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')
#print(soup.select('[data-lid]'))
for item in soup.select('[data-lid]'):
    try:
        print('----------------------------------------')
        print(item.select('h3')[0].get_text())
        print(item.select('a')[0]['href']) 
        print(item.select('.gs_rs')[0].get_text())
        print('----------------------------------------')
    except Exception as e:
        print('')