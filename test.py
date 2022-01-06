from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import requests
ret_arr = []
my_url = 'https://github.com/Data-Analytics-Club-VITCC'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = Soup(page_html, "html.parser")
names = page_soup.findAll("a", {"class": "f4 d-inline-block text-bold mr-1"})
names = ['https://github.com/Data-Analytics-Club-VITCC/'+name.text.strip() for name in names]
for url in names:
    uClient = ureq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = Soup(page_html, "html.parser")

    title = page_soup.findAll("a", {"itemprop": "name codeRepository"})
    title = title[0].text
    about = page_soup.findAll("p", {"class": "f4 mt-3"})
    about = about[0].text.strip()
    lang = page_soup.findAll("span", {"class": "color-fg-default text-bold mr-1"})
    lang = lang[0].text
    star_count = page_soup.findAll("a", {"class": "social-count js-social-count"})
    star_count = int(star_count[0].text.strip())
    branch_count = page_soup.findAll("a", {"class": "Link--primary no-underline"})
    branch_count = int(branch_count[0].findAll("strong")[0].text)
    
    ret = {}
    ret['title'] = title
    ret['about'] = about
    ret['lang'] = lang
    ret['star_count'] = star_count
    ret['branch_count'] = branch_count
    ret['link'] = url
    ret_arr.append(ret)
    
print(ret_arr)