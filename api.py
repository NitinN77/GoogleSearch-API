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
    my_url = 'https://arxiv.org/search/?query=Data+Science&searchtype=all&source=header'
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = Soup(page_html, "html.parser")

    titles = page_soup.findAll("p", {"class": "title is-5 mathjax"})

    abstracts = page_soup.findAll("span", {"class": "abstract-full has-text-grey-dark mathjax"})
    links = page_soup.findAll("p", {"class": "list-title is-inline-block"})

    links_a = []
    for i in range(len(links)):
        links_a.append(str(links[i].findAll("a")[0]).split('''"'''))

    ret = []
    for i in range(len(titles)):
        ret.append([titles[i].text.strip('\n').strip()])
    for i in range(len(abstracts)):
        ret[i].append(abstracts[i].text.strip('\n').strip())
    for i in range(len(links_a)):
        ret[i].append(links_a[i][1])
    return jsonify(ret)


@app.route("/repo", methods=["GET"])
def fetchrepo():
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

        title = page_soup.findAll("a", {"data-pjax": "#js-repo-pjax-container"})
        title = title[0].text
        about = page_soup.findAll("p", {"class": "f4 mt-3"})
        about = about[0].text.strip()
        lang = page_soup.findAll("span", {"class": "color-text-primary text-bold mr-1"})
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

    return jsonify(ret_arr)

@app.route("/blogs", methods=["GET"])
def fetchblogs():
    ret_arr = []
    my_url = 'https://medium.com/@dacvitcc'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    r = requests.get(my_url,headers=headers)
    page_soup = Soup(r.text, "html.parser")
    titles = page_soup.findAll("a", {"class": "et ca"})
    for i in range(len(titles)):
        ret = {}
        ret['title'] = titles[i].text
        ret['img'] = page_soup.findAll("img", {"class":"af io ko"})[i]['src']
        ret['readtime'] = page_soup.findAll("p", {"class":"be b bf bg hf"})[i].findAll("span")[0].text
        ret_arr.append(ret)
    return jsonify(ret_arr)


if __name__ == "__main__":
    app.run(debug=True)