# news.json 파일에서 url을 추출해 웹 페이지 정보를 txt파일로 저장하기

import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

path = r'C:\Users\cubana\python101\COVID-19\news\news.json'

def open_json_file(path):
    with open(path) as json_file:
        json_data = json.load(json_file)
    return json_data

def url_list():
    b = []
    for a in open_json_file(path)["news"]:
        b.append(a["url"])
    return b


base_url = 'https://www.fda.gov/news-events/press-announcements/coronavirus-covid-19-update-daily-roundup-september-3-2020'
con = requests.get(base_url)
soup = BeautifulSoup(con.content, 'lxml')
for 
print(soup)








#urllist = url_list() 
#for urlname in urllist:
#    html = requests.get(urlname)
#
#
#
#    soup = BeautifulSoup(html.content,'lxml')
#print(soup)
#url_list = url_list()
#for urlname in url_list:
#    con = requests.get(urlname)
#    soup = BeautifulSoup(con.content, 'lxml')
#con = requests.get(base_url)
#soup = BeautifulSoup(con.content, 'lxml')
#print(soup)


#for url in mk_url_list()

#print(json_data["news"])
#print(json.dumps(json_data, indent="\t"))

