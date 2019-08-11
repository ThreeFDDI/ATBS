#!/usr/local/bin/python3

import os, re

# set path to be searched
path = "/Users/JT/JTGIT/ATBS/ATBS-8_regex_dir"

# list files in directory
files = os.listdir(path)

# loop through files
for file in files:
    # find .txt files
    if ".txt" in file:
        # open and read file 
        with open(path + "/" + file) as file:
            data = file.read()
            # regex search to match lines containing "test"
            matches = re.findall(".*test.*",data)
            # print matches
            for i in matches:
                print(i)
