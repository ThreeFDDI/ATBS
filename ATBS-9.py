#! /usr/local/bin/python3

import shutil, os

print(os.getcwd())

os.chdir("/Users/JT/JTGIT/ATBS/")

print(os.getcwd())

#print(dir(os))

shutil.copy('/Users/JT/JTGIT/ATBS/ATBS-9_dir1/file1', '/Users/JT/JTGIT/ATBS/ATBS-9_dir1/file2')

