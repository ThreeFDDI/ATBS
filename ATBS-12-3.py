#! /usr/local/bin/python3

import openpyxl, pprint, os

# change directory
os.chdir("/Users/JT/JTGIT/ATBS")

print("Creating workbook...")
# create new workbook

wb = openpyxl.Workbook()

print(wb.get_sheet_names())

sheet = wb.active

print(sheet.title)

sheet.title = "Spam Bacon Eggs Sheet"

print(wb.get_sheet_names())

print(sheet.title)

wb.save("ATBS-12_new.xlsx")

wb.create_sheet()

print(wb.get_sheet_names())
