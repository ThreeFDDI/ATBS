#! /usr/local/bin/python3

import openpyxl, os

os.chdir("/Users/JT/JTGIT/ATBS")

wb = openpyxl.load_workbook("ATBS-12_example.xlsx")

print(type(wb))

sheet = wb.get_sheet_by_name("Sheet3")

print(sheet)

print(type(sheet))

#print(dir(sheet))

print(sheet.title)