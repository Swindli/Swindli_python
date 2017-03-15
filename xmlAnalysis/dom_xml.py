#!/usr/bin/env python
#coding=utf-8

import xml.dom.minidom
from xml.dom.minidom import parse

DOMTree = parse(r"G:\github\Swindli_python\xmlAnalysis\book.xml")
booklist = DOMTree.documentElement
if booklist.hasAttribute("type"):
    print "Root element is",booklist.getAttribute("type")

books = booklist.getElementsByTagName("book")
print "book节点的个数：",books.length

for book in books:
    print "**********book**********"
    if book.hasAttribute("category"):
        print "Category is",book.getAttribute("category")

    title = book.getElementsByTagName('title')[0]
    print "Title is",title.childNodes[0].data

    author = book.getElementsByTagName('author')[0]
    print "Author is",author.childNodes[0].data

    pageNumber = book.getElementsByTagName('pageNumber')[0]
    print "PageNumber is",pageNumber.childNodes[0].data


