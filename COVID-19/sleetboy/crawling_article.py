# 함수 활용하기
# 새로 배운 모듈 활용하기
# 크롤링한 데이터를 다듬어주는 방법 생각해보기

# -*- coding: utf-8 -*-

import os
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

def read_article_data(path):
    with open(path) as fin:
        return json.load(fin).get('news')

def crawler(url):
    hdr = {"User-Agent": "Chrome/66.0.3359.181"}

    req = urllib.request.Request(url, headers=hdr)
    html = urlopen(req)
    bsObj = BeautifulSoup(html, "lxml")
    target_text = bsObj.text
    return target_text

def save_article_data(path, text):
    with open(path, 'w', encoding="utf-8") as fout:
        fout.writelines(text)


def main():
    path_in_json = '\\Users\\cubana\\python101\\COVID-19\\news\\news.json'
    path_out_dir = '\\Users\\cubana\\python101\\COVID-19\\sleetboy\\scrap_files'

    # read input data
    news = read_article_data(path_in_json)

    # crawling
    for article_info in news:
        text = crawler(article_info.get('url'))
        file_name = article_info.get('filename')
        path_out = os.path.join(path_out_dir, file_name)
        save_article_data(path_out, text)

if __name__ == '__main__':
    main()