from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import requests

#my_url = 'https://arxiv.org/search/?query='+args+'&searchtype=all&source=header'
ret_arr = []
my_url = 'https://medium.com/@dacvitcc'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
r = requests.get(my_url,headers=headers)
page_soup = Soup(r.text, "html.parser")
titles = page_soup.findAll("a", {"class": "et ca"})
title = titles[0].text
intros = page_soup.findAll("img", {"class":"af io ko"})
intro = intros[1]['src']
readtime = page_soup.findAll("p", {"class":"be b bf bg hf"})
readtime = readtime[1].findAll("span")
print(readtime[0].text)