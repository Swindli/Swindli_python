#coding=utf-8

import urllib
import urllib2
import re

url = 'http://tieba.baidu.com/p/3639921032'+'?see_lz=1'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
concent = response.read().decode('utf-8','ignore')
pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
items = re.findall(pattern,concent)
for item in items:
    print item