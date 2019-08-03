#!/usr/local/bin/python3

# ATBS-6_table-printer.py prints formatted tables from lists

tableData = [['apples', 'oranges', 'cherries', 'banana','pears'],
             ['Alice', 'Bob', 'Carol', 'David', 'Tim'],
             ['dogs', 'lion', 'moose', 'goose', 'turtle'],
             ['pen', 'pencil', 'marker', 'crayon','highligher']]

# function to format and print
def printTable(list):
    # initialize list of column width
    colWidth = [0]*len(tableData[0])

    # determine longest width per column
    for row in range(len(tableData)):
        for column in range(len(tableData[row])):
            if len((tableData[row][column])) > colWidth[column]:
                colWidth[column] = (len((tableData[row][column])))

    # print rows with right justifcation of longest column width
    for row in range(len(tableData)):
        for column in range(len(tableData[row])):
            print(tableData[row][column].rjust(colWidth[column] + 1), end = "")
        print()
     
printTable(tableData)



