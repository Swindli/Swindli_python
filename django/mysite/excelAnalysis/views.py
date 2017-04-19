#coding=utf-8

from django.shortcuts import render_to_response
import xlrd
import json
# Create your views here.

localFile = r'G:/github/Swindli_python/django/mysite/Result.xlsx'
areaCellValue = '地域/代表处'

CityCounter = {}
areaList = ['北京', '成都', '南京', '上海', '深圳', '武汉', '西安']
areaCell = 0

def inintLocalDate():
    for i in range(7):
        CityCounter[areaList[i]] = 0

def openFile(fileName):
    try:
        data = xlrd.open_workbook(filename=fileName,encoding_override='utf-8')
        return data
    except Exception,e:
        print e

def parseDate(fileName,sheetName):
    data = openFile(fileName)
    table = data.sheet_by_name(sheetName)
    for col in range(table.ncols):
        if table.cell(0,col).value == areaCellValue.decode('utf-8'):
            areaCell = col

    for row in range(1,table.nrows):
        CityCounter[table.cell(row,areaCell).value.encode('utf-8')] += 1

    return CityCounter

def excel(request):
    localseriesList = []
    for i in range(1,7):
        inintLocalDate()
        sheetName = '人员信息' + '(' + str(i) + ')'
        parseDate(localFile,sheetName.decode('utf-8'))
        citycategories = json.dumps(CityCounter.keys(),ensure_ascii=False,encoding='utf-8')
        name = str(i) + '月'
        citydata = CityCounter.values()
        series = {'name':name,'data':citydata}
        localseriesList.append(series)
    seriesList = json.dumps(localseriesList,ensure_ascii=False,encoding='utf-8')
    return render_to_response('excelAnalysis.html',{'citycategories':citycategories,
                                                    'serieslist':seriesList,})
