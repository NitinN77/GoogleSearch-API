from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import requests

#my_url = 'https://arxiv.org/search/?query='+args+'&searchtype=all&source=header'
my_url = 'https://arxiv.org/search/?query=Data+Science&searchtype=all&source=header'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, "html.parser")

titles = page_soup.findAll("p", {"class": "title is-5 mathjax"})

abstracts = page_soup.findAll("span", {"class": "abstract-full has-text-grey-dark mathjax"})
links = page_soup.findAll("p", {"class": "list-title is-inline-block"})
links_a = links[7].findAll("a")[0]
links_a = str(links_a).split('''"''')
print(links_a[1])