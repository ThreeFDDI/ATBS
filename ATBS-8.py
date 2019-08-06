#!/usr/local/bin/python3

# ATBS-8.py

import os

print(os.path.abspath('.'))

os.chdir("ATBS")

print(os.path.abspath('.'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.getcwd())

#os.makedirs("Chap8")

os.chdir("Chap8")

print(os.path.abspath('.'))

print(os.path.basename("/Users/JT/JTGIT/ATBS/Chap8/test.txt"))

print(os.path.dirname("/Users/JT/JTGIT/ATBS/Chap8/test.txt"))

print(os.listdir("/Users/JT/JTGIT/ATBS/"))

totalSize = 0
path = "/Users/JT/JTGIT/ATBS/"
for file in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path, file))

print("Total size of all files: {}".format(totalSize))

helloFile = open('hello.txt')