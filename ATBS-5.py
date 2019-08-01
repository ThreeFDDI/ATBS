#!/usr/local/bin/python3

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def currentBoard(theBoard):
    print("Current\nboard:\n")
    print(theBoard['top-L'] + " | " + theBoard['top-M'] + " | " + theBoard['top-R'])
    print("-"*9)
    print(theBoard['mid-L'] + " | " + theBoard['mid-M'] + " | " + theBoard['mid-R'])
    print("-"*9)
    print(theBoard['low-L'] + " | " + theBoard['low-M'] + " | " + theBoard['low-R'])
    print("\n" + "~"*9 + "\n")

currentBoard(theBoard)

theBoard["low-R"] = "X"

currentBoard(theBoard)