from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import requests

#my_url = 'https://arxiv.org/search/?query='+args+'&searchtype=all&source=header'
my_url = 'https://github.com/Data-Analytics-Club-VITCC'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, "html.parser")
names = page_soup.findAll("a", {"class": "f4 d-inline-block text-bold mr-1"})
names = ['https://github.com/Data-Analytics-Club-VITCC/'+name.text.strip() for name in names]
print(names[1])