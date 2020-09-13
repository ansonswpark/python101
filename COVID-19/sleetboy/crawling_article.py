# 단일 url이 주어졌을 때 해당 링크에서 text추

import urllib.request
import bs4 
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

list_path = r'C:\Users\cubana\python101\COVID-19\news\news.json'

#url 리스트 읽기
def open_json_file(list_path):
    with open(list_path) as json_file:
        json_data = json.load(json_file)
    return json_data

#url 리스트 만들기
def url_list():
    b = []
    for a in open_json_file(list_path)["news"]:
        b.append(a["url"])
    return b

#각각의 url에 해당하는 웹 페이지 내용을 읽어온다.
def read_web_page():
    for url in url_list():
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, 'lxml')
    return print(bsObj)
#url = 'https://en.yna.co.kr/view/AEN20200905001700320'
#html = urllib.request.urlopen(url)
#bsObj = bs4.BeautifulSoup(html, "lxml")


read_web_page()
#print(url_list())

#article = bsObj.find("div", {"class":"article-story"})
#target_text = article.text
#path = 'C:/Users/cubana/python101/COVID-19/sleetboy/scrap_files/00.text'
#with open(path, "w", encoding="utf-8") as file:
#    file.writelines(target_text)
#