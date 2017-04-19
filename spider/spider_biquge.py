#coding=utf-8

import urllib2
import re

class Tool:
    replaceBr = re.compile('<br /><br />|<br />')
    removeNbsp = re.compile('&nbsp.*?;')
    removeExtraTag = re.compile('<.*?>(.*?)<.*?>')
    def replace(self,x):
        x = re.sub(self.replaceBr,"\n",x)
        x = re.sub(self.removeNbsp,"",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()
class BQG:
    def __init__(self,baseUrl,bookCategory,bookNumber,firstPageNumber,lastPageNumber):
        self.baseUrl = baseUrl
        self.bookCategory = bookCategory
        self.bookNumber = bookNumber
        self.firstPageNumber = firstPageNumber
        self.lastPageNumber = lastPageNumber
        self.tool = Tool()
        self.defaultTitle = u"奇趣阁图书"

    def getPage(self,pageNumber):
        try:
            url = self.baseUrl + self.bookCategory + "/" + self.bookNumber + "/" + str(pageNumber) + ".html"
            request = urllib2.Request(url)
            response = urllib2.urlopen(request,timeout=100)
            return response.read().decode('gbk','ignore')
        except urllib2.URLError,e:
            if hasattr(e, "reason"):
                print u"连接书库失败，错误原因", e.reason
                return None

    def getBookTitle(self,page):
        pattern = re.compile('<a href="/xiaoshuo.*?>(.*?)</a>',re.S)
        resurt = re.search(pattern,page)
        if resurt:
            return resurt.group(1).strip()
        else:
            return None

    def getChapterTitle(self,page):
        pattern = re.compile('<h1>(.*?)</h1>',re.S)
        resurt = re.search(pattern,page)
        if resurt:
            return resurt.group(1).strip().encode('utf-8')
        else:
            return  None

    def getContent(self,page):
        pattern = re.compile('<div id="htmlContent.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            content = self.tool.replace(item)
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self,bookTitle):
        if bookTitle is not None:
            self.file = open(bookTitle + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")

    def writeDate(self,chapterTitle,contents):
        for item in contents:
            self.file.write(chapterTitle)
            self.file.write('\n')
            self.file.write(item)

    def start(self):
        indexPage = self.getPage(self.firstPageNumber)
        bookTitle = self.getBookTitle(indexPage)
        self.setFileTitle(bookTitle)
        chapterNumber = int(self.lastPageNumber) - int(self.firstPageNumber) + 1
        print "该书共有"+str(chapterNumber)+"章。"
        for i in range(int(self.firstPageNumber),int(self.lastPageNumber)+1):
            print "正在写入第"+str(i-int(self.firstPageNumber)+1)+"章。"
            page = self.getPage(i)
            chapterTitle = self.getChapterTitle(page)
            contents = self.getContent(page)
            self.writeDate(chapterTitle,contents)
        print "写入完毕。"

baseUrl = 'http://www.ybdu.com/xiaoshuo/'
bookCategory = raw_input("输入图书类别:")
bookNumber = raw_input("输入图书编号:")
firstPageNumber = raw_input("输入第一章编号：")
lastPageNumber = raw_input("输入最后一章编号：")
bqg = BQG(baseUrl,bookCategory,bookNumber,firstPageNumber,lastPageNumber)
bqg.start()
