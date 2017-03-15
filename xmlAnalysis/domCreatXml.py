#!/usr/bin/env python
#coding=utf-8

import xml.dom.minidom

doc = xml.dom.minidom.Document()
root = doc.createElement('Managers')
root.setAttribute('company','xx科技')
root.setAttribute('address','科技软件园')
doc.appendChild(root)
managerList = [{'name':'joy','age':27,'sex':'女'},
               {'name':'tom','age':30,'sex':'男'},
               {'name':'ruby','age':29,'sex':'女'}]
for i in managerList:
    nodeManager = doc.createElement('Manager')

    nodeName = doc.createElement('name')
    nodeName.appendChild(doc.createTextNode((str(i['name']))))

    nodeAge = doc.createElement('age')
    nodeAge.appendChild(doc.createTextNode(str(i['age'])))

    nodeSex = doc.createElement('sex')
    nodeSex.appendChild(doc.createTextNode(str(i['sex'])))

    nodeManager.appendChild(nodeName)
    nodeManager.appendChild(nodeAge)
    nodeManager.appendChild(nodeSex)
    root.appendChild(nodeManager)

fp = open("G:\\github\\Swindli_python\\xmlAnalysis\\Manager.xml",'w')
doc.writexml(fp,indent='',addindent='\t',newl='\n',encoding="utf-8")

