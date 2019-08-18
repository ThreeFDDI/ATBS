#! /usr/local/bin/python3

import shutil, os

top_level = "/Users/JT/JTGIT/ACI"

for folderName, subfolders, filenames in os.walk(top_level):

    if r"/." in folderName:
        continue

    else:
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)

        print('')