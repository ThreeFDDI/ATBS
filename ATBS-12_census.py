#! /usr/local/bin/python3

import openpyxl, os

os.chdir("/Users/JT/JTGIT/ATBS")

wb = openpyxl.load_workbook("ATBS-12_example.xlsx")

sheet = wb.active

col1 = sheet.iter_cols(values_only=False, min_col=2, max_col=2)
print(col1)
for col in col1:
    for row in col:
        print(row)

print("~"*20)

col2 = sheet.iter_cols(values_only=False, min_col=2, max_col=2)
print(col2)
for col in col2:
    for row in col:
        print(row.value)

print("~"*20)

col3 = sheet.iter_cols(values_only=True, min_col=2, max_col=2)
print(col3)

for col in col3:
    for row in col:
        print(row)