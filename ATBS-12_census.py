#! /usr/local/bin/python3

# tabulate census data per county

import openpyxl, pprint, os

os.chdir("/Users/JT/JTGIT/ATBS")

print("Opening workbook...")

wb = openpyxl.load_workbook("ATBS-12_censuspopdata.xlsx")

sheet = wb["Population by Census Tract"]

countyData = {}

# TODO poulate in countyData 

print("Reading rows...")
for row in range(2,sheet.max_row +1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    