#! /usr/local/bin/python3

# tabulate census population data per county

import openpyxl, pprint, os

# change directory
os.chdir("/Users/JT/JTGIT/ATBS")

print("Opening workbook...")
# open census workbook
wb = openpyxl.load_workbook("ATBS-12_censuspopdata.xlsx")

# open census worksheet
sheet = wb["Population by Census Tract"]

# initialize countyData JSON dictionary
countyData = {}

print("Reading rows...")
# iterate rows and set variables for state, county and
for row in range(2,sheet.max_row +1):
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value
    
    # make sure state key exists
    countyData.setdefault(state, {})
    # make sure county key exists
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})

    # increment census tract
    countyData[state][county]["tracts"] += 1
    # tally the population
    countyData[state][county]["pop"] += int(pop)

# pretty print results
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(countyData['TN'])