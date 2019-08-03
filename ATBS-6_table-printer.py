#!/usr/local/bin/python3

# ATBS-6_table-printer.py prints formatted tables from lists

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# function to format and print
def printTable(list):
    # initialize list of column width
    colWidth = [0]*len(tableData[0])

    # determine longest width per column
    for i in range(len(tableData)):
        #if len(i) > colWidth[i]:
         #   print(i)
        #colWidth.append(len(i))
        print(tableData[i])
        print(colWidth)
        print()    
        


printTable(tableData)