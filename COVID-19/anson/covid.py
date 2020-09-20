seed_url = "https://www.nocutnews.co.kr/news/5415306"

import os
import json
import re
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse

def extract_urls_from_webpage(url):
    hdr = {"User-Agent": "Chrome/66.0.3359.181"}
    req = urllib.request.Request(url, headers=hdr)
    bs = BeautifulSoup(urllib.request.urlopen(req), "lxml")
    links = []
    url_parsed = urlparse(url)
    
    for link in bs.findAll('a', attrs={'href': re.compile("^(https?:/)?/")}):
        href = link.get('href')
        if href.startswith('/'):
            links.append("{}://{}{}".format(url_parsed.scheme, url_parsed.netloc, href))
        else:
            links.append(href)

    return set(links)

if __name__ == '__main__':
    urls = extract_urls_from_webpage(seed_url)
    print("# of urls: {}".format(len(urls)))
    print("urls:")
    for url in urls:
        print(url)