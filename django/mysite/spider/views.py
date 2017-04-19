#coding=utf-8

from django.shortcuts import render_to_response
import re
import urllib2
import json

# Create your views here.

def spider(request):
    url = 'http://www.tianqi.com/qiwen/china-1/'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('gbk')
    pattern1 = re.compile('<td width="52"><a href.*?>(.*?)</a></td>', re.S)
    categories = re.findall(pattern1, content)
    categoriesData = json.dumps(categories,ensure_ascii=False,encoding='utf-8')
    pattern2 = re.compile('<td class="red">(.*?)</td>', re.S)
    data1 = re.findall(pattern2, content)[0:12]
    pattern3 = re.compile('<td class="blue">(.*?)</td>', re.S)
    data2 = re.findall(pattern3, content)[0:12]
    for i in range(12):
        data1[i] = int(data1[i].encode('utf-8').replace("\xe2\x84\x83",""))
        data2[i] = int(data2[i].encode('utf-8').replace("\xe2\x84\x83",""))

    return render_to_response('spider.html',{'categories':categoriesData,
                                      'data1':data1,
                                      'data2':data2})

