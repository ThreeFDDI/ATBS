#!/usr/local/bin/python3

# ATBS-14_remove_csv_header.py - Removes the header from all CSV files

import csv, os

# check if directory for modified CSV files exists
os.makedirs("ATBS/ATBS-14_dir/headerRemoved", exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir("ATBS/ATBS-14_dir"):
    if not csvFilename.endswith(".csv"):
        continue

    print("Removing header from " + csvFilename + "...")
    
    # Read the CSV file in skipping first row
    csvFileObj = open(f"ATBS/ATBS-14_dir/{csvFilename}")
    readerObj = csv.reader(csvFileObj)
    csvRows = []
    
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)

    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('ATBS/ATBS-14_dir/headerRemoved', csvFilename), 'w',
         newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

