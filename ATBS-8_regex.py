#!/usr/local/bin/python3

import os, re

# set path to be searched
path = "/Users/JT/JTGIT/ATBS/ATBS-8_regex_dir"

# list files in directory
files = os.listdir(path)

#print(files)

for file in files:
    if ".txt" in file: 
        with open(path + "/" + file) as file:
            data = file.read()
            print(data)