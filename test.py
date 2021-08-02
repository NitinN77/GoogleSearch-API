from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import requests

#my_url = 'https://arxiv.org/search/?query='+args+'&searchtype=all&source=header'
my_url = 'https://github.com/Data-Analytics-Club-VITCC/Task2-Vehicle-Price-Prediction'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, "html.parser")

title = page_soup.findAll("a", {"data-pjax": "#js-repo-pjax-container"})
title = title[0].text
about = page_soup.findAll("p", {"class": "f4 mt-3"})
about = about[0].text.strip()
lang = page_soup.findAll("span", {"class": "color-text-primary text-bold mr-1"})
lang = lang[0].text
star_count = page_soup.findAll("a", {"class": "social-count js-social-count"})
star_count = star_count[0].text.strip()
branch_count = page_soup.findAll("a", {"class": "Link--primary no-underline"})
branch_count = branch_count[0].findAll("strong")[0].text