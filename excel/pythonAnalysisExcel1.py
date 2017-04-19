#!/usr/bin/env python
# coding=utf-8

import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
    workbook = xlrd.open_workbook(r'G:\github\Swindli_python\excel\demo.xlsx')
    print workbook.sheet_names()

    sheet2 = workbook.sheet_by_index(1)
    sheet2 = workbook.sheet_by_name('sheet2')
    print sheet2.name,sheet2.nrows,sheet2.ncols

    merge = []
    for (rlow,rhigh,clow,chigh) in sheet2.merged_cells:
        merge.append([rlow,clow])
    for index in merge:
        print sheet2.cell_value(index[0],index[1])

    rows = sheet2.row_values(3)
    cols = sheet2.col_values(2)
    print rows
    print cols

    print sheet2.cell(1,0).value.encode('utf-8')
    print sheet2.cell_value(1,0).encode('utf-8')
    print sheet2.row_values(1)[0].encode('utf-8')

    print sheet2.cell(1,0).ctype

    date_value = xlrd.xldate_as_tuple(sheet2.cell_value(3, 2),workbook.datemode)
    date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
    print date_tmp

if __name__ == '__main__':
    read_excel()