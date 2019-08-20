#! /usr/local/bin/python3

import openpyxl, os

os.chdir("/Users/JT/JTGIT/ATBS")

wb = openpyxl.load_workbook("ATBS-12_example.xlsx")

print(type(wb))
