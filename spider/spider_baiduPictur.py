#coding=utf-8

import urllib2
import bs4
from bs4 import BeautifulSoup
import re
import os

url = 'https://www.tieba.baidu.com/p/4999729660'
request = urllib2.Request(url)
reponse = urllib2.urlopen(request)
content = reponse.read().decode('utf-8')
soup = BeautifulSoup(content)
picturs = soup.find_all('img')
for pictur in picturs:
    link = pictur.get('src')
    print link
    content2 = urllib2.urlopen(link).read()
    with open(link[-1:],'wb') as code:
        code.write(content2)