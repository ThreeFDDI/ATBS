#!/usr/local/bin/python3

# Chapter 17 – Manipulating Images

# ATBS-17.py 

from PIL import Image

newIm = Image.new('RGBA', (200,400), 'purple')





newIm.save('ATBS/ATBS-17_purple.png')

