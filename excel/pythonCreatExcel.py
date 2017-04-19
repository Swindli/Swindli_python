#!/usr/bin/env python
#coding=utf-8

import xlwt

def set_style(name ,height,bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    borders = xlwt.Borders()
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font
    style.borders = borders

    return style

def write_excel():
    f = xlwt.Workbook()

    sheet1 = f.add_sheet(u'sheet',cell_overwrite_ok=True)
    row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
    col0 = [u'机票',u'船票',u'火车票',u'汽车票',u' 其他']
    status = [u'预定',u'出票',u'退票',u'业务小票']

    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))

    i,j = 1,0
    while i < 4*len(col0) and j < len(col0):
        sheet1.write_merge(i,i+3,0,0,col0[j],set_style('Arial',220,True))
        sheet1.write_merge(i,i+3,7,7)
        i += 4
        j += 1

    sheet1.write_merge(21,21,0,1,u'合计',set_style('Time New Roamn',220,True))

    i = 0
    while i < 4*len(col0):
        for j in range(0,len(status)):
            sheet1.write(j+i+1,1,status[j])
        i += 4

    sheet2 = f.add_sheet(u'sheet2', cell_overwrite_ok=True)
    row0 = [u'姓名', u'年龄', u'出生日期', u'爱好', u'关系']
    column0 = [u'小杰', u'小胖', u'小明', u'大神', u'大仙', u'小敏', u'无名']


    for i in range(0, len(row0)):
        sheet2.write(0, i, row0[i], set_style('Times New Roman', 220, True))

    for i in range(0, len(column0)):
        sheet2.write(i + 1, 0, column0[i], set_style('Times New Roman', 220))

    sheet2.write(1, 2, '1991/11/11')
    sheet2.write_merge(7, 7, 2, 4, u'暂无')
    sheet2.write_merge(1, 2, 4, 4, u'好朋友')

    f.save(r'G:\github\Swindli_python\excel\creat.xls')

if __name__ == '__main__':
    write_excel()


