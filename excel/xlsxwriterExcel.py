#!/usr/bin/env python
#coding=utf-8

import xlsxwriter

workbook = xlsxwriter.Workbook('xlsxwriterExcel.xls')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold':1})

headings = ['Number','Batch1','Batch2']
data = [
    [2,3,4,5,6,7],
    [10,40,50,20,10,50],
    [30,60,70,50,40,30],
]

worksheet.write_row('A1',headings,bold)
worksheet.write_column('A2',data[0])
worksheet.write_column('B2',data[1])
worksheet.write_column('C2',data[2])

chart1 = workbook.add_chart({'type':'colum'})
chart1.add_series({
    'name':'=Sheet1!$B$1',
    'categories':'=Sheet1!$A$2:$a$7',
    'values':'=Sheet1!$B$2:$B$7',
})
chart1.add_series({
    'name':['Sheet1',0,2],
    'categories':['Sheet1',1,0,6,0]


})

