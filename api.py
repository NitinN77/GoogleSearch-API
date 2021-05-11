from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import requests

app = FlaskAPI(__name__)
cors = CORS(app)

@app.route("/news", methods=['GET'])
def fetch():
    args = str(request.args['topic'])
    my_url = 'https://news.google.com/search?q=' + args + '&hl=en-IN&gl=IN&ceid=IN%3Aen'
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = Soup(page_html, "html.parser")
    titles = page_soup.findAll("h3", {"class": "ipQwMb ekueJc RD0gLb"})
    images = page_soup.findAll("img", {"class": "tvs3Id QwxBBf"})
    links = page_soup.findAll("a", {"class": "VDXfz"})
    ret = []
    for i in range(len(titles)):
        ret.append([titles[i].text])
    for i in range(len(images)):
        ret[i].append(images[i].get('src'))
    for i in range(len(links)):
        ret[i].append('https://news.google.com'+str(links[i].get('href'))[1:])
    return jsonify(ret) 

    
@app.route("/papers", methods=['GET'])
def fetchpapers():
    args = str(request.args['topic'])
    ret = []
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + args + '&btnG='
    response=requests.get(url,headers=headers)
    soup=Soup(response.content,'lxml')
    for item in soup.select('[data-lid]'):
        try:
            ret.append({'title': item.select('h3')[0].get_text(), 'link': item.select('a')[0]['href'], 'desc': item.select('.gs_rs')[0].get_text()})
        except Exception as e:
            break
    return jsonify(ret)
    


if __name__ == "__main__":
    app.run(debug=True)