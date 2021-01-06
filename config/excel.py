#!/usr/bin/python3
import xlrd
import xlwt
import requests
import json
from xlutils.copy import copy
#xlrd只适合xls表格。xlsx表格需要使用其他函数
class excel():
    path = r'D:\1.xls'
    excel = xlrd.open_workbook(path)
    sheet_read = excel.sheets()[0]
    nrows = sheet_read.nrows
    excel2 = copy(excel)
    sheet_copy = excel2.get_sheet(0)
    # print(sheet_read.cell(1, 1).value)





