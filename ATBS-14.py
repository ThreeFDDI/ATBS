#!/usr/local/bin/python3

# Chapter 14 – Working with CSV Files and JSON Data

# ATBS-14.py 

import csv, json

#exFile = open("ATBS/ATBS-14_example.csv")
#exReader = csv.reader(exFile)

exReader = csv.reader(open("ATBS/ATBS-14_example.csv"))

exData = list(exReader)

print()
print(exData)
print()

for i in exData:
    print(i)

print()
print(exData[1])
print(exData[5])
print(exData[5][1])
print()

for i in exData[5]:
    print(i)

outputFile = open("ATBS/ATBS-14_output.csv", "w", newline="")