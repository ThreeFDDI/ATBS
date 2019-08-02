#!/usr/local/bin/python3

import sys

name = ""
while name != "your name":
    print("Please type your name.")
    name = input()
    if name == "exit":
        sys.exit()
print("Thank you!!")
