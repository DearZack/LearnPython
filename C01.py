from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "http://www.baidu.com"


def useUrlopen():
    html = urlopen(url)
    print(html.read())


def useBeautifulSoup():
    html = requests.get(url)
    bsObj = BeautifulSoup(html.text, "html.parser")
    print(bsObj.head)


# useUrlopen()
useBeautifulSoup()
