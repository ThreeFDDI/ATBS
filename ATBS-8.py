#!/usr/local/bin/python3

# ATBS-8.py

import os

print(os.path.abspath('.'))

os.chdir("ATBS")

print(os.path.abspath('.'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.getcwd())

#os.makedirs("ATBS-8_directory")

os.chdir("ATBS-8_directory")

print(os.path.abspath('.'))

print(os.path.basename("/Users/JT/JTGIT/ATBS/ATBS-8_directory/test.txt"))

print(os.path.dirname("/Users/JT/JTGIT/ATBS/ATBS-8_directory/test.txt"))

print(os.listdir("/Users/JT/JTGIT/ATBS/"))

totalSize = 0
path = "/Users/JT/JTGIT/ATBS/"
for file in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path, file))

print("Total size of all files: {}".format(totalSize))

helloFile = open('hello.txt')

print(helloFile.read())

baconFile = open('bacon.txt', 'w')

baconFile.write('Hello world!\n')

baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)