#!/usr/local/bin/python3

# ATBS-8.py

import os

print(os.path.abspath('.'))

os.chdir("ATBS")

print(os.path.abspath('.'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.getcwd())

os.makedirs("Chap8")

os.chdir("Chap8")

print(os.path.abspath('.'))

print(os.path.basename('.'))